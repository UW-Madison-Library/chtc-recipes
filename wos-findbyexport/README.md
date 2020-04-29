# Web of Science: Find Articles by Export File

This collection of scripts is used to pull a set of article records out of the Web of Science (WOS) data set. It runs over the CHTC WOS article data set that is serialized as JSON. It consists of four steps of jobs chained together.

## High-level Overview of Processing Chain

### Step 1: Identify The Initial Batch of Years

This job reads a WOS saved search export file (`savedrecs.txt`) that was downloaded from the WOS user interface. Given that this input file is what will vary for each person running this set of jobs, the first step is to identify what years of publication exist in the file. The job is a simple wrapper around a python script to parse the export file. The output of this job will then be fed into the next job, which finds the initial list of article records.

**Sub-directory:** `parsepublicationyears`
**Output:** `years.txt`
**Post-processing:** the `years.txt` file will be moved into the sub-directory for step 2

### Step 2: Find Article Records by WOS Export File

The WOS article IDs (also referred to as accession numbers) in `savedrecs.txt` are matched against the years in which they are published. This job will also generate a list of IDs for the cited references for each matched article.

**Sub-directory:** `findbyexportfile`
**Output:**

* `<YEAR>_<WOS-Collection>-article-matches.json`: article record data files
* `references-<YEAR>.tsv`: reference ID/Year data files

**Post-processing:** the `references-<YEAR>.tsv` files will be moved into the sub-directory for step 3

Note that starting in later years the WOS data set has records in the Web of Science Core Collection and the collection named Emerging Science Citation Index.

### Step 3: Sort the Cited Reference IDs by Publication Year

This job takes the cited reference IDs written out from step 1 and sorts them by the years in which they were published so that the Step 3 jobs will only need to know about the IDs for a year in which they are written.

**Sub-directory:** `sortreferences`
**Output:**

* `<YEAR>-references.tsv`: WOS ID files isolated by <YEAR>
* `wos-findreferences.dag`: a generated DAGMAN file that indicates what years' data step 4 should be run over

**Post-processing:** the `<YEAR>-references.tsv` files will be moved into the sub-directory for step 4

### Step 4: Retrieve the Cited Reference Article Records

This job is equivalent to step 2. It matches article records by their IDs. The input is the IDs of the cited references found in step 2.

**Sub-directory:** `findreferences`
**Output:** `<YEAR>_<WOS-Collection>-referenced-article-matches.json.json` - article record data files

### Notes

Steps 2 and 4 also require a Python distribution package for the `wos_explorer` library. See the [Web of Science Explorer](https://github.com/UW-Madison-Library/wos-explorer) repository.

## Running the Job

Follow these steps to run these CHTC DAG jobs.

1. [Generate a Python distribution package for the WOS Explorer library](https://github.com/UW-Madison-Library/chtc-recipes#creating-a-python-package-for-the-wos-explorer-for-use-within-chtc)
1. Upload the Python `wos_explorer-<VERSION>-.tar.gz` package from step 1 to your account on the CHTC submit server
1. Replace the `savedrecs.txt` file as needed
1. Copy the contents of this git project to your account on the CHTC submit server.
1. SSH to the submit server and submit the DAG job `wos-findbywosexport.dag`

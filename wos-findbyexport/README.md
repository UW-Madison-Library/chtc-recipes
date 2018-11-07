# Web of Science: Find Articles by Export File

This collection of scripts is used to pull a set of article records out of the Web of Science (WOS) data set. It runs over the CHTC WOS article data set serialized as JSON. It consists of three jobs chained together:

## Step 1: Find Article Records by WOS Export File

This job reads a WOS saved search export file downloaded from the WOS UI. The WOS article IDs (also referred to as accession numbers) are matched against the years in which they are published. This job will also generate a list of IDs for the cited references for each matched article.

* `wos-findbywosexport.sub`
* `wos_findbywosexport.sh`
* `find_by_wos_export.py`
* `finder_logging.py`
* `years.txt`

This also requires a CHTC compiled python that includes the `wos_explorer` package. See the [Web of Science Explorer](https://gitlab.library.wisc.edu/ltg/wos-explorer) repository.

## Step 2: Sort the Cited Reference IDs by Publication Year

This job takes the cited reference IDs written out from step 1 and sorts them by the years in which they were published so that the Step 3 jobs will only need to know about the IDs for a year in which they are written.

* `wos-sortrefs.sub`
* `wos-sortrefs.sh`
* contents from `step1-references/`

## Step 3: Retrieve the Cited Reference Article Records

This job takes the `step2-references/` data and generates a job for each year that has a reference.

* `wos-findreferences.sub`
* `wos_findreferences.sh`
* `find_references.py`
* `finder_logging.py`
* contents from `step2-references/`

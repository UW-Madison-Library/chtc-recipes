# CHTC Recipes

A repository to collect the submit files and scripts used in Center for High Throughput Computing (CHTC) jobs.

## Dependencies

### WOS Explorer

See: [WOS Explorer](https://github.com/UW-Madison-Library/wos-explorer)

This is a Python package developed to make it easy to work with the Web of Science (WOS) data set. It is designed to work with the WOS JSON data that is available in the CHTC environment.

The example recipes in this repository utilize Docker containers within the CHTC Condor environment. A container image is hosted on Docker Hub and the submit files reference it.

## Creating a custom Docker container using the WOS Explorer package

If you need to use other Python dependencies besides the WOS Explorer package you can create a custom Docker container that includes your Python dependencies as well as the WOS Explorer package. See the Dockerfile in this repository for an example of how to build the package from source and install the Natural Language Toolkit (NLTK) punctuation data file dependency.

See also: [Running HTC Jobs Using Docker Containers](https://chtc.cs.wisc.edu/uw-research-computing/docker-jobs)

## Current File List

The `common` directory of this repository includes a list of the current JSON files. Starting in 2022 the JSON files are broken into batches of 100,000 records. In previous years the data for a single year was included in a single file. As we learn more about the ways that researchers would like to use these files we know that some processes should be parallelized by Condor by operating on smaller amounts of data than one full year of publication data.

Note that if you would like to run a job that operates on a full year's worth of data in a single execute node, the filenames include the year. This should make it easy to use a Linux wildcard pattern to retrieve all files for a year.

```
$ ls *2010* | grep json
WR_2010_20230122093141_CORE_0001.json.gz
WR_2010_20230122093141_CORE_0002.json.gz
WR_2010_20230122093141_CORE_0003.json.gz
WR_2010_20230122093141_CORE_0004.json.gz
WR_2010_20230122093141_CORE_0005.json.gz
WR_2010_20230122093141_CORE_0006.json.gz
WR_2010_20230122093141_CORE_0007.json.gz
WR_2010_20230122093141_CORE_0008.json.gz
WR_2010_20230122093141_CORE_0009.json.gz
WR_2010_20230122093141_CORE_0010.json.gz
WR_2010_20230122093141_CORE_0011.json.gz
WR_2010_20230122093141_CORE_0012.json.gz
WR_2010_20230122093141_CORE_0013.json.gz
WR_2010_20230122093141_CORE_0014.json.gz
WR_2010_20230122093141_CORE_0015.json.gz
WR_2010_20230122093141_CORE_0016.json.gz
WR_2010_20230122093141_CORE_0017.json.gz
WR_2010_20230122093141_CORE_0018.json.gz
WR_2010_20230122093141_CORE_0019.json.gz
WR_2010_20230122093141_CORE_0020.json.gz
WR_2010_20230122093141_CORE_0021.json.gz
WR_2010_20230122093141_CORE_0022.json.gz
WR_2010_20230122093141_ESCI_0001.json.gz
WR_2010_20230122093141_ESCI_0002.json.gz
```

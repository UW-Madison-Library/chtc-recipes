# CHTC Recipes

A repository to collect the submit files and scripts used in Center for High Throughput Computing jobs.

## Dependencies

### WOS Explorer

See: [WOS Explorer](https://github.com/UW-Madison-Library/wos-explorer)

This is a Python package developed to make it easy to work with the Web of Science (WOS) data set. It is designed to work with the WOS JSON data that is available in the CHTC environment.

In this repository's `common` directory there is a tarball of the WOS Explorer package that was built with all of its dependencies. You will need to include this file in your Condor job. This tarball was created using the CHTC's Python interactive build process. This package primarily bundles the WOS Explorer and its NLTK dependency along with the NLTK "punkt" data set that it utilizes.

## Creating a custom Python dependencies package with the WOS Explorer

If you need to use other Python dependencies besides the WOS Explorer package you can create a custom Python dependencies package in the Condor environment using an interactive Condor job. See the CHTC's main article about this process, [Running Python Jobs on CHTC](https://chtc.cs.wisc.edu/uw-research-computing/python-jobs), specifically the section for creating a portable copy of your Python packages.

### Step 1: Create a WOS Explorer distribution tarball

Choose a location on your computer to clone the git repository:

```
$ git clone git@github.com:UW-Madison-Library/wos-explorer.git
$ cd wos-explorer
$ python setup.py sdist
```

This will generate the file

`./dist/wos_explorer-0.7.3.tar.gz`

Note that the version number may be different when you run it. This file will be used with CHTC Condor jobs.

### Step 2: Creating a Custom Python dependencies bundle with WOS Explorer

Once you have built a copy of the WOS Explorer package, you will then need to create a bundle/tarball of all your Python dependencies in single directory. This must include WOS Explorer package and its dependencies (namely the NLTK package). The CHTC website has instructions for building such a Python distribution. See the section [Adding Python Packages](https://chtc.cs.wisc.edu/uw-research-computing/python-jobs#build) that shows how to use a CHTC Interactive Job.

In addition to any other packages that you install, use the following steps to bundle WOS Explorer, **and importantly**, its dependency on the NLTK data:

```
$ tar xzf python39.tar.gz  
$ export PATH=$PWD/python/bin:$PATH  
$ mkdir packages  
$ python3 -m pip install --target=$PWD/packages wos_explorer-0.7.3.tar.gz  
$ export PYTHONPATH=$PWD/packages  
$ mkdir packages/nltk-data  
$ python3 -m nltk.downloader -d $PWD/packages/nltk-data punkt
```

Note that the first three commands here are part of the CHTC's instructions. The `pip install` command for the WOS Explorer tarball will also install the NLTK package. However, you will also need to install the NLTK's punctuation data set into the packages directory.

These example scripts assume that the the resulting file is named `wosexp-with-dependencies.tar.gz`. This version of the WOS Explorer package can then be used with the CHTC's versions of Python from the CHTC Squid proxy server. For example, a Condor submission file can include the following `transfer_input_files` statement:

```
transfer_input_files = http://proxy.chtc.wisc.edu/SQUID/chtc/python39.tar.gz, wosexp-with-dependencies.tar.gz, <python-script-1> <python-script-2>
```

Where `<python-script-N>` is your custom script that imports the WOS Explorer package.

### Step 3: Using your custom Python packages in a Condor job

Note that once you have assembled these dependencies, you can then use a Bash shell script to prepare a CHTC execute node to use the Python packages/dependencies. Please note that the NLTK Python package dependency will need to know where ot find the NLTK data files. See the last line below for how to set the `NLTK_DATA` environment variable.

```
# Unpack and setup the CHTC compiled Python build
tar -xzf python39.tar.gz
tar -xzf wosexp-with-dependencies.tar.gz

export PATH=$PWD/python/bin:$PATH
export PYTHONPATH=$PWD/packages
export NLTK_DATA=$PWD/packages/nltk-data
```

## Current File List

The `common` directory of this repository includes a list of the current JSON files. Starting in 2022 the JSON files are broken into batches of 100,000 records. In previous years the data for a single year was included in a single file. As we learn more about the ways that researchers would like to use these files we know that some processes should be parallelized by Condor by operating on smaller amounts of data than one full year of publication data.

Note that if you would like to run a job that operates on a full year's worth of data in a single execute node, the filenames begin with the year. This should make it easy to use a Linux wildcard pattern to retrieve all files for a year.

```
$ ls 2010* | grep json
2010_CORE_001.json.gz
2010_CORE_002.json.gz
2010_CORE_003.json.gz
2010_CORE_004.json.gz
2010_CORE_005.json.gz
2010_CORE_006.json.gz
2010_CORE_007.json.gz
2010_CORE_008.json.gz
2010_CORE_009.json.gz
2010_CORE_010.json.gz
2010_CORE_011.json.gz
2010_CORE_012.json.gz
2010_CORE_013.json.gz
2010_CORE_014.json.gz
2010_CORE_015.json.gz
2010_CORE_016.json.gz
2010_CORE_017.json.gz
2010_CORE_018.json.gz
2010_CORE_019.json.gz
2010_CORE_020.json.gz
2010_CORE_021.json.gz
2010_CORE_022.json.gz
2010_ESCI_001.json.gz
2010_ESCI_002.json.gz
```

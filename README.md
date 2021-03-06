# CHTC Recipes

A repository to collect the submit files and scripts used in Center for High Throughput Computing jobs.

## Dependencies

### WOS Explorer

See: [WOS Explorer](https://github.com/UW-Madison-Library/wos-explorer)

This is a Python package developed to make it easy to work with the Web of Science (WOS) data set. It is designed to work with the WOS JSON data that is available in the CHTC environment.

#### Creating a Python Package for the WOS Explorer for Use Within CHTC

Choose a location on your computer to clone the git repository:

```
$ git clone git@github.com:UW-Madison-Library/wos-explorer.git
$ cd wos-explorer
$ python setup.py sdist
```

This will generate the file

`./dist/wos_explorer-0.2.1.tar.gz`

Note that the version number may be different when you run it. This file will be used with CHTC Condor jobs.

# Compile Python with the WOS Explorer Package for Use on CHTC Servers

The steps below outline the process to compile Python 3 with the wos-explorer package so that the wos-explorer code can be used within CHTC jobs.

## Before You Start

### CHTC Python Build Instructions

See: [CHTC Python Build Instructions](http://chtc.cs.wisc.edu/python-jobs)

Steps 2 - 4 below are based on the CHTC instructions and simply add Step 3c.

### WOS Explorer

See: [WOS Explorer](https://gitlab.library.wisc.edu/ltg/wos-explorer)

This is a Python package developed to make it easy to work with the Web of Science (WOS) data set. It is designed to work with the WOS JSON data that is available in the CHTC environment.

## Building the Python Executable for CHTC with WOS Explorer Package

### 1) Clone/checkout a copy of the WOS Explorer code and create a distribution file from the source.

Choose a location on your computer to download the git repository and run these commands.

```
$ git clone git@gitlab.library.wisc.edu:ltg/wos-explorer.git
$ cd wos-explorer
$ python setup.py sdist
```

This will generate the file

`./dist/wos_explorer-0.2.1.tar.gz`

Note that the version number may be different when you run it.

### 2) Clone/checkout the CHTC Python compilation recipe

a) Download a copy of the CHTC recipes and move into the Python compilation directory

```
$ git clone git@gitlab.library.wisc.edu:ltg/chtc-recipes.git
$ cd chtc-recipes/wosexp-pythoncompile/
```

b) Add a copy of the Python source and the WOS Explorer distribution package

[Download a version of Python 3.6](https://www.python.org/downloads/source/). CHTC strongly recommends you do NOT use Python 3.7 at this time.

Copy the file `wos_explorer-0.2.1.tar.gz` from step 1 to this location.

### 3) Copy the files up to the CHTC submit server.

```
$ scp Python-3.6.7.tgz bucky@submit-1.chtc.wisc.edu:~/
$ scp wos_explorer-0.2.tar.gz bucky@submit-1.chtc.wisc.edu:~/
$ scp interactive.sub bucky@submit-1.chtc.wisc.edu:~/
```

### 4) Login and run the installation.

Compiling Python from source involves submitting a job in which your shell session is transferred with the job, as it were. See the "CHTC Python Build Instructions" link above for details. The job is defined in the `interactive.sub` file within this project.

Note that you may need to adjust the version numbers in the `interactive.sub` file for the version numbers you are using. These numbers can be found in submit file's `transfer_input_files` property.

a) Submit the interactive job, then wait for a prompt indicating you have a session.

```
[bucky@submit-1 ~]$ condor_submit -i interactive.sub
Submitting job(s).
1 job(s) submitted to cluster 5547.
Waiting for job to start...
Welcome to slot1_2@matlab-build-1.chtc.wisc.edu!
```

b) Compile Python from source.

This is a standard Unix style compilation from source process. Compiling Python on a CHTC execution server ensures that your CHTC jobs will be using a compatible Python version.

```
[bucky@matlab-build-1 dir_6572]$ mkdir python
[bucky@matlab-build-1 dir_6572]$ tar xvfz Python-3.6.7.tgz
[bucky@matlab-build-1 dir_6572]$ cd Python-3.6.7
[bucky@matlab-build-1 Python-3.6.7]$ ./configure --prefix=$(pwd)/../python
[bucky@matlab-build-1 Python-3.6.7]$ make
[bucky@matlab-build-1 Python-3.6.7]$ make install
[bucky@matlab-build-1 Python-3.6.7]$ cd ..
[bucky@matlab-build-1 dir_6572]$ cp python/bin/python3 python/bin/python
[bucky@matlab-build-1 dir_6572]$ cp python/bin/pip3 python/bin/pip
```

c) Install the WOS Explorer package.

This step will install the WOS Explorer package into the Python installation that you have compiled. This will enable you to call `import wos_explorer` in Python scripts used in CHTC jobs.

```
[bucky@matlab-build-1 dir_6572]$ export PATH=$(pwd)/python/bin:$PATH
[bucky@matlab-build-1 dir_6572]$ pip install wos_explorer-0.2.1.tar.gz
```

d) Finish up by creating a tar package and exiting the interactive session

```
[bucky@matlab-build-1 dir_6572]$ tar -czvf python-3.6.7-with-wosexpl-0.2.1.tar.gz python/
[bucky@matlab-build-1 dir_6572]$ exit
```

After exiting the job on the execution server, the interactive session will complete and the generated tarball will be copied back to your submit server account.

### 5) Copy the Python distribution back to your local hard drive

```
$ scp bucky@submit-1.chtc.wisc.edu:~/python-3.6.7-with-wosexpl-0.2.1.tar.gz .
```

This tar file is now ready to use as a custom Python installation that requires the WOS Explorer package.

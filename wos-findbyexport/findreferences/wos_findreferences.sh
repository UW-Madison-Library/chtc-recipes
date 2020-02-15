#!/bin/bash

# Unpack and setup the CHTC compiled Python build
tar -xzf python36.tar.gz
tar -xzf wos_explorer-0.2.1.tar.gz

export PATH=$PWD/python/bin:$PATH
export PYTHONPATH=$PWD/wos_explorer-0.2.1

# Command line specifies the year to process
year="$1"
cluster_id="$2"
process_id="$3"

# Create a directory for the article data file so it is not copied back to the submit server
working_data_dir="data"
source_file="/mnt/gluster/data2/clarivate_data/CORE_ANNUAL_1900-2017/${year}_CORE/articles.json"

# Copy the source file to the working location
mkdir $working_data_dir
cp $source_file $working_data_dir

# Run the Python code to process the file and find records
python3 find_references.py $year $cluster_id $process_id

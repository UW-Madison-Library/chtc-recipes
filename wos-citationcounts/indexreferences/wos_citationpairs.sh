#!/bin/bash

# Unpack and setup the CHTC compiled Python build
tar -xzf python-3.6.7-with-wosexpl-0.2.1.tar.gz
export PATH=$(pwd)/python/bin:$PATH
mkdir home
export HOME=$(pwd)/home

# Command line specifies the year to process
year="$1"
cluster_id="$2"
process_id="$3"

# Create a directory for the article data file so it is not copied back to the submit server
input_file="/mnt/gluster/data2/clarivate_data/CORE_ANNUAL_1900-2017/${year}_CORE/articles.json"
data_dir="data"
# Copy the source file to the working location
mkdir $data_dir
cp $input_file $data_dir

# Run the Python code to process the file and find records
python find_citation_pairs.py "${data_dir}/articles.json" $data_dir $year

cp "${data_dir}/"*.txt /mnt/gluster/stephenmeyer/citation-pairs/

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
input_file="/mnt/gluster/data2/clarivate_data/CORE_ANNUAL_1900-2017/${year}_CORE/articles.json"
data_dir="data"
# Copy the source file to the working location
mkdir $data_dir
cp $input_file $data_dir

# Run the Python code to process the file and find records
python3 find_citation_pairs.py "${data_dir}/articles.json" $data_dir $year

for file in data/*.txt ; do
  gzip $file
done

cp "${data_dir}/"*.gz /mnt/gluster/stephenmeyer/citation-pairs/

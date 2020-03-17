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
source_dir="/staging/groups/clarivate_data/2020-complete-extract"

# Copy the source files to the working location. The Emerging Science Citation Index (ESCI)
# files only exist from 2015 onward.
mkdir $working_data_dir
cp "${source_dir}/${year}_CORE.json.gz" $working_data_dir
if [ $year -gt "2015" ]; then
  cp "${source_dir}/${year}_ESCI.json.gz" ${working_data_dir}
fi
gunzip "${working_data_dir}/"*.gz

# Run the Python code to process the file and find records
python3 find_references.py $year $cluster_id $process_id

#!/bin/bash

# Unpack and setup the CHTC compiled Python build
tar -xzf python39.tar.gz
tar -xzf wosexp-with-dependencies.tar.gz

export PATH=$PWD/python/bin:$PATH
export PYTHONPATH=$PWD/packages
python3 -c 'import nltk; nltk.download("punkt")'

# Command line specifies the year to process
year="$1"
cluster_id="$2"
process_id="$3"

# Create a directory for the article data file so it is not copied back to the submit server
working_data_dir="data"
source_dir="/staging/groups/clarivate_data/2022-complete-extract"
output_dir="output"

# Copy the source files to the working location. The Emerging Science Citation Index (ESCI)
# files only exist from 2015 onward.
mkdir $working_data_dir
mkdir $output_dir
cp "${source_dir}/${year}_CORE"*.json.gz $working_data_dir
if [ $year -gt "2004" ]; then
  cp "${source_dir}/${year}_ESCI"*.json.gz $working_data_dir
fi
gunzip "${working_data_dir}/"*.gz

# Run the Python code to process the file and find records
python3 match_journals.py $year $cluster_id $process_id

for file in output/*.json ; do
  gzip $file
done

staging_storage_dir="/staging/<USERNAME>/journal-matches"
mkdir -p $staging_storage_dir
cp "${output_dir}/"*.gz $staging_storage_dir

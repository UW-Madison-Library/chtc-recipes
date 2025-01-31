#!/bin/bash

# Command line specifies the year to process
input_file="$1"
cluster_id="$2"
process_id="$3"

# Create a directory for the article data file so it is not copied back to the submit server
source_dir="/staging/groups/clarivate_data/2024-complete-extract/JSON"
working_data_dir="data"
output_dir="output"

# Copy the source files to the working location. The Emerging Science Citation Index (ESCI)
# files only exist from 2015 onward.
mkdir $working_data_dir
mkdir $output_dir
cp "${source_dir}/${input_file}" $working_data_dir
gunzip "${working_data_dir}/${input_file}"

# Run the Python code to process the file and find records
python3 match_articles_by_term.py $input_file $cluster_id $process_id

for file in output/*.json ; do
  gzip $file
done

staging_storage_dir="/staging/<USERNAME>/query-matches"
mkdir -p $staging_storage_dir
cp "${output_dir}/"*.gz $staging_storage_dir

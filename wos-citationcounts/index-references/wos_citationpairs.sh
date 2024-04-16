#!/bin/bash

# Command line specifies the year to process
year="$1"
cluster_id="$2"
process_id="$3"

# Create a directory for the article data file so it is not copied back to the submit server
source_dir="/staging/groups/clarivate_data/2024-complete-extract"
working_data_dir="data"

# Copy the source files to the working location. The Emerging Science Citation Index (ESCI)
# files only exist from 2005 onward.
mkdir $working_data_dir
cp "${source_dir}/WR_${year}"*.json.gz $working_data_dir
gunzip "${working_data_dir}/"*.gz

# Run the Python code to process the file and find records
python3 find_citation_pairs.py $working_data_dir $year

for file in data/*.txt ; do
  gzip $file
done

# IMPORTANT: change the <USERNAME> to your CHTC/NetID username
staging_storage_dir="/staging/<USERNAME>/citation-pairs"
mkdir -p $staging_storage_dir
cp "${working_data_dir}/"*.gz $staging_storage_dir

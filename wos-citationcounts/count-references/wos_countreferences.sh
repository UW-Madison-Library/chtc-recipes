#!/bin/bash

# Command line specifies the year to process
prefix="$1"
cluster_id="$2"
process_id="$3"

# Create a directory for the sorted reference data
# IMPORTANT: change the <USERNAME> to your CHTC/NetID username
src_dir="/staging/<USERNAME>/citation-pairs"
input_file_base="${prefix}-records.sorted"
input_file="${src_dir}/${input_file_base}.txt.gz"
data_dir="data"
output_file="${data_dir}/${input_file_base}-citation-counts.txt"

# Copy the source file to the working location
mkdir $data_dir
cp $input_file $data_dir
gunzip "${data_dir}/${input_file_base}.txt.gz"

# Run the Python code to process the file and count the number of citations per article
python3 count_sorted_references.py "${data_dir}/${input_file_base}.txt" $data_dir

# Compress the output file that was created by the python script and copy it to Staging
gzip $output_file
cp "${output_file}".gz $src_dir

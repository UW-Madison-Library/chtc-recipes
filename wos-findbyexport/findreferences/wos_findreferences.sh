#!/bin/bash

# Command line specifies the year to process
input_file="$1"
id_list="$2"
cluster_id="$3"
process_id="$4"

# Create a directory for the article data file so it is not copied back to the submit server
working_data_dir="data"
output_dir="output"
source_dir="/staging/groups/clarivate_data/2024-complete-extract"

# Copy the source files to the working location.
mkdir $working_data_dir
mkdir $output_dir
cp "${source_dir}/${input_file}" $working_data_dir
gunzip "${working_data_dir}/${input_file}"

# Run the Python code to process the file and find records
python3 find_references.py $input_file $id_list $cluster_id $process_id

staging_storage_dir="/staging/<USERNAME>/findbyexportfile-matches"
mkdir -p $staging_storage_dir

for file in output/*.json ; do
  echo "Processing output file ${file}"
  if [ -s $file ]
  then
    gzip $file
    cp ${file}.gz $staging_storage_dir
    echo "Compressed and copied to staging."
  else
    echo "File empty. Not copying to staging."
  fi
done

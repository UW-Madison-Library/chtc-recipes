#!/bin/bash

# Gather all the input parameters
prefix="$1"
cluster_id="$2"
process_id="$3"

echo "Sorting records for prefix: ${prefix}. Condor Cluster: ${cluster_id}, Condor Process: ${process_id}"

# IMPORTANT: change the <USERNAME> to your CHTC/NetID username
src_dir="/staging/<USERNAME>/citation-pairs"
data_dir="data"
mkdir -p $data_dir

# Gather the data from the Staging file system.
echo "Starting data fetch at `date`"
zipped_file_glob="${prefix}"-*.txt.gz
cp $src_dir/$zipped_file_glob $data_dir
echo "Data fetch completed at `date`"

# Unzip the files that have been compressed to save space on the Staging file system
echo "Unzipping files at `date`"
for file in data/$zipped_file_glob ; do
  gunzip $file
done
echo "Finished unzipping files at `date`"

# Combine all data into a single file, sort it, compress it and copy it back to the Staging file system
echo "Sorting files at `date`"
unzipped_file_glob="${prefix}-*.txt"
sorted_file="${prefix}-records.sorted.txt"

# Sort the files individually
for file in data/$unzipped_file_glob ; do
  sort $file -o "${file}".sorted
  mv "${file}".sorted $file
done

# Merge the files together
find data -maxdepth 1 -type f -name $unzipped_file_glob -print0 | xargs -0 sort -m -o $sorted_file
gzip $sorted_file
mv "${sorted_file}".gz $src_dir
echo "Finished sorting files at `date`"

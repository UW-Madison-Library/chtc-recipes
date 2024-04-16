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
echo "Merging all files `date`"
unzipped_file_glob="*.txt"
combined_file="all-records.merged"
sorted_file="${prefix}-records.sorted.txt"
cat data/$unzipped_file_glob > data/$combined_file
echo "Finished merging files at `date`"

echo "Sorting the combined file at `date`"
java -Xms2g -Xmx2g -jar /work/filesorter-0.4.0.jar data/$combined_file
echo "Finished sorting combined file `date`"

# Move the sorted data back to staging
echo "Moving sorted data to staging at `date`"
mv data/$combined_file data/$sorted_file
gzip data/$sorted_file
mv "data/${sorted_file}".gz $src_dir
echo "Files moved to staging at `date`"

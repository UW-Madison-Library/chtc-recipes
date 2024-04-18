#!/usr/bin/env python3

# Generate a DAG file with the following contents:
#
# JOB D1 wos-findreferences.sub DIR findreferences
# VARS D1 input_file="1900_CORE_001.json.gz"
# VARS D1 id_list="1900_id_list.txt"
# JOB D2 wos-findreferences.sub DIR findreferences
# VARS D2 input_file="1900_CORE_002.json.gz"
# VARS D2 id_list="1900_id_list.txt"
# ...
#
# Generate a <YEAR>_id_list.txt file

import glob
import os
import sys
from datetime import datetime
from collections import defaultdict


start          = datetime.today()
file_inventory = "input_files.txt"


inventory_by_year = defaultdict(set)
with open(file_inventory, "r", encoding="utf-8") as inventory:
    for line in inventory:
        wos_file = line.strip()
        year = int(wos_file[3:7])
        inventory_by_year[year].add(wos_file)


idlists_by_year = dict()

for input_file in glob.glob("input/*.tsv"):
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            year, id = line.split("\t")
            if year != "BLANK" and year <= "2023" and id.strip() != "":
                year = int(year[0:4])
                year = year if year >= 1945 else 1900

                if year not in idlists_by_year:
                    idlists_by_year[year] = open(str(year) + "_id_list.txt", "w", encoding="utf-8")

                idlists_by_year[year].write(id.strip() + "\n")


with open("wos-findreferences.dag", "w", encoding="utf-8") as dag_file:
    count = 0
    for year, output_file in idlists_by_year.items():
        for wos_file in sorted(inventory_by_year[year]):
            count += 1
            dag_file.write("JOB D"  + str(count) + " wos-findreferences.sub DIR findreferences\n")
            dag_file.write("VARS D" + str(count) + " input_file=\"" + wos_file + "\"\n")
            dag_file.write("VARS D" + str(count) + " id_list=\"" + str(year) + "_id_list.txt\"\n")

        output_file.close()


finish = datetime.today()
print( "Started:   ", start )
print( "Finished:  ", finish )
print( "Time Spent:", finish - start, "\n" )

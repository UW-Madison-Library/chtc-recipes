#!/usr/bin/env python3

import sys
import csv
from datetime import datetime
from collections import defaultdict

start          = datetime.today()
exported_file  = "savedrecs.txt"
file_inventory = "input_files.txt"


print("Identifying Years in WOS Export File")


inventory_by_year = defaultdict(set)
with open(file_inventory, "r", encoding="utf-8") as inventory:
    for line in inventory:
        wos_file = line.strip()
        year = int(wos_file[0:4])
        inventory_by_year[year].add(wos_file)


years = set()
for article in csv.DictReader( open(exported_file), delimiter='\t' ):
    year = int(article['PY'])
    if year >= 1945 and year < 2022:
        years.add(year)
    elif year < 1945:
        years.add(1900)


with open("custom_input_files.txt", "w", encoding="utf-8") as file:
    for year in sorted(years):
        for wos_file in sorted(inventory_by_year[year]):
            file.write(wos_file + "\n")


finish = datetime.today()
print( "Started:   ", start )
print( "Finished:  ", finish )
print( "Time Spent:", finish - start, "\n" )

#!/usr/bin/env python3

import sys
import csv
from datetime import datetime

start         = datetime.today()
exported_file = "savedrecs.txt"


print("Identifying Years in WOS Export File")

years = set()
for article in csv.DictReader( open(exported_file), delimiter='\t' ):
    year = int(article['PY'])
    if year >= 1945 and year <= 2018:
        years.add(year)
    elif year < 1945:
        years.add(1900)


with open("years.txt", "w", encoding="utf-8") as file:
    for year in sorted(years):
        file.write(str(year) + "\n")


finish = datetime.today()
print( "Started:   ", start )
print( "Finished:  ", finish )
print( "Time Spent:", finish - start, "\n" )

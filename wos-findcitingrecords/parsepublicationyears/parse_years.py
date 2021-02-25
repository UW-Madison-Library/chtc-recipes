#!/usr/bin/env python3

import sys
import csv
from datetime import datetime

start          = datetime.today()
article_file   = "articles.csv"
LAST_DATA_YEAR = 2019


print("Identifying Earliest Year in WOS Article File")

years = set()
with open(article_file) as csv_file:
    for article in csv.DictReader(csv_file):
        year = int(article["Year"])
        if year >= 1945 and year < 2020:
            years.add(year)
        elif year < 1945:
            years.add(1900)

with open("years.txt", "w", encoding="utf-8") as file:
    for year in range(sorted(years)[0], LAST_DATA_YEAR + 1):
        file.write(str(year) + "\n")


finish = datetime.today()
print( "Started:   ", start )
print( "Finished:  ", finish )
print( "Time Spent:", finish - start, "\n" )

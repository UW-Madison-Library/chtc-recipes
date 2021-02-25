#!/usr/bin/env python3

import sys
import glob
import os
import csv
from datetime import datetime
from wos_explorer.article_collection import ArticleCollection
from wos_explorer.matchers import CitationMatcher

import finder_logging


start      = datetime.today()
year       = sys.argv[1]
cluster_id = sys.argv[2]
process_id = sys.argv[3]

input_files     = glob.glob("data/*.json")
article_file    = "articles.csv"


print( "Find Citing Records - Processing Data for Year:", year, cluster_id, process_id )
finder_logging.configure(cluster_id, process_id)


ids = set()
with open(article_file) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        ids.add(row["ID"])


for input_file in input_files:
    output_file = "output/" + os.path.splitext(os.path.basename(input_file))[0] + "-citing-records.json"
    ArticleCollection(input_file).select(CitationMatcher(ids), output_file)


finish = datetime.today()
print( "Started:   ", start )
print( "Finished:  ", finish )
print( "Time Spent:", finish - start, "\n" )

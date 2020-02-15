#!/usr/bin/env python3

import sys
import pathlib
import csv
from datetime import datetime
from wos_explorer.article_collection import ArticleCollection
from wos_explorer.matchers import IdMatcher

import finder_logging


start      = datetime.today()
year       = sys.argv[1]
cluster_id = sys.argv[2]
process_id = sys.argv[3]


print( "Find References - Processing Data for Year:", year, cluster_id, process_id )

finder_logging.configure(cluster_id, process_id)

input_file      = "data/articles.json"
references_file = year + "-references.tsv"
output_file     = "referenced-article-matches-" + year + ".json"

ids = []
with open(references_file) as file:
    for line in file:
        if len(line.strip().split()) == 2:
            ids.append(line.strip().split('\t')[1])

ArticleCollection(input_file).select(IdMatcher(ids), output_file)


finish = datetime.today()
print( "Started:   ", start )
print( "Finished:  ", finish )
print( "Time Spent:", finish - start, "\n" )

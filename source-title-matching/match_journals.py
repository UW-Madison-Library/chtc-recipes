#!/usr/bin/env python3

import sys
import glob
import os
import csv
from datetime import datetime
from wos_explorer.article_collection import ArticleCollection
from wos_explorer.matchers import SourceTitleMatcher

import finder_logging


start         = datetime.today()
year          = sys.argv[1]
cluster_id    = sys.argv[2]
process_id    = sys.argv[3]
input_files   = glob.glob("data/*.json")
journals_file = "journals.csv"


print( "Find by WOS Export - Processing Data for Year:", year, cluster_id, process_id )
finder_logging.configure(cluster_id, process_id)


match_collections = []
source_titles = [journal['Full Journal Title'] for journal in csv.DictReader( open(journals_file) )]
criteria = SourceTitleMatcher(source_titles)
for input_file in input_files:
    output_file = "output/" + os.path.splitext(os.path.basename(input_file))[0] + "-article-matches.json"
    match_collections.append( ArticleCollection(input_file).select(criteria, output_file) )


article_match_count = 0
for matched_collection in match_collections:
    for article in matched_collection:
        article_match_count += 1


finish = datetime.today()
print( "Articles:  ", article_match_count )
print( "Started:   ", start )
print( "Finished:  ", finish )
print( "Time Spent:", finish - start, "\n" )

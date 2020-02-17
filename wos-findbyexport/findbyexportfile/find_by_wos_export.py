#!/usr/bin/env python3

import sys
import glob
import os
import csv
from datetime import datetime
from wos_explorer.article_collection import ArticleCollection
from wos_explorer.matchers import IdMatcher

import finder_logging


start      = datetime.today()
year       = sys.argv[1]
cluster_id = sys.argv[2]
process_id = sys.argv[3]

input_files     = glob.glob("data/*.json")
exported_file   = "savedrecs.txt"
references_file = "references-" + year + ".tsv"


print( "Find by WOS Export - Processing Data for Year:", year, cluster_id, process_id )
finder_logging.configure(cluster_id, process_id)


match_collections = []
ids = [article['UT'] for article in csv.DictReader( open(exported_file), delimiter='\t' )]
criteria = IdMatcher(ids)
for input_file in input_files:
    output_file = os.path.splitext(os.path.basename(input_file))[0] + "-article-matches.json"
    match_collections.append( ArticleCollection(input_file).select(criteria, output_file) )


article_match_count = 0
reference_count = 0
for matched_collection in match_collections:
    with open(references_file, 'a') as file:
        for article in matched_collection:
            article_match_count += 1
            for reference in article.references():
                reference_count += 1
                year = reference['year'] if reference['year'] is not None else 'BLANK'
                id   = reference['id']   if reference['id']   is not None else ''
                file.write('\t'.join([year, id]) + '\n')


print("Articles:  ", article_match_count)
print("References:", reference_count)


finish = datetime.today()
print( "Started:   ", start )
print( "Finished:  ", finish )
print( "Time Spent:", finish - start, "\n" )

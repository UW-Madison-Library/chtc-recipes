#!/usr/bin/env python3

import sys
# import glob
import os
import csv
from datetime import datetime
from wos_explorer.article_collection import ArticleCollection
from wos_explorer.matchers import IdMatcher

import finder_logging

start = datetime.today()

zipped_input_file = sys.argv[1]
cluster_id        = sys.argv[2]
process_id        = sys.argv[3]
json_input_file   = os.path.splitext(os.path.basename(zipped_input_file))[0]
exported_file     = "savedrecs.txt"
references_file   = "references-" + os.path.splitext(os.path.basename(json_input_file))[0] + ".tsv"


print( "Find by WOS Export - Processing Data for File:", json_input_file, cluster_id, process_id )
finder_logging.configure(cluster_id, process_id)


ids                = [article['UT'] for article in csv.DictReader( open(exported_file), delimiter='\t' )]
criteria           = IdMatcher(ids)
output_file        = "output/" + os.path.splitext(os.path.basename(json_input_file))[0] + "-article-matches.json"
matched_collection = ArticleCollection("data/" + json_input_file).select(criteria, output_file)


article_match_count = 0
reference_count = 0
with open(references_file, 'w') as file:
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

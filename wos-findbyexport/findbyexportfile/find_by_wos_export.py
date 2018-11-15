#!/usr/bin/env python

import sys
import pathlib
import csv
from datetime import datetime
from wos_explorer.article_collection import ArticleCollection
from wos_explorer.matchers import IdMatcher, PhraseMatcher

import finder_logging


start      = datetime.today()
year       = sys.argv[1]
cluster_id = sys.argv[2]
process_id = sys.argv[3]

input_file      = "data/articles.json"
exported_file   = "sample-export.txt"
output_file     = "article-matches-" + year + ".json"
references_file = "references-" + year + ".tsv"


print( "Find by WOS Export - Processing Data for Year:", year, cluster_id, process_id )

finder_logging.configure(cluster_id, process_id)


ids = [article['UT'] for article in csv.DictReader( open(exported_file), delimiter='\t' )]
criteria = IdMatcher(ids)
matches  = ArticleCollection(input_file).select(criteria, output_file)


article_match_count = 0
reference_count = 0
with open(references_file, 'w') as file:
    for article in matches:
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

#!/usr/bin/env python3

import sys
import glob
import os
import csv
from datetime import datetime
from wos_explorer.article_collection import ArticleCollection

import finder_logging
from query import query


start             = datetime.today()
zipped_input_file = sys.argv[1]
json_input_file   = os.path.splitext(os.path.basename(zipped_input_file))[0]
cluster_id        = sys.argv[2]
process_id        = sys.argv[3]


print( "Find by WOS Term Matching - Processing Data for:", zipped_input_file, cluster_id, process_id )
finder_logging.configure(cluster_id, process_id)


print(json_input_file)
output_file = "output/" + os.path.splitext(os.path.basename(json_input_file))[0] + "-article-matches.json"
ArticleCollection("data/" + json_input_file).select(query, output_file)


finish = datetime.today()
print( "Started:   ", start )
print( "Finished:  ", finish )
print( "Time Spent:", finish - start, "\n" )

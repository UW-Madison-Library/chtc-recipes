#!/usr/bin/env python3

import glob
import os
import sys
from datetime import datetime
from wos_explorer.article_collection import ArticleCollection
from wos_explorer.matchers import IdMatcher

import finder_logging


start      = datetime.today()

zipped_input_file = sys.argv[1]
json_input_file   = os.path.splitext(os.path.basename(zipped_input_file))[0]
id_list           = sys.argv[2]
cluster_id        = sys.argv[3]
process_id        = sys.argv[4]


print( "Find References - Processing Data for File:", json_input_file, id_list, cluster_id, process_id )
finder_logging.configure(cluster_id, process_id)


criteria    = IdMatcher( [line.strip() for line in open(id_list)] )
output_file = "output/" + os.path.splitext(os.path.basename(json_input_file))[0] + "-referenced-article-matches.json"
ArticleCollection("data/" + json_input_file).select(criteria, output_file)


finish = datetime.today()
print( "Started:   ", start )
print( "Finished:  ", finish )
print( "Time Spent:", finish - start, "\n" )

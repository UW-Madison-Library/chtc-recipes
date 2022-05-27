#!/usr/bin/env python3

import sys
import glob
import os
import csv
from datetime import datetime
from wos_explorer.article_collection import ArticleCollection
from wos_explorer.matchers import SourceTitleMatcher

import finder_logging


start             = datetime.today()
zipped_input_file = sys.argv[1]
json_input_file   = os.path.splitext(os.path.basename(zipped_input_file))[0]
cluster_id        = sys.argv[2]
process_id        = sys.argv[3]
journals_file     = "journals.csv"


print( "Find by WOS Export - Processing Data for Year:", zipped_input_file, cluster_id, process_id )
finder_logging.configure(cluster_id, process_id)


source_titles = [journal['Full Journal Title'] for journal in csv.DictReader( open(journals_file) )]
criteria      = SourceTitleMatcher(source_titles)
output_file   = "output/" + os.path.splitext(os.path.basename(json_input_file))[0] + "-article-matches.json"
ArticleCollection("data/" + json_input_file).select(criteria, output_file)


finish = datetime.today()
print( "Started:   ", start )
print( "Finished:  ", finish )
print( "Time Spent:", finish - start, "\n" )

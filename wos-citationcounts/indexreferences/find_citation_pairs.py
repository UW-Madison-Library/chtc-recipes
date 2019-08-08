#!/usr/bin/env python

import sys
from datetime import datetime
from wos_explorer.article_collection import ArticleCollection


def get_file_bin(output_files, article_id, output_dir, year):
    """Return an opened/writable output file for the current ID.

    If the appropriate bin file does not yet exist, it will be created.

    Parameters:
    output_files (dict): a lookup table that indexes writable files by prefix and first char
    article_id (str): the article ID that for which the caller is retrieving the appropriate file
    output_dir (str): a string file path where the output files are written

    Returns:
    file object: the file to write the article ID into
    """

    prefix   = article_id.split(":")[0]    if ":" in article_id else "NOPREFIX"
    id_char1 = article_id.split(":")[1][0] if ":" in article_id else article_id[0]
    key      = prefix + "-" + id_char1 + "-" + year

    if key not in output_files:
        output_files[key] = open(output_dir + "/" + key + ".txt", "w")

    return output_files[key]



start      = datetime.today()
input_file = sys.argv[1]
output_dir = sys.argv[2]
year       = sys.argv[3]


# A lookup table that maps output_files
output_files = {}


# Loop thru the article collection and write the references out to
for article in ArticleCollection(input_file):
   for reference in article.references():
       if reference['id'] is not None:
           file = get_file_bin(output_files, reference['id'], output_dir, year)
           file.write("\t".join([reference['id'], article['id']]) + "\n")


# Be sure to close the files!
for id, file in output_files.items():
    file.close()


finish = datetime.today()
print( "Started:   ", start )
print( "Finished:  ", finish )
print( "Time Spent:", finish - start, "\n" )

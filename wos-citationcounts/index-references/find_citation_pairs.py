#!/usr/bin/env python3

import sys
import glob
import hashlib
import json
import re
from datetime import datetime
from wos_explorer.article_collection import ArticleCollection


CHILD_ID_PATTERN = re.compile('.+\.\d+$')


def get_file_bin(output_files, article_id, output_dir, year):
    """Return an opened/writable output file for the current ID.

    If the appropriate file does not yet exist, it will be created.

    Parameters:
    output_files (dict): a lookup table that indexes writable files by first char
    article_id (str): the hashed article ID for which the caller is retrieving the appropriate file
    output_dir (str): a string file path where the output files are written

    Returns:
    file object: the file to write the article ID into
    """

    key = article_id[0] + "-" + year
    if key not in output_files:
        output_files[key] = open(output_dir + "/" + key + ".txt", "w")

    return output_files[key]


def matches_source_item(reference_id):
    """Return true if reference_id is he UID of a matching source item in Web of Science.

    This function detects whether the supplied ID ends in a dot and a numeric value indicating
    it is an increment of another WOS ID.

    Parameters:
    reference_id (str): an ID from a WOS record's reference list

    Returns:
    true if the ID is not the the child of a parent/citing document
    """
    if not reference_id.strip():
        return False
    elif CHILD_ID_PATTERN.match(reference_id) is not None:
        return False
    else:
        return True



start      = datetime.today()
output_dir = sys.argv[1]
year       = sys.argv[2]


# A lookup table that maps output_files
output_files = {}
input_files  = glob.glob(output_dir + "/*.json")


article_count   = 0
reference_count = 0
wos_rec_refs    = 0
# Loop thru the article collection and write the references out
for input_file in input_files:
    print(input_file)
    for article in ArticleCollection(input_file):
        article_count += 1
        for reference in article.references():
            reference_count += 1
            if reference['id'] is not None and matches_source_item(reference['id']):
                wos_rec_refs += 1

                # First Hash the ID of the referenced article. This will help ensure that the output
                # files are evenly distributed in size.
                hash_id = hashlib.sha1(bytearray(reference['id'], "utf-8")).hexdigest()
                file = get_file_bin(output_files, hash_id, output_dir, year)

                # Next write the entry to the output file corresponding to the current hash ID.
                json_str = json.dumps({"article_id": reference['id'], "referring_article": article['id']})
                file.write("\t".join([hash_id, json_str]) + "\n")


# Be sure to close the files!
for id, file in output_files.items():
    file.close()


finish = datetime.today()
print()
print( "Articles:             ", article_count )
print( "References:           ", reference_count )
print( "WOS Record References:", wos_rec_refs )
print()
print( "Started:   ", start )
print( "Finished:  ", finish )
print( "Time Spent:", finish - start, "\n" )

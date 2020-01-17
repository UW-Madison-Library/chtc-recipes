#!/usr/bin/env python

import os
import sys
import json
from datetime import datetime


def write_citation_count_entry(output, article_id, referring_articles, most_cited_article):
    referring_article_count = len(referring_articles)
    if referring_article_count > most_cited_article["referring_article_count"]:
        most_cited_article["article_id"] = article_id
        most_cited_article["referring_article_count"] = referring_article_count

    output.write("\t".join([article_id, str(referring_article_count)]) + "\n")
    referring_articles.clear()


start       = datetime.today()
input_file  = sys.argv[1]
output_dir  = sys.argv[2]
basename    = os.path.basename(input_file)
output_file = output_dir + "/" + os.path.splitext(basename)[0] + "-citation-counts.txt"


most_cited_article  = {"article_id": None, "referring_article_count": 0}
referring_articles  = []
current_article_id  = None
previous_article_id = None


article_count  = 0
citation_count = 0


# Open the output file for writing. Open the input file fo reading and loop through it.
# Each line in the input file represents a single citation entry: an article being cited by another one.
# As the input file entries are in sorted order, when the current line has the same index key as the
# previous one, it is another citation for the same article. When they are different, it is the next
# article in the list, so "tie off" the previous article.
with open(output_file, "w") as output:
    with open(input_file) as file:
        for line in file:
            citation_count += 1

            # Parse the current line's citation
            citation = json.loads(line.split("\t")[1])
            current_article_id = citation["article_id"]

            # When the current article ID is different from the previous one,
            # summarize the reference count for the previous article and clear
            # the referring articles list for the new current article
            if previous_article_id is not None and current_article_id != previous_article_id:
                article_count += 1
                write_citation_count_entry(output, previous_article_id, referring_articles, most_cited_article)

            referring_articles.append(citation["referring_article"])
            previous_article_id = current_article_id

    # Summarize the final article reference count
    article_count += 1
    write_citation_count_entry(output, previous_article_id, referring_articles, most_cited_article)


print()
print("Articles:      ", article_count)
print("Citations:     ", citation_count)
print("Most Citations:", most_cited_article["article_id"] + ":", most_cited_article["referring_article_count"])
print()

finish = datetime.today()
print( "Started:   ", start )
print( "Finished:  ", finish )
print( "Time Spent:", finish - start )
print()

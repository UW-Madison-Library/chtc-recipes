#!/usr/bin/env python3

from wos_explorer.article_collection import ArticleCollection


filepath = '/sample-data/web-of-science/sample-records.json'

print("Confirmation Script:", __file__)
print("Sample Data:", filepath)
print("\nSample Records:")

for article in ArticleCollection(filepath):
    print(article['id'], article['title'])

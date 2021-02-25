# Web of Science: Find Citing Records

This collection of scripts is used to retrieve a set of article records out of the Web of Science (WOS) data set. It runs over the CHTC WOS article data set that is serialized as JSON. The matching criteria is based on a list of known WOS article records. Using the IDs from those known records, this job will retrieve all records that cite one or more records from the known articles.

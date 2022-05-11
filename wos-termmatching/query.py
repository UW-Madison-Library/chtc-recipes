# EXAMPLE QUERY FOR WOS EXPLORER PACKAGE
#
# Consider a (rather nonsensical) Boolean query that may be written as:
#
# ((cat* OR kitten* OR feline*) AND (dog* OR pup* OR canine*)) OR pet* OR "domesticat* animal*"
#
# This query has 3 components. The first is divided into 2 sub-components, each of which is made up of
# another sub-component of 3 terms. All search terms are right-side wildcarded meaning that a plural form
# of the word with an 's' character (or any suffix) would be matched. The third component is a phrase
# that requires domesticat* (which would match "domesticate", "domestication", etc) to be immediately
# followed by the term animal*.
#
# This query would be implemented with the following code. The match_articles_by_term.py script then
# imports the final "query" variable. See the WOS Explorer test suite for more examples.

from wos_explorer.matchers import Query
from wos_explorer.matchers import PhraseMatcher


# Optionally restrict to the following fields in the JSON data.
# This list is an optional parameter passed to a PhraseMatcher object.
fields = ["title", "abstract_text", "keywords"]


cats = [
  PhraseMatcher("cat*", fields),
  PhraseMatcher("kitten*", fields),
  PhraseMatcher("feline*", fields)
]

dogs = [
  PhraseMatcher("dog*", fields),
  PhraseMatcher("pup*", fields),
  PhraseMatcher("canine*", fields)
]

cats_or_dogs = Query([Query(cats, "or"), Query(dogs, "or")], "and")

pets = [
  PhraseMatcher("pet*", fields),
  PhraseMatcher("domesticat* animal*", fields)
]

query = Query([cats_or_dogs, *pets], "or")

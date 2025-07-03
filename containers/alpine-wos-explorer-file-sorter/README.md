# WOS Citation Counts Container

The `Dockerfile` in this directory defines the container used by the sorting stage for this CHTC DAG. Most of the UW-Madison Libraries' CHTC Recipes use our primary container, which includes mainly Python and our WOS Explorer Python package. The sorting stage for this recipe utilizes a Java jar developed by the Libraries to sort large files using multiple CPU cores.

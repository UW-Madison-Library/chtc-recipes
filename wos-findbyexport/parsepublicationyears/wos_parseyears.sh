#!/bin/bash

# Unpack and setup the CHTC compiled Python build
tar -xzf python-3.6.7-with-wosexpl-0.2.1.tar.gz
export PATH=$(pwd)/python/bin:$PATH
mkdir home
export HOME=$(pwd)/home

python parse_years.py

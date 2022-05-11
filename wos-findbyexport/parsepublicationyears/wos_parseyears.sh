#!/bin/bash


# Unpack and setup the CHTC compiled Python build
tar -xzf python39.tar.gz
export PATH=$PWD/python/bin:$PATH


python3 parse_years.py

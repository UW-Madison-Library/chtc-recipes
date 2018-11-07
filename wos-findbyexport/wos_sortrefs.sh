#!/bin/bash

mkdir step2-references

cat article-match-references-* | while read line
do
    if [ "${line:0:5}" != "BLANK" ]; then
        year="${line:0:4}"
        if [ $year -lt "1945" ]; then
            echo "1900" >> "step2-references/years-tmp.txt"
            echo "${line}" >> "step2-references/1900-references.tsv"
        else
            echo "${line:0:4}" >> "step2-references/years-tmp.txt"
            echo "${line}" >> "step2-references/${line:0:4}-references.tsv"
        fi
    fi
done

sort step2-references/years-tmp.txt | uniq > step2-references/years.txt
rm step2-references/years-tmp.txt

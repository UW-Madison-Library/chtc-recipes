#!/bin/bash

cat references-* | while read line
do
    if [ "${line:0:5}" != "BLANK" ]; then
        year="${line:0:4}"
        if [ $year -lt "1945" ]; then
            echo "1900" >> "years-tmp.txt"
            echo "${line}" >> "1900-references.tsv"
        else
            echo "${line:0:4}" >> "years-tmp.txt"
            echo "${line}" >> "${line:0:4}-references.tsv"
        fi
    fi
done

sort years-tmp.txt | uniq > years.txt
rm years-tmp.txt

count=0
cat years.txt | while read line
do
    count=$((count + 1))
    echo "JOB B${count} wos-findreferences.sub DIR findreferences" >> wos-findreferences.dag
    echo "VARS B${count} year=\"${line}\"" >> wos-findreferences.dag
done

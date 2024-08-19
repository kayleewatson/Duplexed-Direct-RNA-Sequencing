#!/usr/bin/bash

tmpfile=$(mktemp --suffix=.txt)
samtools view $@ | awk '{print $1":"$2"+"$6">"$10}' > $tmpfile

python ./softclip_fasta.py $tmpfile

rm $tmpfile

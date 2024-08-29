#!/usr/bin/bash

samtools view $@ | awk '{print $1":"$2"+"$6">"$10}' > softclip_seq_preanalysis_format.txt

python ./softclip_fasta.py softclip_seq_preanalysis_format.txt

rm softclip_seq_preanalysis_format.txt

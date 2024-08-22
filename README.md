# Duplexed-Direct-RNA-Sequencing

![Steps](/images/demultiplex_steps.png)

### Package requirements:
(the commands may work with other versions, but these were the versions used during the analysis for the publication)

* Dorado 0.5.1
* minimap2 2.24-r1122
* Python 3.8.2
* seqkit 0.7.2
* samtools 1.11
* EMBOSS:fuzznuc 6.6.0.0

### Using the commands and scripts
Use the commands in each 'step' in order:
1. [step1_basecall](step1_basecall)
2. [step2_alignment](step2_alignment)
3. [step3_softclips](step3_softclips)
4. [step4_pattern_search](step4_pattern_search)

[NOTE]: For step3_softclips to work properly, the [softclip_fasta.py](softclip_fasta.py) and [softclip_seq.sh](softclip_seq.sh) scripts need to be downloaded and placed in the same directory

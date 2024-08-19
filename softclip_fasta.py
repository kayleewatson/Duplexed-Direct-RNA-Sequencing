#!/usr/bin/env python

import sys
from Bio.Seq import Seq

def clip_amount_strand(read_info):
    for line in read_info:
        sep_id_strand = line.find(":")
        sep_strand_cig = line.find("+")
        sep_cig_seq = line.find(">")
# pull out the SAM tag (indicates the strand)
        strand=int(line[(sep_id_strand + 1):(sep_strand_cig)])
# pull the last character of the CIGAR string
        if strand == 0:
            cig_end = (sep_cig_seq - 1)
            last_char=(line[cig_end])
            seq = line[(sep_cig_seq + 1):(len(line) - 1)]
            if str(last_char) == "M":
                continue
            else:
                read_id = line[0:(sep_id_strand)]
                end_num = (cig_end - 1)
                end = line[end_num]
                while end.isalpha() == False:
                    end_num -= 1
                    end = line[end_num]
                clipped_amount = int(line[(end_num + 1):cig_end])
                clip_seq_strand(read_id, seq, clipped_amount)
        else:
            cig_end = (sep_strand_cig)
            first_char=(line[cig_end])
            seq = Seq(line[(sep_cig_seq + 1):(len(line) - 1)])
            rev_comp_seq = str(seq.reverse_complement())
            read_id = line[0:(sep_id_strand)]
            end_num = (cig_end + 1)
            end = line[end_num]
            while end.isalpha() == False:
                end_num += 1
                end = line[end_num]
            m_s_check = line[(end_num)]
            if str(m_s_check) == "M":
                clipped_amount = 0
            else:
                clipped_amount = int(line[(cig_end + 1):(end_num)])
            clip_seq_strand(read_id, rev_comp_seq, clipped_amount)


def clip_seq_strand(read_id, seq, clipped_amount):
    if clipped_amount > 0:
        clip = seq[(len(seq) - (clipped_amount + 5)):(len(seq))]
        print(">" + read_id + "\n" + clip)
    else:
        pass


reads = open(sys.argv[1], 'r')
lines = reads.readlines()

clip_amount_strand(lines)

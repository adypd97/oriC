#!/usr/bin/env python3

''' 
Format Genomic Data and return
the OriC sequence

Returns : dna_seq (an in-memory string
buffer)

'''
import gzip
import faulthandler
import os
import sys
import io

ORGANISM_PATH = "data/Vibrio_cholerae"
ORGANISM_GENOME_FASTA_FILE = "data/Vibrio_cholerae/GCA_000829215.1_ASM82921v1_genomic.fna.gz"

dna_seq = io.StringIO()
if os.path.exists(ORGANISM_PATH):
    try:
        with gzip.open(ORGANISM_GENOME_FASTA_FILE) as f:
            # read 500 bp at a time
            f.readline()                # skip the unwanted first line 
            for seq in f:
                dna_seq.write(seq.decode('utf-8').rstrip())

    except gzip.BadGzipFile:
        print("Not a gzip file")
        sys.exit(1)
else:
    raise OSError("The files for organism doesn't exist")


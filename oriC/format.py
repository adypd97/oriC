#!/usr/bin/env python3

''' 
Format Genomic Data and return
the OriC sequence

Returns : dna_seq (an in-memory string
buffer)


TODO: Isolate the oriC portion of the genome
and return that (that would be better)
'''
import gzip
import os
import sys
import io
from util import get_kv


def get_dna_seq(ORGANISM):
    ''' 
     Return DNA sequence as in-memory string
     object

     TODO: What if the sequence file is big
     (maybe just return the fileobj (f) in that
     case?)

    '''
    ORG, FGIB = get_kv(ORGANISM)
    ORGANISM_PATH = "data/" + ORG
    ORGANISM_GENOME_FASTA_FILE = ORGANISM_PATH + "/" + FGIB + "_genomic.fna.gz"
    dna_seq = io.StringIO()
    if os.path.exists(ORGANISM_PATH):
        try:
            with gzip.open(ORGANISM_GENOME_FASTA_FILE) as f:
                f.readline()                # skip the unwanted first line 
                for seq in f:
                    dna_seq.write(seq.decode('utf-8').rstrip())

        except gzip.BadGzipFile:
            print("Not a gzip file")
            sys.exit(1)
    else:
        raise OSError("The files for organism doesn't exist")

    return dna_seq


if __name__ == "__main__":
    seq = get_dna_seq("vibrio cholerae")

#!/usr/bin/env python3
'''
Fetch genome data and format it for use.
Connects to ftp.ncbi.nih.gov ftp server.

See FAQ for more : https://www.ncbi.nlm.nih.gov/genome/doc/ftpfaq/

This will only download the latest representative 
genome and meta data for a given species.

Other variants aren't supported(yet).

What is downloaded ?
    1) assembly_file_report 
    2) assembly_file_status 
    3) assembly_file_stats
    4) assembly_file_regions
    5) assembly_genome_fasta

    see above FAQ link for more information
    on each file

How does it work?
On the commandline :
    $ ./fetch_genome.py [GENUS] [SPECIES]
will download the above files in oric/data/GENUS_SPECIES

'''
# TODO: This module would need to be made cross platform
# TODO: Integrity check for files

import sys

# TODO : Enter organism ORG as commandline arguments
# Unfortunately we also need the [assembly accession number].[assembly name]
# So, either we include that in commandline arg or better yet,
# read from a file
#print(sys.argv)
if not len(sys.argv) == 3:
    print("Please enter genus and species both of organism")
    sys.exit(1)
else:
    GENUS = sys.argv[1].lower().title().rstrip()
    SPECIES = sys.argv[2].lower().rstrip()
    ORG = GENUS + "_" + SPECIES

SAVE_DIR = "data/"

BASE_URL = "ftp.ncbi.nih.gov"
GENOME_SUBDIR = "genomes/"
CLASS_BACTERIA_SUBDIR = "genbank/bacteria/"

# VIBRIO_CHOLERAE REPRESENTATIVE (LATEST) EXAMPLE
VIBRIO_CHOLERAE = ORG  + "/representative/GCA_000829215.1_ASM82921v1/"
VIBRIO_CHOLERAE_rep = VIBRIO_CHOLERAE.split("/")[2]
ASSEMBLY_FILE_REPORT = VIBRIO_CHOLERAE_rep + "_assembly_report.txt"
ASSEMBLY_FILE_STATUS = VIBRIO_CHOLERAE_rep + "_assembly_status.txt"
ASSEMBLY_FILE_STATS = VIBRIO_CHOLERAE_rep + "_assembly_stats.txt"
ASSEMBLY_FILE_REGIONS = VIBRIO_CHOLERAE_rep + "_assembly_regions.txt"
ASSEMBLY_GENOME_FASTA = VIBRIO_CHOLERAE_rep  + "_genomic.fna.gz"

ASSEMBLY_LIST = [ASSEMBLY_FILE_REPORT, ASSEMBLY_FILE_STATUS, 
                    ASSEMBLY_FILE_STATS, ASSEMBLY_FILE_REGIONS, ASSEMBLY_GENOME_FASTA]

VIB_CHOLERAE_REQUEST_URL = GENOME_SUBDIR + CLASS_BACTERIA_SUBDIR + VIBRIO_CHOLERAE


def fetch():
    import os
    import os.path
    from ftplib import FTP, error_perm, error_temp
    with FTP(BASE_URL, user="anonymous", passwd="anonymous") as ftp:
        ftp.cwd(VIB_CHOLERAE_REQUEST_URL)
        #ftp.retrlines('LIST')
        org_data_dir = './' + SAVE_DIR + ORG
        if not os.path.exists(org_data_dir):
            os.mkdir(org_data_dir)
        os.chdir(org_data_dir)
        for assembly_file in ASSEMBLY_LIST:
            # if assembly_file already exists, skip it

            WRITE_FLAG = 'w'
            if assembly_file == ASSEMBLY_LIST[-1]:
                WRITE_FLAG = 'wb'
            if os.path.exists(assembly_file) and os.path.getsize(assembly_file):
                continue

            print("Dowloading %s" %(assembly_file))
            with open(assembly_file, WRITE_FLAG) as f:
                try:
                    if WRITE_FLAG == 'w':
                        ftp.retrlines("RETR " + assembly_file, f.write)
                    elif WRITE_FLAG == 'wb':
                        ftp.retrbinary("RETR " + assembly_file, f.write)
                except error_perm:
                    print("No file named %s found, skipping..."%(assembly_file))
                    os.remove(assembly_file)
                    continue
                except error_temp:
                    print("Connection was dropped unexpectedly, Try again!")
                    sys.exit(1)

    print("DONE.. see %s for data retrieved" % org_data_dir)

if __name__ == "__main__":
    fetch()

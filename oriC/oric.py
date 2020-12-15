#!/usr/bin/env python3

'''
Count a k-mer in a given DNA sequence, where
k is the length of the short 'word'.

AND 

Also, find most frequent k-mer within the sequence.
'''

from pprint import pprint as pp
import sys

def hamming_dist(s1, s2):
    ''' Calculate hamming distance between
    two strings of equal length
    '''
    assert len(s1) == len(s2), "strings should be of equal length"
    mismatch = 0
    for v1, v2 in zip(s1, s2):
        if v1 != v2:
            mismatch += 1
    return mismatch

'''
DEPRECIATE
'''
def pattern_count(S, w):
    '''
    Given a sequence S and 
    a word w.

    OUTPUT = no. of times w appears in S
    '''
    len_w = len(w)
    len_S = len(S)
    count_w = 0
    S = S.upper()
    w = w.upper()
    # sliding window of length len_w
    for i in range(0,len_S-len_w):
        if w == S[i:i+len_w]:
            count_w += 1
    return count_w

def pattern_count_w_mis(S, w, d):
    ''' Same as pattern_count(S,w)
    (above) but with the addition
    flexibility of d mismatches in S
    '''
    len_w = len(w)
    len_S = len(S)
    count_w = 0
    S = S.upper()
    w = w.upper()
    # sliding window of length len_w
    for i in range(0,len_S-len_w):
        win = S[i:i+len_w]
        if hamming_dist(w, win) <= d:
            count_w += 1
    return count_w


from util import complement
def frequent_word(S, k, d=0):
    '''
    Given a sequence S and number k
    Find most frequent k-mers in S 
    and return them.

    TODO:INEFFICIENT : O(len(S)^2*k) '''
    kmer_count_dict = {}
    S = S.upper()
    i = 0
    while 1:
        if i == len(S) - k + 1:
            break
        w = S[i:i+k]
        w_prime = complement(w)
        kmer_count_dict[w] = pattern_count_w_mis(S, w, d)
        #kmer_count_dict[w_prime] = pattern_count_w_mis(S, w_prime, d)
        i += 1
    max_kmer_count = max(kmer_count_dict.values())
    freq_kmer_dict = {}
    for k,v in kmer_count_dict.items():
        if v >= 3 and v <= max_kmer_count: # 4 is arbitrary 
            freq_kmer_dict[k] = v

    del kmer_count_dict
    return freq_kmer_dict

def most_freq_kmers(S, d):
    ''' 
    Return most frequent kmers
    for all k ; 3 <= k <= len(S) - 2 ''' 
    from tqdm import tqdm as tq
    len_S = len(S)
    most_freq_kmers_dict = {}
    for i in tq(range(9, 10)): # TODO: fix later, only computing for 9-mers
        kmer_dict = frequent_word(S,i, d)
        kmer_dict_freq_values = list(kmer_dict.values())
        most_freq_kmers_dict[str(i)+'-mer'] = kmer_dict
        
    return most_freq_kmers_dict

def freq_9_kmers_with_compliment(S,d):
    k_mers = set()
    S_k_mers = most_freq_kmers(S,d)
    print(S_k_mers["9-mer"])
    for v in S_k_mers["9-mer"].keys():
        k_mers.add(v)
    return list(k_mers)

        
import sys
import os
def read_oric_region(filename):
    ''' 
    Reading the oriC sequences obtained 
    from skew algorithm
    '''
    seq = ""
    FILE_PATH = os.path.join(os.getcwd(), 'res/{}'.format(filename))
    if os.path.isfile(FILE_PATH):
        with open(FILE_PATH) as f:
            _ = f.readline()
            _ = f.readline()
            _ = f.readline()
            seq = f.readline().strip()
    else:
        raise OSError("Not a file")
        sys.exit(1)
    return seq

def read_dna_file(filename):
    ''' 
    SOON TO BE DEPRECIATED
    TODO: 
    Right now we are only 
    reading txt files of 
    DNA sequences

    TODO:
    We'll figure out the right
    DS for storing the sequence
    info later, right now a string/
    list is good enough
    '''
    import re
    # first look for file with particular
    # signature in ./data/__file__ directory
    # if it exists, then read it
    # make sure than newline characters are taken
    # care of and that the file only has the 
    # requisite sequence data only.

    if re.fullmatch("[a-z0-9]*_[a-z0-9]*_oric.txt", filename):
        data_path = os.path.join(os.getcwd(), 'data')
        if os.path.isdir(data_path):
            os.chdir(data_path)
            file_path = os.path.join(os.getcwd(), filename)
            try:
                file_size = os.path.getsize(file_path)
            except OSError:
                print("Either file doesn't exist or is inaccessible")
                sys.exit(1)
            # Now, the file is avaiable
            seq_data = ""
            with open(file_path, 'r') as f:
                seq_data = "".join(f.read().split("\n"))
        return seq_data
    else:
        print("Filename doesn't match format")
        sys.exit(1)

def usage():
    print("Usage: 1) {} <genus>_<species>_oric.txt <dir> FOR ACCESSING FILES IN ./data/".format(sys.argv[0]))
    print("       2) {} <Genus>_<species>_oric_prediction.txt <dir> FOR ACCESSING FILES IN ./res/".format(sys.argv[0]))
    sys.exit(1)

def create_file_template(g, s, dirname):
    if dirname == "data":
        filename = "{}_{}_oric.txt".format(g.lower(), s.lower())
    else:
        filename = "{}_{}_oric_prediction.txt".format(g.lower().title(), s.lower())
    return filename

'''
For given organism find matching
k-mers that were found with given data
and from skew prediction

Search in :
freq_kmers/ondata and 
freq_kmers/onprediction
'''
def match():
    d = ['GATCAACGT', 'AAGAATGAT', 'AGCATGATC', 'TGATCATCG', 'GATCATCGT', 'CTCTTGATC', 'TGATCATGG', 'ATGATCATG', 'CCTCTTGAT', 'TGATCAAGG', 'CTTGATCAT', 'GAATGATCA', 'AGAATGATC', 'TTGATCATC', 'GCTCTTGAT', 'AAGCATGAT', 'ATGATCAAG', 'GATGATCAA', 'CATGATCAT', 'GCATGATCA', 'AGCTCTTGA', 'ATGATCAAC', 'GATCAAGGT', 'TGATCAACG', 'AATGATCAA', 'CATGATCAA', 'TGATCAAGA', 'TGATCAAGC', 'TCTTGATCA', 'TTGATCATG']

    p = ['TTGCATCAT', 'TTGAATCAT']
    smlr = p if len(p) <= len(d) else d
    matches = set([v for v in smlr if v in d])
    return list(matches)

def get_freq_kmers(g,s,dirname):
    FILE_PATH = os.path.join(os.getcwd(), 'freq_kmers/{}/{}'.format(filename))
    if os.path.isfile(FILE_PATH):
        pass

if __name__ == '__main__':
    S = "AACAAGCATAAAAACATTAAAGAG"
    w = "AAAAA"
    #print(pattern_count(S,w))
    #print(pattern_count_w_mis(S,w,1))
    #print(frequent_word(S,5))
    #print(most_freq_kmers(S))
    #S_oric_region= read_dna_file(sys.argv[1])
    #print(freq_9_kmers_with_compliment(S_oric_region, 1))

    if len(sys.argv) < 4:
        usage()
    else:
        filename = create_file_template(sys.argv[1], sys.argv[2], sys.argv[3])
        if sys.argv[3] == "data":
            S_oric_region= read_dna_file(filename)
        elif sys.argv[3] == "res":
            S_oric_region= read_oric_region(filename)
            S_oric_region.upper()
        print(freq_9_kmers_with_compliment(S_oric_region, 1))

    #print(match())

    # complete process time for call to most_freq_kmers (system + user CPU time)
    '''
    import time
    start = time.process_time()
    _ = most_freq_kmers(S_vib_cho_oric)
    end = time.process_time() - start
    print("{0:.5f} seconds".format(end)) # take roughly 11 seconds to finish
    '''

    '''
    TODO: Make timeit work
    import timeit
    pp(timeit.timeit('most_freq_kmers(read_dna_file("vibrio_cholerae_oric.txt"))', setup="from __main__ import most_freq_kmers, read_dna_file"))
    '''

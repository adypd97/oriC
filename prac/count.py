#!/usr/bin/env python3

'''
Count a k-mer in a given DNA sequence, where
k is the length of the short 'word'.

AND 

Also, find most frequent k-mer within the sequence.
'''

from pprint import pprint as pp

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


def frequent_word(S, k):
    '''
    Given s sequence S and number k
    Find most frequent k-mers in S 
    and return them.

    TODO:NOT VERY EFFICIENT : O(len(S)^2*k)
    '''

    kmer_count_dict = {}
    S = S.upper()
    i = 0
    while 1:
        if i == len(S) - k + 1:
            break
        w = S[i:i+k]
        kmer_count_dict[w] = pattern_count(S,w)
        i += 1
    freq_kmer_dict = {}
    max_freq_kmer = max(kmer_count_dict.values())
    for k,v in kmer_count_dict.items():
        if v == max_freq_kmer:
            freq_kmer_dict[k] = v

    return freq_kmer_dict

def most_freq_kmers(S):
    ''' 
    Return most frequent kmers
    for all k ; 3 <= k <= len(S) - 2
    '''
    len_S = len(S)
    most_freq_kmers_dict = {}
    for i in range(3, len_S-1):
        kmer_dict = frequent_word(S,i)
        kmer_dict_freq_values = list(kmer_dict.values())
        if kmer_dict_freq_values[0] == 1:
            # any word that appeared only once
            # can be skipped
            continue
        else:
            most_freq_kmers_dict[str(i)+'-mer'] = kmer_dict
        
    return most_freq_kmers_dict

        
def read_dna_file(filename):
    ''' 
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
    import os
    import sys
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

if __name__ == '__main__':
    S = "ACAACTATGCATACTATCGGGAACTATCCT"
    w = "ACTAT"
    #print(patter_count(S,w))
    #print(frequent_word(S,5))
    #print(most_freq_kmers(S))
    S_vib_cho_oric = read_dna_file("vibrio_cholerae_oric.txt")
    print(most_freq_kmers(S_vib_cho_oric))
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

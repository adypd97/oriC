#!/usr/bin/env python3

'''
Count a k-mer in a given DNA sequence, where
k is the length of the short 'word'.

AND 

Also, find most frequent k-mer within the sequence.
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

        

if __name__ == '__main__':
    S = "ACAACTATGCATACTATCGGGAACTATCCT"
    w = "ACTAT"
    #print(patter_count(S,w))
    #print(frequent_word(S,5))
    #print(most_freq_kmers(S))

    

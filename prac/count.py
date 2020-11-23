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
    '''
    kmer_count_dict = {}
    i = 0
    while 1:
        if i == len(S) - k + 1:
            break
        w = S[i:i+k]
        kmer_count_dict[w] = pattern_count(S,w)
        i += 1
    freq_kmer_dict = {}
    for k,v in kmer_count_dict.items():
        if v == max(kmer_count_dict.values()):
            freq_kmer_dict[k] = v

    return freq_kmer_dict

        

if __name__ == '__main__':
    S = "ACAACTATGCATACTATCGGGAACTATCCT"
    w = "ACTAT"
    #print(patter_count(S,w))
    print(frequent_word(S,5))

    

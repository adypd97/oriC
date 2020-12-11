#!/usr/bin/env python3

def complement(S):
    '''
    Given a DNA sequence S (in 5' -> 3')
    return the complementary (in 3' -> 5')
    '''
    if integrity_check(S):
        lookup = { 'a' : 't', 'g' : 'c' , 't' : 'a', 'c' : 'g' }
        comp_S = [lookup[n] for n in S]
    else:
        return "Sequence seems to be corrupted, \
                    integrity_check failed!"

    assert len(comp_S) == len(S), "length complementary sequence  \
                                    must match given sequence"
    return ''.join(comp_S)

def integrity_check(S):
    ''' 
    Given a DNA sequence S, 
    return if it is composed only
    of nucleotides A, T, G or C
    in other words, see if integrity is 
    maintained
    '''
    N = ['a', 't', 'g', 'c']
    status = [True if n in N else False for n in S]
    return all(status)
    

if __name__ == "__main__":
    S = "aatttggtgccaaaaaccccc"
    assert complement(S) == "ttaaaccacggtttttggggg"



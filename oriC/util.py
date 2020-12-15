#!/usr/bin/env python3

class SequenceError(Exception):
    pass

def complement(S):
    '''
    Given a DNA sequence S (in 5' -> 3')
    return the complementary (in 3' -> 5')
    '''
    S = S.upper()
    if integrity_check(S):
        lookup = { 'A' : 'T', 'G' : 'C' , 'T' : 'A', 'C' : 'G' }
        comp_S = [lookup[n] for n in S]
    else:
        raise SequenceError("Sequence seems to be corrupted, \
                    integrity_check failed!")

    assert len(comp_S) == len(S), "length complementary sequence  \
                                    must match given sequence"
    return ''.join(comp_S)[::-1]

def integrity_check(S):
    ''' 
    Given a DNA sequence S, 
    return if it is composed only
    of nucleotides A, T, G or C
    in other words, see if integrity is 
    maintained
    '''
    N = ['A', 'T', 'G', 'C']
    status = [True if n in N else False for n in S]
    return all(status)
    

def get_kv(k):
    import sys
    '''
    Return the line in file which has k in it
    '''
    k = k.split()
    assert len(k) == 2, "{}".format(k)
    k = ''.join([k[0].title(), "_", k[1].lower()])
    linkfile = "./linkfile"
    with open(linkfile) as f:
        for line in f.readlines():
            if line.split()[0] == k:
                 return tuple(line.split())
    print("Files related to '{}' weren't found".format(k), file=sys.stderr);
    return (None, None)

    

if __name__ == "__main__":
    #S = "aatttggtgccaaaaaccccc"
    #assert complement(S) == "ttaaaccacggtttttggggg"
    print(complement("atgatcaag"))
    ORG, FGIB = get_kv("vbrio cholerae")

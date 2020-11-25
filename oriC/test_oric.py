#!/usr/bin/env python3

''' Tests '''

import unittest
from oric import pattern_count, frequent_word, most_freq_kmers



class TestCountMethods(unittest.TestCase):

    def test_pattern_count(self):
        S = "ACAACTATGCATACTATCGGGAACTATCCT"
        w = "ACTAT" 
        self.assertEqual(pattern_count(S,w), 3) 

    
    def test_frequent_word(self):
        S = "ACAACTATGCATACTATCGGGAACTATCCT"
        k = 5
        expected = {'ACTAT': 3}
        self.assertEqual(frequent_word(S,k), expected)

    def test_most_freq_kmers(self):
        S = "CAACTATGCATACTATCGGGAACTATCCT"
        expected = {'3-mer': {'ACT': 3, 'CTA': 3, 'TAT': 3}, '4-mer': {'ACTA': 3, 'CTAT': 3}, '5-mer': {'ACTAT': 3}, '6-mer': {'AACTAT': 2, 'ACTATC': 2}}
        self.assertEqual(most_freq_kmers(S), expected)

if __name__ == '__main__':
    unittest.main()

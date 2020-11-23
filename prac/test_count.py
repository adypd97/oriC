#!/usr/bin/env python3

''' Tests '''

import unittest
from count import pattern_count, frequent_word     


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

if __name__ == '__main__':
    unittest.main()

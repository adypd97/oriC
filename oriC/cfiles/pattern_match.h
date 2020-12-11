#ifndef __PATTERN_MATCH_H__
#define __PATTERN_MATCH_H__
#include <inttypes.h>

typedef uint32_t LONG;


enum NCODE { a = 1, c = 2, g = 3, t = 4};
enum NCODE ncode;

LONG hash(char *S);  // hash function 
LONG rolling_hash(char *S);  // hash function 

int compare_hash(LONG h1, LONG h2); // compare hash from text segment(h1) to pattern hash h2

LONG * pattern_match(char *T, char *p, size_t n, size_t m);   // return pointer to array with starting locations
					                      // of matches for p(pattern) in T (target/text)



#endif /*__PATTERN_MATCH_H__*/

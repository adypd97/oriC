#ifndef __PATTERN_MATCH_H__
#define __PATTERN_MATCH_H__
#include <inttypes.h>

typedef uint32_t LONG;


enum NCODE { a = 1, c = 2, g = 3, t = 4};
enum NCODE ncode;

LONG hash(char *S);  // hash function 

LONG * rabin_karp(char *T, char *p);   // return pointer to array with starting locations
					 // of matches for p(pattern) in T (target/text)



#endif /*__PATTERN_MATCH_H__*/

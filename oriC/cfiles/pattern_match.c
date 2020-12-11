#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <math.h>
#include <limits.h>
#include "pattern_match.h"
#define safer_free(p) {free(p); (p) = NULL;}

int main(int argc, char* argv[argc]){

	char *S = "ccatgacttgaa";
	char pattern[] = "atgacttga";
	size_t n = strlen(S);
	size_t m = strlen(pattern);

	LONG *start_locations = pattern_match(S, pattern, n, m);
	if (start_locations) {
		for(size_t i = 0; i < n-m+1; i++)
			printf("%u \n", *(start_locations + i));
		free(start_locations);
	}

	return 0;
}

LONG * pattern_match(char *T, char *p, size_t n , size_t m) {
	LONG *start_locations = malloc(sizeof(LONG)*(n-m+1));
	if (!start_locations)
		return NULL;

	LONG pattern_hash = hash(p); // pattern_hash;

	char temp[m+1];
	memset(temp, 0, sizeof(temp));
	//LONG temp_hash = 0L;
	int status = 1; // default is no match

	for(size_t i = 0; i < n - m + 1; i++) { // how many time we move along text n - m
		for(size_t j = i; j < i + m; j++) {
			strncat(temp, &T[j], 1);
			//printf("%d %d\n", i, j);
		}
		status = compare_hash(hash(temp), pattern_hash);
		if (status == 0) {
			start_locations[i] = (LONG)i;
		}
		memset(temp, 0, sizeof(temp));
	}
	return start_locations;
}

int compare_hash(LONG h1, LONG h2) {
	return h1 == h2 ? 0 : 1; // 0 is success, 1 is failure of match
}

LONG hash(char *S) {
	LONG hash_value = 0L;
	size_t n = strlen(S);
	for(size_t i = 0; i < n; i++) {
		if (S[i] == 'a')
			ncode = a;
		else if (S[i] == 'c')
			ncode = c;
		else if (S[i] == 't')
			ncode = t;
		else
			ncode = g;
		hash_value = (hash_value + ncode*((LONG) pow(4, n-1-i))) % UINT_MAX;
	}
	//static LONG prev_hash = hash_value;
	return hash_value;
}


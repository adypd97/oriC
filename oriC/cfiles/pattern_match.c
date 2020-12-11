#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <math.h>
#include "pattern_match.h"
#define safer_free(p) {free(p); (p) = NULL;}

int main(int argc, char* argv[argc]){

	char S[] = "ccaccaaegta";
	//printf("%s\n", S);
	char pattern[] = "atgacttga";
	LONG hash_value = hash(pattern);
	//printf("Hash value %u\n", hash_value);
	return 0;
}


LONG hash(char *S) {
	LONG hash_value = 0L;
	size_t n = strlen(S);
	printf("%s\n", S);
	for(size_t i = 0; i < n; i++) {
		if (S[i] == 'a')
			ncode = a;
		else if (S[i] == 'c')
			ncode = c;
		else if (S[i] == 't')
			ncode = t;
		else
			ncode = g;
		hash_value += ncode*((LONG) pow(4, n-1-i));
	}

	return hash_value;
}


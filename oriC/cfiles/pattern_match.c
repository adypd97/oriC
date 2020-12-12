#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <math.h>
#include <limits.h>
#include "pattern_match.h"
#define safer_free(p) {free(p); (p) = NULL;}
#define error_msg() {fprintf(stderr, "Error!!\n"); exit(1);}
#define MAXLINE 60  // TODO: Exact specific values for vibrio_cholerae_oric.txt file
#define LINES 10    // 60 characters per line ending in \n (59 + 1) and 10 lines


// TODO: Refactor main() 
int main(int argc, char* argv[argc]){
	if (argc < 2) {
		fprintf(stderr, "Usage: %s <k-mer-pattern> <organism_name>\n", argv[0]);
		exit(1);
	}

	char *org_name = argv[2];
	size_t org_name_len = strlen(org_name);
	char S[MAXLINE*LINES];
	char line[MAXLINE];
	size_t in_file_len = 17 + org_name_len;
	char in_file[in_file_len];
	sprintf(in_file, "../data/%s_oric.txt", org_name);
	FILE *f = fopen(in_file, "r");
	if (ferror(f)) {
		error_msg();
	}
	while (1) {
		fgets(line, sizeof(line), f);
		if (feof(f))
			break;
		size_t n = strlen(line);
		line[n-1] = '\0';
		strncat(S, line, n);
	}
	if (fclose(f) == EOF) {
		error_msg();
	}


	char *pattern = argv[1];                              // get the k-mer pattern from command line
	size_t n = strlen(S);
	size_t m = strlen(pattern);

	size_t outfile_len = 20 + m + strlen(org_name);
	char out_file[outfile_len];
	sprintf(out_file, "../res/%s-locations-%s.txt", pattern, org_name);
	printf("here\n");

	FILE *o_f = fopen(out_file, "w");
	if (ferror(o_f)) {
		error_msg();
	}
	fprintf(o_f, "%zu-mer : %s\n", m, pattern);
	fprintf(o_f, "START LOCATIONS of '%s' in given Sequence \n", pattern);

	printf("here\n");

	LONG *start_locations = pattern_match(S, pattern, n, m);
	if (start_locations) {
		for(size_t i = 0; i < n-m+1; i++) {
			if (*(start_locations + i) != 0)
				fprintf(o_f, "%u \n", *(start_locations + i));
			//printf("%u \n", *(start_locations + i));
		}
		safer_free(start_locations);
	}

	if (fclose(o_f) == EOF) {
		error_msg();
	}

	printf("here\n");

	return 0;
}

LONG * pattern_match(char *T, char *p, size_t n , size_t m) {
	LONG *start_locations = malloc(sizeof(LONG)*(n-m+1)); // TODO: this is not a very space efficient strategy actually
							      // this is very bad space wise imagine if n ~ 3*10^9
							      // perhaps use a linked list DS.
	if (!start_locations)
		return NULL;

	LONG pattern_hash = hash(p);                          // pattern_hash;

	char temp[m+1];
	memset(temp, 0, sizeof(temp));
	int status = 1;                                       // default is no match

	for(size_t i = 0; i < n - m + 1; i++) {               // how many time we move along text n - m
		for(size_t j = i; j < i + m; j++) {
			strncat(temp, &T[j], 1);
		}
		status = compare_hash(hash(temp), pattern_hash);
		if (status == 0 && strcmp(temp, p) == 0) {
			start_locations[i] = (LONG)i;
			status = 1;
		}
		memset(temp, 0, sizeof(temp));
	}
	return start_locations;
}

int compare_hash(LONG h1, LONG h2) {
	return h1 == h2 ? 0 : 1;                               // 0 is success, 1 is failure of match
}

// TODO: make this into a rolling hash function as 
// intended in rabin-karp string matching algorithm
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
	return hash_value;
}


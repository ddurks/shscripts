#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CHOMP(s)    (s[strlen(s) - 1] = 0)

char *sanitize_string(char *s) {
    char *sanitized = malloc(strlen(s));
    char *writer    = sanitized;
    char *reader    = s;

    while (*reader != 0) {
    	if (isalpha(*reader)) {
    	    *writer = *reader;
    	    writer++;
	}
	reader++;
    }

	sanitized[strlen(sanitized)] = 0;
    return sanitized;
}

bool is_palindrome(const char *s) {
    const char *front = s;
    const char *back  = s + strlen(s)-1;

    while (front < back && *front == *back) {
    	front++;
    	back--;
    }

    return (*front == *back);
}

int main(int argc, char *argv[]) {
    char *buffer = malloc(BUFSIZ);
    char *sanitized;
    char *result = malloc(BUFSIZ);

    while (fgets(buffer, BUFSIZ, stdin)) {
    	CHOMP(buffer);

    	sanitized = sanitize_string(buffer);
    	result    = is_palindrome(sanitized) ? "" : "not ";

    	printf("%s is %sa palindrome!\n", buffer, result);
    	free(sanitized);
    }
	free(result);
	free(buffer);
	
    return EXIT_SUCCESS;
}

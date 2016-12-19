all: is_palindrome.c
	gcc -g -Wall is_palindrome.c -o is_palindrome

is_palindrome: is_palindrome.c
	gcc -g -c -Wall is_palindrome.c

test: is_palindrome.c is_palindrome.input is_palindrome.output
	diff is_palindrome.input is_palindrome.output

clean:
	rm *o is_palindrome

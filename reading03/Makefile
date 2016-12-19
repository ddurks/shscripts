all: hello

hello: hello-dynamic hello-static hello-debug hello-profile
	gcc hello-dynamic hello-static hello-debug hello-profile -o hello
hello-dynamic: hello.c
	gcc -c -dynamic hello.c 
hello-static: hello.c
	gcc -c -static hello.c
hello-debug: hello.c
	gcc -c -g hello.c
hello-profile: hello.c
	gcc -c -pg hello.c
clean:
	rm *o hello
Reading 06
==========

#1

	$ echo "All your bases are belong to us" | tr [:lower:] [:upper:]


#2

	$ cat /etc/passwd | cut -d: -f1,7 | grep root | colrm 1 5


#3

	$ echo "monkeys love bananas" | sed -e 's/monkeys/gorillas/g'


#4

	$ cat /etc/passwd | sed -e 's:/bin/sh:/usr/bin/python:g' -e 's:/bin/tcsh:/usr/bin/python:g' -e 's:/bin/bash/:/usr/bin/python:g' | grep python


#5

	$ echo "     monkeys love bananas" | sed -e 's/^ *//g'


#6

	$ cat /etc/passwd | grep '4.*7'


#7

	$ tail -f


#8

	$ comm -12 file1 file2


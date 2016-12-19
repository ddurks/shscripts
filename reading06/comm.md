TLDR - comm
==========

Overview
--------

**comm** - compare two files line by line
	-1 suppress lines unique to file1
	-2 suppress lines unique to file2
	-3 suppress lines common to both files

	(any combo of all three options is acceptable)

Examples
--------

- compare and display only lines common to both

	$ comm -12 file1 file2


Resources
---------

- [Man7 - comm](http://man7.org/linux/man-pages/man1/comm.1.html)
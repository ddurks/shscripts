TLDR - chmod
==========

Overview
--------

**chmod** - changes file mode bits

	- 4 = read permissions
	- 2 = write permissions
	- 1 = execute permissions

Examples
--------

- permissions to yourself only

	$ chmod 700 filename

- permissions to every user

	$ chmod 777 filename

- full permissions for self, read only for everyone else

	$ chmod 744 filename

Resources
---------

- [Man7 - chmod](http://man7.org/linux/man-pages/man1/chmod.1.html)
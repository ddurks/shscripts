General Overview of Awk
=======================

Awk is a powerful text processor for manipulating text and data.

Printing Specific Fields
------------------------
You can print specific fields using awk:

	$ awk '/search_pattern/ {print}' filename


Using BEGIN and END
-------------------
There are BEGIN and END blocks which can be used to execute commands before and after the file processing. The syntax is as follows:

	$ awk 'BEGIN{commands;} /search_pattern/ {commands;} END{commands;}' filename


Modifying FS
------------
You can change the current field separator using:

	$ awk 'BEGIN { FS=":" } {print $1}' filename

This sets the new separator as : instead of the default which is whitespace


Using Pattern Matching
----------------------

Pattern matching uses regular expressions. In addition, you can use variables $1 to refer to column one and so on, as well as $0 to refer to an entire line. For example:

	$ awk '$2 ~ /^name/'

This example only prints the second column of the line starting with "name"

Special Variables
-----------------
There are a set of special variables which can be used to assign certain pieces of information as a file is processed. For example

	FILENAME - references current input file
	FS - references the current field separator (whitespace by default)
	NF - the number of fields in the current record
	NR - the number of the current record


Associative Arrays
------------------
Associative arrays are powerful tools in which members of an array are referenced by a string instead of an integer. They can be used with the following syntax:

	$ awk 'BEGIN{array[""]=0} /search_pattern/ {name[$2]++} END{for(i in name){print name[i], i;}}' filename
Homework 07
===========

Activity 1
----------

#1
I parsed the command line options by first creating an array called args of all of the command line arguments, splitting each at the = using args.split('='). Then, for o, a in args I tested if o was equal to any of the options, and, if so, I set the appropriate variable equal to the variable a.

#2
In order to open the input and output files I used os.open(). For the source file I used the mode os.O_RDONLY, while for the target file I used os.O_WRONLY|os.O_CREAT|os.O_TRUNC

#3
I utilized the seek and skip arguments through an implementation of the os.lseek() command. Every time reading and writing was done I used lseek to start at seek*bs or skip*bs respectively.

#4
I utilized count and bs, by using count as the condition in a while loop. Meaning that the program will only continue reading data while there is data left to be read, and the amount of blocks read in is less than the count variable. With each iteration, bs bytes are transferred.


Activity 2
----------

#1
In order to parse the command line options, I once again made an array called args with all of the options. Then, if there is at least one option, and that option is the name of a directory (os.path.isdir()) I set the first index in the args list to be the dirpath or the directory to work in. Then, I go through the remaining options using the enumerate() command to allow access to adjacent indices. If the option is equal to one of the expected options, then a variable is set accordingly

#2
I walked the directory tree using this for loop:
  
  $ for root, dirs, files in os.walk(dirpath, followlinks = True):
	  	for fname in files:
			fpath = os.path.join(root, fname)
			if include(fpath) != 0:
				print include(fpath)

Which recursively goes through each member and follows all symbolic links

#3
I determined whether or not to print a filesystem objects path by utilizing an include(path) function, which returns the name of a path if the output of all of the test functions is 1. There is a test function for each option. In each of these, there is first an if statement which tests if there is was an option provided by the user. If there was, then a series of conditionals are provided, and the proper output is returned by the result integer. A 1 for a success, a 0 for a failure

#4
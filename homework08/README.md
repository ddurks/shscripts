Homework 08
===========


Activity 1
----------
#1
The parent process keeps track of the child process via os.wait, and it also signals the child process. The child process executes the command and exits when the alarm goes off.

#2
The timeout mechanism worked by setting an alarm and an alarm handler. In the alarm handler was an os.kill call in order to kill the child process.

#3
The test script verifies the correctness of the program by going through a series of if statements and assessing the performance of the timeout.py program at each one compared to what is expected.

#4
If I set seconds and sleep to the same duration, then it kills the alarm each time.

Activity 2
----------
#1
I looped through the filesystem using os.walk. Then, for each name, I checked if it matched the pattern and then added it to my paths dict if it was not already present using my addFiles function.

#2
I loaded the rules using the following:
	$ with open(RULES, 'r') as fileIN:
	  document = yaml.load(fileIN)
and then setting the ACTION and PATTERN variables appropriately using a dict. I then used these variables to check the files and execute the proper action.

#3
I used a dictionary to keep track of and detect changes to files, and I used an associated value from the output of os.path.mtime to detect whether or not a file had been modified

#4
I executed each action by creating an execute function which created a parent and child, and then executed the action in the child.

#5
Rorschach.py sufferes from busy waiting in that it is constantly looping through the directory over and over again in order to find the files that have been modified. This could be fixed by somehow first being able to detect that a modification had been made and only then looping through the directory to find the modified file. One could also mitigate busy waiting in this program by eliminating the constant loop entirely and checking in a different way that didn't involve constant checking. One could implement cache invalidation by deleting allocated memory at times.


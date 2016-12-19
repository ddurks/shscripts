#!/usr/bin/env python2.7

import sys
import os
import tempfile

files = []

for name in sys.argv[1:]:
	if os.path.isfile(name):
		files.append(name)
	else:
		print "\"%s\" does not exist or is not a file" % name

f = tempfile.NamedTemporaryFile()
fd = os.open(f.name, os.O_WRONLY|os.O_CREAT|os.O_RDONLY)

for filename in files:
	os.write(fd,filename + "\n")

os.system('nano %s' % f.name)

with open(f.name) as temp:
	newnames = temp.readlines()

newfiles = []
for newname in newnames:
	newname = newname.rstrip("\n")
	newfiles.append(newname)

for currentfile, newfile in zip(files, newfiles):
	try:
		os.rename(currentfile, newfile)
	except OSError:
		print "Error in renaming", currentfile

f.close()
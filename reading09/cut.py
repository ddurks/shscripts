#!/usr/bin/env python2.7

import getopt
import sys
import re

delim = ' '

try:
	opts, args = getopt.getopt(sys.argv[1:], 'd:f:')
except getopt.GetoptError as e:
	print e

if len(args) == 0:
	args.append('-')

for path in args:
	if path == '-':
		stream = sys.stdin
	else:
		stream = open(path)

	for o, a in opts:
		if o == '-d':
			delim = a
		elif o == '-f':
			arg = str(a)
			fields = arg.split(',')
		else:
			print "error, use -d or -f"

	for line in stream.readlines():
		words = line.split(delim)
		for field in fields:
			if(len(words) >= (int(field))):	
				words.pop(int(field)-1)
		print (delim.join(words)).rstrip()


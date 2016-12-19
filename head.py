#!/usr/bin/env python2.7

import getopt
import sys

amnt = 10

lines = []

try:
	opts, args = getopt.getopt(sys.argv[1:], 'n:')

except getopt.GetOptError as e:
	print e

if len(args) == 0:
	args.append('-')

for path in args:
	if path == '-':
		stream = sys.stdin
	else:
		stream = open(path)

	for line in stream.readlines():
		lines.append(line)
	
	for o, a in opts:
		if o == '-n':
			amnt = int(a)	
		else:
			print "error"
		
	for i in range(amnt):
		print lines[i].rstrip()

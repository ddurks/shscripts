#!/usr/bin/env python2.7

import sys
import getopt

nums = 0

try:
	opts, args = getopt.getopt(sys.argv[1:], 'c')

except getopt.GetOptError as e:
	print e

if len(args) == 0:
	args.append('-')

for path in args:
	if path == '-':
		stream = sys.stdin
	else:
		stream = open(path)

	for o, a in opts:
		if o == '-c':
			nums = 1
		else:
			print "error, unrecognized flag"

	lines = {}
	for line in stream.readlines():
		line = line.strip()
		if line in lines:
			lines[line] += 1
		else:
			lines[line] = 1
			
	for key, val in lines.items():
		if nums == 1:		
			print val, ":", key
		else:
			print key

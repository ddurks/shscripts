#!/bin/env python2.7

import sys
import re
import getopt

newlines = 0
words = 0
characters = 0

try:
	opts, args = getopt.getopt(sys.argv[1:], 'clw')
except getopt.GetoptError as e:
	print e
	sys.exit(2)

if len(args) == 0:
	args.append('-')

for path in args:
	if path == '-':
		stream = sys.stdin
	else:
		stream = open(path)

	for line in stream.readlines():
		newlines += 1
		characters += len(line)
		words += len(re.findall(r'\w+',line))

	if len(opts) == 0:
		print "error, please provide an option"
		sys.exit(2)

	print path
	for o, a in opts:
		if o == "-c":
			print "characters: "+ str(characters)
		elif o == "-l":
			print "newlines: "+ str(newlines)
		elif o == "-w":
			print "words: "+ str(words)
		else:
			print "error: unknown flag... use -w for wordcount, -c for character count, -l for newline count"

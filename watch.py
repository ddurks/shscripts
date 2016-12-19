#!/usr/bin/env python2.7

import getopt
import sys
import os
import time

INTERVAL = 2
go = 1

try:
	opts, args = getopt.getopt(sys.argv[1:], 'n:')

except getopt.GetOptError as e:
	print e

for o, a in opts:
	if o == '-n':
		INTERVAL = int(a)	
	else:
		print "error, incorrect option"

COMMAND = " ".join(args)

try:
	while go:
		os.system("clear")
		print "Every", INTERVAL, "seconds:", COMMAND
		print " "
		os.system(COMMAND)
		time.sleep(INTERVAL)
except KeyboardInterrupt:
	sys.exit(1)
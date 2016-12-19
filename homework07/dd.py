#!/usr/bin/env python2.7

import sys
import os

source = 0
target = 1
bs = 512
count = sys.maxint
iif = 0
oof = 0
seek = 0
skip = 0

args = []
for arg in sys.argv[1:]:
	args.append( arg.split('=') )
	
for o, a in args:
	if o == 'if':
		iif = 1
		try:
			source = os.open(str(a), os.O_RDONLY)
		except OSError as e:
			print >>sys.stderr, 'could not open file {}: {}'.format(str(a), e)
			sys.exit(1)	
	elif o == 'of':
		oof = 1
		try:
			target = os.open(str(a), os.O_WRONLY|os.O_CREAT|os.O_TRUNC)
		except OSError as e:
			print >>sys.stderr, 'could not open file {}: {}'.format(str(a), e)
			sys.exit(1)
	elif o == 'count':
		count = int(a);
	elif o == 'bs':
		bs = int(a);
	elif o == 'seek':
		seek = int(a);
	elif o == 'skip':
		skip = int(a);
	else:
		print "error"

blockcount = 1;
skipstart = skip*bs
seekstart = seek*bs

if(source!=0):
	os.lseek(source, skipstart, os.SEEK_SET)
data = os.read(source, int(bs))
skipstart += bs*count
					
while data and blockcount <= count:
	if(target!=1):
		os.lseek(target, seekstart, os.SEEK_SET)
		seekstart += bs*count
		os.lseek(source, skipstart, os.SEEK_SET)
		skipstart += bs*count	
	os.write(target, data)
	data = os.read(source, int(bs))
	blockcount += 1;
	
os.close(source)
os.close(target)

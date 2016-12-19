#!/usr/bin/env python2.7

import sys
import os
import re
from pwd import getpwuid
import fnmatch

typeIn=executable=readable=writable=empty=name=pathIn=regex=perm=newer=uid=gid=0 
dirpath = os.curdir

args = []
for arg in sys.argv[1:]:
	args.append(arg)

if len(args)>=1 and os.path.isdir(args[0]):
	dirpath = args[0]

for index, arg in enumerate(args):
	if arg == '-type':
		typeIn = args[index+1]
	elif arg == '-executable':
		executable = 1
	elif arg == '-readable':
		readable = 1
	elif arg == '-writable':
		writable = 1
	elif arg == '-empty':
		empty = 1
	elif arg == '-name':
		name = args[index+1]
	elif arg == '-path':
		pathIn = args[index+1]
	elif arg == '-regex':
		regex = args[index+1]
	elif arg == '-perm':
		perm = args[index+1]
	elif arg == '-newer':
		newer = args[index+1]
	elif arg == '-uid':
		uid = args[index+1]
	elif arg == '-gid':
		gid = args[index+1]

def typeTest(path):
	result = 1
	if typeIn != 0:
		if(os.path.isfile(path)):
				typeTest = 'f'
		elif(os.path.isdir(path)):
				typeTest = 'd'
		if typeIn == typeTest:
				result = 1
		else:
				result = 0
	return result

def readTest(path):
	result = 1
	if readable != 0:
		if(os.access(path, os.R_OK)):
			result = 1
		else:
			result = 0
	return result

def writeTest(path):
	result = 1
	if writable != 0:
		if(os.access(path, os.W_OK)):
			result = 1
		else:
			result = 0
	return result

def executeTest(path):
	result = 1
	if executable != 0:
		print path
		print os.access(path, os.X_OK)
		print ' '
		if(os.access(path, os.X_OK)):
			result = 1
		else:
			result = 0
	return result

def emptyTest(path):
	result = 1
	if empty != 0:
		if not os.listdir(path):
			result = 1
		else:
			result = 0
	return result

def nameTest(path):
	result = 1
	if name != 0:
		if os.path.basename(path) == name:
			result = 1
		else:
			result = 0
	return result

def pathTest(path):
	result = 1
	if pathIn != 0:
		if fnmatch.fnmatch(path, pathIn):
			result = 1
		else:
			result = 0
	return result

def regexTest(path):
	result = 1
	if regex != 0:
		if (re.match(regex, os.path.basename(path))):
			result = 1
		else:
			result = 0
	return result

def permTest(path):
	result = 1
	if perm != 0:
		if (oct(os.stat(path)[ST_MODE])[-3:]==perm):
			result = 1
		else:
			result = 0
	return result

def newerTest(path):
	result = 1
	if newer != 0:
		if ( os.stat(path).st_mtime > newer):
			result = 1
		else:
			result = 0
	return result

def uidTest(path):
	result = 1
	if uid != 0:
		print os.stat(path).st_uid
		if ( os.stat(path).st_uid == uid):
			result = 1
		else:
			result = 0
	return result

def gidTest(path):
	result = 1
	if gid != 0:
		if ( os.stat(path).st_gid == gid):
			result = 1
		else:
			result = 0
	return result

def include(path):
	if typeTest(path) and writeTest(path) and readTest(path) and executeTest(path) and emptyTest(path) and nameTest(path) and pathTest(path) and regexTest(path) and permTest(path) and newerTest(path) and gidTest(path) and uidTest(path):
		return path
	else:
		return 0

if include(dirpath) != 0:
	print include(dirpath)
for root, dirs, files in os.walk(dirpath, followlinks = True):
  	for fname in files+dirs:
		fpath = os.path.join(root, fname)
		if include(fpath) != 0:
			print include(fpath)
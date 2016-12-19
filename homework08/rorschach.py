#!/usr/bin/env python2.7
import getopt
import yaml
import os
import sys
import fnmatch
import time
import re
import shlex

#initializing variables
RULES = 'rorschach.yml'
SECONDS = 2
DIRECTORIES = '.'
VERBOSE = False
ACTION = ''
PATTERN = ''

#a dict for paths and a list for actions
paths = {}
action = []

#error message
def err(message, *args):
	print >>sys.stderr, message.format(*args)
	sys.exit(1)

#usage message
def usage(status=0):
	print '''Usage: rorschach.py [-r RULES -t SECONDS] DIRECTORIES...

Options:

    -r RULES    Path to rules file (default is .rorschach.yml)
    -t SECONDS  Time between scans (default is 2 seconds)
    -v          Display verbose debugging output
    -h          Show this help message'''.format(os.path.basename(sys.argv[0]))
	sys.exit(status)

#executes a given action
def execute(action):
	try:
		verbose('Forking...')
		pid = os.fork()
		if pid == 0: #Child
			try:
				if VERBOSE:	
					verbose('Execing...')
				os.execvp(action[0],action)
			except OSError as e:
				err('Execing Failed: {}', e)
		else: #Parent
			try:
				if VERBOSE:
					verbose('Waiting...')
				pid,status = os.wait()
			except OSError as e:
				err('Waiting Failed: {}', e)
	except OSError as e:
		err('Forking Failed: {}', e)

def check_file(name):
	#checks for pattern match
	if fnmatch.fnmatch(name, PATTERN): 
		#check if file is in dictionary
		if name not in paths:
			path = os.path.join(root,name)
			addFiles(name,path)
			#sets name to name variable and executes
			act = ACTION.format(name=name, path=path)
			action = shlex.split(act)
			execute(action)
		#if file isnt in dictionary
		elif name in paths:
			path = os.path.join(root,name)
			if paths[name] != os.path.getmtime(path):
				addFiles(name,path)
				#sets name to name variable and executes
				act = ACTION.format(name=name, path=path)
				action = shlex.split(act)
				execute(action)	


# checks each file in specified directory to see if it matches any of the rules
def check_dir(dirIN):
	#walk through directory
	for root, dirs, files in os.walk(dirIN):
		for name in (dirs+files):
			check_file(name)
			
#Prints out when the program is running
def verbose(message):
	print >>sys.stderr, message

#add files to the paths dict
def addFiles(name, path):
	paths[name] = os.path.getmtime(path)

#Parsing command line options
try:
	opts, args = getopt.getopt(sys.argv[1:], "r:t:vh")
except getopt.GetoptError as e:
	print e
	usage(1)

#if no arguments given, set directory to current directory
DIRECTORIES = args 
if DIRECTORIES == []:
	DIRECTORIES = '.'

#assigning variables based on command line arguments
for opt, arg in opts:
	if opt == '-r':
		RULES = str(arg)
	elif opt == '-t':
		SECONDS	= int(arg)
	elif opt == '-v':
		VERBOSE = True
	elif opt == '-h':
		usage(1)
	else:
		print "error, improper flag"
		usage(1)

#Parsing yml file
with open(RULES, 'r') as fileIN:
	document = yaml.load(fileIN)

ACTION = document["action"]
PATTERN = document["pattern"]

try:
	while True:
		for dirname in DIRECTORIES:
			check_dir(dirname)
			time.sleep(SECONDS)
			os.system('clear')
except KeyboardInterrupt:
	sys.exit(1)

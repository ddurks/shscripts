#!/usr/bin/env python2.7

import getopt
import sys
import os
import signal
import time

#instantiate variables
TIME = 10
VERBOSE = 0

#debug message function
def debug(message, *args):
	print message.format(*args)

#error message function
def error(message, *args):
	print >>sys.stderr, message.format(*args)

#usage
def usage(exit_code=0):
	error('''Usage: timeout.py [-t SECONDS] command...

Options:

      -t SECONDS  Timeout duration before killing command (default is 10 seconds)
      -v          Display verbose debugging output'''.format(os.path.basename(sys.argv[0])))

#alarm function
def receive_alarm(signum, stack):
	debug('Alarm Triggered after {} seconds!', TIME)
	debug('Killing PID {}...', os.getpid())
	os.kill(pid, signal.SIGTERM)

#parse command line arguments
try:
	opts, args = getopt.getopt(sys.argv[1:], 't:vh')
except getopt.GetoptError as e:
	print e

for o, a in opts:
	if o == '-t':
		TIME = int(a)
	elif o == '-v':
		VERBOSE = 1
	elif o == '-h':
		usage(1)
		sys.exit(0)
	else:
		usage(1)

#set up command for input into execvp
COMMAND1 = args[0]
COMMAND2 = args

if VERBOSE:
	debug('Executing "{}" for at most {} seconds...', " ".join(args), TIME)

#fork
try:
	if VERBOSE:
		debug('Forking...')
	pid = os.fork()
except OSError as e:
	error('Unable to fork: {}', e)

#child 
if pid == 0:
	try:
		if VERBOSE:
			debug('Execing...')
		#execute command
		os.execvp(COMMAND1, COMMAND2)
	except OSError as e:
		error('Unable to exec: {}', e)
#parent
else:	
	if VERBOSE:
		#set up alarm
		debug('Enabling Alarm...')
		debug('Waiting...')
	signal.signal(signal.SIGALRM, receive_alarm)
	signal.alarm(TIME)
	try:
		pid, status = os.wait()
	except OSError:
		pid, status = os.wait()
	if VERBOSE:
		debug('Disabling Alarm...')
		debug('Process {} terminated with exit status {}',pid, status)
		sys.exit(status)

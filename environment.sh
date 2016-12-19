#!/bin/bash
#prints out environment variables

cat <<- _EOF_

PATH		is $PATH
HOME		is $HOME
SHELL		is $SHELL
TERM		is $TERM
EDITOR		is $EDITOR
HOSTNAME	is $HOSTNAME
PATH		is $PATH
PWD		is $PWD
_EOF_

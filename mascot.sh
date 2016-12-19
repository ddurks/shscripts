#!/bin/bash

#mascot.sh

case $(uname) in
	Linux) echo "Tux"
	;;
	Darwin) echo "Hexley"
	;;
	FreeBSD | NetBSD | OpenBSD) echo "Beastie"
	;;
esac

#!/bin/sh

for num in $(seq 100); do
	if ./timeout.py -t 2 sleep 2; then
		echo success
	else
		echo failure
	fi
done

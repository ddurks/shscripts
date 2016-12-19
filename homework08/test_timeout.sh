#!/bin/sh
name="timeout.py"

#check if executable
if ! [ -x $name ]; then
    echo "Failed"
    echo $name "is not executable!"
    exit 1
fi

#check for shebang
FIRST=`head -n 1 timeout.py`
VALUE="#!/usr/bin/env python2.7"

if [ "$FIRST" != "$VALUE" ]; then
  echo "Shebang test failed!"
  exit 1
fi

#check standard error
LINES=$(wc -l < "timeout.py")

if ! [ "$LINES" -gt 6 ]; then
    echo "timeout -v test failed!"
    echo "$LINES"
    exit 1
fi

#check if exits with success
for time in $(seq 4); do
    if ./timeout.py -t 5 sleep $time ;then
        echo $name "exit with success failed!"
        exit 1
    fi
done

#check if exits with failure
for time in $(seq 5 2); do
    if ! ./timeout.py -t 1 sleep $time ;then
        echo $name "exit with failure failed!"
        exit 1
    fi
done

#check usage
if ! ./timeout.py -h | egrep -i "usage" > /dev/null ; then
    echo "Usage test failed!"
    exit 1
fi

#if passed all tests test was successful
echo "Test successful!"
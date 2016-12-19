#!/bin/sh

while getopts r:s: name
do
	case $name in
			r)ropt=$OPTARG;;
			s)sopt=$OPTARG;;
			*)echo "Invalid arg";;
	esac
done

if [ $ropt ]; then
	if [ $sopt ]; then
		for i in `seq $ropt`; do
			seq 1 $sopt | shuf | head -1
		done
	else
		for i in `seq $ropt`; do
			seq 1 6 | shuf | head -1
		done
	fi
elif [ $sopt ]; then
	if [ $ropt ]; then
		for i in `seq $ropt`; do
			seq 1 $sopt | shuf | head -1
		done
	else
		for i in {1..10}; do
			seq 1 $sopt | shuf | head -1
		done
	fi
else
	for i in {1..10}; do
		seq 1 6 | shuf | head -1
	done
fi

#!/bin/sh

while getopts n:a name
do
	case $name in
		n)nopt=$OPTARG;;
		a)aopt=1;;
		*)echo "Invalid arg";;
		u)echo disk_usage.sh [-a -n N] directory...
	esac
done

shift $(($OPTIND -1))

if [[ ! -z $nopt ]]; then
	
	for dir in $@; do
		
		du -h $dir | sort -nr | head -$nopt
		
	done

elif [[ ! -z $aopt ]]; then

	for dir in $@; do
			
			du -ah $dir | sort -nr | head -10

	done

else

	for dir in $@; do
		du -h $dir | sort -nr 
	done

fi



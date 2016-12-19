#!/bin/sh
#David Durkin disk_usage.sh

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
		
		du -h $dir 2>/dev/null | sort -nr | head -$nopt
		
	done

elif [[ ! -z $aopt ]]; then

	for dir in $@; do
			
			du -ah $dir 2>/dev/null | sort -nr | head -10 

	done

else

	for dir in $@; do
		du -h $dir 2>/dev/null | sort -nr | head -10
	done

fi



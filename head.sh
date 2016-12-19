#!/bin/sh


while getopts n: name
do
	case $name in
		n)nopt=$OPTARG;;
		h)echo "usage: head.sh\n\n\t-n N\tDisplay the first N lines";;
		*)echo "Invalid arg";;
	esac

done

shift $(($OPTIND -1))

if [[ ! -z $nopt ]]; then

	awk -v lines="$nopt" 'NR<=lines {print}' $1

else

	awk 'NR<=10 {print}' $1

fi
#!/bin/sh

if [ $1 ]; then

	curl -s $1 | awk '/^cpus/ {count+=$2} END{print "Total CPUs:", count;}'
	curl -s $1 | awk 'BEGIN{name[""]=0;} /^name/ {name[$2]++} END{ for(i in name){ if(i != ""){count++;} } print "Total Machines:", count;}'
	curl -s $1 | awk '/^type/ {++type[$2]} END{for(i in type)if(type[i]>most){most=type[i];k=i;} print "Most Prolific Type: " k;}'

else

	curl -s http://catalog.cse.nd.edu:9097/query.text | awk '/^cpus/ {count+=$2} END{print "Total CPUs:", count;}'
	curl -s http://catalog.cse.nd.edu:9097/query.text | awk 'BEGIN{name[""]=0;} /^name/ {name[$2]++} END{ for(i in name){ if(i != ""){count++;} } print "Total Machines:", count;}'
	curl -s http://catalog.cse.nd.edu:9097/query.text | awk '/^type/ {++type[$2]} END{for(i in type)if(type[i]>most){most=type[i];k=i;} print "Most Prolific Type: " k;}'

fi
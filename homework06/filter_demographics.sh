#!/bin/sh

awk 'BEGIN{ FS=","; } 
NR == FNR 
{ ++gender13[$1]; ++race13[$2];
++gender14[$3]; ++race14[$4]; 
++gender15[$5]; ++race15[$6]; 
++gender16[$7]; ++race16[$8]; 
++gender17[$9]; ++race17[$10]; 
++gender18[$11]; ++race18[$12]; }  
END{
	print "year thirteen";
	for(i in gender13){
		print i,'\t', gender13[i]
	};
	race13[U]=0;
	for(i in race13){
		print i,'\t', race13[i]
	};
	print "year fourteen";
	for(i in gender14){
		print i,'\t', gender14[i]
	};
	for(i in race14){
		print i,'\t', race14[i]
	};
	print "year fifteen";
	for(i in gender15){
		print i,'\t', gender15[i]
	};
	for(i in race15){
		print i,'\t', race15[i]
	};
	print "year sixteen";
	for(i in gender16){
		print i,'\t', gender16[i]
	};
	for(i in race16){
		print i,'\t', race16[i]
	};
	print "year seventeen";
	for(i in gender17){
		print i,'\t', gender17[i]
	};
	for(i in race17){
		print i,'\t', race17[i]
	};
	print "year eighteen";
	for(i in gender18){
		print i,'\t', gender18[i]
	};
	for(i in race18){
		print i,'\t', race18[i]
	};
}' | sed '/^ /d' | sed '/201.*/d' | tail -54


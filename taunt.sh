#!/bin/sh

#David Durkin taunt program

PATH=$PATH:/afs/nd.edu/user15/pbui/pub/bin
secs=10
endTime=$(( $(date +%s) + secs ))

function special {
	cowsay "This message is special as hell"
	exit 0
}

function taunt {
	cowsay "You'll have to do better than that"
}

trap special SIGHUP
trap taunt SIGINT SIGTERM

cowsay "Suh dude"

while [ $(date +%s) -lt $endTime ]; do
	true
done

cowsay "This party sucks, I'm out"


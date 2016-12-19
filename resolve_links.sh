#!/bin/bash
#resolve_links.sh

for file in $1/*; do
	if [ -L "$file" ]; then
		echo "$file links to $(readlink $file)"
	fi
done

#!/bin/bash

if [[ $* == *-h* ]] || [[ $* == *--help* ]]; then
	echo "usage: git-reveal [-vh]"					
else
	
	changesDetected=false

	defaultColour=$(tput sgr0)
	red=$(tput setaf 1)
	
	declare -a arr=($(find `pwd` -maxdepth 1 -type d))
	
	for i in "${arr[@]}"; do
		cd $i

		# is this a git dir
		if [ -d .git ]; then

			declare -a gitstatus=`git status -b`
			if [[ $gitstatus != *nothing* ]]; then
				
				# only show this message once
				if ! $changesDetected ; then
					echo "changes detected in:"
					changesDetected=true
				fi
				
				# which repos have changes
				echo "$red $i $defaultColour"
				
				# -v verbose, show changes
				if [[ $* == *-v* ]]; then
					git status -s
					echo ""					
				fi
			fi
		fi
	done

	if ! $changesDetected ; then
		echo "no changed detected"
	fi

fi

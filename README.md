# git-reveal

**git-reveal** finds all the git repositories in the current directory and reveals whether they have any changes to be commit.

## Example

	$ cd my-code-dir
	$ git-reveal
	changes detected in:
	
	/home/you/my-code-dir/repo1
	/home/you/my-code-dir/repo2
	/home/you/my-code-dir/repo3
		
Verbose
		
	$ git-reveal -v
	changes detected in:
	
	/home/you/my-code-dir/repo1
	M README.md

	/home/you/my-code-dir/repo2
	M src/main/scala/HelloWorld.scala
	?? somefile
	
## Install

	$ sud0 ./install.sh
	$ sud0 ./uninstall.sh

## Dependencies
Tested with

	python 2.7.5
	git version 1.8.3.4
	
## To do
-a --all shows all repos, red for ones with changes, green for those without
show a summary line e.g. 22 repos, 3 with changes

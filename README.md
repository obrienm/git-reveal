# git-reveal

**git-reveal** finds all the git repositories in the current directory and reveals whether they have any changes to be commit.

## Example

	$ cd my-code-dir
	$ git-reveal
	/home/you/my-code-dir/repo1
	/home/you/my-code-dir/repo2 [changed]
	/home/you/my-code-dir/repo3 [changed]
	summary: 3 repositories, 2 with changes
		
Verbose
		
	$ git-reveal -v
	/home/you/my-code-dir/repo1
	/home/you/my-code-dir/repo2 [changed]
	M README.md
	/home/you/my-code-dir/repo3 [changed]
	M src/main/scala/HelloWorld.scala
	?? somefile
	summary: 3 repositories, 2 with changes
	
## Install

	$ sud0 ./install.sh
	$ sud0 ./uninstall.sh

## Dependencies
Tested with

	python 2.7.5
	git version 1.8.3.4

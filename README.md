# git-reveal

**git-reveal** is used to summarise all the git repositories within a directory.

## Example

	> cd my-code-dir
	> git-reveal
	  changes detected in:
	  	/home/you/my-code-dir/repo1
		/home/you/my-code-dir/repo2
		/home/you/my-code-dir/repo3
		
	> git-reveal -v
	  changes detected in:
	
	  /home/you/my-code-dir/repo1
	  M README.md

	  /home/you/my-code-dir/repo2
	  M src/main/scala/HelloWorld.scala
	  ?? somefile
	
## Install

sud0 ./install.sh

## Dependencies
git version 1.8.3.4

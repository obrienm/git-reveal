# git-reveal

**git-reveal** finds all the git repositories in the current directory and reveals whether they have any changes to be commit.

## Example

	$ git-reveal
	repo1
	repo2 [changed]
	repo3 [changed]
	summary: 3 repositories, 2 with changes
		
Verbose
	
	$ git-reveal -v
	repo1
	repo2 [changed]
	M README.md
	repo3 [changed]
	?? somefile
	summary: 3 repositories, 2 with changes
	
## Install

	$ sud0 ./install.sh
	$ sud0 ./uninstall.sh

## Dependencies
Tested with

	python 2.7.5
	git version 1.8.3.4

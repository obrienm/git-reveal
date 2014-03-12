#!/usr/bin/python

# a@moschops.me
# https://github.com/obrienm
#
# Finds all git repositories in the current directory and reveals whether they have any changes to be commit.

import sys, os, subprocess
from optparse import OptionParser

def main():
    opts, args = parse()
    repos = findRepos()
    show(repos, opts.verbose)
    summary(repos)

def parse():
    usage = "usage: git-reveal [options]"
    parser = OptionParser(usage=usage)
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", help="show all changed files")
    return parser.parse_args() 

def findRepos():
    dic = os.walk('.').next()
    root = dic[0]        
    dirs = dic[1]
    dirs.append(".")

    return filter(lambda dir: os.path.exists(dir + "/.git"), dirs)

def findReposWithChanges(repos):
    return filter(lambda repo: hasChanges(repo), repos)

def hasChanges(repo): 
    command = "cd '" + repo + "'; git status -b"
    output = subprocess.check_output(command, shell=True)
    
    if "nothing to commit, working directory clean" in output:
        return False
    else:
        return True    

def summary(repos):
    reposWithChanges = findReposWithChanges(repos)
    repStr = "repositories"
    if len(repos) == 1:
        repStr = "repository"
    
    command = 'echo "summary: ' + str(len(repos)) + ' ' + repStr + ', ' + str(len(reposWithChanges)) + ' with changes"'
    execute(command)

def show(repos, verbose):
    for repo in repos:
        if hasChanges(repo):
            command = 'echo "$(tput setaf 1)' + repo + ' [changed] $(tput sgr0)"'
            execute(command)
            if verbose:
                command = "cd '" + repo + "'; git status -s"
                execute(command)
        else:
            command = 'echo "' + repo + '"'
            execute(command)
    
def execute(command):
    print subprocess.check_output(command, shell=True).strip()     

if __name__ == "__main__":
    main()

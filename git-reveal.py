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
    parser = OptionParser(usage="usage: git reveal [options]")
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
    output = repoChanges(repo)
    
    if output == "" or "nothing to commit" in output:
        return False
    else:
        return True    

def summary(repos):
    reposWithChanges = findReposWithChanges(repos)
    repStr = "repositories"
    if len(repos) == 1:
        repStr = "repository"
    
    command = 'echo "----------------------------------------"'
    print execute(command)    
    command = 'echo "summary: ' + str(len(repos)) + ' ' + repStr + ', ' + str(len(reposWithChanges)) + ' with changes"'
    print execute(command)
    command = 'echo "----------------------------------------"'
    print execute(command)

def show(repos, verbose):
    if len(repos) >= 1:
        print execute('echo " ------------------"')        
        print execute('echo " repositories found"')        
        print execute('echo " ------------------"')        

    for repo in repos:
        if hasChanges(repo):
            rChanges = repoChanges(repo).split('\n')
            changeStr = 'changes'
            if len(rChanges) == 1:
                changeStr = 'change'
            
            command = 'echo " $(tput setaf 1)' + repo + ' [' + str(len(rChanges)) + ' ' + changeStr + '] $(tput sgr0)"'
            print execute(command)
            
            if verbose:
                for rChange in rChanges:
                    print("  " + rChange.strip())

        else:
            command = 'echo " ' + repo + '"'
            print execute(command)

def repoChanges(repo):
    command = "cd '" + repo + "'; git status --porcelain"
    return execute(command)

def execute(command):
    return subprocess.check_output(command, shell=True).strip()     

if __name__ == "__main__":
    main()

#!/usr/bin/python

# a@moschops.me
# https://github.com/obrienm
#
# Finds all git repositories in the current directory and reveals whether they have any changes to be commit.

import getopt, sys, os, subprocess


def main():
    opts, args = getOpts(sys.argv[1:])
    verbose = parseOpts(opts)    
    repos = findRepos(verbose)
    show(repos, verbose)
    summary(repos)


def parseOpts(opts):
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
        else:
            assert False, "unhandled option"
            usage()
            
    return verbose
            

def getOpts(argv):
    try:
        return getopt.getopt(argv, "hv", ["help", "verbose"])
    except getopt.GetoptError as err:
        print str(err)
        usage()


def findRepos(verbose):
    dic = os.walk('.').next()
    root = dic[0]        
    dirs = dic[1]
    dirs.append(".")
    
    absoluteDirs = map(lambda dir: os.path.abspath(os.path.join(root, dir)), dirs)
    return filter(lambda dir: os.path.exists(dir + "/.git"), absoluteDirs)


def findReposWithChanges(repos):
    return filter(lambda repo: hasChanges(repo), repos)


def hasChanges(repo): 
    command = "cd '" + repo + "'; git status -b"
    output = subprocess.check_output(command, shell=True)
    
    if "nothing" in output:
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
            command = 'echo "$(tput setaf 8)' + repo + '$(tput sgr0)"'
            execute(command)
    
    

def execute(command):
    print subprocess.check_output(command, shell=True).strip()  
 

def usage():
    print "usage: git-reveal [-hv]"
    print "       -v verbose    show all changed files"
    print "       -h help       show help"
    sys.exit(2)    


if __name__ == "__main__":
    main()

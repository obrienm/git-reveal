#!/usr/bin/python

import getopt, sys, os, subprocess


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hv", ["help", "verbose"])
    except getopt.GetoptError as err:
        print str(err)
        usage()
        
    verbose=False    
    for o, a in opts:
        if o == "-v":
            verbose=True
        elif o in ("-h", "--help"):
            usage()
        else:
            assert False, "unhandled option"
            usage()
    
    scanForRepos(verbose)


def scanForRepos(verbose):

    dic = os.walk('.').next()
    root = dic[0]        
    dirs = dic[1]
    dirs.append(".") #pwd
    
    gitReposFound=False
    reposWithChanges = []
    
    for dir in dirs:
        fullDir=os.path.abspath(os.path.join(root, dir))
        if os.path.exists(fullDir + "/.git"):
            gitReposFound=True
            if hasChanges(fullDir):
                reposWithChanges.append(fullDir)
                
    if not gitReposFound:
        print "no git repositories found"
    else:
        if len(reposWithChanges) > 0:
            print "changes detected in:"
        else:
            print "no changes found"

    for repository in reposWithChanges:
        revealRepo(repository, verbose)
        
        
def hasChanges(repo): 
    command = "cd '" + repo + "'; git status -b"
    output = subprocess.check_output(command, shell=True)
    
    if "nothing" in output:
        return False
    else:
        return True    


def revealRepo(dir, verbose):
    command = 'echo "$(tput setaf 1)' + dir + '$(tput sgr0)"'
    print subprocess.check_output(command, shell=True).strip()
        
    if verbose:
        command2 = "cd '" + dir + "'; git status -s"
        print subprocess.check_output(command2, shell=True).strip() 
        print ""
                                 

def usage():
    print "usage: git-reveal [-hv]"
    print "       -v verbose    show all changed files"
    print "       -h help       show help"
    sys.exit(2)    


if __name__ == "__main__":
    main()

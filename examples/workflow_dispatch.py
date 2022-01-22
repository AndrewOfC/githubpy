
import sys
from githubpy import *


def main():
    import argparse
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-t", "--token")
    parser.add_argument("-o", "--owner")
    parser.add_argument("-r", "--repo")
    parser.add_argument("-w", "--workflow", action='append', default=[])
    parser.add_argument("-b", "--branch", default='master', help="Branch or tag")
    parser.add_argument("-v", "--verbose", action='store_true')
    
    options = parser.parse_args()
    
    ghc = GitHubClient(token=options.token)
    
    result = ghc.ActionsCreateWorkflowDispatch(options.owner, 
                                               options.repo, 
                                               options.workflow[0], 
                                               options.branch, inputs={})
    if not isinstance(result, HttpResponse) and result.status_code != 204:
        print(f"ERROR: {result.message}")
        sys.exit(2)
        
    if options.verbose:
        print(f"# workflow {options.workflow[0]} on {options.branch} launched successfully")
    
    
    return

if __name__ == '__main__':
    main()
        
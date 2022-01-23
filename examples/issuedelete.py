

import requests, githubpy, datetime, operator
import jinja2


def main():
    import argparse
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--token")
    
    options = parser.parse_args()
    
    ghc = githubpy.GitHubClient(token=options.token)
    
    # r = ghc.MetaGetOctocat("foo")
    
    
    while( True):
        resp = ghc.IssuesListForAuthenticatedUser(filter='all', 
                                                  state='all', 
                                                  per_page=10)
        if not isinstance(resp, list) or not resp:
            break 
        
        ghc.IssuesDelete(resp)
        
    return

if __name__ == '__main__':
    main()

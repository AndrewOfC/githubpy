##
## Copyright (c) 2022 Andrew E Page
## 
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
## 
## The above copyright notice and this permission notice shall be included in all
## copies or substantial portions of the Software.
## 
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
## EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
## MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
## IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
## DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
## OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
## OR OTHER DEALINGS IN THE SOFTWARE.
##


import requests, githubV3py, datetime, operator
import jinja2


def main():
    import argparse
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--token")
    
    options = parser.parse_args()
    
    ghc = githubV3py.GitHubClient(token=options.token)
    
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

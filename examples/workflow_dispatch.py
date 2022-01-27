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

import sys
from githubV3py import *


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
        
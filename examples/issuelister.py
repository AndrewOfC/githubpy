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
import csv

from githubV3py import GitHubClient, Issue 

def main():
    import argparse
    
    parser = argparse.ArgumentParser()
    
    
    parser.add_argument("owner")
    parser.add_argument("repo")
    parser.add_argument("-u", "--username")
    parser.add_argument("-p", "--password")
    parser.add_argument("-t", "--token")
    parser.add_argument("-a", "--assignee", default='*', help="user name")
    parser.add_argument("-s", "--state", default='all', help="open,closed,all")
    
    options = parser.parse_args()
    
    if options.token:
        kwargs = { 'token': options.token, 'usesession': True }
    elif options.username and options.password:
        kwargs = { 'username': options.username, 'password': options.password, 'usesession': True }
    else:
        print("--token or --username --password must be specified", file=sys.stderr)
        sys.exit(1)
    
    ghc = GitHubClient(**kwargs)
    
    doc = csv.writer(sys.stdout)
    
    doc.writerow(["created", "assignee", "state", "title", "closed", 'days_open'])
    for issue in GitHubClient.generate(ghc.IssuesListForRepo, options.owner, options.repo, state=options.state):
        isinstance(issue, Issue)
        assignee = (issue.assignee and issue.assignee.login) or ''
        
        if issue.created_at and issue.closed_at:
            days_open = (issue.closed_at - issue.created_at).days
        else:
            days_open = ''
        
        doc.writerow([issue.created_at, assignee, issue.state, issue.title, issue.closed_at, days_open])
        
    
    return

if __name__ == '__main__':
    main()
        
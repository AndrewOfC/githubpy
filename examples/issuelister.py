
import sys
import csv

from githubpy import GitHubClient, Issue 

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
        
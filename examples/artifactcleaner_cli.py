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

import sys, re
import datetime
import fnmatch
import argparse
from operator import attrgetter
import dateparser
import pytz

from githubV3py import GitHubClient, Artifact, Repository, BasicError


class ArtifactCleaner(object):
    def __init__(self, owner, token, verbose=False):
        self._owner = owner
        self._token = token
        self._verbose = verbose
        return
    
    
    ##
    ##
    ##
    def _getverbose(self):
        return self._verbose
  
    verbose = property(_getverbose, doc="get verbose")
    
    @staticmethod
    def match_criteria(string, time=None,
                before=None, after=None,
                glob=None, regex=None):
        
        time_match = True
        name_match = (glob is None) and (regex is None)
        time = time and time.astimezone(datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo)
        
        if time is not None:
            if after:
                time_match = time_match and time > after
            if before:
                time_match = time_match and time < before
                
        if glob:
            name_match = fnmatch.fnmatch(string, glob)
            
        if regex:
            isinstance(regex, re.Pattern)
            name_match = name_match or regex.match(string)
                
        
        return time_match and name_match
    
    def clean(self,
              repo_glob=None, repo_regex=None,
              artifact_glob=None, artifact_regex=None, 
              before=None, after=None,
              all=False,
              dry_run=False,
              verbose=False,
              yes=False):
        
        
        to_delete = []  
        repo_regex=repo_regex and re.compile(repo_regex)
        artifact_regex=artifact_regex and re.compile(artifact_regex)
            
            
        ghc = GitHubClient(token=self._token, usesession=True)
        for repo in GitHubClient.generate(ghc.ReposListForAuthenticatedUser):
            
            if not isinstance(repo, Repository):
                if isinstance(repo, BasicError):
                    message = repo.message
                else:
                    message = f"unexpected response: {repo}"
                    
                raise RuntimeError(message)
            
            if not ArtifactCleaner.match_criteria(repo.name, regex=repo_regex, glob=repo_glob):
                continue
            
        
            for artifact in GitHubClient.generate(ghc.ActionsListArtifactsForRepo, 
                                                  self._owner, repo.name, 
                                                  extractor=attrgetter('artifacts')):
                if not artifact.ok and artifact.status_code == 404:
                    break # expected if repo has no artifacts

                if not ArtifactCleaner.match_criteria(artifact.name, artifact.created_at,
                                                      regex=artifact_regex,
                                                      glob=artifact_glob,
                                                      before=before,
                                                      after=after):
                    continue 
                
                if artifact.expired:
                    continue
                
                to_delete.append((repo.name, artifact.id))
                if self.verbose:
                    
                    print(f"# preparing to delete from '{repo.name}' '{artifact.name}' created on {artifact.created_at}")
                
        if not yes:
            print(f"Ready to delete {len(to_delete)} artifacts")
            while True:
                print(f"Are you sure? (y/n)")
                a = sys.stdin.readline().strip().lower()
                if a == 'n' or a == 'no':
                    return 
                if a == 'y' or a == 'yes':
                    break
              
        if dry_run:
            return 
        
        for reponame, artifact_id in to_delete:
            result = ghc.ActionsDeleteArtifact(self._owner, reponame, artifact_id)
            if not result.ok:
                raise RuntimeError(f" unexpected response {result} {result.message}")
        
            
                
        

def parseTime(t):
    return dateparser.parse(t).astimezone(pytz.UTC)
    
def main():
    
    desc = """"""
    
    parser = argparse.ArgumentParser(description=desc)
    
    parser.add_argument("-o", "--owner", help="repo owner")
    parser.add_argument("-t", "--token", help="access token from: https://github.com/settings/tokens/new")
    
    parser.add_argument("-y", "--yes", action='store_true', help="Do not prompt \"Are you sure?\" (Use with caution)")
    parser.add_argument("-v", "--verbose", action='store_true', help="list artifact info")
    parser.add_argument("-n", "--dry-run", action='store_true', help="list artifacts to be deleted, but do not delete(implies --verbose)")
    
    parser.add_argument("--glob-repo", help="match the repository name by wildcard pattern  (quotes recommended)")
    parser.add_argument("--regex-repo", help="match the repository name by regular expression  (quotes recommended)")
    parser.add_argument("--glob-artifact", help="match artifact name by wildcard pattern (quotes recommended)")
    parser.add_argument("--regex-artifact", help="match artifact by regular expression(quotes recommended)")
    
    parser.add_argument("-b", "--before", type=parseTime, help="artifacts before this date&time")
    parser.add_argument("-a", "--after", type=parseTime, help="artifacts after this date&time")
    parser.add_argument("--all", action='store_true', help="must be set to remove all artifacts from all repos")
    
    options = parser.parse_args()
    
    options.verbose = options.verbose or options.dry_run 
    
    if options.glob_artifact and options.regex_artifact:
        print(f"glob and regex may not be specified together for artifact selection",
              file=sys.stderr)
        exit(1)
        
    if options.glob_repo and options.glob_repo:
        print(f"glob and regex may not be specified together for repo selection",
              file=sys.stderr)
        exit(1)
        
    if not options.all and \
       not options.glob_artifact and \
       not options.regex_artifact and \
       not options.before and \
       not options.after:
        print(f"a glob|regex for branches, a glob|regex for artifacts, --before, --after, or --all must be specified",
              file=sys.stderr)
        exit(1)
        
        
        
    try:        
        ArtifactCleaner(options.owner, options.token, options.verbose).clean(
            yes=options.yes,
            dry_run=options.dry_run,
            all=options.all,
            before=options.before,
            after=options.after,
            repo_glob=options.glob_repo,
            repo_regex=options.regex_repo,
            artifact_glob=options.glob_artifact,
            artifact_regex=options.regex_artifact,
        )
    except RuntimeError as ex:
        print(f"ERROR:  {ex.args[0]}")
        exit(2)
    
    
    
    return 

if __name__ == '__main__':
    main()
    

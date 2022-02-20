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
import argparse
import re
from operator import attrgetter

import githubV3py

def main():
  
  parser = argparse.ArgumentParser()
  parser.add_argument("--token")
  parser.add_argument("--owner")
  parser.add_argument("--remove", action='store_true', help="Remove matching build")
  parser.add_argument("--list", action='store_true', help="list matching builds")
  parser.add_argument("--failed", action='store_true', help="List/remove failed builds")
  parser.add_argument("--cancelled", action='store_true', help="List/remove cancelled builds")
  parser.add_argument("--success", action='store_true', help="List/remove successful builds")
  parser.add_argument("--repo", help="Regex to match repo name")
  parser.add_argument("--commit-message", help="Regex pattern to match commit message")
  parser.add_argument("--branch-name", help="Regex pattern to match branch name")
  parser.add_argument("--workflow-name", help="Regex pattern to match workflow name")
  parser.add_argument("-v", "--verbose", action='store_true')
  
  options = parser.parse_args()
  
  ghc = githubV3py.GitHubClient(token=options.token) 
  
  githubGenerate = githubV3py.GitHubClient.generate
  
  repoRE = options.repo and re.compile(options.repo)
  workflowRE = options.workflow_name and re.compile(options.workflow_name)
  branchRE = options.branch_name and re.compile(options.branch_name)
  commitMsgRE = options.commit_message and re.compile(options.commit_message, re.MULTILINE)
  
  count = 0
  
  for repo in githubGenerate(ghc.ReposListForUser, options.owner, 'owner'):
    
    if not repo.ok:
      print(f"ERROR listing repos: {repo.message}")
      sys.exit(2)
    
    if repoRE and not repoRE.match(repo.name):
      continue
  
    for workflow in githubGenerate(ghc.ActionsListRepoWorkflows, options.owner, repo.name, 
                                                     extractor=attrgetter('workflows')):
      
      if not workflow.ok:
        print(f"ERROR listing workflows: {workflow.message}")
        sys.exit(2)

      if workflowRE and not workflowRE.match(run.name):
        continue
      
      for run in githubGenerate(ghc.ActionsListWorkflowRuns, options.owner, repo.name , workflow.id,                                                      extractor=attrgetter('workflow_runs')):

        if not run.ok:
          print(f"ERROR listing repos: {run.message}")
          sys.exit(2)
        
        if branchRE and not branchRE.match(run.head_branch):
          continue
        
        if commitMsgRE and not commitMsgRE.match(run.head_commit.message):
          continue
        
        select = not (options.failed or options.success or options.cancelled) # if none, select all
        
        select = select or (options.failed and run.conclusion == 'failure')

        select = select or (options.success and run.conclusion == 'success')
        
        select = select or (options.cancelled and run.conclusion == 'cancelled')
        
        if not select:
          continue
        
        count += 1
        
        if options.list:
          print(f"{run.name:10} {run.created_at:%c} {run.head_branch:10} {run.status} '{run.head_commit.message}' {run.conclusion}")
        
        if options.remove:
          result = ghc.ActionsDeleteWorkflowRun(options.owner, repo.name, run.id)
          if not result.ok:
            print(f"ERROR:  {result.message}")
  
  if options.verbose:
    print(f"Found {count} runs")
    print(f"Remaining: {ghc.rateLimitRemaining} reset at: {ghc.rateLimitReset:%I:%M %p}")
  
  return


if __name__ == '__main__':
  main()
  
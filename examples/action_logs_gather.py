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
  parser.add_argument("--workflow", help="workflow name")
  parser.add_argument("--repo", help="Repo name")
  parser.add_argument("--job", help="Regex to match jobname")
  parser.add_argument("--id", help="job id")
  parser.add_argument("--list", action='store_true', help="list only")
  parser.add_argument("--failed", action="store_true", help="Only gather failed jobs")
  parser.add_argument("-n", "--count", type=int, default=1)
  parser.add_argument("-v", "--verbose", action='store_true')

  options = parser.parse_args()
  
  ghc = githubV3py.GitHubClient(token=options.token) 
  
  githubGenerate = githubV3py.GitHubClient.generate
  
  done = False
  for workflow in githubGenerate(ghc.ActionsListRepoWorkflows, options.owner, options.repo, 
                                                   extractor=attrgetter('workflows')):
    
    if not workflow.ok:
      print(f"ERROR listing workflows: {workflow.message}")
      sys.exit(2)

    if workflow.name != options.workflow:
      continue
    
    count = 0
    for run in githubGenerate(ghc.ActionsListWorkflowRuns, options.owner, options.repo , workflow.id, extractor=attrgetter('workflow_runs')):
      #if run.created_at <= after:
      #  continue
        
      ##
      ##
      ##
      for job in githubGenerate(ghc.ActionsListJobsForWorkflowRun, options.owner, options.repo, run.id, extractor=attrgetter('jobs')):
        if options.list:          
          print(f"{run.created_at.isoformat()} {job.name:15s} {run.head_branch:10} {job.status} {job.conclusion}")
        else:
          print(f"##")
          print(f"## {job.name}#{run.run_attempt} {job.conclusion}")
          print(f"##")
          result = ghc.ActionsDownloadJobLogsForWorkflowRun(options.owner, options.repo, job.id)
       
          sys.stdout.write(result.decode('utf-8'))
      count += 1
      if count >= options.count: 
        done = True
        break
    if done:
      break
  

  if options.verbose:
    print(f"Ratelimit remaining: {ghc.rateLimitRemaining} Reset: {ghc.rateLimitReset:%c}")
    return

if __name__ == '__main__':
  main()
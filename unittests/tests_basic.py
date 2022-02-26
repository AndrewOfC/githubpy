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

import sys, os
import unittest
import datetime, time

from testutils import PlatformString

from githubV3py import *

class BasicTests(unittest.TestCase):
    
    def test_create_delete_repo(self):
        reponame = f'foobar-py-{PlatformString()}'
        ghc = GitHubClient(os.environ['GITHUB_TOKEN'])
        
        result = ghc.ReposDelete("GitHubPyTest", reponame)
        self.assertTrue((isinstance(result, HttpResponse) and result.status_code == 204) or result.message == 'Not Found')
        
        
        result = ghc.ReposCreateForAuthenticatedUser(reponame, description="test repo")
        self.assertIsInstance(result, Repository)
    
        found = False
        for attempt in range(3):        
            result = ghc.ReposListForAuthenticatedUser()
            for repo in result:
                found = found or repo.name==reponame
            if found:
                break
            time.sleep(5) # may be some lag between the successful call and database update
                
        self.assertTrue(found)
            
        result = ghc.ReposDelete("GitHubPyTest", reponame)
        self.assertEqual(result.status_code//100, 2) # any 200 should work
        
        return
    
    def test_pagination(self):
        
        ghc = GitHubClient(token=os.environ['GITHUB_TOKEN'])
        
        count = 7
        
        commits = GitHubClient.paginate(ghc.ReposListCommits, 
                                        "geodynamics", 
                                        "aspect", per_page=5, pagination_limit=count)
        
        self.assertEqual(len(commits), count, "didn't get expected count")
        
    def test_datetime_usage(self):
        
        ghc = GitHubClient(token=os.environ['GITHUB_TOKEN'])
        
        since = datetime.datetime(2021, 9, 2)
        until = datetime.datetime(2021, 9, 3)
        
        ##
        ## We tailor the query to a known repo with a known history
        ##
        commits = ghc.ReposListCommits("geodynamics", 
                                        "aspect", since=since, until=until)
        
        self.assertEqual(6, len(commits), "number of commits not what was expected")
        
        return
                
        
    def test_generation(self):
        
        ghc = GitHubClient(token=os.environ['GITHUB_TOKEN'])
        
        count = 7
        
        n = 0 
        for c in GitHubClient.generate(ghc.ReposListCommits, 
                                        "geodynamics", 
                                        "aspect", per_page=5, pagination_limit=count):
            n += 1
        
        
        self.assertEqual(n, count, "didn't get expected count")
        
    def test_generation_error(self):
        
        ghc = GitHubClient(token=os.environ['GITHUB_TOKEN'])
        
        count = 7
        
        n = 0 
        executed = False
        for c in GitHubClient.generate(ghc.ReposListCommits, 
                                        "GitHubPyTest", 
                                        "nonexistentrepo_xxx"):
            self.assertFalse(c.ok)
            executed = True
        
        self.assertTrue(executed)
        
        return
         
    # disabled for now, github  isn't using passswords anymore... for now       
    def xtest_workflow_artifacts(self):
        
        ghc = GitHubClient(token=os.environ['GITHUB_TOKEN'])
        
        # launch a workflow
        
        result = ghc.ActionsCreateWorkflowDispatch('GitHubPyTest', 
                                               'actiontesting', 
                                               'simple_action.yml', 
                                               'Dev', inputs={})
        
        self.assertIsInstance(result, HttpResponse)
        self.assertAlmostEqual(result.status_code, 204) 
        

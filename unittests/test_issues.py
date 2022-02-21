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
import datetime
import githubV3py 
import time

from operator import attrgetter

from testutils import PlatformString, randstring

class IssueTests(unittest.TestCase):
    owner = 'GitHubPyTest'
    repo  = 'actiontesting'
    
    @classmethod
    def setUpClass(clazz):
        ghc = clazz._ghc = githubV3py.GitHubClient(token=os.environ['GITHUB_TOKEN'], usesession=True)
    
        
        t = datetime.datetime.now()
        title = f'Issue {t:%x %X} {PlatformString()}'
        body = "Simple Test Issue"
        
        clazz._setupResp = ghc.IssuesCreate(clazz.owner, clazz.repo, title, body)
      
    @classmethod  
    def tearDownClass(clazz):
        
        ghc = clazz._ghc
        
        ghc.IssuesDelete([clazz._setupResp])
        
        
        return 
        
        
    
    def test001_validatesetup(self):
        
        self.assertTrue(self._setupResp.ok)
        self.assertIsInstance(self._setupResp, githubV3py.Issue)        
        
        return  
    
    def test002_IssuesGet(self):
        
        
        ghc = self._ghc
        issue = self._setupResp
        
        for attempt in range(3):
        
            nissue = ghc.IssuesGet(self.owner, self.repo, issue.number)
            if isinstance(nissue, githubV3py.Issue):
                break
            time.sleep(1)
        
        if attempt > 0:          
            print(f"test002_IssuesGet {attempt+1} attempts")
        
        self.assertIsInstance(nissue, githubV3py.Issue)
        
        self.assertEqual(issue.node_id, nissue.node_id) 
        
    def test003_IssuesComments(self):
        comment = randstring()
        
        ghc = self._ghc
        issue = self._setupResp
        
        resp = ghc.IssuesCreateComment(self.owner, self.repo, issue.number, comment)
        
        self.assertTrue(resp.ok)
        self.assertIsInstance(resp, githubV3py.IssueComment)
        
        nresp = ghc.IssuesGetComment(self.owner, self.repo, resp.id)
        
        self.assertTrue(nresp.ok)
        self.assertEqual(nresp.node_id, resp.node_id)
        
        nresp = ghc.IssuesListComments(self.owner, self.repo, issue.number)
        self.assertIsInstance(nresp, list)
        self.assertGreaterEqual(1, len(nresp)) # other test platforms may be running in parallel
        
        
        
        
        
        nresp = ghc.IssuesDeleteComment(self.owner, self.repo, resp.id)
        self.assertTrue(nresp.ok)
        
        nresp = ghc.IssuesGetComment(self.owner, self.repo, resp.id)
        self.assertFalse(nresp.ok)
        
    
    def test004_addAssignees(self):
        assignees = ['AndrewOfC', 'GitHubPyTest']
                
        ghc = self._ghc
        resp = self._setupResp
        isinstance(ghc, githubV3py.GitHubClient)
        nresp = ghc.IssuesAddAssignees('GitHubPyTest', 'actiontesting', resp.number, assignees)
        
        self.assertTrue(nresp.ok)
        
        ##
        ## we get occasional failures that typically pass when the
        ## test is re-run.  It's possible that the upstream database
        ## is adding the assignees in discreet inserts as opposed
        ## to a 'batch'.   As such we may be querying too quickly.
        ## we'll make two other attempts but if this doesn't resolve
        ## the issue something else will have to be investigated
        ##
        for attempt in range(3):
            nresp = ghc.IssuesGet('GitHubPyTest', 'actiontesting', resp.number)
            s1 = set(assignees)
            s2 = set(map(attrgetter('login'), nresp.assignees))
            if s1 == s2:
                break
            time.sleep(1)
            
        
        
        self.assertEqual(s1,s2)
        if attempt > 0:
            print(f"NOTE: test004_addAssignees passed after {attempt+1} attempts")
        


import sys, os
import unittest
import datetime
import githubV3py 

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
        
        nissue = ghc.IssuesGet(self.owner, self.repo, issue.number)
        
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
        
        
        nresp = ghc.IssuesGet('GitHubPyTest', 'actiontesting', resp.number)
        
        s1 = set(assignees)
        s2 = set(map(attrgetter('login'), nresp.assignees))
        
        self.assertEqual(s1,s2)
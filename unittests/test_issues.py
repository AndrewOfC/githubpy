

import os
import random
import unittest
import datetime
import githubpy 

class IssueTests(unittest.TestCase):
    
    def test_create(self):
        ghc = githubpy.GitHubClient(token=os.environ['GITHUB_TOKEN'])
        
        owner = 'GitHubPyTest'
        repo  = 'actiontesting'
        
        t = datetime.datetime.now()
        title = f'Issue {t:%x %X}'
        body = "Simple Test Issue"
        
        resp = ghc.IssuesCreate(owner, repo, title, body)
        
        self.assertTrue(resp.ok)
        self.assertIsInstance(resp, githubpy.Issue)
        
        return  
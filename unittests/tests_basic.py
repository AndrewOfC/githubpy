
import sys, os
import unittest
import datetime

from githubpy import *

class BasicTests(unittest.TestCase):
    
    def test_create_delete_repo(self):
        reponame = f'foobar-py{sys.version_info.major}.{sys.version_info.minor}-{sys.platform}'
        ghc = GitHubClient(token=os.environ['GITHUB_TOKEN'])
        
        result = ghc.ReposDelete("GitHubPyTest", reponame)
        self.assertTrue((isinstance(result, HttpResponse) and result.status_code == 204) or result.message == 'Not Found')
        
        
        result = ghc.ReposCreateForAuthenticatedUser(reponame, description="test repo")
        self.assertIsInstance(result, Repository)
    
        result = ghc.ReposListForAuthenticatedUser()
        found = False
        for repo in result:
            found = found or repo.name==reponame
            
        self.assertTrue(found)
            
        result = ghc.ReposDelete("GitHubPyTest", reponame)
        
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
                
    def test_workflow_artifacts(self):
        
        ghc = GitHubClient(token=os.environ['GITHUB_TOKEN'])
        
        # launch a workflow
        
        result = ghc.ActionsCreateWorkflowDispatch('GitHubPyTest', 
                                               'actiontesting', 
                                               'simple_action.yml', 
                                               'Dev', inputs={})
        
        self.assertIsInstance(result, HttpResponse)
        self.assertAlmostEqual(result.status_code, 204)
        
        
 

import os
import unittest
import datetime
from testutils import randstring
from githubV3py import *

class MetaTests(unittest.TestCase):
    
    def test_metaRoot(self):
        ghc = GitHubClient()

        meta = ghc.MetaRoot()
        self.assertIsNotNone(meta)
        
        meta = ghc.MetaGet()
        self.assertIsNotNone(meta)
        
        
    def test_codes_of_conduct(self):
        ghc = GitHubClient()
        
        coc = ghc.CodesOfConductGetAllCodesOfConduct()
        self.assertIsNotNone(coc)
        
    
    def octocat_test(self, token):
        
        ghc = GitHubClient(token=token)
        
        text = randstring()
        
        ascii_art = ghc.MetaGetOctocat(text)
        
        self.assertIsInstance(ascii_art, DataResponse)
        
        ascii_art = ascii_art.data.decode('utf-8')
        
        index = ascii_art.find(text)
        
        self.assertNotEqual(index, -1, "Could not find text that was to be rendered")
        
        return
    
    def test_octocat(self):
        self.octocat_test(os.environ['GITHUB_TOKEN'])
    
    def test_callableToken(self):
        self.octocat_test(lambda: os.environ['GITHUB_TOKEN'])
    
    
    def test_emojis(self):
        ghc = GitHubClient(token=os.environ['GITHUB_TOKEN'])
        
        resp = ghc.EmojisGet()
        
        self.assertIsInstance(resp, dict)
        
        return
    
    def test_ratelimits(self):
        
        ##
        ## Test that we're getting the ratelimits correctly from the
        ## headers, using the RateLimitGet method for reference
        ##
        ## Sllight chance that we'll do queries at the 'reset' rollover
        ##
        ghc = GitHubClient(token=os.environ['GITHUB_TOKEN'])
        
        rl = ghc.RateLimitGet()
        
        self.assertLessEqual(ghc.rateLimitRemaining, rl.rate.remaining)
        self.assertEqual(datetime.datetime.fromtimestamp(rl.rate.reset), ghc.rateLimitReset)
        
        ghc.MetaGetOctocat("foo")
        
        # we run these tests in parallel on multiple platforms and python versions
        # as such we may see a 'race condition'
        self.assertLessEqual(ghc.rateLimitRemaining, rl.rate.remaining-1)
        
        
        return 
    
    
    
    
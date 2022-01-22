
import os
import random
import unittest
import datetime
from githubpy import *

class MetaTests(unittest.TestCase):
    @staticmethod
    def randstring(n=10, seed="abcdefghijklmnopqrtstuvwxyzABCDEFGHIJKLMNOPQRTSTUVWXYZ"):
        "Generate a random string"
        return ''.join(random.choices(seed, k=n))
    
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
        
    
    def test_octocat(self):
        
        ghc = GitHubClient(token=os.environ['GITHUB_TOKEN'])
        
        text = MetaTests.randstring()
        
        ascii_art = ghc.MetaGetOctocat(text)
        
        self.assertIsInstance(ascii_art, DataResponse)
        
        ascii_art = ascii_art.data.decode('utf-8')
        
        index = ascii_art.find(text)
        
        self.assertNotEqual(index, -1, "Could not find text that was to be rendered")
        
        
        return
    
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
    
    
    
    
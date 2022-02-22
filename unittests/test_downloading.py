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
import io
from zipfile import ZipFile
import urllib
from operator import attrgetter

from testutils import PlatformString

from githubV3py import *

class DownloadTests(unittest.TestCase):
  
  @classmethod
  def setUpClass(clazz):
    ghc = clazz._ghc = GitHubClient(token=os.environ['GITHUB_TOKEN'], usesession=True)
    # trigger a simple build    
        
    now = datetime.datetime.now()
    timeout = now + datetime.timedelta(minutes=2)
    artifactReady = False
    building = False
    
    while datetime.datetime.now() < timeout and not artifactReady:
      
      result = ghc.ActionsListArtifactsForRepo('AndrewOfC', 'github_simple_action')
      
      artifacts = list(filter(lambda e: not e.expired, result.artifacts))
      
      if artifacts:
        clazz.artifact_id = result.artifacts[0].id
        artifactReady = True
        break
      elif not building:
        building = True
        result = ghc.ActionsCreateWorkflowDispatch('AndrewOfC', 
                                                     "github_simple_action", 
                                                     'simple_action.yml', 
                                                     'master', inputs={})
        
        
        if not isinstance(result, HttpResponse) or result.status_code != 204:
          raise RuntimeError("dispatch failed")
        
      
      
      time.sleep(5)
    
    if not artifactReady:
      raise RuntimeError("no artifact created")
    
  def _checkZipFile(self, data):
    f = io.BytesIO(data)
    
    zf = ZipFile(f, 'r')
    
    return zf.testzip() == None
    
  def test001_download_artifact(self):
    
    ghc = self._ghc
    
    data = ghc.ActionsDownloadArtifact('AndrewOfC', 'github_simple_action', self.artifact_id, 'zip')
    
    self.assertIsInstance(data, bytes)
    self.assertTrue(self._checkZipFile(data))
    
    
  def test002_download_by_chunk(self):
    ghc = self._ghc
        
    data = b''
    count = 0
    for chunk in ghc.ActionsDownloadArtifact('AndrewOfC', 'github_simple_action', self.artifact_id, 'zip',
                                             chunk_size=64):
      data += chunk 
      count += 1
     
    self.assertGreater(count, 2) 
    self.assertTrue(self._checkZipFile(data))
    
  def test003_fetch_url(self):
    
    ghc = self._ghc
    
    url = ghc.ActionsDownloadArtifact('AndrewOfC', 'github_simple_action', self.artifact_id, 'zip', fetch_url=True)
        
    url = urllib.parse.urlparse(url)
    
    self.assertEqual(url.scheme, 'https')
    
    
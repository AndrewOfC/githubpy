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


import io

from .githubclientclasses import *

class Meta(object):


    #
    # get /meta
    #
    def MetaGet(self, ):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/meta#get-github-meta-information
        /meta
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/meta", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ApiOverview(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /octocat
    #
    def MetaGetOctocat(self, s:str=None):
        """Get the octocat as ASCII art
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/meta#get-octocat
        /octocat
        
        arguments:
        s -- The words to show in Octocat's speech bubble
        
        """
        
        data = {}
        if s is not None:
            data['s'] = s
        
        
        r = self._session.get(f"{self._url}/octocat", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return DataResponse(r.content)
            
        
        return UnexpectedResult(r)
    #
    # get /zen
    #
    def MetaGetZen(self, ):
        """Get a random sentence from the Zen of GitHub
        /zen
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/zen", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return DataResponse(r.content)
            
        
        return UnexpectedResult(r)
    #
    # get /
    #
    def MetaRoot(self, ):
        """Get Hypermedia links to resources accessible in GitHub's REST API
        
        https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#root-endpoint
        /
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return MetaRootSuccess(**r.json())
            
        
        return UnexpectedResult(r)
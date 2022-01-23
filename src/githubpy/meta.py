

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


import io

from .githubclientclasses import *

class CodesOfConduct(object):


    #
    # get /codes_of_conduct
    #
    def CodesOfConductGetAllCodesOfConduct(self, ):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/codes-of-conduct#get-all-codes-of-conduct
        /codes_of_conduct
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/codes_of_conduct", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and CodeOfConduct(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /codes_of_conduct/{key}
    #
    def CodesOfConductGetConductCode(self, key:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/codes-of-conduct#get-a-code-of-conduct
        /codes_of_conduct/{key}
        
        arguments:
        key -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/codes_of_conduct/{key}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return CodeOfConduct(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        
        return UnexpectedResult(r)
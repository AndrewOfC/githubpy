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
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

class Licenses(object):


    #
    # get /licenses/{license}
    #
    def LicensesGet(self, license:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/licenses#get-a-license
        /licenses/{license}
        
        arguments:
        license -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/licenses/{license}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return License(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /licenses
    #
    def LicensesGetAllCommonlyUsed(self, featured:bool=None, per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/licenses#get-all-commonly-used-licenses
        /licenses
        
        arguments:
        featured -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if featured is not None:
            data['featured'] = featured
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/licenses", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and LicenseSimple(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/license
    #
    def LicensesGetForRepo(self, owner:str, repo:str):
        """This method returns the contents of the repository's license file, if one is detected.

Similar to [Get repository content](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-repository-content), this method also supports [custom media types](https://docs.github.com/enterprise-server@3.3/rest/overview/media-types) for retrieving the raw license content or rendered license HTML.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/licenses/#get-the-license-for-a-repository
        /repos/{owner}/{repo}/license
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/license", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return LicenseContent(**r.json())
            
        
        return UnexpectedResult(r)
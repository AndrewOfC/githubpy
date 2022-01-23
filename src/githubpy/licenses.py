

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
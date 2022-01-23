

import io

from .githubclientclasses import *

class Gitignore(object):


    #
    # get /gitignore/templates
    #
    def GitignoreGetAllTemplates(self, ):
        """List all templates available to pass as an option when [creating a repository](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-a-repository-for-the-authenticated-user).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gitignore#get-all-gitignore-templates
        /gitignore/templates
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/gitignore/templates", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /gitignore/templates/{name}
    #
    def GitignoreGetTemplate(self, name:str):
        """The API also allows fetching the source of a single template.
Use the raw [media type](https://docs.github.com/enterprise-server@3.3/rest/overview/media-types/) to get the raw contents.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gitignore#get-a-gitignore-template
        /gitignore/templates/{name}
        
        arguments:
        name -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/gitignore/templates/{name}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return GitignoreTemplate(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        
        return UnexpectedResult(r)
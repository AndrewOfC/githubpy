

import io

from .githubclientclasses import *

class Emojis(object):


    #
    # get /emojis
    #
    def EmojisGet(self, ):
        """Lists all the emojis available to use on GitHub Enterprise Server.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/emojis#get-emojis
        /emojis
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/emojis", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return r.json()
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        
        return UnexpectedResult(r)
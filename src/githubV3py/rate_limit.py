

import io

from .githubclientclasses import *

class RateLimit(object):


    #
    # get /rate_limit
    #
    def RateLimitGet(self, ):
        """**Note:** Accessing this endpoint does not count against your REST API rate limit.

**Note:** The `rate` object is deprecated. If you're writing new API client code or updating existing code, you should use the `core` object instead of the `rate` object. The `core` object contains the same information that is present in the `rate` object.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/rate-limit#get-rate-limit-status-for-the-authenticated-user
        /rate_limit
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/rate_limit", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return RateLimitOverview(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
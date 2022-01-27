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

class Gists(object):


    #
    # get /gists/{gist_id}/star
    #
    def GistsCheckIsStarred(self, gist_id:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists#check-if-a-gist-is-starred
        /gists/{gist_id}/star
        
        arguments:
        gist_id -- gist_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/gists/{gist_id}/star", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return GistsCheckIsStarredNotFound(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # post /gists
    #
    def GistsCreate(self, files:object, description:str=None, public=None):
        """Allows you to add a new gist with one or more files.

**Note:** Don't name your files "gistfile" with a numerical suffix. This is the format of the automatic naming scheme that Gist uses internally.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists#create-a-gist
        /gists
        
        arguments:
        files -- Names and content for the files that make up the gist
        description -- Description of the gist
        public -- 
        

        """
    
        data = {
        'files': files,
        'description': description,
        'public': public,
        
        }
        

        
        r = self._session.post(f"{self._url}/gists", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return GistSimple(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /gists/{gist_id}/comments
    #
    def GistsCreateComment(self, gist_id:str,body:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists#create-a-gist-comment
        /gists/{gist_id}/comments
        
        arguments:
        gist_id -- gist_id parameter
        body -- The comment text.
        

        """
    
        data = {
        'body': body,
        
        }
        

        
        r = self._session.post(f"{self._url}/gists/{gist_id}/comments", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return GistComment(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /gists/{gist_id}
    #
    def GistsDelete(self, gist_id:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists#delete-a-gist
        /gists/{gist_id}
        
        arguments:
        gist_id -- gist_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/gists/{gist_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /gists/{gist_id}/comments/{comment_id}
    #
    def GistsDeleteComment(self, gist_id:str, comment_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists#delete-a-gist-comment
        /gists/{gist_id}/comments/{comment_id}
        
        arguments:
        gist_id -- gist_id parameter
        comment_id -- comment_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/gists/{gist_id}/comments/{comment_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # post /gists/{gist_id}/forks
    #
    def GistsFork(self, gist_id:str):
        """**Note**: This was previously `/gists/:gist_id/fork`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists#fork-a-gist
        /gists/{gist_id}/forks
        
        arguments:
        gist_id -- gist_id parameter
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/gists/{gist_id}/forks", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return BaseGist(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # get /gists/{gist_id}
    #
    def GistsGet(self, gist_id:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists#get-a-gist
        /gists/{gist_id}
        
        arguments:
        gist_id -- gist_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/gists/{gist_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return GistSimple(**r.json())
            
        if r.status_code == 403:
            return Forbidden_gist(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /gists/{gist_id}/comments/{comment_id}
    #
    def GistsGetComment(self, gist_id:str, comment_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists#get-a-gist-comment
        /gists/{gist_id}/comments/{comment_id}
        
        arguments:
        gist_id -- gist_id parameter
        comment_id -- comment_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/gists/{gist_id}/comments/{comment_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return GistComment(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return Forbidden_gist(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /gists/{gist_id}/{sha}
    #
    def GistsGetRevision(self, gist_id:str, sha:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists#get-a-gist-revision
        /gists/{gist_id}/{sha}
        
        arguments:
        gist_id -- gist_id parameter
        sha -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/gists/{gist_id}/{sha}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return GistSimple(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /gists
    #
    def GistsList(self, since:datetime=None, per_page=30, page=1):
        """Lists the authenticated user's gists or if called anonymously, this endpoint returns all public gists:
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists#list-gists-for-the-authenticated-user
        /gists
        
        arguments:
        since -- Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if since is not None:
            data['since'] = since.isoformat()
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/gists", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and BaseGist(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /gists/{gist_id}/comments
    #
    def GistsListComments(self, gist_id:str,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists#list-gist-comments
        /gists/{gist_id}/comments
        
        arguments:
        gist_id -- gist_id parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/gists/{gist_id}/comments", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and GistComment(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /gists/{gist_id}/commits
    #
    def GistsListCommits(self, gist_id:str,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists#list-gist-commits
        /gists/{gist_id}/commits
        
        arguments:
        gist_id -- gist_id parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/gists/{gist_id}/commits", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and GistCommit(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /users/{username}/gists
    #
    def GistsListForUser(self, username:str,since:datetime=None, per_page=30, page=1):
        """Lists public gists for the specified user:
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists#list-gists-for-a-user
        /users/{username}/gists
        
        arguments:
        username -- 
        since -- Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if since is not None:
            data['since'] = since.isoformat()
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/users/{username}/gists", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and BaseGist(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /gists/{gist_id}/forks
    #
    def GistsListForks(self, gist_id:str,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists#list-gist-forks
        /gists/{gist_id}/forks
        
        arguments:
        gist_id -- gist_id parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/gists/{gist_id}/forks", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and GistSimple(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /gists/public
    #
    def GistsListPublic(self, since:datetime=None, per_page=30, page=1):
        """List public gists sorted by most recently updated to least recently updated.

Note: With [pagination](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#pagination), you can fetch up to 3000 gists. For example, you can fetch 100 pages with 30 gists per page or 30 pages with 100 gists per page.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists#list-public-gists
        /gists/public
        
        arguments:
        since -- Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if since is not None:
            data['since'] = since.isoformat()
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/gists/public", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and BaseGist(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /gists/starred
    #
    def GistsListStarred(self, since:datetime=None, per_page=30, page=1):
        """List the authenticated user's starred gists:
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists#list-starred-gists
        /gists/starred
        
        arguments:
        since -- Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if since is not None:
            data['since'] = since.isoformat()
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/gists/starred", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and BaseGist(**entry) for entry in r.json() ]
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # put /gists/{gist_id}/star
    #
    def GistsStar(self, gist_id:str):
        """Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#http-verbs)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists#star-a-gist
        /gists/{gist_id}/star
        
        arguments:
        gist_id -- gist_id parameter
        

        """
    
        data = {
        
        }
        

        
        r = self._session.put(f"{self._url}/gists/{gist_id}/star", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /gists/{gist_id}/star
    #
    def GistsUnstar(self, gist_id:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists#unstar-a-gist
        /gists/{gist_id}/star
        
        arguments:
        gist_id -- gist_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/gists/{gist_id}/star", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # patch /gists/{gist_id}
    #
    def GistsUpdate(self, gist_id:str,description:str=None, files:object=None):
        """Allows you to update or delete a gist file and rename gist files. Files from the previous version of the gist that aren't explicitly changed during an edit are unchanged.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists/#update-a-gist
        /gists/{gist_id}
        
        arguments:
        gist_id -- gist_id parameter
        description -- Description of the gist
        files -- Names of files to be updated
        

        """
    
        data = {
        'description': description,
        'files': files,
        
        }
        

        
        r = self._session.patch(f"{self._url}/gists/{gist_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return GistSimple(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /gists/{gist_id}/comments/{comment_id}
    #
    def GistsUpdateComment(self, gist_id:str, comment_id:int,body:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/gists#update-a-gist-comment
        /gists/{gist_id}/comments/{comment_id}
        
        arguments:
        gist_id -- gist_id parameter
        comment_id -- comment_id parameter
        body -- The comment text.
        

        """
    
        data = {
        'body': body,
        
        }
        

        
        r = self._session.patch(f"{self._url}/gists/{gist_id}/comments/{comment_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return GistComment(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
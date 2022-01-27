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

class Users(object):


    #
    # post /user/emails
    #
    def UsersAddEmailForAuthenticatedUser(self, object:object):
        """This endpoint is accessible with the `user` scope.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#add-an-email-address-for-the-authenticated-user
        /user/emails
        
        arguments:
        object -- 
        

        """
    
        data = {
        'object': object,
        
        }
        

        
        r = self._session.post(f"{self._url}/user/emails", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return [ entry and Email(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # get /users/{username}/following/{target_user}
    #
    def UsersCheckFollowingForUser(self, username:str, target_user:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#check-if-a-user-follows-another-user
        /users/{username}/following/{target_user}
        
        arguments:
        username -- 
        target_user -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/users/{username}/following/{target_user}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # get /user/following/{username}
    #
    def UsersCheckPersonIsFollowedByAuthenticated(self, username:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#check-if-a-person-is-followed-by-the-authenticated-user
        /user/following/{username}
        
        arguments:
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/user/following/{username}", 
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
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # post /user/gpg_keys
    #
    def UsersCreateGpgKeyForAuthenticatedUser(self, armored_public_key:str):
        """Adds a GPG key to the authenticated user's GitHub account. Requires that you are authenticated via Basic Auth, or OAuth with at least `write:gpg_key` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#create-a-gpg-key-for-the-authenticated-user
        /user/gpg_keys
        
        arguments:
        armored_public_key -- A GPG key in ASCII-armored format.
        

        """
    
        data = {
        'armored_public_key': armored_public_key,
        
        }
        

        
        r = self._session.post(f"{self._url}/user/gpg_keys", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return GpgKey(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /user/keys
    #
    def UsersCreatePublicSshKeyForAuthenticatedUser(self, key:str, title:str=None):
        """Adds a public SSH key to the authenticated user's GitHub account. Requires that you are authenticated via Basic Auth, or OAuth with at least `write:public_key` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#create-a-public-ssh-key-for-the-authenticated-user
        /user/keys
        
        arguments:
        key -- The public SSH key to add to your GitHub account.
        title -- A descriptive name for the new key.
        

        """
    
        data = {
        'key': key,
        'title': title,
        
        }
        

        
        r = self._session.post(f"{self._url}/user/keys", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Key(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /user/emails
    #
    def UsersDeleteEmailForAuthenticatedUser(self, ):
        """This endpoint is accessible with the `user` scope.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#delete-an-email-address-for-the-authenticated-user
        /user/emails
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/user/emails", 
                           params=data,
                           **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /user/gpg_keys/{gpg_key_id}
    #
    def UsersDeleteGpgKeyForAuthenticatedUser(self, gpg_key_id:int):
        """Removes a GPG key from the authenticated user's GitHub account. Requires that you are authenticated via Basic Auth or via OAuth with at least `admin:gpg_key` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#delete-a-gpg-key-for-the-authenticated-user
        /user/gpg_keys/{gpg_key_id}
        
        arguments:
        gpg_key_id -- gpg_key_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/user/gpg_keys/{gpg_key_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /user/keys/{key_id}
    #
    def UsersDeletePublicSshKeyForAuthenticatedUser(self, key_id:int):
        """Removes a public SSH key from the authenticated user's GitHub account. Requires that you are authenticated via Basic Auth or via OAuth with at least `admin:public_key` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#delete-a-public-ssh-key-for-the-authenticated-user
        /user/keys/{key_id}
        
        arguments:
        key_id -- key_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/user/keys/{key_id}", 
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
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # put /user/following/{username}
    #
    def UsersFollow(self, username:str):
        """Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#http-verbs)."

Following a user requires the user to be logged in and authenticated with basic auth or OAuth with the `user:follow` scope.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#follow-a-user
        /user/following/{username}
        
        arguments:
        username -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.put(f"{self._url}/user/following/{username}", 
                          json=data,
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
            
        if r.status_code == 401:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # get /user
    #
    def UsersGetAuthenticated(self, ):
        """If the authenticated user is authenticated through basic authentication or OAuth with the `user` scope, then the response lists public and private profile information.

If the authenticated user is authenticated through OAuth without the `user` scope, then the response lists only public profile information.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#get-the-authenticated-user
        /user
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/user", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return r.json()
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /users/{username}
    #
    def UsersGetByUsername(self, username:str):
        """Provides publicly available information about someone with a GitHub account.

GitHub Apps with the `Plan` user permission can use this endpoint to retrieve information about a user's GitHub Enterprise Server plan. The GitHub App must be authenticated as a user. See "[Identifying and authorizing users for GitHub Apps](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/)" for details about authentication. For an example response, see 'Response with GitHub Enterprise Server plan information' below"

The `email` key in the following response is the publicly visible email address from your GitHub Enterprise Server [profile page](https://github.com/settings/profile). When setting up your profile, you can select a primary email address to be “public” which provides an email entry for this endpoint. If you do not set a public email address for `email`, then it will have a value of `null`. You only see publicly visible email addresses when authenticated with GitHub Enterprise Server. For more information, see [Authentication](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#authentication).

The Emails API enables you to list all of your email addresses, and toggle a primary email to be visible publicly. For more information, see "[Emails API](https://docs.github.com/enterprise-server@3.3/rest/reference/users#emails)".
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#get-a-user
        /users/{username}
        
        arguments:
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/users/{username}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return r.json()
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /users/{username}/hovercard
    #
    def UsersGetContextForUser(self, username:str,subject_type=None, subject_id:str=None):
        """Provides hovercard information when authenticated through basic auth or OAuth with the `repo` scope. You can find out more about someone in relation to their pull requests, issues, repositories, and organizations.

The `subject_type` and `subject_id` parameters provide context for the person's hovercard, which returns more information than without the parameters. For example, if you wanted to find out more about `octocat` who owns the `Spoon-Knife` repository via cURL, it would look like this:

```shell
 curl -u username:token
  https://api.github.com/users/octocat/hovercard?subject_type=repository&subject_id=1300192
```
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#get-contextual-information-for-a-user
        /users/{username}/hovercard
        
        arguments:
        username -- 
        subject_type -- Identifies which additional information you'd like to receive about the person's hovercard. Can be `organization`, `repository`, `issue`, `pull_request`. **Required** when using `subject_id`.
        subject_id -- Uses the ID for the `subject_type` you specified. **Required** when using `subject_type`.
        
        """
        
        data = {}
        if subject_type is not None:
            data['subject_type'] = subject_type
        if subject_id is not None:
            data['subject_id'] = subject_id
        
        
        r = self._session.get(f"{self._url}/users/{username}/hovercard", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Hovercard(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /user/gpg_keys/{gpg_key_id}
    #
    def UsersGetGpgKeyForAuthenticatedUser(self, gpg_key_id:int):
        """View extended details for a single GPG key. Requires that you are authenticated via Basic Auth or via OAuth with at least `read:gpg_key` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#get-a-gpg-key-for-the-authenticated-user
        /user/gpg_keys/{gpg_key_id}
        
        arguments:
        gpg_key_id -- gpg_key_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/user/gpg_keys/{gpg_key_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return GpgKey(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /user/keys/{key_id}
    #
    def UsersGetPublicSshKeyForAuthenticatedUser(self, key_id:int):
        """View extended details for a single public SSH key. Requires that you are authenticated via Basic Auth or via OAuth with at least `read:public_key` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#get-a-public-ssh-key-for-the-authenticated-user
        /user/keys/{key_id}
        
        arguments:
        key_id -- key_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/user/keys/{key_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Key(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /users
    #
    def UsersList(self, since:int=None, per_page=30):
        """Lists all users, in the order that they signed up on GitHub Enterprise Server. This list includes personal user accounts and organization accounts.

Note: Pagination is powered exclusively by the `since` parameter. Use the [Link header](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#link-header) to get the URL for the next page of users.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#list-users
        /users
        
        arguments:
        since -- A user ID. Only return users with an ID greater than this ID.
        per_page -- Results per page (max 100)
        
        """
        
        data = {}
        if since is not None:
            data['since'] = since
        if per_page is not None:
            data['per_page'] = per_page
        
        
        r = self._session.get(f"{self._url}/users", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and SimpleUser(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /user/emails
    #
    def UsersListEmailsForAuthenticatedUser(self, per_page=30, page=1):
        """Lists all of your email addresses, and specifies which one is visible to the public. This endpoint is accessible with the `user:email` scope.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#list-email-addresses-for-the-authenticated-user
        /user/emails
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/user/emails", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Email(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /user/following
    #
    def UsersListFollowedByAuthenticatedUser(self, per_page=30, page=1):
        """Lists the people who the authenticated user follows.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#list-the-people-the-authenticated-user-follows
        /user/following
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/user/following", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and SimpleUser(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /user/followers
    #
    def UsersListFollowersForAuthenticatedUser(self, per_page=30, page=1):
        """Lists the people following the authenticated user.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#list-followers-of-the-authenticated-user
        /user/followers
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/user/followers", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and SimpleUser(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /users/{username}/followers
    #
    def UsersListFollowersForUser(self, username:str,per_page=30, page=1):
        """Lists the people following the specified user.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#list-followers-of-a-user
        /users/{username}/followers
        
        arguments:
        username -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/users/{username}/followers", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and SimpleUser(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /users/{username}/following
    #
    def UsersListFollowingForUser(self, username:str,per_page=30, page=1):
        """Lists the people who the specified user follows.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#list-the-people-a-user-follows
        /users/{username}/following
        
        arguments:
        username -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/users/{username}/following", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and SimpleUser(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /user/gpg_keys
    #
    def UsersListGpgKeysForAuthenticatedUser(self, per_page=30, page=1):
        """Lists the current user's GPG keys. Requires that you are authenticated via Basic Auth or via OAuth with at least `read:gpg_key` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#list-gpg-keys-for-the-authenticated-user
        /user/gpg_keys
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/user/gpg_keys", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and GpgKey(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /users/{username}/gpg_keys
    #
    def UsersListGpgKeysForUser(self, username:str,per_page=30, page=1):
        """Lists the GPG keys for a user. This information is accessible by anyone.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#list-gpg-keys-for-a-user
        /users/{username}/gpg_keys
        
        arguments:
        username -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/users/{username}/gpg_keys", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and GpgKey(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /user/public_emails
    #
    def UsersListPublicEmailsForAuthenticatedUser(self, per_page=30, page=1):
        """Lists your publicly visible email address, which you can set with the [Set primary email visibility for the authenticated user](https://docs.github.com/enterprise-server@3.3/rest/reference/users#set-primary-email-visibility-for-the-authenticated-user) endpoint. This endpoint is accessible with the `user:email` scope.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#list-public-email-addresses-for-the-authenticated-user
        /user/public_emails
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/user/public_emails", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Email(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /users/{username}/keys
    #
    def UsersListPublicKeysForUser(self, username:str,per_page=30, page=1):
        """Lists the _verified_ public SSH keys for a user. This is accessible by anyone.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#list-public-keys-for-a-user
        /users/{username}/keys
        
        arguments:
        username -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/users/{username}/keys", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and KeySimple(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /user/keys
    #
    def UsersListPublicSshKeysForAuthenticatedUser(self, per_page=30, page=1):
        """Lists the public SSH keys for the authenticated user's GitHub account. Requires that you are authenticated via Basic Auth or via OAuth with at least `read:public_key` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#list-public-ssh-keys-for-the-authenticated-user
        /user/keys
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/user/keys", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Key(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /user/following/{username}
    #
    def UsersUnfollow(self, username:str):
        """Unfollowing a user requires the user to be logged in and authenticated with basic auth or OAuth with the `user:follow` scope.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users#unfollow-a-user
        /user/following/{username}
        
        arguments:
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/user/following/{username}", 
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
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # patch /user
    #
    def UsersUpdateAuthenticated(self, name:str=None, email:str=None, blog:str=None, twitter_username:str=None, company:str=None, location:str=None, hireable:bool=None, bio:str=None):
        """**Note:** If your email is set to private and you send an `email` parameter as part of this request to update your profile, your privacy settings are still enforced: the email address will not be displayed on your public profile or via the API.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/users/#update-the-authenticated-user
        /user
        
        arguments:
        name -- The new name of the user.
        email -- The publicly visible email address of the user.
        blog -- The new blog URL of the user.
        twitter_username -- The new Twitter username of the user.
        company -- The new company of the user.
        location -- The new location of the user.
        hireable -- The new hiring availability of the user.
        bio -- The new short biography of the user.
        

        """
    
        data = {
        'name': name,
        'email': email,
        'blog': blog,
        'twitter_username': twitter_username,
        'company': company,
        'location': location,
        'hireable': hireable,
        'bio': bio,
        
        }
        

        
        r = self._session.patch(f"{self._url}/user", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return PrivateUser(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
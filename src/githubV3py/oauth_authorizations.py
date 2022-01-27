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

class OauthAuthorizations(object):


    #
    # post /authorizations
    #
    def OauthAuthorizationsCreateAuthorization(self, scopes:list=[], note:str=None, note_url:str=None, client_id:str=None, client_secret:str=None, fingerprint:str=None):
        """**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.3/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

**Warning:** Apps must use the [web application flow](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow) to obtain OAuth tokens that work with GitHub Enterprise Server SAML organizations. OAuth tokens created using the Authorizations API will be unable to access GitHub Enterprise Server SAML organizations. For more information, see the [blog post](https://developer.github.com/changes/2019-11-05-deprecated-passwords-and-authorizations-api).

Creates OAuth tokens using [Basic Authentication](https://docs.github.com/enterprise-server@3.3/rest/overview/other-authentication-methods#basic-authentication). If you have two-factor authentication setup, Basic Authentication for this endpoint requires that you use a one-time password (OTP) and your username and password instead of tokens. For more information, see "[Working with two-factor authentication](https://docs.github.com/enterprise-server@3.3/rest/overview/other-authentication-methods#working-with-two-factor-authentication)."

To create tokens for a particular OAuth application using this endpoint, you must authenticate as the user you want to create an authorization for and provide the app's client ID and secret, found on your OAuth application's settings page. If your OAuth application intends to create multiple tokens for one user, use `fingerprint` to differentiate between them.

You can also create tokens on GitHub Enterprise Server from the [personal access tokens settings](https://github.com/settings/tokens) page. Read more about these tokens in [the GitHub Help documentation](https://help.github.com/articles/creating-an-access-token-for-command-line-use).

Organizations that enforce SAML SSO require personal access tokens to be allowed. Read more about allowing tokens in [the GitHub Help documentation](https://help.github.com/articles/about-identity-and-access-management-with-saml-single-sign-on).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations#create-a-new-authorization
        /authorizations
        
        arguments:
        scopes -- A list of scopes that this authorization is in.
        note -- A note to remind you what the OAuth token is for.
        note_url -- A URL to remind you what app the OAuth token is for.
        client_id -- The OAuth app client key for which to create the token.
        client_secret -- The OAuth app client secret for which to create the token.
        fingerprint -- A unique string to distinguish an authorization from others created for the same client ID and user.
        

        """
    
        data = {
        'scopes': scopes,
        'note': note,
        'note_url': note_url,
        'client_id': client_id,
        'client_secret': client_secret,
        'fingerprint': fingerprint,
        
        }
        

        
        r = self._session.post(f"{self._url}/authorizations", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Authorization(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /authorizations/{authorization_id}
    #
    def OauthAuthorizationsDeleteAuthorization(self, authorization_id:int):
        """**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations#delete-an-authorization
        /authorizations/{authorization_id}
        
        arguments:
        authorization_id -- authorization_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/authorizations/{authorization_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /applications/grants/{grant_id}
    #
    def OauthAuthorizationsDeleteGrant(self, grant_id:int):
        """**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.3/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations/) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

Deleting an OAuth application's grant will also delete all OAuth tokens associated with the application for your user. Once deleted, the application has no access to your account and is no longer listed on [the application authorizations settings screen within GitHub](https://github.com/settings/applications#authorized).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations#delete-a-grant
        /applications/grants/{grant_id}
        
        arguments:
        grant_id -- grant_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/applications/grants/{grant_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /authorizations/{authorization_id}
    #
    def OauthAuthorizationsGetAuthorization(self, authorization_id:int):
        """**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations#get-a-single-authorization
        /authorizations/{authorization_id}
        
        arguments:
        authorization_id -- authorization_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/authorizations/{authorization_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Authorization(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /applications/grants/{grant_id}
    #
    def OauthAuthorizationsGetGrant(self, grant_id:int):
        """**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations#get-a-single-grant
        /applications/grants/{grant_id}
        
        arguments:
        grant_id -- grant_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/applications/grants/{grant_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ApplicationGrant(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # put /authorizations/clients/{client_id}
    #
    def OauthAuthorizationsGetOrCreateAuthorizationForApp(self, client_id:str,client_secret:str, scopes:list=[], note:str=None, note_url:str=None, fingerprint:str=None):
        """**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.3/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

**Warning:** Apps must use the [web application flow](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow) to obtain OAuth tokens that work with GitHub Enterprise Server SAML organizations. OAuth tokens created using the Authorizations API will be unable to access GitHub Enterprise Server SAML organizations. For more information, see the [blog post](https://developer.github.com/changes/2019-11-05-deprecated-passwords-and-authorizations-api).

Creates a new authorization for the specified OAuth application, only if an authorization for that application doesn't already exist for the user. The URL includes the 20 character client ID for the OAuth app that is requesting the token. It returns the user's existing authorization for the application if one is present. Otherwise, it creates and returns a new one.

If you have two-factor authentication setup, Basic Authentication for this endpoint requires that you use a one-time password (OTP) and your username and password instead of tokens. For more information, see "[Working with two-factor authentication](https://docs.github.com/enterprise-server@3.3/rest/overview/other-authentication-methods#working-with-two-factor-authentication)."

**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.3/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations#get-or-create-an-authorization-for-a-specific-app
        /authorizations/clients/{client_id}
        
        arguments:
        client_id -- The client ID of your GitHub app.
        client_secret -- The OAuth app client secret for which to create the token.
        scopes -- A list of scopes that this authorization is in.
        note -- A note to remind you what the OAuth token is for.
        note_url -- A URL to remind you what app the OAuth token is for.
        fingerprint -- A unique string to distinguish an authorization from others created for the same client ID and user.
        

        """
    
        data = {
        'client_secret': client_secret,
        'scopes': scopes,
        'note': note,
        'note_url': note_url,
        'fingerprint': fingerprint,
        
        }
        

        
        r = self._session.put(f"{self._url}/authorizations/clients/{client_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Authorization(**r.json())
            
        if r.status_code == 201:
            return Authorization(**r.json())
            
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
    # put /authorizations/clients/{client_id}/{fingerprint}
    #
    def OauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprint(self, client_id:str, fingerprint:str,client_secret:str, scopes:list=[], note:str=None, note_url:str=None):
        """**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.3/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

**Warning:** Apps must use the [web application flow](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow) to obtain OAuth tokens that work with GitHub Enterprise Server SAML organizations. OAuth tokens created using the Authorizations API will be unable to access GitHub Enterprise Server SAML organizations. For more information, see the [blog post](https://developer.github.com/changes/2019-11-05-deprecated-passwords-and-authorizations-api).

This method will create a new authorization for the specified OAuth application, only if an authorization for that application and fingerprint do not already exist for the user. The URL includes the 20 character client ID for the OAuth app that is requesting the token. `fingerprint` is a unique string to distinguish an authorization from others created for the same client ID and user. It returns the user's existing authorization for the application if one is present. Otherwise, it creates and returns a new one.

If you have two-factor authentication setup, Basic Authentication for this endpoint requires that you use a one-time password (OTP) and your username and password instead of tokens. For more information, see "[Working with two-factor authentication](https://docs.github.com/enterprise-server@3.3/rest/overview/other-authentication-methods#working-with-two-factor-authentication)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations#get-or-create-an-authorization-for-a-specific-app-and-fingerprint
        /authorizations/clients/{client_id}/{fingerprint}
        
        arguments:
        client_id -- The client ID of your GitHub app.
        fingerprint -- 
        client_secret -- The OAuth app client secret for which to create the token.
        scopes -- A list of scopes that this authorization is in.
        note -- A note to remind you what the OAuth token is for.
        note_url -- A URL to remind you what app the OAuth token is for.
        

        """
    
        data = {
        'client_secret': client_secret,
        'scopes': scopes,
        'note': note,
        'note_url': note_url,
        
        }
        

        
        r = self._session.put(f"{self._url}/authorizations/clients/{client_id}/{fingerprint}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Authorization(**r.json())
            
        if r.status_code == 201:
            return Authorization(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # get /authorizations
    #
    def OauthAuthorizationsListAuthorizations(self, per_page=30, page=1, client_id:str=None):
        """**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations#list-your-authorizations
        /authorizations
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        client_id -- The client ID of your GitHub app.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        if client_id is not None:
            data['client_id'] = client_id
        
        
        r = self._session.get(f"{self._url}/authorizations", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Authorization(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /applications/grants
    #
    def OauthAuthorizationsListGrants(self, per_page=30, page=1, client_id:str=None):
        """**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.3/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

You can use this API to list the set of OAuth applications that have been granted access to your account. Unlike the [list your authorizations](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations#list-your-authorizations) API, this API does not manage individual tokens. This API will return one entry for each OAuth application that has been granted access to your account, regardless of the number of tokens an application has generated for your user. The list of OAuth applications returned matches what is shown on [the application authorizations settings screen within GitHub](https://github.com/settings/applications#authorized). The `scopes` returned are the union of scopes authorized for the application. For example, if an application has one token with `repo` scope and another token with `user` scope, the grant will return `["repo", "user"]`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations#list-your-grants
        /applications/grants
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        client_id -- The client ID of your GitHub app.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        if client_id is not None:
            data['client_id'] = client_id
        
        
        r = self._session.get(f"{self._url}/applications/grants", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and ApplicationGrant(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # patch /authorizations/{authorization_id}
    #
    def OauthAuthorizationsUpdateAuthorization(self, authorization_id:int,scopes:list=[], add_scopes:list=[], remove_scopes:list=[], note:str=None, note_url:str=None, fingerprint:str=None):
        """**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.3/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

If you have two-factor authentication setup, Basic Authentication for this endpoint requires that you use a one-time password (OTP) and your username and password instead of tokens. For more information, see "[Working with two-factor authentication](https://docs.github.com/enterprise-server@3.3/rest/overview/other-authentication-methods#working-with-two-factor-authentication)."

You can only send one of these scope keys at a time.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/oauth-authorizations#update-an-existing-authorization
        /authorizations/{authorization_id}
        
        arguments:
        authorization_id -- authorization_id parameter
        scopes -- A list of scopes that this authorization is in.
        add_scopes -- A list of scopes to add to this authorization.
        remove_scopes -- A list of scopes to remove from this authorization.
        note -- A note to remind you what the OAuth token is for.
        note_url -- A URL to remind you what app the OAuth token is for.
        fingerprint -- A unique string to distinguish an authorization from others created for the same client ID and user.
        

        """
    
        data = {
        'scopes': scopes,
        'add_scopes': add_scopes,
        'remove_scopes': remove_scopes,
        'note': note,
        'note_url': note_url,
        'fingerprint': fingerprint,
        
        }
        

        
        r = self._session.patch(f"{self._url}/authorizations/{authorization_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Authorization(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
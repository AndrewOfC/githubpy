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

class Apps(object):


    #
    # put /user/installations/{installation_id}/repositories/{repository_id}
    #
    def AppsAddRepoToInstallationForAuthenticatedUser(self, installation_id:int, repository_id:int):
        """Add a single repository to an installation. The authenticated user must have admin access to the repository.

You must use a personal access token (which you can create via the [command line](https://docs.github.com/enterprise-server@3.3/github/authenticating-to-github/creating-a-personal-access-token) or [Basic Authentication](https://docs.github.com/enterprise-server@3.3/rest/overview/other-authentication-methods#basic-authentication)) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#add-a-repository-to-an-app-installation
        /user/installations/{installation_id}/repositories/{repository_id}
        
        arguments:
        installation_id -- installation_id parameter
        repository_id -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.put(f"{self._url}/user/installations/{installation_id}/repositories/{repository_id}", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # get /applications/{client_id}/tokens/{access_token}
    #
    def AppsCheckAuthorization(self, client_id:str, access_token:str):
        """**Deprecation Notice:** GitHub Enterprise Server will discontinue OAuth endpoints that contain `access_token` in the path parameter. We have introduced new endpoints that allow you to securely manage tokens for OAuth Apps by moving `access_token` to the request body. For more information, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-app-endpoint/).

OAuth applications can use a special API method for checking OAuth token validity without exceeding the normal rate limits for failed login attempts. Authentication works differently with this particular endpoint. You must use [Basic Authentication](https://docs.github.com/enterprise-server@3.3/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the OAuth application's `client_id` and `client_secret` as the username and password. Invalid tokens will return `404 NOT FOUND`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#check-an-authorization
        /applications/{client_id}/tokens/{access_token}
        
        arguments:
        client_id -- The client ID of your GitHub app.
        access_token -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/applications/{client_id}/tokens/{access_token}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return NullableAuthorization(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # post /applications/{client_id}/token
    #
    def AppsCheckToken(self, client_id:str,access_token:str):
        """OAuth applications can use a special API method for checking OAuth token validity without exceeding the normal rate limits for failed login attempts. Authentication works differently with this particular endpoint. You must use [Basic Authentication](https://docs.github.com/enterprise-server@3.3/rest/overview/other-authentication-methods#basic-authentication) to use this endpoint, where the username is the OAuth application `client_id` and the password is its `client_secret`. Invalid tokens will return `404 NOT FOUND`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#check-a-token
        /applications/{client_id}/token
        
        arguments:
        client_id -- The client ID of your GitHub app.
        access_token -- The access_token of the OAuth application.
        

        """
    
        data = {
        'access_token': access_token,
        
        }
        

        
        r = self._session.post(f"{self._url}/applications/{client_id}/token", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Authorization(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/content_references/{content_reference_id}/attachments
    #
    def AppsCreateContentAttachment(self, owner:str, repo:str, content_reference_id:int,body:str, title:str):
        """Creates an attachment under a content reference URL in the body or comment of an issue or pull request. Use the `id` and `repository` `full_name` of the content reference from the [`content_reference` event](https://docs.github.com/enterprise-server@3.3/webhooks/event-payloads/#content_reference) to create an attachment.

The app must create a content attachment within six hours of the content reference URL being posted. See "[Using content attachments](https://docs.github.com/enterprise-server@3.3/apps/using-content-attachments/)" for details about content attachments.

You must use an [installation access token](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#create-a-content-attachment
        /repos/{owner}/{repo}/content_references/{content_reference_id}/attachments
        
        arguments:
        owner -- The owner of the repository. Determined from the `repository` `full_name` of the `content_reference` event.
        repo -- The name of the repository. Determined from the `repository` `full_name` of the `content_reference` event.
        content_reference_id -- The `id` of the `content_reference` event.
        body -- The body of the attachment
        title -- The title of the attachment
        

        """
    
        data = {
        'body': body,
        'title': title,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/content_references/{content_reference_id}/attachments", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Contentreferenceattachment(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        if r.status_code == 415:
            return Preview_header_missing(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /app-manifests/{code}/conversions
    #
    def AppsCreateFromManifest(self, code:str,object:object):
        """Use this endpoint to complete the handshake necessary when implementing the [GitHub App Manifest flow](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/creating-github-apps-from-a-manifest/). When you create a GitHub App with the manifest flow, you receive a temporary `code` used to retrieve the GitHub App's `id`, `pem` (private key), and `webhook_secret`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#create-a-github-app-from-a-manifest
        /app-manifests/{code}/conversions
        
        arguments:
        code -- 
        object -- 
        

        """
    
        data = {
        'object': object,
        
        }
        

        
        r = self._session.post(f"{self._url}/app-manifests/{code}/conversions", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Integration(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationErrorSimple(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /app/installations/{installation_id}/access_tokens
    #
    def AppsCreateInstallationAccessToken(self, installation_id:int,repositories:list=[], repository_ids:list=[], permissions:dict=None):
        """Creates an installation access token that enables a GitHub App to make authenticated API requests for the app's installation on an organization or individual account. Installation tokens expire one hour from the time you create them. Using an expired token produces a status code of `401 - Unauthorized`, and requires creating a new installation token. By default the installation token has access to all repositories that the installation can access. To restrict the access to specific repositories, you can provide the `repository_ids` when creating the token. When you omit `repository_ids`, the response does not contain the `repositories` key.

You must use a [JWT](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps/#create-an-installation-access-token-for-an-app
        /app/installations/{installation_id}/access_tokens
        
        arguments:
        installation_id -- installation_id parameter
        repositories -- List of repository names that the token should have access to
        repository_ids -- List of repository IDs that the token should have access to
        permissions -- 
        

        """
    
        data = {
        'repositories': repositories,
        'repository_ids': repository_ids,
        'permissions': permissions,
        
        }
        

        
        r = self._session.post(f"{self._url}/app/installations/{installation_id}/access_tokens", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return InstallationToken(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 415:
            return Preview_header_missing(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /applications/{client_id}/grant
    #
    def AppsDeleteAuthorization(self, client_id:str):
        """OAuth application owners can revoke a grant for their OAuth application and a specific user. You must use [Basic Authentication](https://docs.github.com/enterprise-server@3.3/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the OAuth application's `client_id` and `client_secret` as the username and password. You must also provide a valid OAuth `access_token` as an input parameter and the grant for the token's owner will be deleted.
Deleting an OAuth application's grant will also delete all OAuth tokens associated with the application for the user. Once deleted, the application will have no access to the user's account and will no longer be listed on [the application authorizations settings screen within GitHub](https://github.com/settings/applications#authorized).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#delete-an-app-authorization
        /applications/{client_id}/grant
        
        arguments:
        client_id -- The client ID of your GitHub app.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/applications/{client_id}/grant", 
                           params=data,
                           **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /app/installations/{installation_id}
    #
    def AppsDeleteInstallation(self, installation_id:int):
        """Uninstalls a GitHub App on a user, organization, or business account. If you prefer to temporarily suspend an app's access to your account's resources, then we recommend the "[Suspend an app installation](https://docs.github.com/enterprise-server@3.3/rest/reference/apps/#suspend-an-app-installation)" endpoint.

You must use a [JWT](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#delete-an-installation-for-the-authenticated-app
        /app/installations/{installation_id}
        
        arguments:
        installation_id -- installation_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/app/installations/{installation_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /applications/{client_id}/token
    #
    def AppsDeleteToken(self, client_id:str):
        """OAuth application owners can revoke a single token for an OAuth application. You must use [Basic Authentication](https://docs.github.com/enterprise-server@3.3/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the OAuth application's `client_id` and `client_secret` as the username and password.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#delete-an-app-token
        /applications/{client_id}/token
        
        arguments:
        client_id -- The client ID of your GitHub app.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/applications/{client_id}/token", 
                           params=data,
                           **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /app
    #
    def AppsGetAuthenticated(self, ):
        """Returns the GitHub App associated with the authentication credentials used. To see how many app installations are associated with this GitHub App, see the `installations_count` in the response. For more details about your app's installations, see the "[List installations for the authenticated app](https://docs.github.com/enterprise-server@3.3/rest/reference/apps#list-installations-for-the-authenticated-app)" endpoint.

You must use a [JWT](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#get-the-authenticated-app
        /app
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/app", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Integration(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /apps/{app_slug}
    #
    def AppsGetBySlug(self, app_slug:str):
        """**Note**: The `:app_slug` is just the URL-friendly name of your GitHub App. You can find this on the settings page for your GitHub App (e.g., `https://github.com/settings/apps/:app_slug`).

If the GitHub App you specify is public, you can access this endpoint without authenticating. If the GitHub App you specify is private, you must authenticate with a [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) or an [installation access token](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps/#get-an-app
        /apps/{app_slug}
        
        arguments:
        app_slug -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/apps/{app_slug}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Integration(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 415:
            return Preview_header_missing(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /app/installations/{installation_id}
    #
    def AppsGetInstallation(self, installation_id:int):
        """Enables an authenticated GitHub App to find an installation's information using the installation id. The installation's account type (`target_type`) will be either an organization or a user account, depending which account the repository belongs to.

You must use a [JWT](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#get-an-installation-for-the-authenticated-app
        /app/installations/{installation_id}
        
        arguments:
        installation_id -- installation_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/app/installations/{installation_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Installation(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 415:
            return Preview_header_missing(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/installation
    #
    def AppsGetOrgInstallation(self, org:str):
        """Enables an authenticated GitHub App to find the organization's installation information.

You must use a [JWT](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#get-an-organization-installation-for-the-authenticated-app
        /orgs/{org}/installation
        
        arguments:
        org -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/installation", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Installation(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/installation
    #
    def AppsGetRepoInstallation(self, owner:str, repo:str):
        """Enables an authenticated GitHub App to find the repository's installation information. The installation's account type will be either an organization or a user account, depending which account the repository belongs to.

You must use a [JWT](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#get-a-repository-installation-for-the-authenticated-app
        /repos/{owner}/{repo}/installation
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/installation", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Installation(**r.json())
            
        if r.status_code == 301:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /users/{username}/installation
    #
    def AppsGetUserInstallation(self, username:str):
        """Enables an authenticated GitHub App to find the user’s installation information.

You must use a [JWT](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#get-a-user-installation-for-the-authenticated-app
        /users/{username}/installation
        
        arguments:
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/users/{username}/installation", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Installation(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /app/hook/config
    #
    def AppsGetWebhookConfigForApp(self, ):
        """Returns the webhook configuration for a GitHub App. For more information about configuring a webhook for your app, see "[Creating a GitHub App](/developers/apps/creating-a-github-app)."

You must use a [JWT](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#get-a-webhook-configuration-for-an-app
        /app/hook/config
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/app/hook/config", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return WebhookConfiguration(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /app/hook/deliveries/{delivery_id}
    #
    def AppsGetWebhookDelivery(self, delivery_id:int):
        """Returns a delivery for the webhook configured for a GitHub App.

You must use a [JWT](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#get-a-delivery-for-an-app-webhook
        /app/hook/deliveries/{delivery_id}
        
        arguments:
        delivery_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/app/hook/deliveries/{delivery_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return WebhookDelivery(**r.json())
            
        if r.status_code == 400:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /user/installations/{installation_id}/repositories
    #
    def AppsListInstallationReposForAuthenticatedUser(self, installation_id:int,per_page=30, page=1):
        """List repositories that the authenticated user has explicit permission (`:read`, `:write`, or `:admin`) to access for an installation.

The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.

You must use a [user-to-server OAuth access token](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/#identifying-users-on-your-site), created for a user who has authorized your GitHub App, to access this endpoint.

The access the user has to each repository is included in the hash under the `permissions` key.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#list-repositories-accessible-to-the-user-access-token
        /user/installations/{installation_id}/repositories
        
        arguments:
        installation_id -- installation_id parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/user/installations/{installation_id}/repositories", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return AppsListInstallationReposForAuthenticatedUserSuccess(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /app/installations
    #
    def AppsListInstallations(self, per_page=30, page=1, since:datetime=None, outdated:str=None):
        """You must use a [JWT](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

The permissions the installation has are included under the `permissions` key.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#list-installations-for-the-authenticated-app
        /app/installations
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        since -- Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        outdated -- 
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        if since is not None:
            data['since'] = since.isoformat()
        if outdated is not None:
            data['outdated'] = outdated
        
        
        r = self._session.get(f"{self._url}/app/installations", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Installation(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /user/installations
    #
    def AppsListInstallationsForAuthenticatedUser(self, per_page=30, page=1):
        """Lists installations of your GitHub App that the authenticated user has explicit permission (`:read`, `:write`, or `:admin`) to access.

You must use a [user-to-server OAuth access token](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/#identifying-users-on-your-site), created for a user who has authorized your GitHub App, to access this endpoint.

The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.

You can find the permissions for the installation under the `permissions` key.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#list-app-installations-accessible-to-the-user-access-token
        /user/installations
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/user/installations", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return AppsListInstallationsForAuthenticatedUserSuccess(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 415:
            return Preview_header_missing(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /installation/repositories
    #
    def AppsListReposAccessibleToInstallation(self, per_page=30, page=1):
        """List repositories that an app installation can access.

You must use an [installation access token](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#list-repositories-accessible-to-the-app-installation
        /installation/repositories
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/installation/repositories", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return AppsListReposAccessibleToInstallationSuccess(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /app/hook/deliveries
    #
    def AppsListWebhookDeliveries(self, per_page=30, cursor:str=None):
        """Returns a list of webhook deliveries for the webhook configured for a GitHub App.

You must use a [JWT](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#list-deliveries-for-an-app-webhook
        /app/hook/deliveries
        
        arguments:
        per_page -- Results per page (max 100)
        cursor -- Used for pagination: the starting delivery from which the page of deliveries is fetched. Refer to the `link` header for the next and previous page cursors.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if cursor is not None:
            data['cursor'] = cursor
        
        
        r = self._session.get(f"{self._url}/app/hook/deliveries", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and SimpleWebhookDelivery(**entry) for entry in r.json() ]
            
        if r.status_code == 400:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # post /app/hook/deliveries/{delivery_id}/attempts
    #
    def AppsRedeliverWebhookDelivery(self, delivery_id:int):
        """Redeliver a delivery for the webhook configured for a GitHub App.

You must use a [JWT](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#redeliver-a-delivery-for-an-app-webhook
        /app/hook/deliveries/{delivery_id}/attempts
        
        arguments:
        delivery_id -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/app/hook/deliveries/{delivery_id}/attempts", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 202:
            return r.json()
            
        if r.status_code == 400:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /user/installations/{installation_id}/repositories/{repository_id}
    #
    def AppsRemoveRepoFromInstallationForAuthenticatedUser(self, installation_id:int, repository_id:int):
        """Remove a single repository from an installation. The authenticated user must have admin access to the repository.

You must use a personal access token (which you can create via the [command line](https://docs.github.com/enterprise-server@3.3/github/authenticating-to-github/creating-a-personal-access-token) or [Basic Authentication](https://docs.github.com/enterprise-server@3.3/rest/overview/other-authentication-methods#basic-authentication)) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#remove-a-repository-from-an-app-installation
        /user/installations/{installation_id}/repositories/{repository_id}
        
        arguments:
        installation_id -- installation_id parameter
        repository_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/user/installations/{installation_id}/repositories/{repository_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # post /applications/{client_id}/tokens/{access_token}
    #
    def AppsResetAuthorization(self, client_id:str, access_token:str):
        """**Deprecation Notice:** GitHub Enterprise Server will discontinue OAuth endpoints that contain `access_token` in the path parameter. We have introduced new endpoints that allow you to securely manage tokens for OAuth Apps by moving `access_token` to the request body. For more information, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-app-endpoint/).

OAuth applications can use this API method to reset a valid OAuth token without end-user involvement. Applications must save the "token" property in the response because changes take effect immediately. You must use [Basic Authentication](https://docs.github.com/enterprise-server@3.3/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the OAuth application's `client_id` and `client_secret` as the username and password. Invalid tokens will return `404 NOT FOUND`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#reset-an-authorization
        /applications/{client_id}/tokens/{access_token}
        
        arguments:
        client_id -- The client ID of your GitHub app.
        access_token -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/applications/{client_id}/tokens/{access_token}", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Authorization(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /applications/{client_id}/token
    #
    def AppsResetToken(self, client_id:str,access_token:str):
        """OAuth applications can use this API method to reset a valid OAuth token without end-user involvement. Applications must save the "token" property in the response because changes take effect immediately. You must use [Basic Authentication](https://docs.github.com/enterprise-server@3.3/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the OAuth application's `client_id` and `client_secret` as the username and password. Invalid tokens will return `404 NOT FOUND`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#reset-a-token
        /applications/{client_id}/token
        
        arguments:
        client_id -- The client ID of your GitHub app.
        access_token -- The access_token of the OAuth application.
        

        """
    
        data = {
        'access_token': access_token,
        
        }
        

        
        r = self._session.patch(f"{self._url}/applications/{client_id}/token", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Authorization(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /applications/{client_id}/tokens/{access_token}
    #
    def AppsRevokeAuthorizationForApplication(self, client_id:str, access_token:str):
        """**Deprecation Notice:** GitHub Enterprise Server will discontinue OAuth endpoints that contain `access_token` in the path parameter. We have introduced new endpoints that allow you to securely manage tokens for OAuth Apps by moving `access_token` to the request body. For more information, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-app-endpoint/).

OAuth application owners can revoke a single token for an OAuth application. You must use [Basic Authentication](https://docs.github.com/enterprise-server@3.3/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the OAuth application's `client_id` and `client_secret` as the username and password.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#revoke-an-authorization-for-an-application
        /applications/{client_id}/tokens/{access_token}
        
        arguments:
        client_id -- The client ID of your GitHub app.
        access_token -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/applications/{client_id}/tokens/{access_token}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /applications/{client_id}/grants/{access_token}
    #
    def AppsRevokeGrantForApplication(self, client_id:str, access_token:str):
        """**Deprecation Notice:** GitHub Enterprise Server will discontinue OAuth endpoints that contain `access_token` in the path parameter. We have introduced new endpoints that allow you to securely manage tokens for OAuth Apps by moving `access_token` to the request body. For more information, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-app-endpoint/).

OAuth application owners can revoke a grant for their OAuth application and a specific user. You must use [Basic Authentication](https://docs.github.com/enterprise-server@3.3/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the OAuth application's `client_id` and `client_secret` as the username and password. You must also provide a valid token as `:access_token` and the grant for the token's owner will be deleted.

Deleting an OAuth application's grant will also delete all OAuth tokens associated with the application for the user. Once deleted, the application will have no access to the user's account and will no longer be listed on [the Applications settings page under "Authorized OAuth Apps" on GitHub Enterprise Server](https://github.com/settings/applications#authorized).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#revoke-a-grant-for-an-application
        /applications/{client_id}/grants/{access_token}
        
        arguments:
        client_id -- The client ID of your GitHub app.
        access_token -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/applications/{client_id}/grants/{access_token}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /installation/token
    #
    def AppsRevokeInstallationAccessToken(self, ):
        """Revokes the installation token you're using to authenticate as an installation and access this endpoint.

Once an installation token is revoked, the token is invalidated and cannot be used. Other endpoints that require the revoked installation token must have a new installation token to work. You can create a new token using the "[Create an installation access token for an app](https://docs.github.com/enterprise-server@3.3/rest/reference/apps#create-an-installation-access-token-for-an-app)" endpoint.

You must use an [installation access token](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#revoke-an-installation-access-token
        /installation/token
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/installation/token", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # post /applications/{client_id}/token/scoped
    #
    def AppsScopeToken(self, client_id:str,access_token:str, target:str=None, target_id:int=None, repositories:list=[], repository_ids:list=[], permissions:dict=None):
        """Use a non-scoped user-to-server OAuth access token to create a repository scoped and/or permission scoped user-to-server OAuth access token. You can specify which repositories the token can access and which permissions are granted to the token. You must use [Basic Authentication](https://docs.github.com/enterprise-server@3.3/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the OAuth application's `client_id` and `client_secret` as the username and password. Invalid tokens will return `404 NOT FOUND`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#create-a-scoped-access-token
        /applications/{client_id}/token/scoped
        
        arguments:
        client_id -- The client ID of your GitHub app.
        access_token -- The OAuth access token used to authenticate to the GitHub API.
        target -- The name of the user or organization to scope the user-to-server access token to. **Required** unless `target_id` is specified.
        target_id -- The ID of the user or organization to scope the user-to-server access token to. **Required** unless `target` is specified.
        repositories -- The list of repository names to scope the user-to-server access token to. `repositories` may not be specified if `repository_ids` is specified.
        repository_ids -- The list of repository IDs to scope the user-to-server access token to. `repository_ids` may not be specified if `repositories` is specified.
        permissions -- 
        

        """
    
        data = {
        'access_token': access_token,
        'target': target,
        'target_id': target_id,
        'repositories': repositories,
        'repository_ids': repository_ids,
        'permissions': permissions,
        
        }
        

        
        r = self._session.post(f"{self._url}/applications/{client_id}/token/scoped", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Authorization(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /app/installations/{installation_id}/suspended
    #
    def AppsSuspendInstallation(self, installation_id:int):
        """Suspends a GitHub App on a user, organization, or business account, which blocks the app from accessing the account's resources. When a GitHub App is suspended, the app's access to the GitHub Enterprise Server API or webhook events is blocked for that account.

You must use a [JWT](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#suspend-an-app-installation
        /app/installations/{installation_id}/suspended
        
        arguments:
        installation_id -- installation_id parameter
        

        """
    
        data = {
        
        }
        

        
        r = self._session.put(f"{self._url}/app/installations/{installation_id}/suspended", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /app/installations/{installation_id}/suspended
    #
    def AppsUnsuspendInstallation(self, installation_id:int):
        """Removes a GitHub App installation suspension.

You must use a [JWT](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#unsuspend-an-app-installation
        /app/installations/{installation_id}/suspended
        
        arguments:
        installation_id -- installation_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/app/installations/{installation_id}/suspended", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # patch /app/hook/config
    #
    def AppsUpdateWebhookConfigForApp(self, url:str=None, content_type:str=None, secret:str=None, insecure_ssl=None):
        """Updates the webhook configuration for a GitHub App. For more information about configuring a webhook for your app, see "[Creating a GitHub App](/developers/apps/creating-a-github-app)."

You must use a [JWT](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/apps#update-a-webhook-configuration-for-an-app
        /app/hook/config
        
        arguments:
        url -- 
        content_type -- 
        secret -- 
        insecure_ssl -- 
        

        """
    
        data = {
        'url': url,
        'content_type': content_type,
        'secret': secret,
        'insecure_ssl': insecure_ssl,
        
        }
        

        
        r = self._session.patch(f"{self._url}/app/hook/config", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return WebhookConfiguration(**r.json())
            

        return UnexpectedResult(r)
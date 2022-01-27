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

class Orgs(object):


    #
    # get /orgs/{org}/members/{username}
    #
    def OrgsCheckMembershipForUser(self, org:str, username:str):
        """Check if a user is, publicly or privately, a member of the organization.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#check-organization-membership-for-a-user
        /orgs/{org}/members/{username}
        
        arguments:
        org -- 
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/members/{username}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 302:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/public_members/{username}
    #
    def OrgsCheckPublicMembershipForUser(self, org:str, username:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#check-public-organization-membership-for-a-user
        /orgs/{org}/public_members/{username}
        
        arguments:
        org -- 
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/public_members/{username}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # put /orgs/{org}/outside_collaborators/{username}
    #
    def OrgsConvertMemberToOutsideCollaborator(self, org:str, username:str):
        """When an organization member is converted to an outside collaborator, they'll only have access to the repositories that their current team membership allows. The user will no longer be a member of the organization. For more information, see "[Converting an organization member to an outside collaborator](https://help.github.com/articles/converting-an-organization-member-to-an-outside-collaborator/)".
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#convert-an-organization-member-to-outside-collaborator
        /orgs/{org}/outside_collaborators/{username}
        
        arguments:
        org -- 
        username -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.put(f"{self._url}/orgs/{org}/outside_collaborators/{username}", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 202:
            return OrgsConvertMemberToOutsideCollaborator202(**r.json())
            
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /orgs/{org}/hooks
    #
    def OrgsCreateWebhook(self, org:str,config:dict, name:str, events:list=['push'], active:bool=True):
        """Here's how you can create a hook that posts payloads in JSON format:
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#create-an-organization-webhook
        /orgs/{org}/hooks
        
        arguments:
        org -- 
        config -- Key/value pairs to provide settings for this webhook. [These are defined below](https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#create-hook-config-params).
        name -- Must be passed as "web".
        events -- Determines what [events](https://docs.github.com/enterprise-server@3.3/webhooks/event-payloads) the hook is triggered for.
        active -- Determines if notifications are sent when the webhook is triggered. Set to `true` to send notifications.
        

        """
    
        data = {
        'config': config,
        'name': name,
        'events': events,
        'active': active,
        
        }
        

        
        r = self._session.post(f"{self._url}/orgs/{org}/hooks", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return OrgHook(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/hooks/{hook_id}
    #
    def OrgsDeleteWebhook(self, org:str, hook_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#delete-an-organization-webhook
        /orgs/{org}/hooks/{hook_id}
        
        arguments:
        org -- 
        hook_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/hooks/{hook_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}
    #
    def OrgsGet(self, org:str):
        """To see many of the organization response values, you need to be an authenticated organization owner with the `admin:org` scope. When the value of `two_factor_requirement_enabled` is `true`, the organization requires all members, billing managers, and outside collaborators to enable [two-factor authentication](https://help.github.com/articles/securing-your-account-with-two-factor-authentication-2fa/).

GitHub Apps with the `Organization plan` permission can use this endpoint to retrieve information about an organization's GitHub Enterprise Server plan. See "[Authenticating with GitHub Apps](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/)" for details. For an example response, see 'Response with GitHub Enterprise Server plan information' below."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#get-an-organization
        /orgs/{org}
        
        arguments:
        org -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return OrganizationFull(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/audit-log
    #
    def OrgsGetAuditLog(self, org:str,phrase:str=None, after:str=None, before:str=None, direction='desc', per_page=30, page=1):
        """Gets the audit log for an organization. For more information, see "[Reviewing the audit log for your organization](https://docs.github.com/enterprise-server@3.3/github/setting-up-and-managing-organizations-and-teams/reviewing-the-audit-log-for-your-organization)."

To use this endpoint, you must be an organization owner, and you must use an access token with the `admin:org` scope. GitHub Apps must have the `organization_administration` read permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#get-audit-log
        /orgs/{org}/audit-log
        
        arguments:
        org -- 
        phrase -- A search phrase. For more information, see [Searching the audit log](https://docs.github.com/enterprise-server@3.3/github/setting-up-and-managing-organizations-and-teams/reviewing-the-audit-log-for-your-organization#searching-the-audit-log).
        after -- A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for events after this cursor.
        before -- A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for events before this cursor.
        direction -- One of `asc` (ascending) or `desc` (descending).
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if phrase is not None:
            data['phrase'] = phrase
        if after is not None:
            data['after'] = after
        if before is not None:
            data['before'] = before
        if direction is not None:
            data['direction'] = direction
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/audit-log", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            json = r.json()
            return json and [ entry and AuditLogEvent(**AuditLogEvent.patchEntry(entry)) for entry in json ]
            
        
        return UnexpectedResult(r)
    #
    # get /user/memberships/orgs/{org}
    #
    def OrgsGetMembershipForAuthenticatedUser(self, org:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#get-an-organization-membership-for-the-authenticated-user
        /user/memberships/orgs/{org}
        
        arguments:
        org -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/user/memberships/orgs/{org}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return OrgMembership(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/memberships/{username}
    #
    def OrgsGetMembershipForUser(self, org:str, username:str):
        """In order to get a user's membership with an organization, the authenticated user must be an organization member. The `state` parameter in the response can be used to identify the user's membership status.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#get-organization-membership-for-a-user
        /orgs/{org}/memberships/{username}
        
        arguments:
        org -- 
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/memberships/{username}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return OrgMembership(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/hooks/{hook_id}
    #
    def OrgsGetWebhook(self, org:str, hook_id:int):
        """Returns a webhook configured in an organization. To get only the webhook `config` properties, see "[Get a webhook configuration for an organization](/rest/reference/orgs#get-a-webhook-configuration-for-an-organization)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#get-an-organization-webhook
        /orgs/{org}/hooks/{hook_id}
        
        arguments:
        org -- 
        hook_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/hooks/{hook_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return OrgHook(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/hooks/{hook_id}/config
    #
    def OrgsGetWebhookConfigForOrg(self, org:str, hook_id:int):
        """Returns the webhook configuration for an organization. To get more information about the webhook, including the `active` state and `events`, use "[Get an organization webhook ](/rest/reference/orgs#get-an-organization-webhook)."

Access tokens must have the `admin:org_hook` scope, and GitHub Apps must have the `organization_hooks:read` permission.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#get-a-webhook-configuration-for-an-organization
        /orgs/{org}/hooks/{hook_id}/config
        
        arguments:
        org -- 
        hook_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/hooks/{hook_id}/config", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return WebhookConfiguration(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}
    #
    def OrgsGetWebhookDelivery(self, org:str, hook_id:int, delivery_id:int):
        """Returns a delivery for a webhook configured in an organization.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#get-a-webhook-delivery-for-an-organization-webhook
        /orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}
        
        arguments:
        org -- 
        hook_id -- 
        delivery_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}", 
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
    # get /organizations
    #
    def OrgsList(self, since:int=None, per_page=30):
        """Lists all organizations, in the order that they were created on GitHub Enterprise Server.

**Note:** Pagination is powered exclusively by the `since` parameter. Use the [Link header](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#link-header) to get the URL for the next page of organizations.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#list-organizations
        /organizations
        
        arguments:
        since -- An organization ID. Only return organizations with an ID greater than this ID.
        per_page -- Results per page (max 100)
        
        """
        
        data = {}
        if since is not None:
            data['since'] = since
        if per_page is not None:
            data['per_page'] = per_page
        
        
        r = self._session.get(f"{self._url}/organizations", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and OrganizationSimple(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/installations
    #
    def OrgsListAppInstallations(self, org:str,per_page=30, page=1):
        """Lists all GitHub Apps in an organization. The installation count includes all GitHub Apps installed on repositories in the organization. You must be an organization owner with `admin:read` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#list-app-installations-for-an-organization
        /orgs/{org}/installations
        
        arguments:
        org -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/installations", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return OrgsListAppInstallationsSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /user/orgs
    #
    def OrgsListForAuthenticatedUser(self, per_page=30, page=1):
        """List organizations for the authenticated user.

**OAuth scope requirements**

This only lists organizations that your authorization allows you to operate on in some way (e.g., you can list teams with `read:org` scope, you can publicize your organization membership with `user` scope, etc.). Therefore, this API requires at least `user` or `read:org` scope. OAuth requests with insufficient scope receive a `403 Forbidden` response.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#list-organizations-for-the-authenticated-user
        /user/orgs
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/user/orgs", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and OrganizationSimple(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /users/{username}/orgs
    #
    def OrgsListForUser(self, username:str,per_page=30, page=1):
        """List [public organization memberships](https://help.github.com/articles/publicizing-or-concealing-organization-membership) for the specified user.

This method only lists _public_ memberships, regardless of authentication. If you need to fetch all of the organization memberships (public and private) for the authenticated user, use the [List organizations for the authenticated user](https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#list-organizations-for-the-authenticated-user) API instead.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#list-organizations-for-a-user
        /users/{username}/orgs
        
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
        
        
        r = self._session.get(f"{self._url}/users/{username}/orgs", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and OrganizationSimple(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/members
    #
    def OrgsListMembers(self, org:str,filter='all', role='all', per_page=30, page=1):
        """List all users who are members of an organization. If the authenticated user is also a member of this organization then both concealed and public members will be returned.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#list-organization-members
        /orgs/{org}/members
        
        arguments:
        org -- 
        filter -- Filter members returned in the list. Can be one of:  
\* `2fa_disabled` - Members without [two-factor authentication](https://github.com/blog/1614-two-factor-authentication) enabled. Available for organization owners.  
\* `all` - All members the authenticated user can see.
        role -- Filter members returned by their role. Can be one of:  
\* `all` - All members of the organization, regardless of role.  
\* `admin` - Organization owners.  
\* `member` - Non-owner organization members.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if filter is not None:
            data['filter'] = filter
        if role is not None:
            data['role'] = role
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/members", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and SimpleUser(**entry) for entry in r.json() ]
            
        if r.status_code == 302:
            return HttpResponse(r)
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /user/memberships/orgs
    #
    def OrgsListMembershipsForAuthenticatedUser(self, state=None, per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#list-organization-memberships-for-the-authenticated-user
        /user/memberships/orgs
        
        arguments:
        state -- Indicates the state of the memberships to return. Can be either `active` or `pending`. If not specified, the API returns both active and pending memberships.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if state is not None:
            data['state'] = state
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/user/memberships/orgs", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and OrgMembership(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/outside_collaborators
    #
    def OrgsListOutsideCollaborators(self, org:str,filter='all', per_page=30, page=1):
        """List all users who are outside collaborators of an organization.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#list-outside-collaborators-for-an-organization
        /orgs/{org}/outside_collaborators
        
        arguments:
        org -- 
        filter -- Filter members returned in the list. Can be one of:  
\* `2fa_disabled` - Members without [two-factor authentication](https://github.com/blog/1614-two-factor-authentication) enabled. Available for organization owners.  
\* `all` - All members the authenticated user can see.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if filter is not None:
            data['filter'] = filter
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/outside_collaborators", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and SimpleUser(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/public_members
    #
    def OrgsListPublicMembers(self, org:str,per_page=30, page=1):
        """Members of an organization can choose to have their membership publicized or not.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#list-public-organization-members
        /orgs/{org}/public_members
        
        arguments:
        org -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/public_members", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and SimpleUser(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/hooks/{hook_id}/deliveries
    #
    def OrgsListWebhookDeliveries(self, org:str, hook_id:int,per_page=30, cursor:str=None):
        """Returns a list of webhook deliveries for a webhook configured in an organization.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#list-deliveries-for-an-organization-webhook
        /orgs/{org}/hooks/{hook_id}/deliveries
        
        arguments:
        org -- 
        hook_id -- 
        per_page -- Results per page (max 100)
        cursor -- Used for pagination: the starting delivery from which the page of deliveries is fetched. Refer to the `link` header for the next and previous page cursors.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if cursor is not None:
            data['cursor'] = cursor
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/hooks/{hook_id}/deliveries", 
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
    # get /orgs/{org}/hooks
    #
    def OrgsListWebhooks(self, org:str,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#list-organization-webhooks
        /orgs/{org}/hooks
        
        arguments:
        org -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/hooks", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and OrgHook(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # post /orgs/{org}/hooks/{hook_id}/pings
    #
    def OrgsPingWebhook(self, org:str, hook_id:int):
        """This will trigger a [ping event](https://docs.github.com/enterprise-server@3.3/webhooks/#ping-event) to be sent to the hook.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#ping-an-organization-webhook
        /orgs/{org}/hooks/{hook_id}/pings
        
        arguments:
        org -- 
        hook_id -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/orgs/{org}/hooks/{hook_id}/pings", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}/attempts
    #
    def OrgsRedeliverWebhookDelivery(self, org:str, hook_id:int, delivery_id:int):
        """Redeliver a delivery for a webhook configured in an organization.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#redeliver-a-delivery-for-an-organization-webhook
        /orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}/attempts
        
        arguments:
        org -- 
        hook_id -- 
        delivery_id -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}/attempts", 
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
    # delete /orgs/{org}/members/{username}
    #
    def OrgsRemoveMember(self, org:str, username:str):
        """Removing a user from this list will remove them from all teams and they will no longer have any access to the organization's repositories.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#remove-an-organization-member
        /orgs/{org}/members/{username}
        
        arguments:
        org -- 
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/members/{username}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/memberships/{username}
    #
    def OrgsRemoveMembershipForUser(self, org:str, username:str):
        """In order to remove a user's membership with an organization, the authenticated user must be an organization owner.

If the specified user is an active member of the organization, this will remove them from the organization. If the specified user has been invited to the organization, this will cancel their invitation. The specified user will receive an email notification in both cases.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#remove-organization-membership-for-a-user
        /orgs/{org}/memberships/{username}
        
        arguments:
        org -- 
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/memberships/{username}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/outside_collaborators/{username}
    #
    def OrgsRemoveOutsideCollaborator(self, org:str, username:str):
        """Removing a user from this list will remove them from all the organization's repositories.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#remove-outside-collaborator-from-an-organization
        /orgs/{org}/outside_collaborators/{username}
        
        arguments:
        org -- 
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/outside_collaborators/{username}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 422:
            return OrgsRemoveOutsideCollaborator422(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/public_members/{username}
    #
    def OrgsRemovePublicMembershipForAuthenticatedUser(self, org:str, username:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#remove-public-organization-membership-for-the-authenticated-user
        /orgs/{org}/public_members/{username}
        
        arguments:
        org -- 
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/public_members/{username}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # put /orgs/{org}/memberships/{username}
    #
    def OrgsSetMembershipForUser(self, org:str, username:str,role:str='member'):
        """Only authenticated organization owners can add a member to the organization or update the member's role.

*   If the authenticated user is _adding_ a member to the organization, the invited user will receive an email inviting them to the organization. The user's [membership status](https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#get-organization-membership-for-a-user) will be `pending` until they accept the invitation.
    
*   Authenticated users can _update_ a user's membership by passing the `role` parameter. If the authenticated user changes a member's role to `admin`, the affected user will receive an email notifying them that they've been made an organization owner. If the authenticated user changes an owner's role to `member`, no email will be sent.

**Rate limits**

To prevent abuse, the authenticated user is limited to 50 organization invitations per 24 hour period. If the organization is more than one month old or on a paid plan, the limit is 500 invitations per 24 hour period.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#set-organization-membership-for-a-user
        /orgs/{org}/memberships/{username}
        
        arguments:
        org -- 
        username -- 
        role -- The role to give the user in the organization. Can be one of:  
\* `admin` - The user will become an owner of the organization.  
\* `member` - The user will become a non-owner member of the organization.
        

        """
    
        data = {
        'role': role,
        
        }
        

        
        r = self._session.put(f"{self._url}/orgs/{org}/memberships/{username}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return OrgMembership(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /orgs/{org}/public_members/{username}
    #
    def OrgsSetPublicMembershipForAuthenticatedUser(self, org:str, username:str):
        """The user can publicize their own membership. (A user cannot publicize the membership for another user.)

Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#http-verbs)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#set-public-organization-membership-for-the-authenticated-user
        /orgs/{org}/public_members/{username}
        
        arguments:
        org -- 
        username -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.put(f"{self._url}/orgs/{org}/public_members/{username}", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /orgs/{org}
    #
    def OrgsUpdate(self, org:str,billing_email:str=None, company:str=None, email:str=None, twitter_username:str=None, location:str=None, name:str=None, description:str=None, has_organization_projects:bool=None, has_repository_projects:bool=None, default_repository_permission:str='read', members_can_create_repositories:bool=True, members_can_create_internal_repositories:bool=None, members_can_create_private_repositories:bool=None, members_can_create_public_repositories:bool=None, members_allowed_repository_creation_type:str=None, members_can_create_pages:bool=True, members_can_fork_private_repositories:bool=False, blog:str=None):
        """**Parameter Deprecation Notice:** GitHub Enterprise Server will replace and discontinue `members_allowed_repository_creation_type` in favor of more granular permissions. The new input parameters are `members_can_create_public_repositories`, `members_can_create_private_repositories` for all organizations and `members_can_create_internal_repositories` for organizations associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+. For more information, see the [blog post](https://developer.github.com/changes/2019-12-03-internal-visibility-changes).

Enables an authenticated organization owner with the `admin:org` scope to update the organization's profile and member privileges.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs/#update-an-organization
        /orgs/{org}
        
        arguments:
        org -- 
        billing_email -- Billing email address. This address is not publicized.
        company -- The company name.
        email -- The publicly visible email address.
        twitter_username -- The Twitter username of the company.
        location -- The location.
        name -- The shorthand name of the company.
        description -- The description of the company.
        has_organization_projects -- Toggles whether an organization can use organization projects.
        has_repository_projects -- Toggles whether repositories that belong to the organization can use repository projects.
        default_repository_permission -- Default permission level members have for organization repositories:  
\* `read` - can pull, but not push to or administer this repository.  
\* `write` - can pull and push, but not administer this repository.  
\* `admin` - can pull, push, and administer this repository.  
\* `none` - no permissions granted by default.
        members_can_create_repositories -- Toggles the ability of non-admin organization members to create repositories. Can be one of:  
\* `true` - all organization members can create repositories.  
\* `false` - only organization owners can create repositories.  
Default: `true`  
**Note:** A parameter can override this parameter. See `members_allowed_repository_creation_type` in this table for details. **Note:** A parameter can override this parameter. See `members_allowed_repository_creation_type` in this table for details.
        members_can_create_internal_repositories -- Toggles whether organization members can create internal repositories, which are visible to all enterprise members. You can only allow members to create internal repositories if your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+. Can be one of:  
\* `true` - all organization members can create internal repositories.  
\* `false` - only organization owners can create internal repositories.  
Default: `true`. For more information, see "[Restricting repository creation in your organization](https://help.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)" in the GitHub Help documentation.
        members_can_create_private_repositories -- Toggles whether organization members can create private repositories, which are visible to organization members with permission. Can be one of:  
\* `true` - all organization members can create private repositories.  
\* `false` - only organization owners can create private repositories.  
Default: `true`. For more information, see "[Restricting repository creation in your organization](https://help.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)" in the GitHub Help documentation.
        members_can_create_public_repositories -- Toggles whether organization members can create public repositories, which are visible to anyone. Can be one of:  
\* `true` - all organization members can create public repositories.  
\* `false` - only organization owners can create public repositories.  
Default: `true`. For more information, see "[Restricting repository creation in your organization](https://help.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)" in the GitHub Help documentation.
        members_allowed_repository_creation_type -- Specifies which types of repositories non-admin organization members can create. Can be one of:  
\* `all` - all organization members can create public and private repositories.  
\* `private` - members can create private repositories. This option is only available to repositories that are part of an organization on GitHub Enterprise Cloud.  
\* `none` - only admin members can create repositories.  
**Note:** This parameter is deprecated and will be removed in the future. Its return value ignores internal repositories. Using this parameter overrides values set in `members_can_create_repositories`. See the parameter deprecation notice in the operation description for details.
        members_can_create_pages -- Toggles whether organization members can create GitHub Pages sites. Can be one of:  
\* `true` - all organization members can create GitHub Pages sites.  
\* `false` - no organization members can create GitHub Pages sites. Existing published sites will not be impacted.
        members_can_fork_private_repositories -- Toggles whether organization members can fork private organization repositories. Can be one of:  
\* `true` - all organization members can fork private repositories within the organization.  
\* `false` - no organization members can fork private repositories within the organization.
        blog -- 
        

        """
    
        data = {
        'billing_email': billing_email,
        'company': company,
        'email': email,
        'twitter_username': twitter_username,
        'location': location,
        'name': name,
        'description': description,
        'has_organization_projects': has_organization_projects,
        'has_repository_projects': has_repository_projects,
        'default_repository_permission': default_repository_permission,
        'members_can_create_repositories': members_can_create_repositories,
        'members_can_create_internal_repositories': members_can_create_internal_repositories,
        'members_can_create_private_repositories': members_can_create_private_repositories,
        'members_can_create_public_repositories': members_can_create_public_repositories,
        'members_allowed_repository_creation_type': members_allowed_repository_creation_type,
        'members_can_create_pages': members_can_create_pages,
        'members_can_fork_private_repositories': members_can_fork_private_repositories,
        'blog': blog,
        
        }
        

        
        r = self._session.patch(f"{self._url}/orgs/{org}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return OrganizationFull(**r.json())
            
        if r.status_code == 422:
            return r.json()
            
        if r.status_code == 409:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /user/memberships/orgs/{org}
    #
    def OrgsUpdateMembershipForAuthenticatedUser(self, org:str,state:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#update-an-organization-membership-for-the-authenticated-user
        /user/memberships/orgs/{org}
        
        arguments:
        org -- 
        state -- The state that the membership should be in. Only `"active"` will be accepted.
        

        """
    
        data = {
        'state': state,
        
        }
        

        
        r = self._session.patch(f"{self._url}/user/memberships/orgs/{org}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return OrgMembership(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /orgs/{org}/hooks/{hook_id}
    #
    def OrgsUpdateWebhook(self, org:str, hook_id:int,config:dict=None, events:list=['push'], active:bool=True, name:str=None):
        """Updates a webhook configured in an organization. When you update a webhook, the `secret` will be overwritten. If you previously had a `secret` set, you must provide the same `secret` or set a new `secret` or the secret will be removed. If you are only updating individual webhook `config` properties, use "[Update a webhook configuration for an organization](/rest/reference/orgs#update-a-webhook-configuration-for-an-organization)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#update-an-organization-webhook
        /orgs/{org}/hooks/{hook_id}
        
        arguments:
        org -- 
        hook_id -- 
        config -- Key/value pairs to provide settings for this webhook. [These are defined below](https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#update-hook-config-params).
        events -- Determines what [events](https://docs.github.com/enterprise-server@3.3/webhooks/event-payloads) the hook is triggered for.
        active -- Determines if notifications are sent when the webhook is triggered. Set to `true` to send notifications.
        name -- 
        

        """
    
        data = {
        'config': config,
        'events': events,
        'active': active,
        'name': name,
        
        }
        

        
        r = self._session.patch(f"{self._url}/orgs/{org}/hooks/{hook_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return OrgHook(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /orgs/{org}/hooks/{hook_id}/config
    #
    def OrgsUpdateWebhookConfigForOrg(self, org:str, hook_id:int,url:str=None, content_type:str=None, secret:str=None, insecure_ssl=None):
        """Updates the webhook configuration for an organization. To update more information about the webhook, including the `active` state and `events`, use "[Update an organization webhook ](/rest/reference/orgs#update-an-organization-webhook)."

Access tokens must have the `admin:org_hook` scope, and GitHub Apps must have the `organization_hooks:write` permission.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#update-a-webhook-configuration-for-an-organization
        /orgs/{org}/hooks/{hook_id}/config
        
        arguments:
        org -- 
        hook_id -- 
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
        

        
        r = self._session.patch(f"{self._url}/orgs/{org}/hooks/{hook_id}/config", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return WebhookConfiguration(**r.json())
            

        return UnexpectedResult(r)
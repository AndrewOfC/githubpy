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

class EnterpriseAdmin(object):


    #
    # post /setup/api/settings/authorized-keys
    #
    def EnterpriseAdminAddAuthorizedSshKey(self, authorized_key:str):
        """**Note:** The request body for this operation must be submitted as `application/x-www-form-urlencoded` data. You can submit a parameter value as a string, or you can use a tool such as `curl` to submit a parameter value as the contents of a text file. For more information, see the [`curl` documentation](https://curl.se/docs/manpage.html#--data-urlencode).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#add-an-authorized-ssh-key
        /setup/api/settings/authorized-keys
        
        arguments:
        authorized_key -- The public SSH key.
        

        """
    
        data = {
        'authorized_key': authorized_key,
        
        }
        

        
        r = self._session.post(f"{self._url}/setup/api/settings/authorized-keys", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/x-www-form-urlencoded'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            json = r.json()
            return json and [ entry and SshKey(**SshKey.patchEntry(entry)) for entry in json ]
            

        return UnexpectedResult(r)
    #
    # put /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations/{org_id}
    #
    def EnterpriseAdminAddOrgAccessToSelfHostedRunnerGroupInEnterprise(self, enterprise:str, runner_group_id:int, org_id:int):
        """Adds an organization to the list of selected organizations that can access a self-hosted runner group. The runner group must have `visibility` set to `selected`. For more information, see "[Create a self-hosted runner group for an enterprise](#create-a-self-hosted-runner-group-for-an-enterprise)."

You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#add-organization-access-to-a-self-hosted-runner-group-in-an-enterprise
        /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations/{org_id}
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        runner_group_id -- Unique identifier of the self-hosted runner group.
        org_id -- Unique identifier of an organization.
        

        """
    
        data = {
        
        }
        

        
        r = self._session.put(f"{self._url}/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations/{org_id}", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners/{runner_id}
    #
    def EnterpriseAdminAddSelfHostedRunnerToGroupForEnterprise(self, enterprise:str, runner_group_id:int, runner_id:int):
        """Adds a self-hosted runner to a runner group configured in an enterprise.

You must authenticate using an access token with the `manage_runners:enterprise`
scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#add-a-self-hosted-runner-to-a-group-for-an-enterprise
        /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners/{runner_id}
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        runner_group_id -- Unique identifier of the self-hosted runner group.
        runner_id -- Unique identifier of the self-hosted runner.
        

        """
    
        data = {
        
        }
        

        
        r = self._session.put(f"{self._url}/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners/{runner_id}", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # post /setup/api/start
    #
    def EnterpriseAdminCreateEnterpriseServerLicense(self, license:str, password:str=None, settings:str=None):
        """When you boot a GitHub instance for the first time, you can use the following endpoint to upload a license.

Note that you need to `POST` to [`/setup/api/configure`](https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#start-a-configuration-process) to start the actual configuration process.

When using this endpoint, your GitHub instance must have a password set. This can be accomplished two ways:

1.  If you're working directly with the API before accessing the web interface, you must pass in the password parameter to set your password.
2.  If you set up your instance via the web interface before accessing the API, your calls to this endpoint do not need the password parameter.

**Note:** The request body for this operation must be submitted as `application/x-www-form-urlencoded` data. You can submit a parameter value as a string, or you can use a tool such as `curl` to submit a parameter value as the contents of a text file. For more information, see the [`curl` documentation](https://curl.se/docs/manpage.html#--data-urlencode).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#create-a-github-enterprise-server-license
        /setup/api/start
        
        arguments:
        license -- The content of your _.ghl_ license file.
        password -- You **must** provide a password _only if_ you are uploading your license for the first time. If you previously set a password through the web interface, you don't need this parameter.
        settings -- An optional JSON string containing the installation settings. For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-settings).
        

        """
    
        data = {
        'license': license,
        'password': password,
        'settings': settings,
        
        }
        

        
        r = self._session.post(f"{self._url}/setup/api/start", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/x-www-form-urlencoded'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 202:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # post /admin/hooks
    #
    def EnterpriseAdminCreateGlobalWebhook(self, config:dict, name:str, events:list=[], active:bool=True):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#create-a-global-webhook
        /admin/hooks
        
        arguments:
        config -- Key/value pairs to provide settings for this webhook.
        name -- Must be passed as "web".
        events -- The [events](https://docs.github.com/enterprise-server@3.3/webhooks/event-payloads) that trigger this webhook. A global webhook can be triggered by `user` and `organization` events. Default: `user` and `organization`.
        active -- Determines if notifications are sent when the webhook is triggered. Set to `true` to send notifications.
        

        """
    
        data = {
        'config': config,
        'name': name,
        'events': events,
        'active': active,
        
        }
        

        
        r = self._session.post(f"{self._url}/admin/hooks", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return GlobalHook(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /admin/users/{username}/authorizations
    #
    def EnterpriseAdminCreateImpersonationOAuthToken(self, username:str,scopes:list=[]):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#create-an-impersonation-oauth-token
        /admin/users/{username}/authorizations
        
        arguments:
        username -- 
        scopes -- A list of [scopes](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        

        """
    
        data = {
        'scopes': scopes,
        
        }
        

        
        r = self._session.post(f"{self._url}/admin/users/{username}/authorizations", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Authorization(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /admin/organizations
    #
    def EnterpriseAdminCreateOrg(self, admin:str, login:str, profile_name:str=None):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#create-an-organization
        /admin/organizations
        
        arguments:
        admin -- The login of the user who will manage this organization.
        login -- The organization's username.
        profile_name -- The organization's display name.
        

        """
    
        data = {
        'admin': admin,
        'login': login,
        'profile_name': profile_name,
        
        }
        

        
        r = self._session.post(f"{self._url}/admin/organizations", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return OrganizationSimple(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /admin/pre-receive-environments
    #
    def EnterpriseAdminCreatePreReceiveEnvironment(self, image_url:str, name:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#create-a-pre-receive-environment
        /admin/pre-receive-environments
        
        arguments:
        image_url -- URL from which to download a tarball of this environment.
        name -- The new pre-receive environment's name.
        

        """
    
        data = {
        'image_url': image_url,
        'name': name,
        
        }
        

        
        r = self._session.post(f"{self._url}/admin/pre-receive-environments", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return PreReceiveEnvironment(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /admin/pre-receive-hooks
    #
    def EnterpriseAdminCreatePreReceiveHook(self, environment:dict, script_repository:dict, script:str, name:str, enforcement:str=None, allow_downstream_configuration:bool=None):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#create-a-pre-receive-hook
        /admin/pre-receive-hooks
        
        arguments:
        environment -- The pre-receive environment where the script is executed.
        script_repository -- The GitHub repository where the script is kept.
        script -- The script that the hook runs.
        name -- The name of the hook.
        enforcement -- The state of enforcement for this hook. default: `disabled`
        allow_downstream_configuration -- Whether enforcement can be overridden at the org or repo level. default: `false`
        

        """
    
        data = {
        'environment': environment,
        'script_repository': script_repository,
        'script': script,
        'name': name,
        'enforcement': enforcement,
        'allow_downstream_configuration': allow_downstream_configuration,
        
        }
        

        
        r = self._session.post(f"{self._url}/admin/pre-receive-hooks", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return PreReceiveHook(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /enterprises/{enterprise}/actions/runners/registration-token
    #
    def EnterpriseAdminCreateRegistrationTokenForEnterprise(self, enterprise:str):
        """Returns a token that you can pass to the `config` script. The token expires after one hour.

You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.

#### Example using registration token

Configure your self-hosted runner, replacing `TOKEN` with the registration token provided by this endpoint.

```
./config.sh --url https://github.com/enterprises/octo-enterprise --token TOKEN
```
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#create-a-registration-token-for-an-enterprise
        /enterprises/{enterprise}/actions/runners/registration-token
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/enterprises/{enterprise}/actions/runners/registration-token", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return AuthenticationToken(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /enterprises/{enterprise}/actions/runners/remove-token
    #
    def EnterpriseAdminCreateRemoveTokenForEnterprise(self, enterprise:str):
        """Returns a token that you can pass to the `config` script to remove a self-hosted runner from an enterprise. The token expires after one hour.

You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.

#### Example using remove token

To remove your self-hosted runner from an enterprise, replace `TOKEN` with the remove token provided by this
endpoint.

```
./config.sh remove --token TOKEN
```
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#create-a-remove-token-for-an-enterprise
        /enterprises/{enterprise}/actions/runners/remove-token
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/enterprises/{enterprise}/actions/runners/remove-token", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return AuthenticationToken(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /enterprises/{enterprise}/actions/runner-groups
    #
    def EnterpriseAdminCreateSelfHostedRunnerGroupForEnterprise(self, enterprise:str,name:str, visibility:str=None, selected_organization_ids:list=[], runners:list=[], allows_public_repositories:bool=False):
        """Creates a new self-hosted runner group for an enterprise.

You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#create-self-hosted-runner-group-for-an-enterprise
        /enterprises/{enterprise}/actions/runner-groups
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        name -- Name of the runner group.
        visibility -- Visibility of a runner group. You can select all organizations or select individual organization. Can be one of: `all` or `selected`
        selected_organization_ids -- List of organization IDs that can access the runner group.
        runners -- List of runner IDs to add to the runner group.
        allows_public_repositories -- Whether the runner group can be used by `public` repositories.
        

        """
    
        data = {
        'name': name,
        'visibility': visibility,
        'selected_organization_ids': selected_organization_ids,
        'runners': runners,
        'allows_public_repositories': allows_public_repositories,
        
        }
        

        
        r = self._session.post(f"{self._url}/enterprises/{enterprise}/actions/runner-groups", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return RunnerGroupsEnterprise(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /admin/users
    #
    def EnterpriseAdminCreateUser(self, login:str, email:str=None):
        """If an external authentication mechanism is used, the login name should match the login name in the external system. If you are using LDAP authentication, you should also [update the LDAP mapping](https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#update-ldap-mapping-for-a-user) for the user.

The login name will be normalized to only contain alphanumeric characters or single hyphens. For example, if you send `"octo_cat"` as the login, a user named `"octo-cat"` will be created.

If the login name or email address is already associated with an account, the server will return a `422` response.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#create-a-user
        /admin/users
        
        arguments:
        login -- The user's username.
        email -- **Required for built-in authentication.** The user's email address. This parameter can be omitted when using CAS, LDAP, or SAML. For details on built-in and centrally-managed authentication, see the the [GitHub authentication guide](https://help.github.com/enterprise/2.18/admin/guides/user-management/authenticating-users-for-your-github-enterprise-server-instance/).
        

        """
    
        data = {
        'login': login,
        'email': email,
        
        }
        

        
        r = self._session.post(f"{self._url}/admin/users", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return SimpleUser(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /admin/hooks/{hook_id}
    #
    def EnterpriseAdminDeleteGlobalWebhook(self, hook_id:int,accept='application/vnd.github.superpro-preview+json'):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#delete-a-global-webhook
        /admin/hooks/{hook_id}
        
        arguments:
        hook_id -- 
        accept -- This API is under preview and subject to change.
        
        """
        
        data = {}
        if accept is not None:
            data['accept'] = accept
        
        
        r = self._session.delete(f"{self._url}/admin/hooks/{hook_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /admin/users/{username}/authorizations
    #
    def EnterpriseAdminDeleteImpersonationOAuthToken(self, username:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#delete-an-impersonation-oauth-token
        /admin/users/{username}/authorizations
        
        arguments:
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/admin/users/{username}/authorizations", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /admin/tokens/{token_id}
    #
    def EnterpriseAdminDeletePersonalAccessToken(self, token_id:int):
        """Deletes a personal access token. Returns a `403 - Forbidden` status when a personal access token is in use. For example, if you access this endpoint with the same personal access token that you are trying to delete, you will receive this error.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#delete-a-personal-access-token
        /admin/tokens/{token_id}
        
        arguments:
        token_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/admin/tokens/{token_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /admin/pre-receive-environments/{pre_receive_environment_id}
    #
    def EnterpriseAdminDeletePreReceiveEnvironment(self, pre_receive_environment_id:int):
        """If you attempt to delete an environment that cannot be deleted, you will receive a `422 Unprocessable Entity` response.

The possible error messages are:

*   _Cannot modify or delete the default environment_
*   _Cannot delete environment that has hooks_
*   _Cannot delete environment when download is in progress_
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#delete-a-pre-receive-environment
        /admin/pre-receive-environments/{pre_receive_environment_id}
        
        arguments:
        pre_receive_environment_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/admin/pre-receive-environments/{pre_receive_environment_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 422:
            return EnterpriseAdminDeletePreReceiveEnvironment422(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /admin/pre-receive-hooks/{pre_receive_hook_id}
    #
    def EnterpriseAdminDeletePreReceiveHook(self, pre_receive_hook_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#delete-a-pre-receive-hook
        /admin/pre-receive-hooks/{pre_receive_hook_id}
        
        arguments:
        pre_receive_hook_id -- pre_receive_hook_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/admin/pre-receive-hooks/{pre_receive_hook_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /admin/keys/{key_ids}
    #
    def EnterpriseAdminDeletePublicKey(self, key_ids:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#delete-a-public-key
        /admin/keys/{key_ids}
        
        arguments:
        key_ids -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/admin/keys/{key_ids}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /enterprises/{enterprise}/actions/runners/{runner_id}
    #
    def EnterpriseAdminDeleteSelfHostedRunnerFromEnterprise(self, enterprise:str, runner_id:int):
        """Forces the removal of a self-hosted runner from an enterprise. You can use this endpoint to completely remove the runner when the machine you were using no longer exists.

You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#delete-self-hosted-runner-from-an-enterprise
        /enterprises/{enterprise}/actions/runners/{runner_id}
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        runner_id -- Unique identifier of the self-hosted runner.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/enterprises/{enterprise}/actions/runners/{runner_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}
    #
    def EnterpriseAdminDeleteSelfHostedRunnerGroupFromEnterprise(self, enterprise:str, runner_group_id:int):
        """Deletes a self-hosted runner group for an enterprise.

You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#delete-a-self-hosted-runner-group-from-an-enterprise
        /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        runner_group_id -- Unique identifier of the self-hosted runner group.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /admin/users/{username}
    #
    def EnterpriseAdminDeleteUser(self, username:str):
        """Deleting a user will delete all their repositories, gists, applications, and personal settings. [Suspending a user](https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#suspend-a-user) is often a better option.

You can delete any user account except your own.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#delete-a-user
        /admin/users/{username}
        
        arguments:
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/admin/users/{username}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /users/{username}/site_admin
    #
    def EnterpriseAdminDemoteSiteAdministrator(self, username:str):
        """You can demote any user account except your own.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#demote-a-site-administrator
        /users/{username}/site_admin
        
        arguments:
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/users/{username}/site_admin", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /enterprises/{enterprise}/actions/permissions/organizations/{org_id}
    #
    def EnterpriseAdminDisableSelectedOrganizationGithubActionsEnterprise(self, enterprise:str, org_id:int):
        """Removes an organization from the list of selected organizations that are enabled for GitHub Actions in an enterprise. To use this endpoint, the enterprise permission policy for `enabled_organizations` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise)."

You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#disable-a-selected-organization-for-github-actions-in-an-enterprise
        /enterprises/{enterprise}/actions/permissions/organizations/{org_id}
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        org_id -- Unique identifier of an organization.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/enterprises/{enterprise}/actions/permissions/organizations/{org_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # post /setup/api/maintenance
    #
    def EnterpriseAdminEnableOrDisableMaintenanceMode(self, maintenance:str):
        """**Note:** The request body for this operation must be submitted as `application/x-www-form-urlencoded` data. You can submit a parameter value as a string, or you can use a tool such as `curl` to submit a parameter value as the contents of a text file. For more information, see the [`curl` documentation](https://curl.se/docs/manpage.html#--data-urlencode).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#enable-or-disable-maintenance-mode
        /setup/api/maintenance
        
        arguments:
        maintenance -- A JSON string with the attributes `enabled` and `when`.

The possible values for `enabled` are `true` and `false`. When it's `false`, the attribute `when` is ignored and the maintenance mode is turned off. `when` defines the time period when the maintenance was enabled.

The possible values for `when` are `now` or any date parseable by [mojombo/chronic](https://github.com/mojombo/chronic).
        

        """
    
        data = {
        'maintenance': maintenance,
        
        }
        

        
        r = self._session.post(f"{self._url}/setup/api/maintenance", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/x-www-form-urlencoded'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return MaintenanceStatus(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /enterprises/{enterprise}/actions/permissions/organizations/{org_id}
    #
    def EnterpriseAdminEnableSelectedOrganizationGithubActionsEnterprise(self, enterprise:str, org_id:int):
        """Adds an organization to the list of selected organizations that are enabled for GitHub Actions in an enterprise. To use this endpoint, the enterprise permission policy for `enabled_organizations` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise)."

You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#enable-a-selected-organization-for-github-actions-in-an-enterprise
        /enterprises/{enterprise}/actions/permissions/organizations/{org_id}
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        org_id -- Unique identifier of an organization.
        

        """
    
        data = {
        
        }
        

        
        r = self._session.put(f"{self._url}/enterprises/{enterprise}/actions/permissions/organizations/{org_id}", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # get /setup/api/settings/authorized-keys
    #
    def EnterpriseAdminGetAllAuthorizedSshKeys(self, ):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-all-authorized-ssh-keys
        /setup/api/settings/authorized-keys
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/setup/api/settings/authorized-keys", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            json = r.json()
            return json and [ entry and SshKey(**SshKey.patchEntry(entry)) for entry in json ]
            
        
        return UnexpectedResult(r)
    #
    # get /enterprise/stats/all
    #
    def EnterpriseAdminGetAllStats(self, ):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-statistics
        /enterprise/stats/all
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/enterprise/stats/all", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return EnterpriseOverview(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /enterprises/{enterprise}/actions/permissions/selected-actions
    #
    def EnterpriseAdminGetAllowedActionsEnterprise(self, enterprise:str):
        """Gets the selected actions that are allowed in an enterprise. To use this endpoint, the enterprise permission policy for `allowed_actions` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise)."

You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-allowed-actions-for-an-enterprise
        /enterprises/{enterprise}/actions/permissions/selected-actions
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/enterprises/{enterprise}/actions/permissions/selected-actions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return SelectedActions(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /enterprise/announcement
    #
    def EnterpriseAdminGetAnnouncement(self, ):
        """Gets the current message and expiration date of the global announcement banner in your enterprise.
        /enterprise/announcement
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/enterprise/announcement", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return EnterpriseAnnouncement(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /enterprises/{enterprise}/audit-log
    #
    def EnterpriseAdminGetAuditLog(self, enterprise:str,phrase:str=None, after:str=None, before:str=None, direction='desc', page=1, per_page=30):
        """Gets the audit log for an enterprise. To use this endpoint, you must be an enterprise admin, and you must use an access token with the `admin:enterprise` scope.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-the-audit-log-for-an-enterprise
        /enterprises/{enterprise}/audit-log
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        phrase -- A search phrase. For more information, see [Searching the audit log](https://docs.github.com/enterprise-server@3.3/github/setting-up-and-managing-organizations-and-teams/reviewing-the-audit-log-for-your-organization#searching-the-audit-log).
        after -- A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for events after this cursor.
        before -- A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for events before this cursor.
        direction -- One of `asc` (ascending) or `desc` (descending).
        page -- Page number of the results to fetch.
        per_page -- Results per page (max 100)
        
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
        if page is not None:
            data['page'] = page
        if per_page is not None:
            data['per_page'] = per_page
        
        
        r = self._session.get(f"{self._url}/enterprises/{enterprise}/audit-log", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            json = r.json()
            return json and [ entry and AuditLogEvent(**AuditLogEvent.patchEntry(entry)) for entry in json ]
            
        
        return UnexpectedResult(r)
    #
    # get /enterprise/stats/comments
    #
    def EnterpriseAdminGetCommentStats(self, ):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-comment-statistics
        /enterprise/stats/comments
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/enterprise/stats/comments", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return EnterpriseCommentOverview(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /setup/api/configcheck
    #
    def EnterpriseAdminGetConfigurationStatus(self, ):
        """This endpoint allows you to check the status of the most recent configuration process:

Note that you may need to wait several seconds after you start a process before you can check its status.

The different statuses are:

| Status        | Description                       |
| ------------- | --------------------------------- |
| `PENDING`     | The job has not started yet       |
| `CONFIGURING` | The job is running                |
| `DONE`        | The job has finished correctly    |
| `FAILED`      | The job has finished unexpectedly |
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-the-configuration-status
        /setup/api/configcheck
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/setup/api/configcheck", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ConfigurationStatus(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /admin/pre-receive-environments/{pre_receive_environment_id}/downloads/latest
    #
    def EnterpriseAdminGetDownloadStatusForPreReceiveEnvironment(self, pre_receive_environment_id:int):
        """In addition to seeing the download status at the "[Get a pre-receive environment](#get-a-pre-receive-environment)" endpoint, there is also this separate endpoint for just the download status.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-the-download-status-for-a-pre-receive-environment
        /admin/pre-receive-environments/{pre_receive_environment_id}/downloads/latest
        
        arguments:
        pre_receive_environment_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/admin/pre-receive-environments/{pre_receive_environment_id}/downloads/latest", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return PreReceiveEnvironmentDownloadStatus(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /enterprise/stats/gists
    #
    def EnterpriseAdminGetGistStats(self, ):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-gist-statistics
        /enterprise/stats/gists
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/enterprise/stats/gists", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return EnterpriseGistOverview(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /enterprises/{enterprise}/actions/permissions
    #
    def EnterpriseAdminGetGithubActionsPermissionsEnterprise(self, enterprise:str):
        """Gets the GitHub Actions permissions policy for organizations and allowed actions in an enterprise.

You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-github-actions-permissions-for-an-enterprise
        /enterprises/{enterprise}/actions/permissions
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/enterprises/{enterprise}/actions/permissions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsEnterprisePermissions(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /admin/hooks/{hook_id}
    #
    def EnterpriseAdminGetGlobalWebhook(self, hook_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-a-global-webhook
        /admin/hooks/{hook_id}
        
        arguments:
        hook_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/admin/hooks/{hook_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return GlobalHook(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /enterprise/stats/hooks
    #
    def EnterpriseAdminGetHooksStats(self, ):
        """Get hooks statistics
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-hooks-statistics
        /enterprise/stats/hooks
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/enterprise/stats/hooks", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return EnterpriseHookOverview(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /enterprise/stats/issues
    #
    def EnterpriseAdminGetIssueStats(self, ):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-issues-statistics
        /enterprise/stats/issues
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/enterprise/stats/issues", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return EnterpriseIssueOverview(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /enterprise/settings/license
    #
    def EnterpriseAdminGetLicenseInformation(self, ):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-license-information
        /enterprise/settings/license
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/enterprise/settings/license", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return LicenseInfo(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /setup/api/maintenance
    #
    def EnterpriseAdminGetMaintenanceStatus(self, ):
        """Check your installation's maintenance status:
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-the-maintenance-status
        /setup/api/maintenance
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/setup/api/maintenance", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return MaintenanceStatus(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /enterprise/stats/milestones
    #
    def EnterpriseAdminGetMilestoneStats(self, ):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-milestone-statistics
        /enterprise/stats/milestones
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/enterprise/stats/milestones", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return EnterpriseMilestoneOverview(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /enterprise/stats/orgs
    #
    def EnterpriseAdminGetOrgStats(self, ):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-organization-statistics
        /enterprise/stats/orgs
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/enterprise/stats/orgs", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return EnterpriseOrganizationOverview(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /enterprise/stats/pages
    #
    def EnterpriseAdminGetPagesStats(self, ):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-pages-statistics
        /enterprise/stats/pages
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/enterprise/stats/pages", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return EnterprisePageOverview(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /admin/pre-receive-environments/{pre_receive_environment_id}
    #
    def EnterpriseAdminGetPreReceiveEnvironment(self, pre_receive_environment_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-a-pre-receive-environment
        /admin/pre-receive-environments/{pre_receive_environment_id}
        
        arguments:
        pre_receive_environment_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/admin/pre-receive-environments/{pre_receive_environment_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return PreReceiveEnvironment(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /admin/pre-receive-hooks/{pre_receive_hook_id}
    #
    def EnterpriseAdminGetPreReceiveHook(self, pre_receive_hook_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-a-pre-receive-hook
        /admin/pre-receive-hooks/{pre_receive_hook_id}
        
        arguments:
        pre_receive_hook_id -- pre_receive_hook_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/admin/pre-receive-hooks/{pre_receive_hook_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return PreReceiveHook(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}
    #
    def EnterpriseAdminGetPreReceiveHookForOrg(self, org:str, pre_receive_hook_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-a-pre-receive-hook-for-an-organization
        /orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}
        
        arguments:
        org -- 
        pre_receive_hook_id -- pre_receive_hook_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return OrgPreReceiveHook(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}
    #
    def EnterpriseAdminGetPreReceiveHookForRepo(self, owner:str, repo:str, pre_receive_hook_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-a-pre-receive-hook-for-a-repository
        /repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}
        
        arguments:
        owner -- 
        repo -- 
        pre_receive_hook_id -- pre_receive_hook_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return RepositoryPreReceiveHook(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /enterprise/stats/pulls
    #
    def EnterpriseAdminGetPullRequestStats(self, ):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-pull-requests-statistics
        /enterprise/stats/pulls
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/enterprise/stats/pulls", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return EnterprisePullRequestOverview(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /enterprise/stats/repos
    #
    def EnterpriseAdminGetRepoStats(self, ):
        """Get repository statistics
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-repository-statistics
        /enterprise/stats/repos
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/enterprise/stats/repos", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return EnterpriseRepositoryOverview(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /enterprises/{enterprise}/actions/runners/{runner_id}
    #
    def EnterpriseAdminGetSelfHostedRunnerForEnterprise(self, enterprise:str, runner_id:int):
        """Gets a specific self-hosted runner configured in an enterprise.

You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-a-self-hosted-runner-for-an-enterprise
        /enterprises/{enterprise}/actions/runners/{runner_id}
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        runner_id -- Unique identifier of the self-hosted runner.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/enterprises/{enterprise}/actions/runners/{runner_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return SelfHostedRunners(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}
    #
    def EnterpriseAdminGetSelfHostedRunnerGroupForEnterprise(self, enterprise:str, runner_group_id:int):
        """Gets a specific self-hosted runner group for an enterprise.

You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-a-self-hosted-runner-group-for-an-enterprise
        /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        runner_group_id -- Unique identifier of the self-hosted runner group.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return RunnerGroupsEnterprise(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /setup/api/settings
    #
    def EnterpriseAdminGetSettings(self, ):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-settings
        /setup/api/settings
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/setup/api/settings", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return EnterpriseSettings(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /enterprise/stats/users
    #
    def EnterpriseAdminGetUserStats(self, ):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-users-statistics
        /enterprise/stats/users
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/enterprise/stats/users", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return EnterpriseUserOverview(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /admin/hooks
    #
    def EnterpriseAdminListGlobalWebhooks(self, accept='application/vnd.github.superpro-preview+json', per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#list-global-webhooks
        /admin/hooks
        
        arguments:
        accept -- This API is under preview and subject to change.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if accept is not None:
            data['accept'] = accept
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/admin/hooks", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and GlobalHook(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations
    #
    def EnterpriseAdminListOrgAccessToSelfHostedRunnerGroupInEnterprise(self, enterprise:str, runner_group_id:int,per_page=30, page=1):
        """Lists the organizations with access to a self-hosted runner group.

You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#list-organization-access-to-a-self-hosted-runner-group-in-a-enterprise
        /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        runner_group_id -- Unique identifier of the self-hosted runner group.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return EnterpriseAdminListOrgAccessToSelfHostedRunnerGroupInEnterpriseSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /admin/tokens
    #
    def EnterpriseAdminListPersonalAccessTokens(self, per_page=30, page=1):
        """Lists personal access tokens for all users, including admin users.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#list-personal-access-tokens
        /admin/tokens
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/admin/tokens", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Authorization(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /admin/pre-receive-environments
    #
    def EnterpriseAdminListPreReceiveEnvironments(self, per_page=30, page=1, direction='desc', sort='created'):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#list-pre-receive-environments
        /admin/pre-receive-environments
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        direction -- One of `asc` (ascending) or `desc` (descending).
        sort -- 
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        if direction is not None:
            data['direction'] = direction
        if sort is not None:
            data['sort'] = sort
        
        
        r = self._session.get(f"{self._url}/admin/pre-receive-environments", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and PreReceiveEnvironment(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /admin/pre-receive-hooks
    #
    def EnterpriseAdminListPreReceiveHooks(self, per_page=30, page=1, direction='desc', sort='created'):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#list-pre-receive-hooks
        /admin/pre-receive-hooks
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        direction -- One of `asc` (ascending) or `desc` (descending).
        sort -- 
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        if direction is not None:
            data['direction'] = direction
        if sort is not None:
            data['sort'] = sort
        
        
        r = self._session.get(f"{self._url}/admin/pre-receive-hooks", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and PreReceiveHook(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/pre-receive-hooks
    #
    def EnterpriseAdminListPreReceiveHooksForOrg(self, org:str,per_page=30, page=1, direction='desc', sort='created'):
        """List all pre-receive hooks that are enabled or testing for this organization as well as any disabled hooks that can be configured at the organization level. Globally disabled pre-receive hooks that do not allow downstream configuration are not listed.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#list-pre-receive-hooks-for-an-organization
        /orgs/{org}/pre-receive-hooks
        
        arguments:
        org -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        direction -- One of `asc` (ascending) or `desc` (descending).
        sort -- 
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        if direction is not None:
            data['direction'] = direction
        if sort is not None:
            data['sort'] = sort
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/pre-receive-hooks", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and OrgPreReceiveHook(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/pre-receive-hooks
    #
    def EnterpriseAdminListPreReceiveHooksForRepo(self, owner:str, repo:str,per_page=30, page=1, direction='desc', sort='created'):
        """List all pre-receive hooks that are enabled or testing for this repository as well as any disabled hooks that are allowed to be enabled at the repository level. Pre-receive hooks that are disabled at a higher level and are not configurable will not be listed.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#list-pre-receive-hooks-for-a-repository
        /repos/{owner}/{repo}/pre-receive-hooks
        
        arguments:
        owner -- 
        repo -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        direction -- One of `asc` (ascending) or `desc` (descending).
        sort -- 
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        if direction is not None:
            data['direction'] = direction
        if sort is not None:
            data['sort'] = sort
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/pre-receive-hooks", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and RepositoryPreReceiveHook(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /admin/keys
    #
    def EnterpriseAdminListPublicKeys(self, per_page=30, page=1, direction='desc', sort='created', since:str=None):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#list-public-keys
        /admin/keys
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        direction -- One of `asc` (ascending) or `desc` (descending).
        sort -- 
        since -- Only show public keys accessed after the given time.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        if direction is not None:
            data['direction'] = direction
        if sort is not None:
            data['sort'] = sort
        if since is not None:
            data['since'] = since
        
        
        r = self._session.get(f"{self._url}/admin/keys", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and PublicKeyFull(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /enterprises/{enterprise}/actions/runners/downloads
    #
    def EnterpriseAdminListRunnerApplicationsForEnterprise(self, enterprise:str):
        """Lists binaries for the runner application that you can download and run.

You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#list-runner-applications-for-an-enterprise
        /enterprises/{enterprise}/actions/runners/downloads
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/enterprises/{enterprise}/actions/runners/downloads", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and RunnerApplication(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /enterprises/{enterprise}/actions/permissions/organizations
    #
    def EnterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise(self, enterprise:str,per_page=30, page=1):
        """Lists the organizations that are selected to have GitHub Actions enabled in an enterprise. To use this endpoint, the enterprise permission policy for `enabled_organizations` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise)."

You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#list-selected-organizations-enabled-for-github-actions-in-an-enterprise
        /enterprises/{enterprise}/actions/permissions/organizations
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/enterprises/{enterprise}/actions/permissions/organizations", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return EnterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterpriseSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /enterprises/{enterprise}/actions/runner-groups
    #
    def EnterpriseAdminListSelfHostedRunnerGroupsForEnterprise(self, enterprise:str,per_page=30, page=1):
        """Lists all self-hosted runner groups for an enterprise.

You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#list-self-hosted-runner-groups-for-an-enterprise
        /enterprises/{enterprise}/actions/runner-groups
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/enterprises/{enterprise}/actions/runner-groups", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return EnterpriseAdminListSelfHostedRunnerGroupsForEnterpriseSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /enterprises/{enterprise}/actions/runners
    #
    def EnterpriseAdminListSelfHostedRunnersForEnterprise(self, enterprise:str,per_page=30, page=1):
        """Lists all self-hosted runners configured for an enterprise.

You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#list-self-hosted-runners-for-an-enterprise
        /enterprises/{enterprise}/actions/runners
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/enterprises/{enterprise}/actions/runners", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return EnterpriseAdminListSelfHostedRunnersForEnterpriseSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners
    #
    def EnterpriseAdminListSelfHostedRunnersInGroupForEnterprise(self, enterprise:str, runner_group_id:int,per_page=30, page=1):
        """Lists the self-hosted runners that are in a specific enterprise group.

You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#list-self-hosted-runners-in-a-group-for-an-enterprise
        /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        runner_group_id -- Unique identifier of the self-hosted runner group.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return EnterpriseAdminListSelfHostedRunnersInGroupForEnterpriseSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # post /admin/hooks/{hook_id}/pings
    #
    def EnterpriseAdminPingGlobalWebhook(self, hook_id:int):
        """This will trigger a [ping event](https://docs.github.com/enterprise-server@3.3/webhooks/#ping-event) to be sent to the webhook.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#ping-a-global-webhook
        /admin/hooks/{hook_id}/pings
        
        arguments:
        hook_id -- 
        accept -- This API is under preview and subject to change.
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/admin/hooks/{hook_id}/pings", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /users/{username}/site_admin
    #
    def EnterpriseAdminPromoteUserToBeSiteAdministrator(self, username:str):
        """Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#http-verbs)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#promote-a-user-to-be-a-site-administrator
        /users/{username}/site_admin
        
        arguments:
        username -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.put(f"{self._url}/users/{username}/site_admin", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # delete /enterprise/announcement
    #
    def EnterpriseAdminRemoveAnnouncement(self, ):
        """Removes the global announcement banner in your enterprise.
        /enterprise/announcement
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/enterprise/announcement", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /setup/api/settings/authorized-keys
    #
    def EnterpriseAdminRemoveAuthorizedSshKey(self, ):
        """**Note:** The request body for this operation must be submitted as `application/x-www-form-urlencoded` data. You can submit a parameter value as a string, or you can use a tool such as `curl` to submit a parameter value as the contents of a text file. For more information, see the [`curl` documentation](https://curl.se/docs/manpage.html#--data-urlencode).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#remove-an-authorized-ssh-key
        /setup/api/settings/authorized-keys
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/setup/api/settings/authorized-keys", 
                           params=data,
                           **self._requests_kwargs({'Content-Type':  'application/x-www-form-urlencoded'}))
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            json = r.json()
            return json and [ entry and SshKey(**SshKey.patchEntry(entry)) for entry in json ]
            
        
        return UnexpectedResult(r)
    #
    # delete /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations/{org_id}
    #
    def EnterpriseAdminRemoveOrgAccessToSelfHostedRunnerGroupInEnterprise(self, enterprise:str, runner_group_id:int, org_id:int):
        """Removes an organization from the list of selected organizations that can access a self-hosted runner group. The runner group must have `visibility` set to `selected`. For more information, see "[Create a self-hosted runner group for an enterprise](#create-a-self-hosted-runner-group-for-an-enterprise)."

You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#remove-organization-access-to-a-self-hosted-runner-group-in-an-enterprise
        /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations/{org_id}
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        runner_group_id -- Unique identifier of the self-hosted runner group.
        org_id -- Unique identifier of an organization.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations/{org_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}
    #
    def EnterpriseAdminRemovePreReceiveHookEnforcementForOrg(self, org:str, pre_receive_hook_id:int):
        """Removes any overrides for this hook at the org level for this org.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#remove-pre-receive-hook-enforcement-for-an-organization
        /orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}
        
        arguments:
        org -- 
        pre_receive_hook_id -- pre_receive_hook_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return OrgPreReceiveHook(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}
    #
    def EnterpriseAdminRemovePreReceiveHookEnforcementForRepo(self, owner:str, repo:str, pre_receive_hook_id:int):
        """Deletes any overridden enforcement on this repository for the specified hook.

Responds with effective values inherited from owner and/or global level.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#remove-pre-receive-hook-enforcement-for-a-repository
        /repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}
        
        arguments:
        owner -- 
        repo -- 
        pre_receive_hook_id -- pre_receive_hook_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return RepositoryPreReceiveHook(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners/{runner_id}
    #
    def EnterpriseAdminRemoveSelfHostedRunnerFromGroupForEnterprise(self, enterprise:str, runner_group_id:int, runner_id:int):
        """Removes a self-hosted runner from a group configured in an enterprise. The runner is then returned to the default group.

You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#remove-a-self-hosted-runner-from-a-group-for-an-enterprise
        /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners/{runner_id}
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        runner_group_id -- Unique identifier of the self-hosted runner group.
        runner_id -- Unique identifier of the self-hosted runner.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners/{runner_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # put /enterprises/{enterprise}/actions/permissions/selected-actions
    #
    def EnterpriseAdminSetAllowedActionsEnterprise(self, enterprise:str,patterns_allowed:list, github_owned_allowed:bool):
        """Sets the actions that are allowed in an enterprise. To use this endpoint, the enterprise permission policy for `allowed_actions` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise)."

You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#set-allowed-actions-for-an-enterprise
        /enterprises/{enterprise}/actions/permissions/selected-actions
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        patterns_allowed -- Specifies a list of string-matching patterns to allow specific action(s). Wildcards, tags, and SHAs are allowed. For example, `monalisa/octocat@*`, `monalisa/octocat@v2`, `monalisa/*`."
        github_owned_allowed -- Whether GitHub-owned actions are allowed. For example, this includes the actions in the `actions` organization.
        

        """
    
        data = {
        'patterns_allowed': patterns_allowed,
        'github_owned_allowed': github_owned_allowed,
        
        }
        

        
        r = self._session.put(f"{self._url}/enterprises/{enterprise}/actions/permissions/selected-actions", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # patch /enterprise/announcement
    #
    def EnterpriseAdminSetAnnouncement(self, announcement:str, expires_at:datetime=None):
        """Sets the message and expiration time for the global announcement banner in your enterprise.
        /enterprise/announcement
        
        arguments:
        announcement -- 
        expires_at -- 
        

        """
    
        data = {
        'announcement': announcement,
        'expires_at': expires_at,
        
        }
        

        
        r = self._session.patch(f"{self._url}/enterprise/announcement", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return EnterpriseAnnouncement(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /enterprises/{enterprise}/actions/permissions
    #
    def EnterpriseAdminSetGithubActionsPermissionsEnterprise(self, enterprise:str,enabled_organizations:str, allowed_actions:str=None):
        """Sets the GitHub Actions permissions policy for organizations and allowed actions in an enterprise.

You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#set-github-actions-permissions-for-an-enterprise
        /enterprises/{enterprise}/actions/permissions
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        enabled_organizations -- 
        allowed_actions -- 
        

        """
    
        data = {
        'enabled_organizations': enabled_organizations,
        'allowed_actions': allowed_actions,
        
        }
        

        
        r = self._session.put(f"{self._url}/enterprises/{enterprise}/actions/permissions", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations
    #
    def EnterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterprise(self, enterprise:str, runner_group_id:int,selected_organization_ids:list):
        """Replaces the list of organizations that have access to a self-hosted runner configured in an enterprise.

You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#set-organization-access-to-a-self-hosted-runner-group-in-an-enterprise
        /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        runner_group_id -- Unique identifier of the self-hosted runner group.
        selected_organization_ids -- List of organization IDs that can access the runner group.
        

        """
    
        data = {
        'selected_organization_ids': selected_organization_ids,
        
        }
        

        
        r = self._session.put(f"{self._url}/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /enterprises/{enterprise}/actions/permissions/organizations
    #
    def EnterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterprise(self, enterprise:str,selected_organization_ids:list):
        """Replaces the list of selected organizations that are enabled for GitHub Actions in an enterprise. To use this endpoint, the enterprise permission policy for `enabled_organizations` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise)."

You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#set-selected-organizations-enabled-for-github-actions-in-an-enterprise
        /enterprises/{enterprise}/actions/permissions/organizations
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        selected_organization_ids -- List of organization IDs to enable for GitHub Actions.
        

        """
    
        data = {
        'selected_organization_ids': selected_organization_ids,
        
        }
        

        
        r = self._session.put(f"{self._url}/enterprises/{enterprise}/actions/permissions/organizations", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners
    #
    def EnterpriseAdminSetSelfHostedRunnersInGroupForEnterprise(self, enterprise:str, runner_group_id:int,runners:list):
        """Replaces the list of self-hosted runners that are part of an enterprise runner group.

You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#set-self-hosted-runners-in-a-group-for-an-enterprise
        /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        runner_group_id -- Unique identifier of the self-hosted runner group.
        runners -- List of runner IDs to add to the runner group.
        

        """
    
        data = {
        'runners': runners,
        
        }
        

        
        r = self._session.put(f"{self._url}/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /setup/api/settings
    #
    def EnterpriseAdminSetSettings(self, settings:str):
        """For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-settings).

**Note:** The request body for this operation must be submitted as `application/x-www-form-urlencoded` data. You can submit a parameter value as a string, or you can use a tool such as `curl` to submit a parameter value as the contents of a text file. For more information, see the [`curl` documentation](https://curl.se/docs/manpage.html#--data-urlencode).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#set-settings
        /setup/api/settings
        
        arguments:
        settings -- A JSON string with the new settings. Note that you only need to pass the specific settings you want to modify. For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#get-settings).
        

        """
    
        data = {
        'settings': settings,
        
        }
        

        
        r = self._session.put(f"{self._url}/setup/api/settings", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/x-www-form-urlencoded'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # post /setup/api/configure
    #
    def EnterpriseAdminStartConfigurationProcess(self, ):
        """This endpoint allows you to start a configuration process at any time for your updated settings to take effect:
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#start-a-configuration-process
        /setup/api/configure
        
        arguments:
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/setup/api/configure", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 202:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # post /admin/pre-receive-environments/{pre_receive_environment_id}/downloads
    #
    def EnterpriseAdminStartPreReceiveEnvironmentDownload(self, pre_receive_environment_id:int):
        """Triggers a new download of the environment tarball from the environment's `image_url`. When the download is finished, the newly downloaded tarball will overwrite the existing environment.

If a download cannot be triggered, you will receive a `422 Unprocessable Entity` response.

The possible error messages are:

* _Cannot modify or delete the default environment_
* _Can not start a new download when a download is in progress_
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#start-a-pre-receive-environment-download
        /admin/pre-receive-environments/{pre_receive_environment_id}/downloads
        
        arguments:
        pre_receive_environment_id -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/admin/pre-receive-environments/{pre_receive_environment_id}/downloads", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 202:
            return PreReceiveEnvironmentDownloadStatus(**r.json())
            
        if r.status_code == 422:
            return EnterpriseAdminStartPreReceiveEnvironmentDownload422(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /users/{username}/suspended
    #
    def EnterpriseAdminSuspendUser(self, username:str,reason:str=None):
        """If your GitHub instance uses [LDAP Sync with Active Directory LDAP servers](https://help.github.com/enterprise/admin/guides/user-management/using-ldap), Active Directory LDAP-authenticated users cannot be suspended through this API. If you attempt to suspend an Active Directory LDAP-authenticated user through this API, it will return a `403` response.

You can suspend any user account except your own.

Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#http-verbs)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#suspend-a-user
        /users/{username}/suspended
        
        arguments:
        username -- 
        reason -- The reason the user is being suspended. This message will be logged in the [audit log](https://help.github.com/enterprise/admin/articles/audit-logging/). If you don't provide a `reason`, it will default to "Suspended via API by _SITE\_ADMINISTRATOR_", where _SITE\_ADMINISTRATOR_ is the person who performed the action.
        

        """
    
        data = {
        'reason': reason,
        
        }
        

        
        r = self._session.put(f"{self._url}/users/{username}/suspended", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # post /admin/ldap/teams/{team_id}/sync
    #
    def EnterpriseAdminSyncLdapMappingForTeam(self, team_id:int):
        """Note that this API call does not automatically initiate an LDAP sync. Rather, if a `201` is returned, the sync job is queued successfully, and is performed when the instance is ready.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#sync-ldap-mapping-for-a-team
        /admin/ldap/teams/{team_id}/sync
        
        arguments:
        team_id -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/admin/ldap/teams/{team_id}/sync", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return EnterpriseAdminSyncLdapMappingForTeamSuccess(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /admin/ldap/users/{username}/sync
    #
    def EnterpriseAdminSyncLdapMappingForUser(self, username:str):
        """Note that this API call does not automatically initiate an LDAP sync. Rather, if a `201` is returned, the sync job is queued successfully, and is performed when the instance is ready.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#sync-ldap-mapping-for-a-user
        /admin/ldap/users/{username}/sync
        
        arguments:
        username -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/admin/ldap/users/{username}/sync", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return EnterpriseAdminSyncLdapMappingForUserSuccess(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /users/{username}/suspended
    #
    def EnterpriseAdminUnsuspendUser(self, username:str):
        """If your GitHub instance uses [LDAP Sync with Active Directory LDAP servers](https://help.github.com/enterprise/admin/guides/user-management/using-ldap), this API is disabled and will return a `403` response. Active Directory LDAP-authenticated users cannot be unsuspended using the API.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#unsuspend-a-user
        /users/{username}/suspended
        
        arguments:
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/users/{username}/suspended", 
                           params=data,
                           **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # patch /admin/hooks/{hook_id}
    #
    def EnterpriseAdminUpdateGlobalWebhook(self, hook_id:int,config:dict=None, events:list=[], active:bool=True):
        """Parameters that are not provided will be overwritten with the default value or removed if no default exists.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#update-a-global-webhook
        /admin/hooks/{hook_id}
        
        arguments:
        hook_id -- 
        config -- Key/value pairs to provide settings for this webhook.
        events -- The [events](https://docs.github.com/enterprise-server@3.3/webhooks/event-payloads) that trigger this webhook. A global webhook can be triggered by `user` and `organization` events. Default: `user` and `organization`.
        active -- Determines if notifications are sent when the webhook is triggered. Set to `true` to send notifications.
        

        """
    
        data = {
        'config': config,
        'events': events,
        'active': active,
        
        }
        

        
        r = self._session.patch(f"{self._url}/admin/hooks/{hook_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return GlobalHook2(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /admin/ldap/teams/{team_id}/mapping
    #
    def EnterpriseAdminUpdateLdapMappingForTeam(self, team_id:int,ldap_dn:str):
        """Updates the [distinguished name](https://www.ldap.com/ldap-dns-and-rdns) (DN) of the LDAP entry to map to a team. [LDAP synchronization](https://help.github.com/enterprise/admin/guides/user-management/using-ldap/#enabling-ldap-sync) must be enabled to map LDAP entries to a team. Use the [Create a team](https://docs.github.com/enterprise-server@3.3/rest/reference/teams/#create-a-team) endpoint to create a team with LDAP mapping.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#update-ldap-mapping-for-a-team
        /admin/ldap/teams/{team_id}/mapping
        
        arguments:
        team_id -- 
        ldap_dn -- The [distinguished name](https://www.ldap.com/ldap-dns-and-rdns) (DN) of the LDAP entry to map to a team.
        

        """
    
        data = {
        'ldap_dn': ldap_dn,
        
        }
        

        
        r = self._session.patch(f"{self._url}/admin/ldap/teams/{team_id}/mapping", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return LdapMappingTeam(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /admin/ldap/users/{username}/mapping
    #
    def EnterpriseAdminUpdateLdapMappingForUser(self, username:str,ldap_dn:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#update-ldap-mapping-for-a-user
        /admin/ldap/users/{username}/mapping
        
        arguments:
        username -- 
        ldap_dn -- The [distinguished name](https://www.ldap.com/ldap-dns-and-rdns) (DN) of the LDAP entry to map to a team.
        

        """
    
        data = {
        'ldap_dn': ldap_dn,
        
        }
        

        
        r = self._session.patch(f"{self._url}/admin/ldap/users/{username}/mapping", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return LdapPrivateUser(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /admin/organizations/{org}
    #
    def EnterpriseAdminUpdateOrgName(self, org:str,login:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#update-an-organization-name
        /admin/organizations/{org}
        
        arguments:
        org -- 
        login -- The organization's new name.
        

        """
    
        data = {
        'login': login,
        
        }
        

        
        r = self._session.patch(f"{self._url}/admin/organizations/{org}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 202:
            return EnterpriseAdminUpdateOrgName202(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /admin/pre-receive-environments/{pre_receive_environment_id}
    #
    def EnterpriseAdminUpdatePreReceiveEnvironment(self, pre_receive_environment_id:int,name:str=None, image_url:str=None):
        """You cannot modify the default environment. If you attempt to modify the default environment, you will receive a `422 Unprocessable Entity` response.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#update-a-pre-receive-environment
        /admin/pre-receive-environments/{pre_receive_environment_id}
        
        arguments:
        pre_receive_environment_id -- 
        name -- This pre-receive environment's new name.
        image_url -- URL from which to download a tarball of this environment.
        

        """
    
        data = {
        'name': name,
        'image_url': image_url,
        
        }
        

        
        r = self._session.patch(f"{self._url}/admin/pre-receive-environments/{pre_receive_environment_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return PreReceiveEnvironment(**r.json())
            
        if r.status_code == 422:
            return EnterpriseAdminUpdatePreReceiveEnvironment422(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /admin/pre-receive-hooks/{pre_receive_hook_id}
    #
    def EnterpriseAdminUpdatePreReceiveHook(self, pre_receive_hook_id:int,name:str=None, script:str=None, script_repository:dict=None, environment:dict=None, enforcement:str=None, allow_downstream_configuration:bool=None):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#update-a-pre-receive-hook
        /admin/pre-receive-hooks/{pre_receive_hook_id}
        
        arguments:
        pre_receive_hook_id -- pre_receive_hook_id parameter
        name -- The name of the hook.
        script -- The script that the hook runs.
        script_repository -- The GitHub repository where the script is kept.
        environment -- The pre-receive environment where the script is executed.
        enforcement -- The state of enforcement for this hook.
        allow_downstream_configuration -- Whether enforcement can be overridden at the org or repo level.
        

        """
    
        data = {
        'name': name,
        'script': script,
        'script_repository': script_repository,
        'environment': environment,
        'enforcement': enforcement,
        'allow_downstream_configuration': allow_downstream_configuration,
        
        }
        

        
        r = self._session.patch(f"{self._url}/admin/pre-receive-hooks/{pre_receive_hook_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return PreReceiveHook(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}
    #
    def EnterpriseAdminUpdatePreReceiveHookEnforcementForOrg(self, org:str, pre_receive_hook_id:int,enforcement:str=None, allow_downstream_configuration:bool=None):
        """For pre-receive hooks which are allowed to be configured at the org level, you can set `enforcement` and `allow_downstream_configuration`
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#update-pre-receive-hook-enforcement-for-an-organization
        /orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}
        
        arguments:
        org -- 
        pre_receive_hook_id -- pre_receive_hook_id parameter
        enforcement -- The state of enforcement for the hook on this repository.
        allow_downstream_configuration -- Whether repositories can override enforcement.
        

        """
    
        data = {
        'enforcement': enforcement,
        'allow_downstream_configuration': allow_downstream_configuration,
        
        }
        

        
        r = self._session.patch(f"{self._url}/orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return OrgPreReceiveHook(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}
    #
    def EnterpriseAdminUpdatePreReceiveHookEnforcementForRepo(self, owner:str, repo:str, pre_receive_hook_id:int,enforcement:str=None):
        """For pre-receive hooks which are allowed to be configured at the repo level, you can set `enforcement`
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#update-pre-receive-hook-enforcement-for-a-repository
        /repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}
        
        arguments:
        owner -- 
        repo -- 
        pre_receive_hook_id -- pre_receive_hook_id parameter
        enforcement -- The state of enforcement for the hook on this repository.
        

        """
    
        data = {
        'enforcement': enforcement,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return RepositoryPreReceiveHook(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}
    #
    def EnterpriseAdminUpdateSelfHostedRunnerGroupForEnterprise(self, enterprise:str, runner_group_id:int,name:str=None, visibility:str='all', allows_public_repositories:bool=False):
        """Updates the `name` and `visibility` of a self-hosted runner group in an enterprise.

You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#update-a-self-hosted-runner-group-for-an-enterprise
        /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}
        
        arguments:
        enterprise -- The slug version of the enterprise name. You can also substitute this value with the enterprise id.
        runner_group_id -- Unique identifier of the self-hosted runner group.
        name -- Name of the runner group.
        visibility -- Visibility of a runner group. You can select all organizations or select individual organizations. Can be one of: `all` or `selected`
        allows_public_repositories -- Whether the runner group can be used by `public` repositories.
        

        """
    
        data = {
        'name': name,
        'visibility': visibility,
        'allows_public_repositories': allows_public_repositories,
        
        }
        

        
        r = self._session.patch(f"{self._url}/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return RunnerGroupsEnterprise(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /admin/users/{username}
    #
    def EnterpriseAdminUpdateUsernameForUser(self, username:str,login:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#update-the-username-for-a-user
        /admin/users/{username}
        
        arguments:
        username -- 
        login -- The user's new username.
        

        """
    
        data = {
        'login': login,
        
        }
        

        
        r = self._session.patch(f"{self._url}/admin/users/{username}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 202:
            return EnterpriseAdminUpdateUsernameForUser202(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /setup/api/upgrade
    #
    def EnterpriseAdminUpgradeLicense(self, license:str=None):
        """This API upgrades your license and also triggers the configuration process.

**Note:** The request body for this operation must be submitted as `application/x-www-form-urlencoded` data. You can submit a parameter value as a string, or you can use a tool such as `curl` to submit a parameter value as the contents of a text file. For more information, see the [`curl` documentation](https://curl.se/docs/manpage.html#--data-urlencode).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/enterprise-admin#upgrade-a-license
        /setup/api/upgrade
        
        arguments:
        license -- The content of your new _.ghl_ license file.
        

        """
    
        data = {
        'license': license,
        
        }
        

        
        r = self._session.post(f"{self._url}/setup/api/upgrade", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/x-www-form-urlencoded'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 202:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
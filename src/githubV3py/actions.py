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

class Actions(object):


    #
    # put /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id}
    #
    def ActionsAddRepoAccessToSelfHostedRunnerGroupInOrg(self, org:str, runner_group_id:int, repository_id:int):
        """Adds a repository to the list of selected repositories that can access a self-hosted runner group. The runner group must have `visibility` set to `selected`. For more information, see "[Create a self-hosted runner group for an organization](#create-a-self-hosted-runner-group-for-an-organization)."
You must authenticate using an access token with the `admin:org` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#add-repository-acess-to-a-self-hosted-runner-group-in-an-organization
        /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id}
        
        arguments:
        org -- 
        runner_group_id -- Unique identifier of the self-hosted runner group.
        repository_id -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.put(f"{self._url}/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id}", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}
    #
    def ActionsAddSelectedRepoToOrgSecret(self, org:str, secret_name:str, repository_id:int):
        """Adds a repository to an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/enterprise-server@3.3/rest/reference/actions#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#add-selected-repository-to-an-organization-secret
        /orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}
        
        arguments:
        org -- 
        secret_name -- secret_name parameter
        repository_id -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.put(f"{self._url}/orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 409:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id}
    #
    def ActionsAddSelfHostedRunnerToGroupForOrg(self, org:str, runner_group_id:int, runner_id:int):
        """Adds a self-hosted runner to a runner group configured in an organization.
You must authenticate using an access token with the `admin:org` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#add-a-self-hosted-runner-to-a-group-for-an-organization
        /orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id}
        
        arguments:
        org -- 
        runner_group_id -- Unique identifier of the self-hosted runner group.
        runner_id -- Unique identifier of the self-hosted runner.
        

        """
    
        data = {
        
        }
        

        
        r = self._session.put(f"{self._url}/orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id}", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/actions/runs/{run_id}/cancel
    #
    def ActionsCancelWorkflowRun(self, owner:str, repo:str, run_id:int):
        """Cancels a workflow run using its `id`. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#cancel-a-workflow-run
        /repos/{owner}/{repo}/actions/runs/{run_id}/cancel
        
        arguments:
        owner -- 
        repo -- 
        run_id -- The id of the workflow run.
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/actions/runs/{run_id}/cancel", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 202:
            return ActionsCancelWorkflowRun202(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name}
    #
    def ActionsCreateOrUpdateEnvironmentSecret(self, repository_id:int, environment_name:str, secret_name:str,key_id:str, encrypted_value:str):
        """Creates or updates an environment secret with an encrypted value. Encrypt your secret using
[LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). You must authenticate using an access
token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets` repository permission to use
this endpoint.

#### Example encrypting a secret using Node.js

Encrypt your secret using the [tweetsodium](https://github.com/github/tweetsodium) library.

```
const sodium = require('tweetsodium');

const key = "base64-encoded-public-key";
const value = "plain-text-secret";

// Convert the message and key to Uint8Array's (Buffer implements that interface)
const messageBytes = Buffer.from(value);
const keyBytes = Buffer.from(key, 'base64');

// Encrypt using LibSodium.
const encryptedBytes = sodium.seal(messageBytes, keyBytes);

// Base64 the encrypted secret
const encrypted = Buffer.from(encryptedBytes).toString('base64');

console.log(encrypted);
```


#### Example encrypting a secret using Python

Encrypt your secret using [pynacl](https://pynacl.readthedocs.io/en/stable/public/#nacl-public-sealedbox) with Python 3.

```
from base64 import b64encode
from nacl import encoding, public

def encrypt(public_key: str, secret_value: str) -> str:
  \"""Encrypt a Unicode string using the public key.\"""
  public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
  sealed_box = public.SealedBox(public_key)
  encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
  return b64encode(encrypted).decode("utf-8")
```

#### Example encrypting a secret using C#

Encrypt your secret using the [Sodium.Core](https://www.nuget.org/packages/Sodium.Core/) package.

```
var secretValue = System.Text.Encoding.UTF8.GetBytes("mySecret");
var publicKey = Convert.FromBase64String("2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvvcCU=");

var sealedPublicKeyBox = Sodium.SealedPublicKeyBox.Create(secretValue, publicKey);

Console.WriteLine(Convert.ToBase64String(sealedPublicKeyBox));
```

#### Example encrypting a secret using Ruby

Encrypt your secret using the [rbnacl](https://github.com/RubyCrypto/rbnacl) gem.

```ruby
require "rbnacl"
require "base64"

key = Base64.decode64("+ZYvJDZMHUfBkJdyq5Zm9SKqeuBQ4sj+6sfjlH4CgG0=")
public_key = RbNaCl::PublicKey.new(key)

box = RbNaCl::Boxes::Sealed.from_public_key(public_key)
encrypted_secret = box.encrypt("my_secret")

# Print the base64 encoded secret
puts Base64.strict_encode64(encrypted_secret)
```
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#create-or-update-an-environment-secret
        /repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name}
        
        arguments:
        repository_id -- 
        environment_name -- The name of the environment
        secret_name -- secret_name parameter
        key_id -- ID of the key you used to encrypt the secret.
        encrypted_value -- Value for your secret, encrypted with [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using the public key retrieved from the [Get an environment public key](https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-an-environment-public-key) endpoint.
        

        """
    
        data = {
        'key_id': key_id,
        'encrypted_value': encrypted_value,
        
        }
        

        
        r = self._session.put(f"{self._url}/repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return EmptyObject(**r.json())
            
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /orgs/{org}/actions/secrets/{secret_name}
    #
    def ActionsCreateOrUpdateOrgSecret(self, org:str, secret_name:str,visibility:str, encrypted_value:str=None, key_id:str=None, selected_repository_ids:list=[]):
        """Creates or updates an organization secret with an encrypted value. Encrypt your secret using
[LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). You must authenticate using an access
token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to
use this endpoint.

#### Example encrypting a secret using Node.js

Encrypt your secret using the [tweetsodium](https://github.com/github/tweetsodium) library.

```
const sodium = require('tweetsodium');

const key = "base64-encoded-public-key";
const value = "plain-text-secret";

// Convert the message and key to Uint8Array's (Buffer implements that interface)
const messageBytes = Buffer.from(value);
const keyBytes = Buffer.from(key, 'base64');

// Encrypt using LibSodium.
const encryptedBytes = sodium.seal(messageBytes, keyBytes);

// Base64 the encrypted secret
const encrypted = Buffer.from(encryptedBytes).toString('base64');

console.log(encrypted);
```


#### Example encrypting a secret using Python

Encrypt your secret using [pynacl](https://pynacl.readthedocs.io/en/stable/public/#nacl-public-sealedbox) with Python 3.

```
from base64 import b64encode
from nacl import encoding, public

def encrypt(public_key: str, secret_value: str) -> str:
  \"""Encrypt a Unicode string using the public key.\"""
  public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
  sealed_box = public.SealedBox(public_key)
  encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
  return b64encode(encrypted).decode("utf-8")
```

#### Example encrypting a secret using C#

Encrypt your secret using the [Sodium.Core](https://www.nuget.org/packages/Sodium.Core/) package.

```
var secretValue = System.Text.Encoding.UTF8.GetBytes("mySecret");
var publicKey = Convert.FromBase64String("2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvvcCU=");

var sealedPublicKeyBox = Sodium.SealedPublicKeyBox.Create(secretValue, publicKey);

Console.WriteLine(Convert.ToBase64String(sealedPublicKeyBox));
```

#### Example encrypting a secret using Ruby

Encrypt your secret using the [rbnacl](https://github.com/RubyCrypto/rbnacl) gem.

```ruby
require "rbnacl"
require "base64"

key = Base64.decode64("+ZYvJDZMHUfBkJdyq5Zm9SKqeuBQ4sj+6sfjlH4CgG0=")
public_key = RbNaCl::PublicKey.new(key)

box = RbNaCl::Boxes::Sealed.from_public_key(public_key)
encrypted_secret = box.encrypt("my_secret")

# Print the base64 encoded secret
puts Base64.strict_encode64(encrypted_secret)
```
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#create-or-update-an-organization-secret
        /orgs/{org}/actions/secrets/{secret_name}
        
        arguments:
        org -- 
        secret_name -- secret_name parameter
        visibility -- Configures the access that repositories have to the organization secret. Can be one of:  
\- `all` - All repositories in an organization can access the secret.  
\- `private` - Private repositories in an organization can access the secret.  
\- `selected` - Only specific repositories can access the secret.
        encrypted_value -- Value for your secret, encrypted with [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using the public key retrieved from the [Get an organization public key](https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-an-organization-public-key) endpoint.
        key_id -- ID of the key you used to encrypt the secret.
        selected_repository_ids -- An array of repository ids that can access the organization secret. You can only provide a list of repository ids when the `visibility` is set to `selected`. You can manage the list of selected repositories using the [List selected repositories for an organization secret](https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-selected-repositories-for-an-organization-secret), [Set selected repositories for an organization secret](https://docs.github.com/enterprise-server@3.3/rest/reference/actions#set-selected-repositories-for-an-organization-secret), and [Remove selected repository from an organization secret](https://docs.github.com/enterprise-server@3.3/rest/reference/actions#remove-selected-repository-from-an-organization-secret) endpoints.
        

        """
    
        data = {
        'visibility': visibility,
        'encrypted_value': encrypted_value,
        'key_id': key_id,
        'selected_repository_ids': selected_repository_ids,
        
        }
        

        
        r = self._session.put(f"{self._url}/orgs/{org}/actions/secrets/{secret_name}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return EmptyObject(**r.json())
            
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/actions/secrets/{secret_name}
    #
    def ActionsCreateOrUpdateRepoSecret(self, owner:str, repo:str, secret_name:str,encrypted_value:str=None, key_id:str=None):
        """Creates or updates a repository secret with an encrypted value. Encrypt your secret using
[LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). You must authenticate using an access
token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets` repository permission to use
this endpoint.

#### Example encrypting a secret using Node.js

Encrypt your secret using the [tweetsodium](https://github.com/github/tweetsodium) library.

```
const sodium = require('tweetsodium');

const key = "base64-encoded-public-key";
const value = "plain-text-secret";

// Convert the message and key to Uint8Array's (Buffer implements that interface)
const messageBytes = Buffer.from(value);
const keyBytes = Buffer.from(key, 'base64');

// Encrypt using LibSodium.
const encryptedBytes = sodium.seal(messageBytes, keyBytes);

// Base64 the encrypted secret
const encrypted = Buffer.from(encryptedBytes).toString('base64');

console.log(encrypted);
```


#### Example encrypting a secret using Python

Encrypt your secret using [pynacl](https://pynacl.readthedocs.io/en/stable/public/#nacl-public-sealedbox) with Python 3.

```
from base64 import b64encode
from nacl import encoding, public

def encrypt(public_key: str, secret_value: str) -> str:
  \"""Encrypt a Unicode string using the public key.\"""
  public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
  sealed_box = public.SealedBox(public_key)
  encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
  return b64encode(encrypted).decode("utf-8")
```

#### Example encrypting a secret using C#

Encrypt your secret using the [Sodium.Core](https://www.nuget.org/packages/Sodium.Core/) package.

```
var secretValue = System.Text.Encoding.UTF8.GetBytes("mySecret");
var publicKey = Convert.FromBase64String("2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvvcCU=");

var sealedPublicKeyBox = Sodium.SealedPublicKeyBox.Create(secretValue, publicKey);

Console.WriteLine(Convert.ToBase64String(sealedPublicKeyBox));
```

#### Example encrypting a secret using Ruby

Encrypt your secret using the [rbnacl](https://github.com/RubyCrypto/rbnacl) gem.

```ruby
require "rbnacl"
require "base64"

key = Base64.decode64("+ZYvJDZMHUfBkJdyq5Zm9SKqeuBQ4sj+6sfjlH4CgG0=")
public_key = RbNaCl::PublicKey.new(key)

box = RbNaCl::Boxes::Sealed.from_public_key(public_key)
encrypted_secret = box.encrypt("my_secret")

# Print the base64 encoded secret
puts Base64.strict_encode64(encrypted_secret)
```
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#create-or-update-a-repository-secret
        /repos/{owner}/{repo}/actions/secrets/{secret_name}
        
        arguments:
        owner -- 
        repo -- 
        secret_name -- secret_name parameter
        encrypted_value -- Value for your secret, encrypted with [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using the public key retrieved from the [Get a repository public key](https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-a-repository-public-key) endpoint.
        key_id -- ID of the key you used to encrypt the secret.
        

        """
    
        data = {
        'encrypted_value': encrypted_value,
        'key_id': key_id,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/actions/secrets/{secret_name}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return ActionsCreateOrUpdateRepoSecretSuccess(**r.json())
            
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # post /orgs/{org}/actions/runners/registration-token
    #
    def ActionsCreateRegistrationTokenForOrg(self, org:str):
        """Returns a token that you can pass to the `config` script. The token expires after one hour.

You must authenticate using an access token with the `admin:org` scope to use this endpoint.

#### Example using registration token

Configure your self-hosted runner, replacing `TOKEN` with the registration token provided by this endpoint.

```
./config.sh --url https://github.com/octo-org --token TOKEN
```
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#create-a-registration-token-for-an-organization
        /orgs/{org}/actions/runners/registration-token
        
        arguments:
        org -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/orgs/{org}/actions/runners/registration-token", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return AuthenticationToken(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/actions/runners/registration-token
    #
    def ActionsCreateRegistrationTokenForRepo(self, owner:str, repo:str):
        """Returns a token that you can pass to the `config` script. The token expires after one hour. You must authenticate
using an access token with the `repo` scope to use this endpoint.

#### Example using registration token
 
Configure your self-hosted runner, replacing `TOKEN` with the registration token provided by this endpoint.

```
./config.sh --url https://github.com/octo-org/octo-repo-artifacts --token TOKEN
```
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#create-a-registration-token-for-a-repository
        /repos/{owner}/{repo}/actions/runners/registration-token
        
        arguments:
        owner -- 
        repo -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/actions/runners/registration-token", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return AuthenticationToken(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /orgs/{org}/actions/runners/remove-token
    #
    def ActionsCreateRemoveTokenForOrg(self, org:str):
        """Returns a token that you can pass to the `config` script to remove a self-hosted runner from an organization. The token expires after one hour.

You must authenticate using an access token with the `admin:org` scope to use this endpoint.

#### Example using remove token

To remove your self-hosted runner from an organization, replace `TOKEN` with the remove token provided by this
endpoint.

```
./config.sh remove --token TOKEN
```
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#create-a-remove-token-for-an-organization
        /orgs/{org}/actions/runners/remove-token
        
        arguments:
        org -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/orgs/{org}/actions/runners/remove-token", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return AuthenticationToken(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/actions/runners/remove-token
    #
    def ActionsCreateRemoveTokenForRepo(self, owner:str, repo:str):
        """Returns a token that you can pass to remove a self-hosted runner from a repository. The token expires after one hour.
You must authenticate using an access token with the `repo` scope to use this endpoint.

#### Example using remove token
 
To remove your self-hosted runner from a repository, replace TOKEN with the remove token provided by this endpoint.

```
./config.sh remove --token TOKEN
```
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#create-a-remove-token-for-a-repository
        /repos/{owner}/{repo}/actions/runners/remove-token
        
        arguments:
        owner -- 
        repo -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/actions/runners/remove-token", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return AuthenticationToken(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /orgs/{org}/actions/runner-groups
    #
    def ActionsCreateSelfHostedRunnerGroupForOrg(self, org:str,name:str, visibility:str='all', selected_repository_ids:list=[], runners:list=[], allows_public_repositories:bool=False):
        """The self-hosted runner groups REST API is available with GitHub Enterprise Cloud and GitHub Enterprise Server. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."

Creates a new self-hosted runner group for an organization.

You must authenticate using an access token with the `admin:org` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#create-a-self-hosted-runner-group-for-an-organization
        /orgs/{org}/actions/runner-groups
        
        arguments:
        org -- 
        name -- Name of the runner group.
        visibility -- Visibility of a runner group. You can select all repositories, select individual repositories, or limit access to private repositories. Can be one of: `all`, `selected`, or `private`.
        selected_repository_ids -- List of repository IDs that can access the runner group.
        runners -- List of runner IDs to add to the runner group.
        allows_public_repositories -- Whether the runner group can be used by `public` repositories.
        

        """
    
        data = {
        'name': name,
        'visibility': visibility,
        'selected_repository_ids': selected_repository_ids,
        'runners': runners,
        'allows_public_repositories': allows_public_repositories,
        
        }
        

        
        r = self._session.post(f"{self._url}/orgs/{org}/actions/runner-groups", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return RunnerGroupsOrg(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches
    #
    def ActionsCreateWorkflowDispatch(self, owner:str, repo:str, workflow_id:('integer', 'string'),ref:str, inputs:object=None):
        """You can use this endpoint to manually trigger a GitHub Actions workflow run. You can replace `workflow_id` with the workflow file name. For example, you could use `main.yaml`.

You must configure your GitHub Actions workflow to run when the [`workflow_dispatch` webhook](/developers/webhooks-and-events/webhook-events-and-payloads#workflow_dispatch) event occurs. The `inputs` are configured in the workflow file. For more information about how to configure the `workflow_dispatch` event in the workflow file, see "[Events that trigger workflows](/actions/reference/events-that-trigger-workflows#workflow_dispatch)."

You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this endpoint. For more information, see "[Creating a personal access token for the command line](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#create-a-workflow-dispatch-event
        /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches
        
        arguments:
        owner -- 
        repo -- 
        workflow_id -- The ID of the workflow. You can also pass the workflow file name as a string.
        ref -- The git reference for the workflow. The reference can be a branch or tag name.
        inputs -- Input keys and values configured in the workflow file. The maximum number of properties is 10. Any default properties configured in the workflow file will be used when `inputs` are omitted.
        

        """
    
        data = {
        'ref': ref,
        'inputs': inputs,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/actions/artifacts/{artifact_id}
    #
    def ActionsDeleteArtifact(self, owner:str, repo:str, artifact_id:int):
        """Deletes an artifact for a workflow run. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#delete-an-artifact
        /repos/{owner}/{repo}/actions/artifacts/{artifact_id}
        
        arguments:
        owner -- 
        repo -- 
        artifact_id -- artifact_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/actions/artifacts/{artifact_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name}
    #
    def ActionsDeleteEnvironmentSecret(self, repository_id:int, environment_name:str, secret_name:str):
        """Deletes a secret in an environment using the secret name. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets` repository permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#delete-an-environment-secret
        /repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name}
        
        arguments:
        repository_id -- 
        environment_name -- The name of the environment
        secret_name -- secret_name parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/actions/secrets/{secret_name}
    #
    def ActionsDeleteOrgSecret(self, org:str, secret_name:str):
        """Deletes a secret in an organization using the secret name. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#delete-an-organization-secret
        /orgs/{org}/actions/secrets/{secret_name}
        
        arguments:
        org -- 
        secret_name -- secret_name parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/actions/secrets/{secret_name}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/actions/secrets/{secret_name}
    #
    def ActionsDeleteRepoSecret(self, owner:str, repo:str, secret_name:str):
        """Deletes a secret in a repository using the secret name. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets` repository permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#delete-a-repository-secret
        /repos/{owner}/{repo}/actions/secrets/{secret_name}
        
        arguments:
        owner -- 
        repo -- 
        secret_name -- secret_name parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/actions/secrets/{secret_name}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/actions/runners/{runner_id}
    #
    def ActionsDeleteSelfHostedRunnerFromOrg(self, org:str, runner_id:int):
        """Forces the removal of a self-hosted runner from an organization. You can use this endpoint to completely remove the runner when the machine you were using no longer exists.

You must authenticate using an access token with the `admin:org` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#delete-a-self-hosted-runner-from-an-organization
        /orgs/{org}/actions/runners/{runner_id}
        
        arguments:
        org -- 
        runner_id -- Unique identifier of the self-hosted runner.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/actions/runners/{runner_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/actions/runners/{runner_id}
    #
    def ActionsDeleteSelfHostedRunnerFromRepo(self, owner:str, repo:str, runner_id:int):
        """Forces the removal of a self-hosted runner from a repository. You can use this endpoint to completely remove the runner when the machine you were using no longer exists.

You must authenticate using an access token with the `repo`
scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#delete-a-self-hosted-runner-from-a-repository
        /repos/{owner}/{repo}/actions/runners/{runner_id}
        
        arguments:
        owner -- 
        repo -- 
        runner_id -- Unique identifier of the self-hosted runner.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/actions/runners/{runner_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/actions/runner-groups/{runner_group_id}
    #
    def ActionsDeleteSelfHostedRunnerGroupFromOrg(self, org:str, runner_group_id:int):
        """Deletes a self-hosted runner group for an organization.
You must authenticate using an access token with the `admin:org` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#delete-a-self-hosted-runner-group-from-an-organization
        /orgs/{org}/actions/runner-groups/{runner_group_id}
        
        arguments:
        org -- 
        runner_group_id -- Unique identifier of the self-hosted runner group.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/actions/runner-groups/{runner_group_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/actions/runs/{run_id}
    #
    def ActionsDeleteWorkflowRun(self, owner:str, repo:str, run_id:int):
        """Delete a specific workflow run. Anyone with write access to the repository can use this endpoint. If the repository is
private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:write` permission to use
this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#delete-a-workflow-run
        /repos/{owner}/{repo}/actions/runs/{run_id}
        
        arguments:
        owner -- 
        repo -- 
        run_id -- The id of the workflow run.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/actions/runs/{run_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/actions/runs/{run_id}/logs
    #
    def ActionsDeleteWorkflowRunLogs(self, owner:str, repo:str, run_id:int):
        """Deletes all logs for a workflow run. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#delete-workflow-run-logs
        /repos/{owner}/{repo}/actions/runs/{run_id}/logs
        
        arguments:
        owner -- 
        repo -- 
        run_id -- The id of the workflow run.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/actions/runs/{run_id}/logs", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/actions/permissions/repositories/{repository_id}
    #
    def ActionsDisableSelectedRepositoryGithubActionsOrganization(self, org:str, repository_id:int):
        """Removes a repository from the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."

You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#disable-a-selected-repository-for-github-actions-in-an-organization
        /orgs/{org}/actions/permissions/repositories/{repository_id}
        
        arguments:
        org -- 
        repository_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/actions/permissions/repositories/{repository_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable
    #
    def ActionsDisableWorkflow(self, owner:str, repo:str, workflow_id:('integer', 'string')):
        """Disables a workflow and sets the `state` of the workflow to `disabled_manually`. You can replace `workflow_id` with the workflow file name. For example, you could use `main.yaml`.

You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#disable-a-workflow
        /repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable
        
        arguments:
        owner -- 
        repo -- 
        workflow_id -- The ID of the workflow. You can also pass the workflow file name as a string.
        

        """
    
        data = {
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/artifacts/{artifact_id}/{archive_format}
    #
    def ActionsDownloadArtifact(self, owner:str, repo:str, artifact_id:int, archive_format:str):
        """Gets a redirect URL to download an archive for a repository. This URL expires after 1 minute. Look for `Location:` in
the response header to find the URL for the download. The `:archive_format` must be `zip`. Anyone with read access to
the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope.
GitHub Apps must have the `actions:read` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#download-an-artifact
        /repos/{owner}/{repo}/actions/artifacts/{artifact_id}/{archive_format}
        
        arguments:
        owner -- 
        repo -- 
        artifact_id -- artifact_id parameter
        archive_format -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/{archive_format}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 302:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/jobs/{job_id}/logs
    #
    def ActionsDownloadJobLogsForWorkflowRun(self, owner:str, repo:str, job_id:int):
        """Gets a redirect URL to download a plain text file of logs for a workflow job. This link expires after 1 minute. Look
for `Location:` in the response header to find the URL for the download. Anyone with read access to the repository can
use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must
have the `actions:read` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#download-job-logs-for-a-workflow-run
        /repos/{owner}/{repo}/actions/jobs/{job_id}/logs
        
        arguments:
        owner -- 
        repo -- 
        job_id -- job_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/jobs/{job_id}/logs", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 302:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/runs/{run_id}/logs
    #
    def ActionsDownloadWorkflowRunLogs(self, owner:str, repo:str, run_id:int):
        """Gets a redirect URL to download an archive of log files for a workflow run. This link expires after 1 minute. Look for
`Location:` in the response header to find the URL for the download. Anyone with read access to the repository can use
this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have
the `actions:read` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#download-workflow-run-logs
        /repos/{owner}/{repo}/actions/runs/{run_id}/logs
        
        arguments:
        owner -- 
        repo -- 
        run_id -- The id of the workflow run.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/runs/{run_id}/logs", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 302:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # put /orgs/{org}/actions/permissions/repositories/{repository_id}
    #
    def ActionsEnableSelectedRepositoryGithubActionsOrganization(self, org:str, repository_id:int):
        """Adds a repository to the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."

You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#enable-a-selected-repository-for-github-actions-in-an-organization
        /orgs/{org}/actions/permissions/repositories/{repository_id}
        
        arguments:
        org -- 
        repository_id -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.put(f"{self._url}/orgs/{org}/actions/permissions/repositories/{repository_id}", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable
    #
    def ActionsEnableWorkflow(self, owner:str, repo:str, workflow_id:('integer', 'string')):
        """Enables a workflow and sets the `state` of the workflow to `active`. You can replace `workflow_id` with the workflow file name. For example, you could use `main.yaml`.

You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#enable-a-workflow
        /repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable
        
        arguments:
        owner -- 
        repo -- 
        workflow_id -- The ID of the workflow. You can also pass the workflow file name as a string.
        

        """
    
        data = {
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # get /orgs/{org}/actions/permissions/selected-actions
    #
    def ActionsGetAllowedActionsOrganization(self, org:str):
        """Gets the selected actions that are allowed in an organization. To use this endpoint, the organization permission policy for `allowed_actions` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization).""

You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-allowed-actions-for-an-organization
        /orgs/{org}/actions/permissions/selected-actions
        
        arguments:
        org -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/actions/permissions/selected-actions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return SelectedActions(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/permissions/selected-actions
    #
    def ActionsGetAllowedActionsRepository(self, owner:str, repo:str):
        """Gets the settings for selected actions that are allowed in a repository. To use this endpoint, the repository policy for `allowed_actions` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for a repository](#set-github-actions-permissions-for-a-repository)."

You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `administration` repository permission to use this API.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-allowed-actions-for-a-repository
        /repos/{owner}/{repo}/actions/permissions/selected-actions
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/permissions/selected-actions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return SelectedActions(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/artifacts/{artifact_id}
    #
    def ActionsGetArtifact(self, owner:str, repo:str, artifact_id:int):
        """Gets a specific artifact for a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-an-artifact
        /repos/{owner}/{repo}/actions/artifacts/{artifact_id}
        
        arguments:
        owner -- 
        repo -- 
        artifact_id -- artifact_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/artifacts/{artifact_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Artifact(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repositories/{repository_id}/environments/{environment_name}/secrets/public-key
    #
    def ActionsGetEnvironmentPublicKey(self, repository_id:int, environment_name:str):
        """Get the public key for an environment, which you need to encrypt environment secrets. You need to encrypt a secret before you can create or update secrets. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `secrets` repository permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-an-environment-public-key
        /repositories/{repository_id}/environments/{environment_name}/secrets/public-key
        
        arguments:
        repository_id -- 
        environment_name -- The name of the environment
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repositories/{repository_id}/environments/{environment_name}/secrets/public-key", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Actionspublickey(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name}
    #
    def ActionsGetEnvironmentSecret(self, repository_id:int, environment_name:str, secret_name:str):
        """Gets a single environment secret without revealing its encrypted value. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets` repository permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-an-environment-secret
        /repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name}
        
        arguments:
        repository_id -- 
        environment_name -- The name of the environment
        secret_name -- secret_name parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsSecret(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/actions/permissions
    #
    def ActionsGetGithubActionsPermissionsOrganization(self, org:str):
        """Gets the GitHub Actions permissions policy for repositories and allowed actions in an organization.

You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-github-actions-permissions-for-an-organization
        /orgs/{org}/actions/permissions
        
        arguments:
        org -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/actions/permissions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsOrganizationPermissions(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/permissions
    #
    def ActionsGetGithubActionsPermissionsRepository(self, owner:str, repo:str):
        """Gets the GitHub Actions permissions policy for a repository, including whether GitHub Actions is enabled and the actions allowed to run in the repository.

You must authenticate using an access token with the `repo` scope to use this
endpoint. GitHub Apps must have the `administration` repository permission to use this API.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-github-actions-permissions-for-a-repository
        /repos/{owner}/{repo}/actions/permissions
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/permissions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsRepositoryPermissions(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/jobs/{job_id}
    #
    def ActionsGetJobForWorkflowRun(self, owner:str, repo:str, job_id:int):
        """Gets a specific job in a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-a-job-for-a-workflow-run
        /repos/{owner}/{repo}/actions/jobs/{job_id}
        
        arguments:
        owner -- 
        repo -- 
        job_id -- job_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/jobs/{job_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Job(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/actions/secrets/public-key
    #
    def ActionsGetOrgPublicKey(self, org:str):
        """Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-an-organization-public-key
        /orgs/{org}/actions/secrets/public-key
        
        arguments:
        org -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/actions/secrets/public-key", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Actionspublickey(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/actions/secrets/{secret_name}
    #
    def ActionsGetOrgSecret(self, org:str, secret_name:str):
        """Gets a single organization secret without revealing its encrypted value. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-an-organization-secret
        /orgs/{org}/actions/secrets/{secret_name}
        
        arguments:
        org -- 
        secret_name -- secret_name parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/actions/secrets/{secret_name}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsSecretForAnOrganization(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments
    #
    def ActionsGetPendingDeploymentsForRun(self, owner:str, repo:str, run_id:int):
        """Get all deployment environments for a workflow run that are waiting for protection rules to pass.

Anyone with read access to the repository can use this endpoint. If the repository is private, you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-pending-deployments-for-a-workflow-run
        /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments
        
        arguments:
        owner -- 
        repo -- 
        run_id -- The id of the workflow run.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and PendingDeployment(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/secrets/public-key
    #
    def ActionsGetRepoPublicKey(self, owner:str, repo:str):
        """Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `secrets` repository permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-a-repository-public-key
        /repos/{owner}/{repo}/actions/secrets/public-key
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/secrets/public-key", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Actionspublickey(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/secrets/{secret_name}
    #
    def ActionsGetRepoSecret(self, owner:str, repo:str, secret_name:str):
        """Gets a single repository secret without revealing its encrypted value. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets` repository permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-a-repository-secret
        /repos/{owner}/{repo}/actions/secrets/{secret_name}
        
        arguments:
        owner -- 
        repo -- 
        secret_name -- secret_name parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/secrets/{secret_name}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsSecret(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/runs/{run_id}/approvals
    #
    def ActionsGetReviewsForRun(self, owner:str, repo:str, run_id:int):
        """Anyone with read access to the repository can use this endpoint. If the repository is private, you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-the-review-history-for-a-workflow-run
        /repos/{owner}/{repo}/actions/runs/{run_id}/approvals
        
        arguments:
        owner -- 
        repo -- 
        run_id -- The id of the workflow run.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/runs/{run_id}/approvals", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and EnvironmentApprovals(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/actions/runners/{runner_id}
    #
    def ActionsGetSelfHostedRunnerForOrg(self, org:str, runner_id:int):
        """Gets a specific self-hosted runner configured in an organization.

You must authenticate using an access token with the `admin:org` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-a-self-hosted-runner-for-an-organization
        /orgs/{org}/actions/runners/{runner_id}
        
        arguments:
        org -- 
        runner_id -- Unique identifier of the self-hosted runner.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/actions/runners/{runner_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return SelfHostedRunners(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/runners/{runner_id}
    #
    def ActionsGetSelfHostedRunnerForRepo(self, owner:str, repo:str, runner_id:int):
        """Gets a specific self-hosted runner configured in a repository.

You must authenticate using an access token with the `repo` scope to use this
endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-a-self-hosted-runner-for-a-repository
        /repos/{owner}/{repo}/actions/runners/{runner_id}
        
        arguments:
        owner -- 
        repo -- 
        runner_id -- Unique identifier of the self-hosted runner.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/runners/{runner_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return SelfHostedRunners(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/actions/runner-groups/{runner_group_id}
    #
    def ActionsGetSelfHostedRunnerGroupForOrg(self, org:str, runner_group_id:int):
        """Gets a specific self-hosted runner group for an organization.
You must authenticate using an access token with the `admin:org` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-a-self-hosted-runner-group-for-an-organization
        /orgs/{org}/actions/runner-groups/{runner_group_id}
        
        arguments:
        org -- 
        runner_group_id -- Unique identifier of the self-hosted runner group.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/actions/runner-groups/{runner_group_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return RunnerGroupsOrg(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/workflows/{workflow_id}
    #
    def ActionsGetWorkflow(self, owner:str, repo:str, workflow_id:('integer', 'string')):
        """Gets a specific workflow. You can replace `workflow_id` with the workflow file name. For example, you could use `main.yaml`. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-a-workflow
        /repos/{owner}/{repo}/actions/workflows/{workflow_id}
        
        arguments:
        owner -- 
        repo -- 
        workflow_id -- The ID of the workflow. You can also pass the workflow file name as a string.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/workflows/{workflow_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Workflow(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/runs/{run_id}
    #
    def ActionsGetWorkflowRun(self, owner:str, repo:str, run_id:int,exclude_pull_requests:bool=None):
        """Gets a specific workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-a-workflow-run
        /repos/{owner}/{repo}/actions/runs/{run_id}
        
        arguments:
        owner -- 
        repo -- 
        run_id -- The id of the workflow run.
        exclude_pull_requests -- If `true` pull requests are omitted from the response (empty array).
        
        """
        
        data = {}
        if exclude_pull_requests is not None:
            data['exclude_pull_requests'] = exclude_pull_requests
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/runs/{run_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return WorkflowRun(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}
    #
    def ActionsGetWorkflowRunAttempt(self, owner:str, repo:str, run_id:int, attempt_number:int,exclude_pull_requests:bool=None):
        """Gets a specific workflow run attempt. Anyone with read access to the repository
can use this endpoint. If the repository is private you must use an access token
with the `repo` scope. GitHub Apps must have the `actions:read` permission to
use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#get-a-workflow-run-attempt
        /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}
        
        arguments:
        owner -- 
        repo -- 
        run_id -- The id of the workflow run.
        attempt_number -- The attempt number of the workflow run.
        exclude_pull_requests -- If `true` pull requests are omitted from the response (empty array).
        
        """
        
        data = {}
        if exclude_pull_requests is not None:
            data['exclude_pull_requests'] = exclude_pull_requests
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return WorkflowRun(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/artifacts
    #
    def ActionsListArtifactsForRepo(self, owner:str, repo:str,per_page=30, page=1):
        """Lists all artifacts for a repository. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-artifacts-for-a-repository
        /repos/{owner}/{repo}/actions/artifacts
        
        arguments:
        owner -- 
        repo -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/artifacts", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsListArtifactsForRepoSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repositories/{repository_id}/environments/{environment_name}/secrets
    #
    def ActionsListEnvironmentSecrets(self, repository_id:int, environment_name:str,per_page=30, page=1):
        """Lists all secrets available in an environment without revealing their encrypted values. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets` repository permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-environment-secrets
        /repositories/{repository_id}/environments/{environment_name}/secrets
        
        arguments:
        repository_id -- 
        environment_name -- The name of the environment
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repositories/{repository_id}/environments/{environment_name}/secrets", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsListEnvironmentSecretsSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/runs/{run_id}/jobs
    #
    def ActionsListJobsForWorkflowRun(self, owner:str, repo:str, run_id:int,filter='latest', per_page=30, page=1):
        """Lists jobs for a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#parameters).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-jobs-for-a-workflow-run
        /repos/{owner}/{repo}/actions/runs/{run_id}/jobs
        
        arguments:
        owner -- 
        repo -- 
        run_id -- The id of the workflow run.
        filter -- Filters jobs by their `completed_at` timestamp. Can be one of:  
\* `latest`: Returns jobs from the most recent execution of the workflow run.  
\* `all`: Returns all jobs for a workflow run, including from old executions of the workflow run.
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
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/runs/{run_id}/jobs", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsListJobsForWorkflowRunSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs
    #
    def ActionsListJobsForWorkflowRunAttempt(self, owner:str, repo:str, run_id:int, attempt_number:int,per_page=30, page=1):
        """Lists jobs for a specific workflow run attempt. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#parameters).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-jobs-for-a-workflow-run-attempt
        /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs
        
        arguments:
        owner -- 
        repo -- 
        run_id -- The id of the workflow run.
        attempt_number -- The attempt number of the workflow run.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsListJobsForWorkflowRunAttemptSuccess(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/actions/secrets
    #
    def ActionsListOrgSecrets(self, org:str,per_page=30, page=1):
        """Lists all secrets available in an organization without revealing their encrypted values. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-organization-secrets
        /orgs/{org}/actions/secrets
        
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
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/actions/secrets", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsListOrgSecretsSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories
    #
    def ActionsListRepoAccessToSelfHostedRunnerGroupInOrg(self, org:str, runner_group_id:int,page=1, per_page=30):
        """The self-hosted runner groups REST API is available with GitHub Enterprise Cloud and GitHub Enterprise Server. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."

Lists the repositories with access to a self-hosted runner group configured in an organization.

You must authenticate using an access token with the `admin:org` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-repository-access-to-a-self-hosted-runner-group-in-an-organization
        /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories
        
        arguments:
        org -- 
        runner_group_id -- Unique identifier of the self-hosted runner group.
        page -- Page number of the results to fetch.
        per_page -- Results per page (max 100)
        
        """
        
        data = {}
        if page is not None:
            data['page'] = page
        if per_page is not None:
            data['per_page'] = per_page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsListRepoAccessToSelfHostedRunnerGroupInOrgSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/secrets
    #
    def ActionsListRepoSecrets(self, owner:str, repo:str,per_page=30, page=1):
        """Lists all secrets available in a repository without revealing their encrypted values. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets` repository permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-repository-secrets
        /repos/{owner}/{repo}/actions/secrets
        
        arguments:
        owner -- 
        repo -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/secrets", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsListRepoSecretsSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/workflows
    #
    def ActionsListRepoWorkflows(self, owner:str, repo:str,per_page=30, page=1):
        """Lists the workflows in a repository. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-repository-workflows
        /repos/{owner}/{repo}/actions/workflows
        
        arguments:
        owner -- 
        repo -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/workflows", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsListRepoWorkflowsSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/actions/runners/downloads
    #
    def ActionsListRunnerApplicationsForOrg(self, org:str):
        """Lists binaries for the runner application that you can download and run.

You must authenticate using an access token with the `admin:org` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-runner-applications-for-an-organization
        /orgs/{org}/actions/runners/downloads
        
        arguments:
        org -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/actions/runners/downloads", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and RunnerApplication(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/runners/downloads
    #
    def ActionsListRunnerApplicationsForRepo(self, owner:str, repo:str):
        """Lists binaries for the runner application that you can download and run.

You must authenticate using an access token with the `repo` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-runner-applications-for-a-repository
        /repos/{owner}/{repo}/actions/runners/downloads
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/runners/downloads", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and RunnerApplication(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/actions/secrets/{secret_name}/repositories
    #
    def ActionsListSelectedReposForOrgSecret(self, org:str, secret_name:str,page=1, per_page=30):
        """Lists all repositories that have been selected when the `visibility` for repository access to a secret is set to `selected`. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-selected-repositories-for-an-organization-secret
        /orgs/{org}/actions/secrets/{secret_name}/repositories
        
        arguments:
        org -- 
        secret_name -- secret_name parameter
        page -- Page number of the results to fetch.
        per_page -- Results per page (max 100)
        
        """
        
        data = {}
        if page is not None:
            data['page'] = page
        if per_page is not None:
            data['per_page'] = per_page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/actions/secrets/{secret_name}/repositories", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsListSelectedReposForOrgSecretSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/actions/permissions/repositories
    #
    def ActionsListSelectedRepositoriesEnabledGithubActionsOrganization(self, org:str,per_page=30, page=1):
        """Lists the selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."

You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-selected-repositories-enabled-for-github-actions-in-an-organization
        /orgs/{org}/actions/permissions/repositories
        
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
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/actions/permissions/repositories", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsListSelectedRepositoriesEnabledGithubActionsOrganizationSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/actions/runner-groups
    #
    def ActionsListSelfHostedRunnerGroupsForOrg(self, org:str,per_page=30, page=1):
        """Lists all self-hosted runner groups configured in an organization and inherited from an enterprise.
You must authenticate using an access token with the `admin:org` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-self-hosted-runner-groups-for-an-organization
        /orgs/{org}/actions/runner-groups
        
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
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/actions/runner-groups", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsListSelfHostedRunnerGroupsForOrgSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/actions/runners
    #
    def ActionsListSelfHostedRunnersForOrg(self, org:str,per_page=30, page=1):
        """Lists all self-hosted runners configured in an organization.

You must authenticate using an access token with the `admin:org` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-self-hosted-runners-for-an-organization
        /orgs/{org}/actions/runners
        
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
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/actions/runners", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsListSelfHostedRunnersForOrgSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/runners
    #
    def ActionsListSelfHostedRunnersForRepo(self, owner:str, repo:str,per_page=30, page=1):
        """Lists all self-hosted runners configured in a repository. You must authenticate using an access token with the `repo` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-self-hosted-runners-for-a-repository
        /repos/{owner}/{repo}/actions/runners
        
        arguments:
        owner -- 
        repo -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/runners", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsListSelfHostedRunnersForRepoSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/actions/runner-groups/{runner_group_id}/runners
    #
    def ActionsListSelfHostedRunnersInGroupForOrg(self, org:str, runner_group_id:int,per_page=30, page=1):
        """Lists self-hosted runners that are in a specific organization group.
You must authenticate using an access token with the `admin:org` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-self-hosted-runners-in-a-group-for-an-organization
        /orgs/{org}/actions/runner-groups/{runner_group_id}/runners
        
        arguments:
        org -- 
        runner_group_id -- Unique identifier of the self-hosted runner group.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/actions/runner-groups/{runner_group_id}/runners", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsListSelfHostedRunnersInGroupForOrgSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/runs/{run_id}/artifacts
    #
    def ActionsListWorkflowRunArtifacts(self, owner:str, repo:str, run_id:int,per_page=30, page=1):
        """Lists artifacts for a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-workflow-run-artifacts
        /repos/{owner}/{repo}/actions/runs/{run_id}/artifacts
        
        arguments:
        owner -- 
        repo -- 
        run_id -- The id of the workflow run.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsListWorkflowRunArtifactsSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs
    #
    def ActionsListWorkflowRuns(self, owner:str, repo:str, workflow_id:('integer', 'string'),actor:str=None, branch:str=None, event:str=None, status=None, per_page=30, page=1, created:datetime=None, exclude_pull_requests:bool=None):
        """List all workflow runs for a workflow. You can replace `workflow_id` with the workflow file name. For example, you could use `main.yaml`. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#parameters).

Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-workflow-runs
        /repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs
        
        arguments:
        owner -- 
        repo -- 
        workflow_id -- The ID of the workflow. You can also pass the workflow file name as a string.
        actor -- Returns someone's workflow runs. Use the login for the user who created the `push` associated with the check suite or workflow run.
        branch -- Returns workflow runs associated with a branch. Use the name of the branch of the `push`.
        event -- Returns workflow run triggered by the event you specify. For example, `push`, `pull_request` or `issue`. For more information, see "[Events that trigger workflows](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/events-that-trigger-workflows)."
        status -- Returns workflow runs with the check run `status` or `conclusion` that you specify. For example, a conclusion can be `success` or a status can be `in_progress`. Only GitHub can set a status of `waiting` or `requested`. For a list of the possible `status` and `conclusion` options, see "[Create a check run](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#create-a-check-run)."
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        created -- 
        exclude_pull_requests -- If `true` pull requests are omitted from the response (empty array).
        
        """
        
        data = {}
        if actor is not None:
            data['actor'] = actor
        if branch is not None:
            data['branch'] = branch
        if event is not None:
            data['event'] = event
        if status is not None:
            data['status'] = status
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        if created is not None:
            data['created'] = created.isoformat()
        if exclude_pull_requests is not None:
            data['exclude_pull_requests'] = exclude_pull_requests
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsListWorkflowRunsSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/actions/runs
    #
    def ActionsListWorkflowRunsForRepo(self, owner:str, repo:str,actor:str=None, branch:str=None, event:str=None, status=None, per_page=30, page=1, created:datetime=None, exclude_pull_requests:bool=None):
        """Lists all workflow runs for a repository. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#parameters).

Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#list-workflow-runs-for-a-repository
        /repos/{owner}/{repo}/actions/runs
        
        arguments:
        owner -- 
        repo -- 
        actor -- Returns someone's workflow runs. Use the login for the user who created the `push` associated with the check suite or workflow run.
        branch -- Returns workflow runs associated with a branch. Use the name of the branch of the `push`.
        event -- Returns workflow run triggered by the event you specify. For example, `push`, `pull_request` or `issue`. For more information, see "[Events that trigger workflows](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/events-that-trigger-workflows)."
        status -- Returns workflow runs with the check run `status` or `conclusion` that you specify. For example, a conclusion can be `success` or a status can be `in_progress`. Only GitHub can set a status of `waiting` or `requested`. For a list of the possible `status` and `conclusion` options, see "[Create a check run](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#create-a-check-run)."
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        created -- 
        exclude_pull_requests -- If `true` pull requests are omitted from the response (empty array).
        
        """
        
        data = {}
        if actor is not None:
            data['actor'] = actor
        if branch is not None:
            data['branch'] = branch
        if event is not None:
            data['event'] = event
        if status is not None:
            data['status'] = status
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        if created is not None:
            data['created'] = created.isoformat()
        if exclude_pull_requests is not None:
            data['exclude_pull_requests'] = exclude_pull_requests
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/actions/runs", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ActionsListWorkflowRunsForRepoSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/actions/runs/{run_id}/rerun
    #
    def ActionsReRunWorkflow(self, owner:str, repo:str, run_id:int):
        """Re-runs your workflow run using its `id`. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#re-run-a-workflow
        /repos/{owner}/{repo}/actions/runs/{run_id}/rerun
        
        arguments:
        owner -- 
        repo -- 
        run_id -- The id of the workflow run.
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/actions/runs/{run_id}/rerun", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return ActionsReRunWorkflowSuccess(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id}
    #
    def ActionsRemoveRepoAccessToSelfHostedRunnerGroupInOrg(self, org:str, runner_group_id:int, repository_id:int):
        """Removes a repository from the list of selected repositories that can access a self-hosted runner group. The runner group must have `visibility` set to `selected`. For more information, see "[Create a self-hosted runner group for an organization](#create-a-self-hosted-runner-group-for-an-organization)."
You must authenticate using an access token with the `admin:org` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#remove-repository-access-to-a-self-hosted-runner-group-in-an-organization
        /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id}
        
        arguments:
        org -- 
        runner_group_id -- Unique identifier of the self-hosted runner group.
        repository_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}
    #
    def ActionsRemoveSelectedRepoFromOrgSecret(self, org:str, secret_name:str, repository_id:int):
        """Removes a repository from an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/enterprise-server@3.3/rest/reference/actions#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#remove-selected-repository-from-an-organization-secret
        /orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}
        
        arguments:
        org -- 
        secret_name -- secret_name parameter
        repository_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 409:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id}
    #
    def ActionsRemoveSelfHostedRunnerFromGroupForOrg(self, org:str, runner_group_id:int, runner_id:int):
        """Removes a self-hosted runner from a group configured in an organization. The runner is then returned to the default group.
You must authenticate using an access token with the `admin:org` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#remove-a-self-hosted-runner-from-a-group-for-an-organization
        /orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id}
        
        arguments:
        org -- 
        runner_group_id -- Unique identifier of the self-hosted runner group.
        runner_id -- Unique identifier of the self-hosted runner.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments
    #
    def ActionsReviewPendingDeploymentsForRun(self, owner:str, repo:str, run_id:int,comment:str, state:str, environment_ids:list):
        """Approve or reject pending deployments that are waiting on approval by a required reviewer.

Anyone with read access to the repository contents and deployments can use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#review-pending-deployments-for-a-workflow-run
        /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments
        
        arguments:
        owner -- 
        repo -- 
        run_id -- The id of the workflow run.
        comment -- A comment to accompany the deployment review
        state -- Whether to approve or reject deployment to the specified environments. Must be one of: `approved` or `rejected`
        environment_ids -- The list of environment ids to approve or reject
        

        """
    
        data = {
        'comment': comment,
        'state': state,
        'environment_ids': environment_ids,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return [ entry and Deployment(**entry) for entry in r.json() ]
            

        return UnexpectedResult(r)
    #
    # put /orgs/{org}/actions/permissions/selected-actions
    #
    def ActionsSetAllowedActionsOrganization(self, org:str,patterns_allowed:list, github_owned_allowed:bool):
        """Sets the actions that are allowed in an organization. To use this endpoint, the organization permission policy for `allowed_actions` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."

If the organization belongs to an enterprise that has `selected` actions set at the enterprise level, then you cannot override any of the enterprise's allowed actions settings.

To use the `patterns_allowed` setting for private repositories, the organization must belong to an enterprise. If the organization does not belong to an enterprise, then the `patterns_allowed` setting only applies to public repositories in the organization.

You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#set-allowed-actions-for-an-organization
        /orgs/{org}/actions/permissions/selected-actions
        
        arguments:
        org -- 
        patterns_allowed -- Specifies a list of string-matching patterns to allow specific action(s). Wildcards, tags, and SHAs are allowed. For example, `monalisa/octocat@*`, `monalisa/octocat@v2`, `monalisa/*`."
        github_owned_allowed -- Whether GitHub-owned actions are allowed. For example, this includes the actions in the `actions` organization.
        

        """
    
        data = {
        'patterns_allowed': patterns_allowed,
        'github_owned_allowed': github_owned_allowed,
        
        }
        

        
        r = self._session.put(f"{self._url}/orgs/{org}/actions/permissions/selected-actions", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/actions/permissions/selected-actions
    #
    def ActionsSetAllowedActionsRepository(self, owner:str, repo:str,patterns_allowed:list, github_owned_allowed:bool):
        """Sets the actions that are allowed in a repository. To use this endpoint, the repository permission policy for `allowed_actions` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for a repository](#set-github-actions-permissions-for-a-repository)."

If the repository belongs to an organization or enterprise that has `selected` actions set at the organization or enterprise levels, then you cannot override any of the allowed actions settings.

To use the `patterns_allowed` setting for private repositories, the repository must belong to an enterprise. If the repository does not belong to an enterprise, then the `patterns_allowed` setting only applies to public repositories.

You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `administration` repository permission to use this API.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#set-allowed-actions-for-a-repository
        /repos/{owner}/{repo}/actions/permissions/selected-actions
        
        arguments:
        owner -- 
        repo -- 
        patterns_allowed -- Specifies a list of string-matching patterns to allow specific action(s). Wildcards, tags, and SHAs are allowed. For example, `monalisa/octocat@*`, `monalisa/octocat@v2`, `monalisa/*`."
        github_owned_allowed -- Whether GitHub-owned actions are allowed. For example, this includes the actions in the `actions` organization.
        

        """
    
        data = {
        'patterns_allowed': patterns_allowed,
        'github_owned_allowed': github_owned_allowed,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/actions/permissions/selected-actions", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /orgs/{org}/actions/permissions
    #
    def ActionsSetGithubActionsPermissionsOrganization(self, org:str,enabled_repositories:str, allowed_actions:str=None):
        """Sets the GitHub Actions permissions policy for repositories and allowed actions in an organization.

If the organization belongs to an enterprise that has set restrictive permissions at the enterprise level, such as `allowed_actions` to `selected` actions, then you cannot override them for the organization.

You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#set-github-actions-permissions-for-an-organization
        /orgs/{org}/actions/permissions
        
        arguments:
        org -- 
        enabled_repositories -- 
        allowed_actions -- 
        

        """
    
        data = {
        'enabled_repositories': enabled_repositories,
        'allowed_actions': allowed_actions,
        
        }
        

        
        r = self._session.put(f"{self._url}/orgs/{org}/actions/permissions", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/actions/permissions
    #
    def ActionsSetGithubActionsPermissionsRepository(self, owner:str, repo:str,enabled:bool, allowed_actions:str=None):
        """Sets the GitHub Actions permissions policy for enabling GitHub Actions and allowed actions in the repository.

If the repository belongs to an organization or enterprise that has set restrictive permissions at the organization or enterprise levels, such as `allowed_actions` to `selected` actions, then you cannot override them for the repository.

You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `administration` repository permission to use this API.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#set-github-actions-permissions-for-a-repository
        /repos/{owner}/{repo}/actions/permissions
        
        arguments:
        owner -- 
        repo -- 
        enabled -- 
        allowed_actions -- 
        

        """
    
        data = {
        'enabled': enabled,
        'allowed_actions': allowed_actions,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/actions/permissions", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories
    #
    def ActionsSetRepoAccessToSelfHostedRunnerGroupInOrg(self, org:str, runner_group_id:int,selected_repository_ids:list):
        """Replaces the list of repositories that have access to a self-hosted runner group configured in an organization.
You must authenticate using an access token with the `admin:org` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#set-repository-access-to-a-self-hosted-runner-group-in-an-organization
        /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories
        
        arguments:
        org -- 
        runner_group_id -- Unique identifier of the self-hosted runner group.
        selected_repository_ids -- List of repository IDs that can access the runner group.
        

        """
    
        data = {
        'selected_repository_ids': selected_repository_ids,
        
        }
        

        
        r = self._session.put(f"{self._url}/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /orgs/{org}/actions/secrets/{secret_name}/repositories
    #
    def ActionsSetSelectedReposForOrgSecret(self, org:str, secret_name:str,selected_repository_ids:list):
        """Replaces all repositories for an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/enterprise-server@3.3/rest/reference/actions#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#set-selected-repositories-for-an-organization-secret
        /orgs/{org}/actions/secrets/{secret_name}/repositories
        
        arguments:
        org -- 
        secret_name -- secret_name parameter
        selected_repository_ids -- An array of repository ids that can access the organization secret. You can only provide a list of repository ids when the `visibility` is set to `selected`. You can add and remove individual repositories using the [Set selected repositories for an organization secret](https://docs.github.com/enterprise-server@3.3/rest/reference/actions#set-selected-repositories-for-an-organization-secret) and [Remove selected repository from an organization secret](https://docs.github.com/enterprise-server@3.3/rest/reference/actions#remove-selected-repository-from-an-organization-secret) endpoints.
        

        """
    
        data = {
        'selected_repository_ids': selected_repository_ids,
        
        }
        

        
        r = self._session.put(f"{self._url}/orgs/{org}/actions/secrets/{secret_name}/repositories", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /orgs/{org}/actions/permissions/repositories
    #
    def ActionsSetSelectedRepositoriesEnabledGithubActionsOrganization(self, org:str,selected_repository_ids:list):
        """Replaces the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."

You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#set-selected-repositories-enabled-for-github-actions-in-an-organization
        /orgs/{org}/actions/permissions/repositories
        
        arguments:
        org -- 
        selected_repository_ids -- List of repository IDs to enable for GitHub Actions.
        

        """
    
        data = {
        'selected_repository_ids': selected_repository_ids,
        
        }
        

        
        r = self._session.put(f"{self._url}/orgs/{org}/actions/permissions/repositories", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /orgs/{org}/actions/runner-groups/{runner_group_id}/runners
    #
    def ActionsSetSelfHostedRunnersInGroupForOrg(self, org:str, runner_group_id:int,runners:list):
        """Replaces the list of self-hosted runners that are part of an organization runner group.
You must authenticate using an access token with the `admin:org` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#set-self-hosted-runners-in-a-group-for-an-organization
        /orgs/{org}/actions/runner-groups/{runner_group_id}/runners
        
        arguments:
        org -- 
        runner_group_id -- Unique identifier of the self-hosted runner group.
        runners -- List of runner IDs to add to the runner group.
        

        """
    
        data = {
        'runners': runners,
        
        }
        

        
        r = self._session.put(f"{self._url}/orgs/{org}/actions/runner-groups/{runner_group_id}/runners", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # patch /orgs/{org}/actions/runner-groups/{runner_group_id}
    #
    def ActionsUpdateSelfHostedRunnerGroupForOrg(self, org:str, runner_group_id:int,name:str, visibility:str=None, allows_public_repositories:bool=False):
        """Updates the `name` and `visibility` of a self-hosted runner group in an organization.
You must authenticate using an access token with the `admin:org` scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/actions#update-a-self-hosted-runner-group-for-an-organization
        /orgs/{org}/actions/runner-groups/{runner_group_id}
        
        arguments:
        org -- 
        runner_group_id -- Unique identifier of the self-hosted runner group.
        name -- Name of the runner group.
        visibility -- Visibility of a runner group. You can select all repositories, select individual repositories, or all private repositories. Can be one of: `all`, `selected`, or `private`.
        allows_public_repositories -- Whether the runner group can be used by `public` repositories.
        

        """
    
        data = {
        'name': name,
        'visibility': visibility,
        'allows_public_repositories': allows_public_repositories,
        
        }
        

        
        r = self._session.patch(f"{self._url}/orgs/{org}/actions/runner-groups/{runner_group_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return RunnerGroupsOrg(**r.json())
            

        return UnexpectedResult(r)
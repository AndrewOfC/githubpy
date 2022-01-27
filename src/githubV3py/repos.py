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

class Repos(object):


    #
    # patch /user/repository_invitations/{invitation_id}
    #
    def ReposAcceptInvitationForAuthenticatedUser(self, invitation_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#accept-a-repository-invitation
        /user/repository_invitations/{invitation_id}
        
        arguments:
        invitation_id -- invitation_id parameter
        

        """
    
        data = {
        
        }
        

        
        r = self._session.patch(f"{self._url}/user/repository_invitations/{invitation_id}", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 409:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps
    #
    def ReposAddAppAccessRestrictions(self, owner:str, repo:str, branch:str,object:object):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Grants the specified apps push access for this branch. Only installed GitHub Apps with `write` access to the `contents` permission can be added as authorized actors on a protected branch.

| Type    | Description                                                                                                                                                |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `array` | The GitHub Apps that have push access to this branch. Use the app's `slug`. **Note**: The list of users, apps, and teams in total is limited to 100 items. |
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#add-app-access-restrictions
        /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        object -- 
        

        """
    
        data = {
        'object': object,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return [ entry and Integration(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/collaborators/{username}
    #
    def ReposAddCollaborator(self, owner:str, repo:str, username:str,permission:str='push', permissions:str=None):
        """This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.

For more information on permission levels, see "[Repository permission levels for an organization](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)". There are restrictions on which permissions can be granted to organization members when an organization base role is in place. In this case, the permission being given must be equal to or higher than the org base permission. Otherwise, the request will fail with:

```
Cannot assign {member} permission of {role name}
```

Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#http-verbs)."

The invitee will receive a notification that they have been invited to the repository, which they must accept or decline. They may do this via the notifications page, the email they receive, or by using the [repository invitations API endpoints](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#invitations).

**Rate limits**

You are limited to sending 50 invitations to a repository per 24 hour period. Note there is no limit if you are inviting organization members to an organization repository.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#add-a-repository-collaborator
        /repos/{owner}/{repo}/collaborators/{username}
        
        arguments:
        owner -- 
        repo -- 
        username -- 
        permission -- The permission to grant the collaborator. **Only valid on organization-owned repositories.** Can be one of:  
\* `pull` - can pull, but not push to or administer this repository.  
\* `push` - can pull and push, but not administer this repository.  
\* `admin` - can pull, push and administer this repository.  
\* `maintain` - Recommended for project managers who need to manage the repository without access to sensitive or destructive actions.  
\* `triage` - Recommended for contributors who need to proactively manage issues and pull requests without write access.
        permissions -- 
        

        """
    
        data = {
        'permission': permission,
        'permissions': permissions,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/collaborators/{username}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return RepositoryInvitation(**r.json())
            
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts
    #
    def ReposAddStatusCheckContexts(self, owner:str, repo:str, branch:str,object:object):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#add-status-check-contexts
        /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        object -- 
        

        """
    
        data = {
        'object': object,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return [ entry for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams
    #
    def ReposAddTeamAccessRestrictions(self, owner:str, repo:str, branch:str,object:object):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Grants the specified teams push access for this branch. You can also give push access to child teams.

| Type    | Description                                                                                                                                |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `array` | The teams that can have push access. Use the team's `slug`. **Note**: The list of users, apps, and teams in total is limited to 100 items. |
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#add-team-access-restrictions
        /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        object -- 
        

        """
    
        data = {
        'object': object,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return [ entry and Team(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users
    #
    def ReposAddUserAccessRestrictions(self, owner:str, repo:str, branch:str,object:object):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Grants the specified people push access for this branch.

| Type    | Description                                                                                                                   |
| ------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `array` | Usernames for people who can have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. |
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#add-user-access-restrictions
        /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        object -- 
        

        """
    
        data = {
        'object': object,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return [ entry and SimpleUser(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/collaborators/{username}
    #
    def ReposCheckCollaborator(self, owner:str, repo:str, username:str):
        """For organization-owned repositories, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners.

Team members will include the members of child teams.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#check-if-a-user-is-a-repository-collaborator
        /repos/{owner}/{repo}/collaborators/{username}
        
        arguments:
        owner -- 
        repo -- 
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/collaborators/{username}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/compare/{basehead}
    #
    def ReposCompareCommits(self, owner:str, repo:str, basehead:str,page=1, per_page=30):
        """The `basehead` param is comprised of two parts: `base` and `head`. Both must be branch names in `repo`. To compare branches across other repositories in the same network as `repo`, use the format `<USERNAME>:branch`.

The response from the API is equivalent to running the `git log base..head` command; however, commits are returned in chronological order. Pass the appropriate [media type](https://docs.github.com/enterprise-server@3.3/rest/overview/media-types/#commits-commit-comparison-and-pull-requests) to fetch diff and patch formats.

The response also includes details on the files that were changed between the two commits. This includes the status of the change (for example, if a file was added, removed, modified, or renamed), and details of the change itself. For example, files with a `renamed` status have a `previous_filename` field showing the previous filename of the file, and files with a `modified` status have a `patch` field showing the changes made to the file.

**Working with large comparisons**

To process a response with a large number of commits, you can use (`per_page` or `page`) to paginate the results. When using paging, the list of changed files is only returned with page 1, but includes all changed files for the entire comparison. For more information on working with pagination, see "[Traversing with pagination](/rest/guides/traversing-with-pagination)."

When calling this API without any paging parameters (`per_page` or `page`), the returned list is limited to 250 commits and the last commit in the list is the most recent of the entire comparison. When a paging parameter is specified, the first commit in the returned list of each page is the earliest.

**Signature verification object**

The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:

| Name | Type | Description |
| ---- | ---- | ----------- |
| `verified` | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified. |
| `reason` | `string` | The reason for verified value. Possible values and their meanings are enumerated in table below. |
| `signature` | `string` | The signature that was extracted from the commit. |
| `payload` | `string` | The value that was signed. |

These are the possible values for `reason` in the `verification` object:

| Value | Description |
| ----- | ----------- |
| `expired_key` | The key that made the signature is expired. |
| `not_signing_key` | The "signing" flag is not among the usage flags in the GPG key that made the signature. |
| `gpgverify_error` | There was an error communicating with the signature verification service. |
| `gpgverify_unavailable` | The signature verification service is currently unavailable. |
| `unsigned` | The object does not include a signature. |
| `unknown_signature_type` | A non-PGP signature was found in the commit. |
| `no_user` | No user was associated with the `committer` email address in the commit. |
| `unverified_email` | The `committer` email address in the commit was associated with a user, but the email address is not verified on her/his account. |
| `bad_email` | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature. |
| `unknown_key` | The key that made the signature has not been registered with any user's account. |
| `malformed_signature` | There was an error parsing the signature. |
| `invalid` | The signature could not be cryptographically verified using the key whose key-id was found in the signature. |
| `valid` | None of the above errors applied, so the signature is considered to be verified. |
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#compare-two-commits
        /repos/{owner}/{repo}/compare/{basehead}
        
        arguments:
        owner -- 
        repo -- 
        basehead -- The base branch and head branch to compare. This parameter expects the format `{base}...{head}`.
        page -- Page number of the results to fetch.
        per_page -- Results per page (max 100)
        
        """
        
        data = {}
        if page is not None:
            data['page'] = page
        if per_page is not None:
            data['per_page'] = per_page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/compare/{basehead}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return CommitComparison(**r.json())
            
        if r.status_code == 500:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/autolinks
    #
    def ReposCreateAutolink(self, owner:str, repo:str,url_template:str, key_prefix:str):
        """Users with admin access to the repository can create an autolink.
        
        https://docs.github.com/enterprise-server@3.3/v3/repos#create-an-autolink
        /repos/{owner}/{repo}/autolinks
        
        arguments:
        owner -- 
        repo -- 
        url_template -- The URL must contain <num> for the reference number.
        key_prefix -- The prefix appended by a number will generate a link any time it is found in an issue, pull request, or commit.
        

        """
    
        data = {
        'url_template': url_template,
        'key_prefix': key_prefix,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/autolinks", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return AutolinkReference(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/commits/{commit_sha}/comments
    #
    def ReposCreateCommitComment(self, owner:str, repo:str, commit_sha:str,body:str, path:str=None, position:int=None, line:int=None):
        """Create a comment for a commit using its `:commit_sha`.

This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-a-commit-comment
        /repos/{owner}/{repo}/commits/{commit_sha}/comments
        
        arguments:
        owner -- 
        repo -- 
        commit_sha -- commit_sha parameter
        body -- The contents of the comment.
        path -- Relative path of the file to comment on.
        position -- Line index in the diff to comment on.
        line -- **Deprecated**. Use **position** parameter instead. Line number in the file to comment on.
        

        """
    
        data = {
        'body': body,
        'path': path,
        'position': position,
        'line': line,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/commits/{commit_sha}/comments", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return CommitComment(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures
    #
    def ReposCreateCommitSignatureProtection(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

When authenticated with admin or owner permissions to the repository, you can use this endpoint to require signed commits on a branch. You must enable branch protection to require signed commits.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-commit-signature-protection
        /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return ProtectedBranchAdminEnforced(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/statuses/{sha}
    #
    def ReposCreateCommitStatus(self, owner:str, repo:str, sha:str,state:str, target_url:str=None, description:str=None, context:str='default'):
        """Users with push access in a repository can create commit statuses for a given SHA.

Note: there is a limit of 1000 statuses per `sha` and `context` within a repository. Attempts to create more than 1000 statuses will result in a validation error.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-a-commit-status
        /repos/{owner}/{repo}/statuses/{sha}
        
        arguments:
        owner -- 
        repo -- 
        sha -- 
        state -- The state of the status. Can be one of `error`, `failure`, `pending`, or `success`.
        target_url -- The target URL to associate with this status. This URL will be linked from the GitHub UI to allow users to easily see the source of the status.  
For example, if your continuous integration system is posting build status, you would want to provide the deep link for the build output for this specific SHA:  
`http://ci.example.com/user/repo/build/sha`
        description -- A short description of the status.
        context -- A string label to differentiate this status from the status of other systems. This field is case-insensitive.
        

        """
    
        data = {
        'state': state,
        'target_url': target_url,
        'description': description,
        'context': context,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/statuses/{sha}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Status(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/keys
    #
    def ReposCreateDeployKey(self, owner:str, repo:str,key:str, title:str=None, read_only:bool=None):
        """You can create a read-only deploy key.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-a-deploy-key
        /repos/{owner}/{repo}/keys
        
        arguments:
        owner -- 
        repo -- 
        key -- The contents of the key.
        title -- A name for the key.
        read_only -- If `true`, the key will only be able to read repository contents. Otherwise, the key will be able to read and write.  
  
Deploy keys with write access can perform the same actions as an organization member with admin access, or a collaborator on a personal repository. For more information, see "[Repository permission levels for an organization](https://help.github.com/articles/repository-permission-levels-for-an-organization/)" and "[Permission levels for a user account repository](https://help.github.com/articles/permission-levels-for-a-user-account-repository/)."
        

        """
    
        data = {
        'key': key,
        'title': title,
        'read_only': read_only,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/keys", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return DeployKey(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/deployments
    #
    def ReposCreateDeployment(self, owner:str, repo:str,ref:str, task:str='deploy', auto_merge:bool=True, required_contexts:list=[], payload=None, environment:str='production', description:str='""', transient_environment:bool=False, production_environment:bool=None):
        """Deployments offer a few configurable parameters with certain defaults.

The `ref` parameter can be any named branch, tag, or SHA. At GitHub Enterprise Server we often deploy branches and verify them
before we merge a pull request.

The `environment` parameter allows deployments to be issued to different runtime environments. Teams often have
multiple environments for verifying their applications, such as `production`, `staging`, and `qa`. This parameter
makes it easier to track which environments have requested deployments. The default environment is `production`.

The `auto_merge` parameter is used to ensure that the requested ref is not behind the repository's default branch. If
the ref _is_ behind the default branch for the repository, we will attempt to merge it for you. If the merge succeeds,
the API will return a successful merge commit. If merge conflicts prevent the merge from succeeding, the API will
return a failure response.

By default, [commit statuses](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#statuses) for every submitted context must be in a `success`
state. The `required_contexts` parameter allows you to specify a subset of contexts that must be `success`, or to
specify contexts that have not yet been submitted. You are not required to use commit statuses to deploy. If you do
not require any contexts or create any commit statuses, the deployment will always succeed.

The `payload` parameter is available for any extra information that a deployment system might need. It is a JSON text
field that will be passed on when a deployment event is dispatched.

The `task` parameter is used by the deployment system to allow different execution paths. In the web world this might
be `deploy:migrations` to run schema changes on the system. In the compiled world this could be a flag to compile an
application with debugging enabled.

Users with `repo` or `repo_deployment` scopes can create a deployment for a given ref.

#### Merged branch response
You will see this response when GitHub automatically merges the base branch into the topic branch instead of creating
a deployment. This auto-merge happens when:
*   Auto-merge option is enabled in the repository
*   Topic branch does not include the latest changes on the base branch, which is `master` in the response example
*   There are no merge conflicts

If there are no new commits in the base branch, a new request to create a deployment should give a successful
response.

#### Merge conflict response
This error happens when the `auto_merge` option is enabled and when the default branch (in this case `master`), can't
be merged into the branch that's being deployed (in this case `topic-branch`), due to merge conflicts.

#### Failed commit status checks
This error happens when the `required_contexts` parameter indicates that one or more contexts need to have a `success`
status for the commit to be deployed, but one or more of the required contexts do not have a state of `success`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-a-deployment
        /repos/{owner}/{repo}/deployments
        
        arguments:
        owner -- 
        repo -- 
        ref -- The ref to deploy. This can be a branch, tag, or SHA.
        task -- Specifies a task to execute (e.g., `deploy` or `deploy:migrations`).
        auto_merge -- Attempts to automatically merge the default branch into the requested ref, if it's behind the default branch.
        required_contexts -- The [status](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#statuses) contexts to verify against commit status checks. If you omit this parameter, GitHub verifies all unique contexts before creating a deployment. To bypass checking entirely, pass an empty array. Defaults to all unique contexts.
        payload -- 
        environment -- Name for the target deployment environment (e.g., `production`, `staging`, `qa`).
        description -- Short description of the deployment.
        transient_environment -- Specifies if the given environment is specific to the deployment and will no longer exist at some point in the future. Default: `false`
        production_environment -- Specifies if the given environment is one that end-users directly interact with. Default: `true` when `environment` is `production` and `false` otherwise.
        

        """
    
        data = {
        'ref': ref,
        'task': task,
        'auto_merge': auto_merge,
        'required_contexts': required_contexts,
        'payload': payload,
        'environment': environment,
        'description': description,
        'transient_environment': transient_environment,
        'production_environment': production_environment,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/deployments", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Deployment(**r.json())
            
        if r.status_code == 202:
            return ReposCreateDeployment202(**r.json())
            
        if r.status_code == 409:
            return HttpResponse(r)
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/deployments/{deployment_id}/statuses
    #
    def ReposCreateDeploymentStatus(self, owner:str, repo:str, deployment_id:int,state:str, target_url:str='""', log_url:str='""', description:str='""', environment:str=None, environment_url:str='""', auto_inactive:bool=None):
        """Users with `push` access can create deployment statuses for a given deployment.

GitHub Apps require `read & write` access to "Deployments" and `read-only` access to "Repo contents" (for private repos). OAuth Apps require the `repo_deployment` scope.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-a-deployment-status
        /repos/{owner}/{repo}/deployments/{deployment_id}/statuses
        
        arguments:
        owner -- 
        repo -- 
        deployment_id -- deployment_id parameter
        state -- The state of the status. Can be one of `error`, `failure`, `inactive`, `in_progress`, `queued`, `pending`, or `success`. When you set a transient deployment to `inactive`, the deployment will be shown as `destroyed` in GitHub.
        target_url -- The target URL to associate with this status. This URL should contain output to keep the user updated while the task is running or serve as historical information for what happened in the deployment. **Note:** It's recommended to use the `log_url` parameter, which replaces `target_url`.
        log_url -- The full URL of the deployment's output. This parameter replaces `target_url`. We will continue to accept `target_url` to support legacy uses, but we recommend replacing `target_url` with `log_url`. Setting `log_url` will automatically set `target_url` to the same value. Default: `""`
        description -- A short description of the status. The maximum description length is 140 characters.
        environment -- Name for the target deployment environment, which can be changed when setting a deploy status. For example, `production`, `staging`, or `qa`.
        environment_url -- Sets the URL for accessing your environment. Default: `""`
        auto_inactive -- Adds a new `inactive` status to all prior non-transient, non-production environment deployments with the same repository and `environment` name as the created status's deployment. An `inactive` status is only added to deployments that had a `success` state. Default: `true`
        

        """
    
        data = {
        'state': state,
        'target_url': target_url,
        'log_url': log_url,
        'description': description,
        'environment': environment,
        'environment_url': environment_url,
        'auto_inactive': auto_inactive,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/deployments/{deployment_id}/statuses", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return DeploymentStatus(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/dispatches
    #
    def ReposCreateDispatchEvent(self, owner:str, repo:str,event_type:str, client_payload:object=None):
        """You can use this endpoint to trigger a webhook event called `repository_dispatch` when you want activity that happens outside of GitHub Enterprise Server to trigger a GitHub Actions workflow or GitHub App webhook. You must configure your GitHub Actions workflow or GitHub App to run when the `repository_dispatch` event occurs. For an example `repository_dispatch` webhook payload, see "[RepositoryDispatchEvent](https://docs.github.com/enterprise-server@3.3/webhooks/event-payloads/#repository_dispatch)."

The `client_payload` parameter is available for any extra information that your workflow might need. This parameter is a JSON payload that will be passed on when the webhook event is dispatched. For example, the `client_payload` can include a message that a user would like to send using a GitHub Actions workflow. Or the `client_payload` can be used as a test to debug your workflow.

This endpoint requires write access to the repository by providing either:

  - Personal access tokens with `repo` scope. For more information, see "[Creating a personal access token for the command line](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line)" in the GitHub Help documentation.
  - GitHub Apps with both `metadata:read` and `contents:read&write` permissions.

This input example shows how you can use the `client_payload` as a test to debug your workflow.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-a-repository-dispatch-event
        /repos/{owner}/{repo}/dispatches
        
        arguments:
        owner -- 
        repo -- 
        event_type -- A custom webhook event name.
        client_payload -- JSON payload with extra information about the webhook event that your action or worklow may use.
        

        """
    
        data = {
        'event_type': event_type,
        'client_payload': client_payload,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/dispatches", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /user/repos
    #
    def ReposCreateForAuthenticatedUser(self, name:str, description:str=None, homepage:str=None, private:bool=False, has_issues:bool=True, has_projects:bool=True, has_wiki:bool=True, team_id:int=None, auto_init:bool=False, gitignore_template:str=None, license_template:str=None, allow_squash_merge:bool=True, allow_merge_commit:bool=True, allow_rebase_merge:bool=True, allow_auto_merge:bool=False, delete_branch_on_merge:bool=False, has_downloads:bool=True, is_template:bool=False):
        """Creates a new repository for the authenticated user.

**OAuth scope requirements**

When using [OAuth](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:

*   `public_repo` scope or `repo` scope to create a public repository. Note: For GitHub AE, use `repo` scope to create an internal repository.
*   `repo` scope to create a private repository.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-a-repository-for-the-authenticated-user
        /user/repos
        
        arguments:
        name -- The name of the repository.
        description -- A short description of the repository.
        homepage -- A URL with more information about the repository.
        private -- Whether the repository is private.
        has_issues -- Whether issues are enabled.
        has_projects -- Whether projects are enabled.
        has_wiki -- Whether the wiki is enabled.
        team_id -- The id of the team that will be granted access to this repository. This is only valid when creating a repository in an organization.
        auto_init -- Whether the repository is initialized with a minimal README.
        gitignore_template -- The desired language or platform to apply to the .gitignore.
        license_template -- The license keyword of the open source license for this repository.
        allow_squash_merge -- Whether to allow squash merges for pull requests.
        allow_merge_commit -- Whether to allow merge commits for pull requests.
        allow_rebase_merge -- Whether to allow rebase merges for pull requests.
        allow_auto_merge -- Whether to allow Auto-merge to be used on pull requests.
        delete_branch_on_merge -- Whether to delete head branches when pull requests are merged
        has_downloads -- Whether downloads are enabled.
        is_template -- Whether this repository acts as a template that can be used to generate new repositories.
        

        """
    
        data = {
        'name': name,
        'description': description,
        'homepage': homepage,
        'private': private,
        'has_issues': has_issues,
        'has_projects': has_projects,
        'has_wiki': has_wiki,
        'team_id': team_id,
        'auto_init': auto_init,
        'gitignore_template': gitignore_template,
        'license_template': license_template,
        'allow_squash_merge': allow_squash_merge,
        'allow_merge_commit': allow_merge_commit,
        'allow_rebase_merge': allow_rebase_merge,
        'allow_auto_merge': allow_auto_merge,
        'delete_branch_on_merge': delete_branch_on_merge,
        'has_downloads': has_downloads,
        'is_template': is_template,
        
        }
        

        
        r = self._session.post(f"{self._url}/user/repos", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Repository(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 400:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/forks
    #
    def ReposCreateFork(self, owner:str, repo:str,organization:str=None):
        """Create a fork for the authenticated user.

**Note**: Forking a Repository happens asynchronously. You may have to wait a short period of time before you can access the git objects. If this takes longer than 5 minutes, be sure to contact [GitHub Enterprise Server Support](https://support.github.com/contact?tags=dotcom-rest-api).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-a-fork
        /repos/{owner}/{repo}/forks
        
        arguments:
        owner -- 
        repo -- 
        organization -- Optional parameter to specify the organization name if forking into an organization.
        

        """
    
        data = {
        'organization': organization,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/forks", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 202:
            return FullRepository(**r.json())
            
        if r.status_code == 400:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /orgs/{org}/repos
    #
    def ReposCreateInOrg(self, org:str,name:str, description:str=None, homepage:str=None, private:bool=False, visibility:str=None, has_issues:bool=True, has_projects:bool=True, has_wiki:bool=True, is_template:bool=False, team_id:int=None, auto_init:bool=False, gitignore_template:str=None, license_template:str=None, allow_squash_merge:bool=True, allow_merge_commit:bool=True, allow_rebase_merge:bool=True, allow_auto_merge:bool=False, delete_branch_on_merge:bool=False):
        """Creates a new repository in the specified organization. The authenticated user must be a member of the organization.

**OAuth scope requirements**

When using [OAuth](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:

*   `public_repo` scope or `repo` scope to create a public repository. Note: For GitHub AE, use `repo` scope to create an internal repository.
*   `repo` scope to create a private repository
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-an-organization-repository
        /orgs/{org}/repos
        
        arguments:
        org -- 
        name -- The name of the repository.
        description -- A short description of the repository.
        homepage -- A URL with more information about the repository.
        private -- Whether the repository is private.
        visibility -- Can be `public` or `private`. If your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+, `visibility` can also be `internal`. Note: For GitHub Enterprise Server and GitHub AE, this endpoint will only list repositories available to all users on the enterprise. For more information, see "[Creating an internal repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/about-repository-visibility#about-internal-repositories)" in the GitHub Help documentation.
        has_issues -- Either `true` to enable issues for this repository or `false` to disable them.
        has_projects -- Either `true` to enable projects for this repository or `false` to disable them. **Note:** If you're creating a repository in an organization that has disabled repository projects, the default is `false`, and if you pass `true`, the API returns an error.
        has_wiki -- Either `true` to enable the wiki for this repository or `false` to disable it.
        is_template -- Either `true` to make this repo available as a template repository or `false` to prevent it.
        team_id -- The id of the team that will be granted access to this repository. This is only valid when creating a repository in an organization.
        auto_init -- Pass `true` to create an initial commit with empty README.
        gitignore_template -- Desired language or platform [.gitignore template](https://github.com/github/gitignore) to apply. Use the name of the template without the extension. For example, "Haskell".
        license_template -- Choose an [open source license template](https://choosealicense.com/) that best suits your needs, and then use the [license keyword](https://help.github.com/articles/licensing-a-repository/#searching-github-by-license-type) as the `license_template` string. For example, "mit" or "mpl-2.0".
        allow_squash_merge -- Either `true` to allow squash-merging pull requests, or `false` to prevent squash-merging.
        allow_merge_commit -- Either `true` to allow merging pull requests with a merge commit, or `false` to prevent merging pull requests with merge commits.
        allow_rebase_merge -- Either `true` to allow rebase-merging pull requests, or `false` to prevent rebase-merging.
        allow_auto_merge -- Either `true` to allow auto-merge on pull requests, or `false` to disallow auto-merge.
        delete_branch_on_merge -- Either `true` to allow automatically deleting head branches when pull requests are merged, or `false` to prevent automatic deletion.
        

        """
    
        data = {
        'name': name,
        'description': description,
        'homepage': homepage,
        'private': private,
        'visibility': visibility,
        'has_issues': has_issues,
        'has_projects': has_projects,
        'has_wiki': has_wiki,
        'is_template': is_template,
        'team_id': team_id,
        'auto_init': auto_init,
        'gitignore_template': gitignore_template,
        'license_template': license_template,
        'allow_squash_merge': allow_squash_merge,
        'allow_merge_commit': allow_merge_commit,
        'allow_rebase_merge': allow_rebase_merge,
        'allow_auto_merge': allow_auto_merge,
        'delete_branch_on_merge': delete_branch_on_merge,
        
        }
        

        
        r = self._session.post(f"{self._url}/orgs/{org}/repos", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Repository(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/environments/{environment_name}
    #
    def ReposCreateOrUpdateEnvironment(self, owner:str, repo:str, environment_name:str,wait_timer:int=None, reviewers:list=[], deployment_branch_policy:dict=None):
        """Create or update an environment with protection rules, such as required reviewers. For more information about environment protection rules, see "[Environments](/actions/reference/environments#environment-protection-rules)."

**Note:** Although you can use this operation to specify that only branches that match specified name patterns can deploy to this environment, you must use the UI to set the name patterns. For more information, see "[Environments](/actions/reference/environments#deployment-branches)."

**Note:** To create or update secrets for an environment, see "[Secrets](/rest/reference/actions#secrets)."

You must authenticate using an access token with the repo scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-or-update-an-environment
        /repos/{owner}/{repo}/environments/{environment_name}
        
        arguments:
        owner -- 
        repo -- 
        environment_name -- The name of the environment
        wait_timer -- 
        reviewers -- The people or teams that may review jobs that reference the environment. You can list up to six users or teams as reviewers. The reviewers must have at least read access to the repository. Only one of the required reviewers needs to approve the job for it to proceed.
        deployment_branch_policy -- 
        

        """
    
        data = {
        'wait_timer': wait_timer,
        'reviewers': reviewers,
        'deployment_branch_policy': deployment_branch_policy,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/environments/{environment_name}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Environment(**r.json())
            
        if r.status_code == 422:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/contents/{path}
    #
    def ReposCreateOrUpdateFileContents(self, owner:str, repo:str, path:str,content:str, message:str, sha:str=None, branch:str=None, committer:dict=None, author:dict=None):
        """Creates a new file or replaces an existing file in a repository.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-or-update-file-contents
        /repos/{owner}/{repo}/contents/{path}
        
        arguments:
        owner -- 
        repo -- 
        path -- path parameter
        content -- The new file content, using Base64 encoding.
        message -- The commit message.
        sha -- **Required if you are updating a file**. The blob SHA of the file being replaced.
        branch -- The branch name. Default: the repository’s default branch (usually `master`)
        committer -- The person that committed the file. Default: the authenticated user.
        author -- The author of the file. Default: The `committer` or the authenticated user if you omit `committer`.
        

        """
    
        data = {
        'content': content,
        'message': message,
        'sha': sha,
        'branch': branch,
        'committer': committer,
        'author': author,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/contents/{path}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return FileCommit(**r.json())
            
        if r.status_code == 201:
            return FileCommit(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 409:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/pages
    #
    def ReposCreatePagesSite(self, owner:str, repo:str,source:dict):
        """Configures a GitHub Enterprise Server Pages site. For more information, see "[About GitHub Pages](/github/working-with-github-pages/about-github-pages)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-a-github-pages-site
        /repos/{owner}/{repo}/pages
        
        arguments:
        owner -- 
        repo -- 
        source -- The source branch and directory used to publish your Pages site.
        

        """
    
        data = {
        'source': source,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/pages", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return GithubPages(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 409:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/releases
    #
    def ReposCreateRelease(self, owner:str, repo:str,tag_name:str, target_commitish:str=None, name:str=None, body:str=None, draft:bool=False, prerelease:bool=False, generate_release_notes:bool=False):
        """Users with push access to the repository can create a release.

This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-a-release
        /repos/{owner}/{repo}/releases
        
        arguments:
        owner -- 
        repo -- 
        tag_name -- The name of the tag.
        target_commitish -- Specifies the commitish value that determines where the Git tag is created from. Can be any branch or commit SHA. Unused if the Git tag already exists. Default: the repository's default branch (usually `master`).
        name -- The name of the release.
        body -- Text describing the contents of the tag.
        draft -- `true` to create a draft (unpublished) release, `false` to create a published one.
        prerelease -- `true` to identify the release as a prerelease. `false` to identify the release as a full release.
        generate_release_notes -- Whether to automatically generate the name and body for this release. If `name` is specified, the specified name will be used; otherwise, a name will be automatically generated. If `body` is specified, the body will be pre-pended to the automatically generated notes.
        

        """
    
        data = {
        'tag_name': tag_name,
        'target_commitish': target_commitish,
        'name': name,
        'body': body,
        'draft': draft,
        'prerelease': prerelease,
        'generate_release_notes': generate_release_notes,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/releases", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Release(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{template_owner}/{template_repo}/generate
    #
    def ReposCreateUsingTemplate(self, template_owner:str, template_repo:str,name:str, owner:str=None, description:str=None, include_all_branches:bool=False, private:bool=False):
        """Creates a new repository using a repository template. Use the `template_owner` and `template_repo` route parameters to specify the repository to use as the template. The authenticated user must own or be a member of an organization that owns the repository. To check if a repository is available to use as a template, get the repository's information using the [Get a repository](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-a-repository) endpoint and check that the `is_template` key is `true`.

**OAuth scope requirements**

When using [OAuth](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:

*   `public_repo` scope or `repo` scope to create a public repository. Note: For GitHub AE, use `repo` scope to create an internal repository.
*   `repo` scope to create a private repository
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-a-repository-using-a-template
        /repos/{template_owner}/{template_repo}/generate
        
        arguments:
        template_owner -- 
        template_repo -- 
        name -- The name of the new repository.
        owner -- The organization or person who will own the new repository. To create a new repository in an organization, the authenticated user must be a member of the specified organization.
        description -- A short description of the new repository.
        include_all_branches -- Set to `true` to include the directory structure and files from all branches in the template repository, and not just the default branch. Default: `false`.
        private -- Either `true` to create a new private repository or `false` to create a new public one.
        

        """
    
        data = {
        'name': name,
        'owner': owner,
        'description': description,
        'include_all_branches': include_all_branches,
        'private': private,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{template_owner}/{template_repo}/generate", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Repository(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/hooks
    #
    def ReposCreateWebhook(self, owner:str, repo:str,name:str=None, config:dict=None, events:list=['push'], active:bool=True):
        """Repositories can have multiple webhooks installed. Each webhook should have a unique `config`. Multiple webhooks can
share the same `config` as long as those webhooks do not have any `events` that overlap.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-a-repository-webhook
        /repos/{owner}/{repo}/hooks
        
        arguments:
        owner -- 
        repo -- 
        name -- Use `web` to create a webhook. Default: `web`. This parameter only accepts the value `web`.
        config -- Key/value pairs to provide settings for this webhook. [These are defined below](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-hook-config-params).
        events -- Determines what [events](https://docs.github.com/enterprise-server@3.3/webhooks/event-payloads) the hook is triggered for.
        active -- Determines if notifications are sent when the webhook is triggered. Set to `true` to send notifications.
        

        """
    
        data = {
        'name': name,
        'config': config,
        'events': events,
        'active': active,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/hooks", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Webhook(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /user/repository_invitations/{invitation_id}
    #
    def ReposDeclineInvitationForAuthenticatedUser(self, invitation_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#decline-a-repository-invitation
        /user/repository_invitations/{invitation_id}
        
        arguments:
        invitation_id -- invitation_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/user/repository_invitations/{invitation_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 409:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}
    #
    def ReposDelete(self, owner:str, repo:str):
        """Deleting a repository requires admin access. If OAuth is used, the `delete_repo` scope is required.

If an organization owner has configured the organization to prevent members from deleting organization-owned
repositories, you will get a `403 Forbidden` response.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#delete-a-repository
        /repos/{owner}/{repo}
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return ReposDeleteForbidden(**r.json())
            
        if r.status_code == 307:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/branches/{branch}/protection/restrictions
    #
    def ReposDeleteAccessRestrictions(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Disables the ability to restrict who can push to this branch.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#delete-access-restrictions
        /repos/{owner}/{repo}/branches/{branch}/protection/restrictions
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins
    #
    def ReposDeleteAdminBranchProtection(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Removing admin enforcement requires admin or owner permissions to the repository and branch protection to be enabled.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#delete-admin-branch-protection
        /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/environments/{environment_name}
    #
    def ReposDeleteAnEnvironment(self, owner:str, repo:str, environment_name:str):
        """You must authenticate using an access token with the repo scope to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#delete-an-environment
        /repos/{owner}/{repo}/environments/{environment_name}
        
        arguments:
        owner -- 
        repo -- 
        environment_name -- The name of the environment
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/environments/{environment_name}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/autolinks/{autolink_id}
    #
    def ReposDeleteAutolink(self, owner:str, repo:str, autolink_id:int):
        """This deletes a single autolink reference by ID that was configured for the given repository.

Information about autolinks are only available to repository administrators.
        
        https://docs.github.com/enterprise-server@3.3/v3/repos#delete-autolink
        /repos/{owner}/{repo}/autolinks/{autolink_id}
        
        arguments:
        owner -- 
        repo -- 
        autolink_id -- autolink_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/autolinks/{autolink_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/branches/{branch}/protection
    #
    def ReposDeleteBranchProtection(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#delete-branch-protection
        /repos/{owner}/{repo}/branches/{branch}/protection
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/comments/{comment_id}
    #
    def ReposDeleteCommitComment(self, owner:str, repo:str, comment_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#delete-a-commit-comment
        /repos/{owner}/{repo}/comments/{comment_id}
        
        arguments:
        owner -- 
        repo -- 
        comment_id -- comment_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/comments/{comment_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures
    #
    def ReposDeleteCommitSignatureProtection(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

When authenticated with admin or owner permissions to the repository, you can use this endpoint to disable required signed commits on a branch. You must enable branch protection to require signed commits.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#delete-commit-signature-protection
        /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/keys/{key_id}
    #
    def ReposDeleteDeployKey(self, owner:str, repo:str, key_id:int):
        """Deploy keys are immutable. If you need to update a key, remove the key and create a new one instead.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#delete-a-deploy-key
        /repos/{owner}/{repo}/keys/{key_id}
        
        arguments:
        owner -- 
        repo -- 
        key_id -- key_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/keys/{key_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/deployments/{deployment_id}
    #
    def ReposDeleteDeployment(self, owner:str, repo:str, deployment_id:int):
        """To ensure there can always be an active deployment, you can only delete an _inactive_ deployment. Anyone with `repo` or `repo_deployment` scopes can delete an inactive deployment.

To set a deployment as inactive, you must:

*   Create a new deployment that is active so that the system has a record of the current state, then delete the previously active deployment.
*   Mark the active deployment as inactive by adding any non-successful deployment status.

For more information, see "[Create a deployment](https://docs.github.com/enterprise-server@3.3/rest/reference/repos/#create-a-deployment)" and "[Create a deployment status](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-a-deployment-status)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#delete-a-deployment
        /repos/{owner}/{repo}/deployments/{deployment_id}
        
        arguments:
        owner -- 
        repo -- 
        deployment_id -- deployment_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/deployments/{deployment_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationErrorSimple(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/contents/{path}
    #
    def ReposDeleteFile(self, owner:str, repo:str, path:str):
        """Deletes a file in a repository.

You can provide an additional `committer` parameter, which is an object containing information about the committer. Or, you can provide an `author` parameter, which is an object containing information about the author.

The `author` section is optional and is filled in with the `committer` information if omitted. If the `committer` information is omitted, the authenticated user's information is used.

You must provide values for both `name` and `email`, whether you choose to use `author` or `committer`. Otherwise, you'll receive a `422` status code.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#delete-a-file
        /repos/{owner}/{repo}/contents/{path}
        
        arguments:
        owner -- 
        repo -- 
        path -- path parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/contents/{path}", 
                           params=data,
                           **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return FileCommit(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 409:
            return BasicError(**r.json())
            
        if r.status_code == 503:
            return Service_unavailable(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/invitations/{invitation_id}
    #
    def ReposDeleteInvitation(self, owner:str, repo:str, invitation_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#delete-a-repository-invitation
        /repos/{owner}/{repo}/invitations/{invitation_id}
        
        arguments:
        owner -- 
        repo -- 
        invitation_id -- invitation_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/invitations/{invitation_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/pages
    #
    def ReposDeletePagesSite(self, owner:str, repo:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#delete-a-github-pages-site
        /repos/{owner}/{repo}/pages
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/pages", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews
    #
    def ReposDeletePullRequestReviewProtection(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#delete-pull-request-review-protection
        /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/releases/{release_id}
    #
    def ReposDeleteRelease(self, owner:str, repo:str, release_id:int):
        """Users with push access to the repository can delete a release.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#delete-a-release
        /repos/{owner}/{repo}/releases/{release_id}
        
        arguments:
        owner -- 
        repo -- 
        release_id -- release_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/releases/{release_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/releases/assets/{asset_id}
    #
    def ReposDeleteReleaseAsset(self, owner:str, repo:str, asset_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#delete-a-release-asset
        /repos/{owner}/{repo}/releases/assets/{asset_id}
        
        arguments:
        owner -- 
        repo -- 
        asset_id -- asset_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/releases/assets/{asset_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/hooks/{hook_id}
    #
    def ReposDeleteWebhook(self, owner:str, repo:str, hook_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#delete-a-repository-webhook
        /repos/{owner}/{repo}/hooks/{hook_id}
        
        arguments:
        owner -- 
        repo -- 
        hook_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/hooks/{hook_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/lfs
    #
    def ReposDisableLfsForRepo(self, owner:str, repo:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#disable-git-lfs-for-a-repository
        /repos/{owner}/{repo}/lfs
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/lfs", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/tarball/{ref}
    #
    def ReposDownloadTarballArchive(self, owner:str, repo:str, ref:str):
        """Gets a redirect URL to download a tar archive for a repository. If you omit `:ref`, the repository’s default branch (usually
`master`) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use
the `Location` header to make a second `GET` request.
**Note**: For private repositories, these links are temporary and expire after five minutes.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#download-a-repository-archive
        /repos/{owner}/{repo}/tarball/{ref}
        
        arguments:
        owner -- 
        repo -- 
        ref -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/tarball/{ref}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 302:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/zipball/{ref}
    #
    def ReposDownloadZipballArchive(self, owner:str, repo:str, ref:str):
        """Gets a redirect URL to download a zip archive for a repository. If you omit `:ref`, the repository’s default branch (usually
`master`) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use
the `Location` header to make a second `GET` request.
**Note**: For private repositories, these links are temporary and expire after five minutes.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#download-a-repository-archive
        /repos/{owner}/{repo}/zipball/{ref}
        
        arguments:
        owner -- 
        repo -- 
        ref -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/zipball/{ref}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 302:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/lfs
    #
    def ReposEnableLfsForRepo(self, owner:str, repo:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#enable-git-lfs-for-a-repository
        /repos/{owner}/{repo}/lfs
        
        arguments:
        owner -- 
        repo -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/lfs", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 202:
            return r.json()
            
        if r.status_code == 403:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/releases/generate-notes
    #
    def ReposGenerateReleaseNotes(self, owner:str, repo:str,tag_name:str, target_commitish:str=None, previous_tag_name:str=None, configuration_file_path:str=None):
        """Generate a name and body describing a [release](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#releases). The body content will be markdown formatted and contain information like the changes since last release and users who contributed. The generated release notes are not saved anywhere. They are intended to be generated and used when creating a new release.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#generate-release-notes
        /repos/{owner}/{repo}/releases/generate-notes
        
        arguments:
        owner -- 
        repo -- 
        tag_name -- The tag name for the release. This can be an existing tag or a new one.
        target_commitish -- Specifies the commitish value that will be the target for the release's tag. Required if the supplied tag_name does not reference an existing tag. Ignored if the tag_name already exists.
        previous_tag_name -- The name of the previous tag to use as the starting point for the release notes. Use to manually specify the range for the set of changes considered as part this release.
        configuration_file_path -- Specifies a path to a file in the repository containing configuration settings used for generating the release notes. If unspecified, the configuration file located in the repository at '.github/release.yml' or '.github/release.yaml' will be used. If that is not present, the default configuration will be used.
        

        """
    
        data = {
        'tag_name': tag_name,
        'target_commitish': target_commitish,
        'previous_tag_name': previous_tag_name,
        'configuration_file_path': configuration_file_path,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/releases/generate-notes", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return GeneratedReleaseNotesContent(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}
    #
    def ReposGet(self, owner:str, repo:str):
        """The `parent` and `source` objects are present when the repository is a fork. `parent` is the repository this repository was forked from, `source` is the ultimate source for the network.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-a-repository
        /repos/{owner}/{repo}
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return FullRepository(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 301:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/branches/{branch}/protection/restrictions
    #
    def ReposGetAccessRestrictions(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Lists who has access to this protected branch.

**Note**: Users, apps, and teams `restrictions` are only available for organization-owned repositories.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-access-restrictions
        /repos/{owner}/{repo}/branches/{branch}/protection/restrictions
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return BranchRestrictionPolicy(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins
    #
    def ReposGetAdminBranchProtection(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-admin-branch-protection
        /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ProtectedBranchAdminEnforced(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/environments
    #
    def ReposGetAllEnvironments(self, owner:str, repo:str):
        """Get all environments for a repository.

Anyone with read access to the repository can use this endpoint. If the repository is private, you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-all-environments
        /repos/{owner}/{repo}/environments
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/environments", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ReposGetAllEnvironmentsSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts
    #
    def ReposGetAllStatusCheckContexts(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-all-status-check-contexts
        /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/topics
    #
    def ReposGetAllTopics(self, owner:str, repo:str,page=1, per_page=30):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-all-repository-topics
        /repos/{owner}/{repo}/topics
        
        arguments:
        owner -- 
        repo -- 
        page -- Page number of the results to fetch.
        per_page -- Results per page (max 100)
        
        """
        
        data = {}
        if page is not None:
            data['page'] = page
        if per_page is not None:
            data['per_page'] = per_page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/topics", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Topic(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps
    #
    def ReposGetAppsWithAccessToProtectedBranch(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Lists the GitHub Apps that have push access to this branch. Only installed GitHub Apps with `write` access to the `contents` permission can be added as authorized actors on a protected branch.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-apps-with-access-to-the-protected-branch
        /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Integration(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/autolinks/{autolink_id}
    #
    def ReposGetAutolink(self, owner:str, repo:str, autolink_id:int):
        """This returns a single autolink reference by ID that was configured for the given repository.

Information about autolinks are only available to repository administrators.
        
        https://docs.github.com/enterprise-server@3.3/v3/repos#get-autolink
        /repos/{owner}/{repo}/autolinks/{autolink_id}
        
        arguments:
        owner -- 
        repo -- 
        autolink_id -- autolink_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/autolinks/{autolink_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return AutolinkReference(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/branches/{branch}
    #
    def ReposGetBranch(self, owner:str, repo:str, branch:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-a-branch
        /repos/{owner}/{repo}/branches/{branch}
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/branches/{branch}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return BranchWithProtection(**r.json())
            
        if r.status_code == 301:
            return BasicError(**r.json())
            
        if r.status_code == 415:
            return Preview_header_missing(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/branches/{branch}/protection
    #
    def ReposGetBranchProtection(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-branch-protection
        /repos/{owner}/{repo}/branches/{branch}/protection
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return BranchProtection(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/stats/code_frequency
    #
    def ReposGetCodeFrequencyStats(self, owner:str, repo:str):
        """Returns a weekly aggregate of the number of additions and deletions pushed to a repository.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-the-weekly-commit-activity
        /repos/{owner}/{repo}/stats/code_frequency
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/stats/code_frequency", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and [ entry2 for entry2 in entry ] for entry in r.json() ]
            
        if r.status_code == 202:
            return r.json()
            
        if r.status_code == 204:
            return NoContent(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/collaborators/{username}/permission
    #
    def ReposGetCollaboratorPermissionLevel(self, owner:str, repo:str, username:str):
        """Checks the repository permission of a collaborator. The possible repository permissions are `admin`, `write`, `read`, and `none`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-repository-permissions-for-a-user
        /repos/{owner}/{repo}/collaborators/{username}/permission
        
        arguments:
        owner -- 
        repo -- 
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/collaborators/{username}/permission", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return RepositoryCollaboratorPermission(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/commits/{ref}/status
    #
    def ReposGetCombinedStatusForRef(self, owner:str, repo:str, ref:str,per_page=30, page=1):
        """Users with pull access in a repository can access a combined view of commit statuses for a given ref. The ref can be a SHA, a branch name, or a tag name.


Additionally, a combined `state` is returned. The `state` is one of:

*   **failure** if any of the contexts report as `error` or `failure`
*   **pending** if there are no statuses or a context is `pending`
*   **success** if the latest status for all contexts is `success`
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-the-combined-status-for-a-specific-reference
        /repos/{owner}/{repo}/commits/{ref}/status
        
        arguments:
        owner -- 
        repo -- 
        ref -- ref parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/commits/{ref}/status", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return CombinedCommitStatus(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/commits/{ref}
    #
    def ReposGetCommit(self, owner:str, repo:str, ref:str,page=1, per_page=30):
        """Returns the contents of a single commit reference. You must have `read` access for the repository to use this endpoint.

**Note:** If there are more than 300 files in the commit diff, the response will include pagination link headers for the remaining files, up to a limit of 3000 files. Each page contains the static commit information, and the only changes are to the file listing.

You can pass the appropriate [media type](https://docs.github.com/enterprise-server@3.3/rest/overview/media-types/#commits-commit-comparison-and-pull-requests) to  fetch `diff` and `patch` formats. Diffs with binary data will have no `patch` property.

To return only the SHA-1 hash of the commit reference, you can provide the `sha` custom [media type](https://docs.github.com/enterprise-server@3.3/rest/overview/media-types/#commits-commit-comparison-and-pull-requests) in the `Accept` header. You can use this endpoint to check if a remote reference's SHA-1 hash is the same as your local reference's SHA-1 hash by providing the local SHA-1 reference as the ETag.

**Signature verification object**

The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:

| Name | Type | Description |
| ---- | ---- | ----------- |
| `verified` | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified. |
| `reason` | `string` | The reason for verified value. Possible values and their meanings are enumerated in table below. |
| `signature` | `string` | The signature that was extracted from the commit. |
| `payload` | `string` | The value that was signed. |

These are the possible values for `reason` in the `verification` object:

| Value | Description |
| ----- | ----------- |
| `expired_key` | The key that made the signature is expired. |
| `not_signing_key` | The "signing" flag is not among the usage flags in the GPG key that made the signature. |
| `gpgverify_error` | There was an error communicating with the signature verification service. |
| `gpgverify_unavailable` | The signature verification service is currently unavailable. |
| `unsigned` | The object does not include a signature. |
| `unknown_signature_type` | A non-PGP signature was found in the commit. |
| `no_user` | No user was associated with the `committer` email address in the commit. |
| `unverified_email` | The `committer` email address in the commit was associated with a user, but the email address is not verified on her/his account. |
| `bad_email` | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature. |
| `unknown_key` | The key that made the signature has not been registered with any user's account. |
| `malformed_signature` | There was an error parsing the signature. |
| `invalid` | The signature could not be cryptographically verified using the key whose key-id was found in the signature. |
| `valid` | None of the above errors applied, so the signature is considered to be verified. |
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-a-commit
        /repos/{owner}/{repo}/commits/{ref}
        
        arguments:
        owner -- 
        repo -- 
        ref -- ref parameter
        page -- Page number of the results to fetch.
        per_page -- Results per page (max 100)
        
        """
        
        data = {}
        if page is not None:
            data['page'] = page
        if per_page is not None:
            data['per_page'] = per_page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/commits/{ref}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Commit(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 500:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/stats/commit_activity
    #
    def ReposGetCommitActivityStats(self, owner:str, repo:str):
        """Returns the last year of commit activity grouped by week. The `days` array is a group of commits per day, starting on `Sunday`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-the-last-year-of-commit-activity
        /repos/{owner}/{repo}/stats/commit_activity
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/stats/commit_activity", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and CommitActivity(**entry) for entry in r.json() ]
            
        if r.status_code == 202:
            return r.json()
            
        if r.status_code == 204:
            return NoContent(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/comments/{comment_id}
    #
    def ReposGetCommitComment(self, owner:str, repo:str, comment_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-a-commit-comment
        /repos/{owner}/{repo}/comments/{comment_id}
        
        arguments:
        owner -- 
        repo -- 
        comment_id -- comment_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/comments/{comment_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return CommitComment(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures
    #
    def ReposGetCommitSignatureProtection(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

When authenticated with admin or owner permissions to the repository, you can use this endpoint to check whether a branch requires signed commits. An enabled status of `true` indicates you must sign commits on this branch. For more information, see [Signing commits with GPG](https://help.github.com/articles/signing-commits-with-gpg) in GitHub Help.

**Note**: You must enable branch protection to require signed commits.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-commit-signature-protection
        /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ProtectedBranchAdminEnforced(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/contents/{path}
    #
    def ReposGetContent(self, owner:str, repo:str, path:str,ref:str=None):
        """Gets the contents of a file or directory in a repository. Specify the file path or directory in `:path`. If you omit
`:path`, you will receive the contents of the repository's root directory. See the description below regarding what the API response includes for directories. 

Files and symlinks support [a custom media type](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#custom-media-types) for
retrieving the raw content or rendered HTML (when supported). All content types support [a custom media
type](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#custom-media-types) to ensure the content is returned in a consistent
object format.

**Note**:
*   To get a repository's contents recursively, you can [recursively get the tree](https://docs.github.com/enterprise-server@3.3/rest/reference/git#trees).
*   This API has an upper limit of 1,000 files for a directory. If you need to retrieve more files, use the [Git Trees
API](https://docs.github.com/enterprise-server@3.3/rest/reference/git#get-a-tree).
*   This API supports files up to 1 megabyte in size.

#### If the content is a directory
The response will be an array of objects, one object for each item in the directory.
When listing the contents of a directory, submodules have their "type" specified as "file". Logically, the value
_should_ be "submodule". This behavior exists in API v3 [for backwards compatibility purposes](https://git.io/v1YCW).
In the next major version of the API, the type will be returned as "submodule".

#### If the content is a symlink 
If the requested `:path` points to a symlink, and the symlink's target is a normal file in the repository, then the
API responds with the content of the file (in the format shown in the example. Otherwise, the API responds with an object 
describing the symlink itself.

#### If the content is a submodule
The `submodule_git_url` identifies the location of the submodule repository, and the `sha` identifies a specific
commit within the submodule repository. Git uses the given URL when cloning the submodule repository, and checks out
the submodule at that specific commit.

If the submodule repository is not hosted on github.com, the Git URLs (`git_url` and `_links["git"]`) and the
github.com URLs (`html_url` and `_links["html"]`) will have null values.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-repository-content
        /repos/{owner}/{repo}/contents/{path}
        
        arguments:
        owner -- 
        repo -- 
        path -- path parameter
        ref -- The name of the commit/branch/tag. Default: the repository’s default branch (usually `master`)
        
        """
        
        data = {}
        if ref is not None:
            data['ref'] = ref
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/contents/{path}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return r.json()
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 302:
            return Found(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/stats/contributors
    #
    def ReposGetContributorsStats(self, owner:str, repo:str):
        """
Returns the `total` number of commits authored by the contributor. In addition, the response includes a Weekly Hash (`weeks` array) with the following information:

*   `w` - Start of the week, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time).
*   `a` - Number of additions
*   `d` - Number of deletions
*   `c` - Number of commits
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-all-contributor-commit-activity
        /repos/{owner}/{repo}/stats/contributors
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/stats/contributors", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and ContributorActivity(**entry) for entry in r.json() ]
            
        if r.status_code == 202:
            return r.json()
            
        if r.status_code == 204:
            return NoContent(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/keys/{key_id}
    #
    def ReposGetDeployKey(self, owner:str, repo:str, key_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-a-deploy-key
        /repos/{owner}/{repo}/keys/{key_id}
        
        arguments:
        owner -- 
        repo -- 
        key_id -- key_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/keys/{key_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return DeployKey(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/deployments/{deployment_id}
    #
    def ReposGetDeployment(self, owner:str, repo:str, deployment_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-a-deployment
        /repos/{owner}/{repo}/deployments/{deployment_id}
        
        arguments:
        owner -- 
        repo -- 
        deployment_id -- deployment_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/deployments/{deployment_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Deployment(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id}
    #
    def ReposGetDeploymentStatus(self, owner:str, repo:str, deployment_id:int, status_id:int):
        """Users with pull access can view a deployment status for a deployment:
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-a-deployment-status
        /repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id}
        
        arguments:
        owner -- 
        repo -- 
        deployment_id -- deployment_id parameter
        status_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return DeploymentStatus(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/environments/{environment_name}
    #
    def ReposGetEnvironment(self, owner:str, repo:str, environment_name:str):
        """Anyone with read access to the repository can use this endpoint. If the repository is private, you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-an-environment
        /repos/{owner}/{repo}/environments/{environment_name}
        
        arguments:
        owner -- 
        repo -- 
        environment_name -- The name of the environment
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/environments/{environment_name}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Environment(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/pages/builds/latest
    #
    def ReposGetLatestPagesBuild(self, owner:str, repo:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-latest-pages-build
        /repos/{owner}/{repo}/pages/builds/latest
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/pages/builds/latest", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return PageBuild(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/releases/latest
    #
    def ReposGetLatestRelease(self, owner:str, repo:str):
        """View the latest published full release for the repository.

The latest release is the most recent non-prerelease, non-draft release, sorted by the `created_at` attribute. The `created_at` attribute is the date of the commit used for the release, and not the date when the release was drafted or published.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-the-latest-release
        /repos/{owner}/{repo}/releases/latest
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/releases/latest", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Release(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/pages
    #
    def ReposGetPages(self, owner:str, repo:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-a-github-pages-site
        /repos/{owner}/{repo}/pages
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/pages", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return GithubPages(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/pages/builds/{build_id}
    #
    def ReposGetPagesBuild(self, owner:str, repo:str, build_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-github-pages-build
        /repos/{owner}/{repo}/pages/builds/{build_id}
        
        arguments:
        owner -- 
        repo -- 
        build_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/pages/builds/{build_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return PageBuild(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/stats/participation
    #
    def ReposGetParticipationStats(self, owner:str, repo:str):
        """Returns the total commit counts for the `owner` and total commit counts in `all`. `all` is everyone combined, including the `owner` in the last 52 weeks. If you'd like to get the commit counts for non-owners, you can subtract `owner` from `all`.

The array order is oldest week (index 0) to most recent week.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-the-weekly-commit-count
        /repos/{owner}/{repo}/stats/participation
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/stats/participation", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ParticipationStats(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews
    #
    def ReposGetPullRequestReviewProtection(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-pull-request-review-protection
        /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ProtectedBranchPullRequestReview(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/stats/punch_card
    #
    def ReposGetPunchCardStats(self, owner:str, repo:str):
        """Each array contains the day number, hour number, and number of commits:

*   `0-6`: Sunday - Saturday
*   `0-23`: Hour of day
*   Number of commits

For example, `[2, 14, 25]` indicates that there were 25 total commits, during the 2:00pm hour on Tuesdays. All times are based on the time zone of individual commits.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-the-hourly-commit-count-for-each-day
        /repos/{owner}/{repo}/stats/punch_card
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/stats/punch_card", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and [ entry2 for entry2 in entry ] for entry in r.json() ]
            
        if r.status_code == 204:
            return NoContent(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/readme
    #
    def ReposGetReadme(self, owner:str, repo:str,ref:str=None):
        """Gets the preferred README for a repository.

READMEs support [custom media types](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#custom-media-types) for retrieving the raw content or rendered HTML.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-a-repository-readme
        /repos/{owner}/{repo}/readme
        
        arguments:
        owner -- 
        repo -- 
        ref -- The name of the commit/branch/tag. Default: the repository’s default branch (usually `master`)
        
        """
        
        data = {}
        if ref is not None:
            data['ref'] = ref
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/readme", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ContentFile(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/readme/{dir}
    #
    def ReposGetReadmeInDirectory(self, owner:str, repo:str, dir:str,ref:str=None):
        """Gets the README from a repository directory.

READMEs support [custom media types](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#custom-media-types) for retrieving the raw content or rendered HTML.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-a-repository-directory-readme
        /repos/{owner}/{repo}/readme/{dir}
        
        arguments:
        owner -- 
        repo -- 
        dir -- The alternate path to look for a README file
        ref -- The name of the commit/branch/tag. Default: the repository’s default branch (usually `master`)
        
        """
        
        data = {}
        if ref is not None:
            data['ref'] = ref
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/readme/{dir}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ContentFile(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/releases/{release_id}
    #
    def ReposGetRelease(self, owner:str, repo:str, release_id:int):
        """**Note:** This returns an `upload_url` key corresponding to the endpoint for uploading release assets. This key is a [hypermedia resource](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#hypermedia).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-a-release
        /repos/{owner}/{repo}/releases/{release_id}
        
        arguments:
        owner -- 
        repo -- 
        release_id -- release_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/releases/{release_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Release(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/releases/assets/{asset_id}
    #
    def ReposGetReleaseAsset(self, owner:str, repo:str, asset_id:int):
        """To download the asset's binary content, set the `Accept` header of the request to [`application/octet-stream`](https://docs.github.com/enterprise-server@3.3/rest/overview/media-types). The API will either redirect the client to the location, or stream it directly if possible. API clients should handle both a `200` or `302` response.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-a-release-asset
        /repos/{owner}/{repo}/releases/assets/{asset_id}
        
        arguments:
        owner -- 
        repo -- 
        asset_id -- asset_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/releases/assets/{asset_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ReleaseAsset(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 415:
            return Preview_header_missing(**r.json())
            
        if r.status_code == 302:
            return Found(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/releases/tags/{tag}
    #
    def ReposGetReleaseByTag(self, owner:str, repo:str, tag:str):
        """Get a published release with the specified tag.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-a-release-by-tag-name
        /repos/{owner}/{repo}/releases/tags/{tag}
        
        arguments:
        owner -- 
        repo -- 
        tag -- tag parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/releases/tags/{tag}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Release(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks
    #
    def ReposGetStatusChecksProtection(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-status-checks-protection
        /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return StatusCheckPolicy(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams
    #
    def ReposGetTeamsWithAccessToProtectedBranch(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Lists the teams who have push access to this branch. The list includes child teams.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-teams-with-access-to-the-protected-branch
        /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Team(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users
    #
    def ReposGetUsersWithAccessToProtectedBranch(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Lists the people who have push access to this branch.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-users-with-access-to-the-protected-branch
        /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and SimpleUser(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/hooks/{hook_id}
    #
    def ReposGetWebhook(self, owner:str, repo:str, hook_id:int):
        """Returns a webhook configured in a repository. To get only the webhook `config` properties, see "[Get a webhook configuration for a repository](/rest/reference/repos#get-a-webhook-configuration-for-a-repository)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-a-repository-webhook
        /repos/{owner}/{repo}/hooks/{hook_id}
        
        arguments:
        owner -- 
        repo -- 
        hook_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/hooks/{hook_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Webhook(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/hooks/{hook_id}/config
    #
    def ReposGetWebhookConfigForRepo(self, owner:str, repo:str, hook_id:int):
        """Returns the webhook configuration for a repository. To get more information about the webhook, including the `active` state and `events`, use "[Get a repository webhook](/rest/reference/orgs#get-a-repository-webhook)."

Access tokens must have the `read:repo_hook` or `repo` scope, and GitHub Apps must have the `repository_hooks:read` permission.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-a-webhook-configuration-for-a-repository
        /repos/{owner}/{repo}/hooks/{hook_id}/config
        
        arguments:
        owner -- 
        repo -- 
        hook_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/hooks/{hook_id}/config", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return WebhookConfiguration(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}
    #
    def ReposGetWebhookDelivery(self, owner:str, repo:str, hook_id:int, delivery_id:int):
        """Returns a delivery for a webhook configured in a repository.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#get-a-delivery-for-a-repository-webhook
        /repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}
        
        arguments:
        owner -- 
        repo -- 
        hook_id -- 
        delivery_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}", 
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
    # get /repos/{owner}/{repo}/autolinks
    #
    def ReposListAutolinks(self, owner:str, repo:str,page=1):
        """This returns a list of autolinks configured for the given repository.

Information about autolinks are only available to repository administrators.
        
        https://docs.github.com/enterprise-server@3.3/v3/repos#list-autolinks
        /repos/{owner}/{repo}/autolinks
        
        arguments:
        owner -- 
        repo -- 
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/autolinks", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and AutolinkReference(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/branches
    #
    def ReposListBranches(self, owner:str, repo:str,protected:bool=None, per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-branches
        /repos/{owner}/{repo}/branches
        
        arguments:
        owner -- 
        repo -- 
        protected -- Setting to `true` returns only protected branches. When set to `false`, only unprotected branches are returned. Omitting this parameter returns all branches.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if protected is not None:
            data['protected'] = protected
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/branches", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and ShortBranch(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head
    #
    def ReposListBranchesForHeadCommit(self, owner:str, repo:str, commit_sha:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Returns all branches where the given commit SHA is the HEAD, or latest commit for the branch.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-branches-for-head-commit
        /repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head
        
        arguments:
        owner -- 
        repo -- 
        commit_sha -- commit_sha parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and BranchShort(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/collaborators
    #
    def ReposListCollaborators(self, owner:str, repo:str,affiliation='all', per_page=30, page=1):
        """For organization-owned repositories, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners.

Team members will include the members of child teams.

You must have push access to the repository in order to list collaborators.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-repository-collaborators
        /repos/{owner}/{repo}/collaborators
        
        arguments:
        owner -- 
        repo -- 
        affiliation -- Filters the collaborators by their affiliation. Can be one of:  
\* `outside`: Outside collaborators of a project that are not a member of the project's organization.  
\* `direct`: Collaborators with permissions to a project, regardless of organization membership status.  
\* `all`: All collaborators the authenticated user can see.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if affiliation is not None:
            data['affiliation'] = affiliation
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/collaborators", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Collaborator(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/commits/{commit_sha}/comments
    #
    def ReposListCommentsForCommit(self, owner:str, repo:str, commit_sha:str,per_page=30, page=1):
        """Use the `:commit_sha` to specify the commit that will have its comments listed.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-commit-comments
        /repos/{owner}/{repo}/commits/{commit_sha}/comments
        
        arguments:
        owner -- 
        repo -- 
        commit_sha -- commit_sha parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/commits/{commit_sha}/comments", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and CommitComment(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/comments
    #
    def ReposListCommitCommentsForRepo(self, owner:str, repo:str,per_page=30, page=1):
        """Commit Comments use [these custom media types](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#custom-media-types). You can read more about the use of media types in the API [here](https://docs.github.com/enterprise-server@3.3/rest/overview/media-types/).

Comments are ordered by ascending ID.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-commit-comments-for-a-repository
        /repos/{owner}/{repo}/comments
        
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
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/comments", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and CommitComment(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/commits/{ref}/statuses
    #
    def ReposListCommitStatusesForRef(self, owner:str, repo:str, ref:str,per_page=30, page=1):
        """Users with pull access in a repository can view commit statuses for a given ref. The ref can be a SHA, a branch name, or a tag name. Statuses are returned in reverse chronological order. The first status in the list will be the latest one.

This resource is also available via a legacy route: `GET /repos/:owner/:repo/statuses/:ref`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-commit-statuses-for-a-reference
        /repos/{owner}/{repo}/commits/{ref}/statuses
        
        arguments:
        owner -- 
        repo -- 
        ref -- ref parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/commits/{ref}/statuses", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Status(**entry) for entry in r.json() ]
            
        if r.status_code == 301:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/commits
    #
    def ReposListCommits(self, owner:str, repo:str,sha:str=None, path:str=None, author:str=None, since:datetime=None, until:datetime=None, per_page=30, page=1):
        """**Signature verification object**

The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:

| Name | Type | Description |
| ---- | ---- | ----------- |
| `verified` | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified. |
| `reason` | `string` | The reason for verified value. Possible values and their meanings are enumerated in table below. |
| `signature` | `string` | The signature that was extracted from the commit. |
| `payload` | `string` | The value that was signed. |

These are the possible values for `reason` in the `verification` object:

| Value | Description |
| ----- | ----------- |
| `expired_key` | The key that made the signature is expired. |
| `not_signing_key` | The "signing" flag is not among the usage flags in the GPG key that made the signature. |
| `gpgverify_error` | There was an error communicating with the signature verification service. |
| `gpgverify_unavailable` | The signature verification service is currently unavailable. |
| `unsigned` | The object does not include a signature. |
| `unknown_signature_type` | A non-PGP signature was found in the commit. |
| `no_user` | No user was associated with the `committer` email address in the commit. |
| `unverified_email` | The `committer` email address in the commit was associated with a user, but the email address is not verified on her/his account. |
| `bad_email` | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature. |
| `unknown_key` | The key that made the signature has not been registered with any user's account. |
| `malformed_signature` | There was an error parsing the signature. |
| `invalid` | The signature could not be cryptographically verified using the key whose key-id was found in the signature. |
| `valid` | None of the above errors applied, so the signature is considered to be verified. |
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-commits
        /repos/{owner}/{repo}/commits
        
        arguments:
        owner -- 
        repo -- 
        sha -- SHA or branch to start listing commits from. Default: the repository’s default branch (usually `master`).
        path -- Only commits containing this file path will be returned.
        author -- GitHub login or email address by which to filter by commit author.
        since -- Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        until -- Only commits before this date will be returned. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if sha is not None:
            data['sha'] = sha
        if path is not None:
            data['path'] = path
        if author is not None:
            data['author'] = author
        if since is not None:
            data['since'] = since.isoformat()
        if until is not None:
            data['until'] = until.isoformat()
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/commits", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Commit(**entry) for entry in r.json() ]
            
        if r.status_code == 500:
            return BasicError(**r.json())
            
        if r.status_code == 400:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 409:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/contributors
    #
    def ReposListContributors(self, owner:str, repo:str,anon:str=None, per_page=30, page=1):
        """Lists contributors to the specified repository and sorts them by the number of commits per contributor in descending order. This endpoint may return information that is a few hours old because the GitHub REST API v3 caches contributor data to improve performance.

GitHub identifies contributors by author email address. This endpoint groups contribution counts by GitHub user, which includes all associated email addresses. To improve performance, only the first 500 author email addresses in the repository link to GitHub users. The rest will appear as anonymous contributors without associated GitHub user information.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-repository-contributors
        /repos/{owner}/{repo}/contributors
        
        arguments:
        owner -- 
        repo -- 
        anon -- Set to `1` or `true` to include anonymous contributors in results.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if anon is not None:
            data['anon'] = anon
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/contributors", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Contributor(**entry) for entry in r.json() ]
            
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/keys
    #
    def ReposListDeployKeys(self, owner:str, repo:str,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-deploy-keys
        /repos/{owner}/{repo}/keys
        
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
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/keys", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and DeployKey(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/deployments/{deployment_id}/statuses
    #
    def ReposListDeploymentStatuses(self, owner:str, repo:str, deployment_id:int,per_page=30, page=1):
        """Users with pull access can view deployment statuses for a deployment:
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-deployment-statuses
        /repos/{owner}/{repo}/deployments/{deployment_id}/statuses
        
        arguments:
        owner -- 
        repo -- 
        deployment_id -- deployment_id parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/deployments/{deployment_id}/statuses", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and DeploymentStatus(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/deployments
    #
    def ReposListDeployments(self, owner:str, repo:str,sha:str=None, ref:str=None, task:str=None, environment:str=None, per_page=30, page=1):
        """Simple filtering of deployments is available via query parameters:
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-deployments
        /repos/{owner}/{repo}/deployments
        
        arguments:
        owner -- 
        repo -- 
        sha -- The SHA recorded at creation time.
        ref -- The name of the ref. This can be a branch, tag, or SHA.
        task -- The name of the task for the deployment (e.g., `deploy` or `deploy:migrations`).
        environment -- The name of the environment that was deployed to (e.g., `staging` or `production`).
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if sha is not None:
            data['sha'] = sha
        if ref is not None:
            data['ref'] = ref
        if task is not None:
            data['task'] = task
        if environment is not None:
            data['environment'] = environment
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/deployments", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Deployment(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /user/repos
    #
    def ReposListForAuthenticatedUser(self, visibility='all', affiliation:str=None, type=None, sort='created', direction='desc', per_page=30, page=1, since:datetime=None, before:datetime=None):
        """Lists repositories that the authenticated user has explicit permission (`:read`, `:write`, or `:admin`) to access.

The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-repositories-for-the-authenticated-user
        /user/repos
        
        arguments:
        visibility -- Can be one of `all`, `public`, or `private`. Note: For GitHub AE, can be one of `all`, `internal`, or `private`.
        affiliation -- Comma-separated list of values. Can include:  
\* `owner`: Repositories that are owned by the authenticated user.  
\* `collaborator`: Repositories that the user has been added to as a collaborator.  
\* `organization_member`: Repositories that the user has access to through being a member of an organization. This includes every repository on every team that the user is on.
        type -- Can be one of `all`, `owner`, `public`, `private`, `member`. Note: For GitHub AE, can be one of `all`, `owner`, `internal`, `private`, `member`. Default: `all`  
  
Will cause a `422` error if used in the same request as **visibility** or **affiliation**. Will cause a `422` error if used in the same request as **visibility** or **affiliation**.
        sort -- Can be one of `created`, `updated`, `pushed`, `full_name`.
        direction -- One of `asc` (ascending) or `desc` (descending).
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        since -- Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        before -- Only show notifications updated before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        
        """
        
        data = {}
        if visibility is not None:
            data['visibility'] = visibility
        if affiliation is not None:
            data['affiliation'] = affiliation
        if type is not None:
            data['type'] = type
        if sort is not None:
            data['sort'] = sort
        if direction is not None:
            data['direction'] = direction
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        if since is not None:
            data['since'] = since.isoformat()
        if before is not None:
            data['before'] = before.isoformat()
        
        
        r = self._session.get(f"{self._url}/user/repos", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Repository(**entry) for entry in r.json() ]
            
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
    # get /orgs/{org}/repos
    #
    def ReposListForOrg(self, org:str,type=None, sort='created', direction='desc', per_page=30, page=1):
        """Lists repositories for the specified organization.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-organization-repositories
        /orgs/{org}/repos
        
        arguments:
        org -- 
        type -- Specifies the types of repositories you want returned. Can be one of `all`, `public`, `private`, `forks`, `sources`, `member`, `internal`. Note: For GitHub AE, can be one of `all`, `private`, `forks`, `sources`, `member`, `internal`. Default: `all`. If your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+, `type` can also be `internal`. However, the `internal` value is not yet supported when a GitHub App calls this API with an installation access token.
        sort -- Can be one of `created`, `updated`, `pushed`, `full_name`.
        direction -- One of `asc` (ascending) or `desc` (descending).
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if type is not None:
            data['type'] = type
        if sort is not None:
            data['sort'] = sort
        if direction is not None:
            data['direction'] = direction
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/repos", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and MinimalRepository(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /users/{username}/repos
    #
    def ReposListForUser(self, username:str,type='owner', sort='created', direction='desc', per_page=30, page=1):
        """Lists public repositories for the specified user. Note: For GitHub AE, this endpoint will list internal repositories for the specified user.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-repositories-for-a-user
        /users/{username}/repos
        
        arguments:
        username -- 
        type -- Can be one of `all`, `owner`, `member`.
        sort -- Can be one of `created`, `updated`, `pushed`, `full_name`.
        direction -- One of `asc` (ascending) or `desc` (descending).
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if type is not None:
            data['type'] = type
        if sort is not None:
            data['sort'] = sort
        if direction is not None:
            data['direction'] = direction
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/users/{username}/repos", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and MinimalRepository(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/forks
    #
    def ReposListForks(self, owner:str, repo:str,sort='newest', per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-forks
        /repos/{owner}/{repo}/forks
        
        arguments:
        owner -- 
        repo -- 
        sort -- The sort order. Can be either `newest`, `oldest`, or `stargazers`.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if sort is not None:
            data['sort'] = sort
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/forks", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and MinimalRepository(**entry) for entry in r.json() ]
            
        if r.status_code == 400:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/invitations
    #
    def ReposListInvitations(self, owner:str, repo:str,per_page=30, page=1):
        """When authenticating as a user with admin rights to a repository, this endpoint will list all currently open repository invitations.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-repository-invitations
        /repos/{owner}/{repo}/invitations
        
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
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/invitations", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and RepositoryInvitation(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /user/repository_invitations
    #
    def ReposListInvitationsForAuthenticatedUser(self, per_page=30, page=1):
        """When authenticating as a user, this endpoint will list all currently open repository invitations for that user.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-repository-invitations-for-the-authenticated-user
        /user/repository_invitations
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/user/repository_invitations", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and RepositoryInvitation(**entry) for entry in r.json() ]
            
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
    # get /repos/{owner}/{repo}/languages
    #
    def ReposListLanguages(self, owner:str, repo:str):
        """Lists languages for the specified repository. The value shown for each language is the number of bytes of code written in that language.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-repository-languages
        /repos/{owner}/{repo}/languages
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/languages", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return r.json()
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/pages/builds
    #
    def ReposListPagesBuilds(self, owner:str, repo:str,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-github-pages-builds
        /repos/{owner}/{repo}/pages/builds
        
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
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/pages/builds", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and PageBuild(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repositories
    #
    def ReposListPublic(self, since:int=None, visibility='public'):
        """Lists all public repositories in the order that they were created.

Note:
- For GitHub Enterprise Server, this endpoint will only list repositories available to all users on the enterprise.
- Pagination is powered exclusively by the `since` parameter. Use the [Link header](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#link-header) to get the URL for the next page of repositories.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-public-repositories
        /repositories
        
        arguments:
        since -- A repository ID. Only return repositories with an ID greater than this ID.
        visibility -- Specifies the types of repositories to return. Can be one of `all` or `public`. Default: `public`. Note: For GitHub Enterprise Server and GitHub AE, this endpoint will only list repositories available to all users on the enterprise.
        
        """
        
        data = {}
        if since is not None:
            data['since'] = since
        if visibility is not None:
            data['visibility'] = visibility
        
        
        r = self._session.get(f"{self._url}/repositories", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and MinimalRepository(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/commits/{commit_sha}/pulls
    #
    def ReposListPullRequestsAssociatedWithCommit(self, owner:str, repo:str, commit_sha:str,per_page=30, page=1):
        """Lists the merged pull request that introduced the commit to the repository. If the commit is not present in the default branch, additionally returns open pull requests associated with the commit. The results may include open and closed pull requests. Additional preview headers may be required to see certain details for associated pull requests, such as whether a pull request is in a draft state. For more information about previews that might affect this endpoint, see the [List pull requests](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#list-pull-requests) endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-pull-requests-associated-with-a-commit
        /repos/{owner}/{repo}/commits/{commit_sha}/pulls
        
        arguments:
        owner -- 
        repo -- 
        commit_sha -- commit_sha parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/commits/{commit_sha}/pulls", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and PullRequestSimple(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/releases/{release_id}/assets
    #
    def ReposListReleaseAssets(self, owner:str, repo:str, release_id:int,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-release-assets
        /repos/{owner}/{repo}/releases/{release_id}/assets
        
        arguments:
        owner -- 
        repo -- 
        release_id -- release_id parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/releases/{release_id}/assets", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and ReleaseAsset(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/releases
    #
    def ReposListReleases(self, owner:str, repo:str,per_page=30, page=1):
        """This returns a list of releases, which does not include regular Git tags that have not been associated with a release. To get a list of Git tags, use the [Repository Tags API](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-repository-tags).

Information about published releases are available to everyone. Only users with push access will receive listings for draft releases.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-releases
        /repos/{owner}/{repo}/releases
        
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
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/releases", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Release(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/tags
    #
    def ReposListTags(self, owner:str, repo:str,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-repository-tags
        /repos/{owner}/{repo}/tags
        
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
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/tags", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Tag(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/teams
    #
    def ReposListTeams(self, owner:str, repo:str,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-repository-teams
        /repos/{owner}/{repo}/teams
        
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
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/teams", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Team(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/hooks/{hook_id}/deliveries
    #
    def ReposListWebhookDeliveries(self, owner:str, repo:str, hook_id:int,per_page=30, cursor:str=None):
        """Returns a list of webhook deliveries for a webhook configured in a repository.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-deliveries-for-a-repository-webhook
        /repos/{owner}/{repo}/hooks/{hook_id}/deliveries
        
        arguments:
        owner -- 
        repo -- 
        hook_id -- 
        per_page -- Results per page (max 100)
        cursor -- Used for pagination: the starting delivery from which the page of deliveries is fetched. Refer to the `link` header for the next and previous page cursors.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if cursor is not None:
            data['cursor'] = cursor
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/hooks/{hook_id}/deliveries", 
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
    # get /repos/{owner}/{repo}/hooks
    #
    def ReposListWebhooks(self, owner:str, repo:str,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-repository-webhooks
        /repos/{owner}/{repo}/hooks
        
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
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/hooks", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Webhook(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/merges
    #
    def ReposMerge(self, owner:str, repo:str,head:str, base:str, commit_message:str=None):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#merge-a-branch
        /repos/{owner}/{repo}/merges
        
        arguments:
        owner -- 
        repo -- 
        head -- The head to merge. This can be a branch name or a commit SHA1.
        base -- The name of the base branch that the head will be merged into.
        commit_message -- Commit message to use for the merge commit. If omitted, a default message will be used.
        

        """
    
        data = {
        'head': head,
        'base': base,
        'commit_message': commit_message,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/merges", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Commit(**r.json())
            
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        if r.status_code == 409:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/merge-upstream
    #
    def ReposMergeUpstream(self, owner:str, repo:str,branch:str):
        """Sync a branch of a forked repository to keep it up-to-date with the upstream repository.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#sync-a-fork-branch-with-the-upstream-repository
        /repos/{owner}/{repo}/merge-upstream
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch which should be updated to match upstream.
        

        """
    
        data = {
        'branch': branch,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/merge-upstream", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return MergedUpstream(**r.json())
            
        if r.status_code == 409:
            return HttpResponse(r)
            
        if r.status_code == 422:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/hooks/{hook_id}/pings
    #
    def ReposPingWebhook(self, owner:str, repo:str, hook_id:int):
        """This will trigger a [ping event](https://docs.github.com/enterprise-server@3.3/webhooks/#ping-event) to be sent to the hook.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#ping-a-repository-webhook
        /repos/{owner}/{repo}/hooks/{hook_id}/pings
        
        arguments:
        owner -- 
        repo -- 
        hook_id -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/hooks/{hook_id}/pings", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}/attempts
    #
    def ReposRedeliverWebhookDelivery(self, owner:str, repo:str, hook_id:int, delivery_id:int):
        """Redeliver a webhook delivery for a webhook configured in a repository.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#redeliver-a-delivery-for-a-repository-webhook
        /repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}/attempts
        
        arguments:
        owner -- 
        repo -- 
        hook_id -- 
        delivery_id -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}/attempts", 
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
    # delete /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps
    #
    def ReposRemoveAppAccessRestrictions(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Removes the ability of an app to push to this branch. Only installed GitHub Apps with `write` access to the `contents` permission can be added as authorized actors on a protected branch.

| Type    | Description                                                                                                                                                |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `array` | The GitHub Apps that have push access to this branch. Use the app's `slug`. **Note**: The list of users, apps, and teams in total is limited to 100 items. |
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#remove-app-access-restrictions
        /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps", 
                           params=data,
                           **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Integration(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/collaborators/{username}
    #
    def ReposRemoveCollaborator(self, owner:str, repo:str, username:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#remove-a-repository-collaborator
        /repos/{owner}/{repo}/collaborators/{username}
        
        arguments:
        owner -- 
        repo -- 
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/collaborators/{username}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts
    #
    def ReposRemoveStatusCheckContexts(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#remove-status-check-contexts
        /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts", 
                           params=data,
                           **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks
    #
    def ReposRemoveStatusCheckProtection(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#remove-status-check-protection
        /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams
    #
    def ReposRemoveTeamAccessRestrictions(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Removes the ability of a team to push to this branch. You can also remove push access for child teams.

| Type    | Description                                                                                                                                         |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `array` | Teams that should no longer have push access. Use the team's `slug`. **Note**: The list of users, apps, and teams in total is limited to 100 items. |
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#remove-team-access-restrictions
        /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams", 
                           params=data,
                           **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Team(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users
    #
    def ReposRemoveUserAccessRestrictions(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Removes the ability of a user to push to this branch.

| Type    | Description                                                                                                                                   |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `array` | Usernames of the people who should no longer have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. |
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#remove-user-access-restrictions
        /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users", 
                           params=data,
                           **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and SimpleUser(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/branches/{branch}/rename
    #
    def ReposRenameBranch(self, owner:str, repo:str, branch:str,new_name:str):
        """Renames a branch in a repository.

**Note:** Although the API responds immediately, the branch rename process might take some extra time to complete in the background. You won't be able to push to the old branch name while the rename process is in progress. For more information, see "[Renaming a branch](https://docs.github.com/enterprise-server@3.3/github/administering-a-repository/renaming-a-branch)".

The permissions required to use this endpoint depends on whether you are renaming the default branch.

To rename a non-default branch:

* Users must have push access.
* GitHub Apps must have the `contents:write` repository permission.

To rename the default branch:

* Users must have admin or owner permissions.
* GitHub Apps must have the `administration:write` repository permission.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#rename-a-branch
        /repos/{owner}/{repo}/branches/{branch}/rename
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        new_name -- The new name of the branch.
        

        """
    
        data = {
        'new_name': new_name,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/rename", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return BranchWithProtection(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/topics
    #
    def ReposReplaceAllTopics(self, owner:str, repo:str,names:list):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#replace-all-repository-topics
        /repos/{owner}/{repo}/topics
        
        arguments:
        owner -- 
        repo -- 
        names -- An array of topics to add to the repository. Pass one or more topics to _replace_ the set of existing topics. Send an empty array (`[]`) to clear all topics from the repository. **Note:** Topic `names` cannot contain uppercase letters.
        

        """
    
        data = {
        'names': names,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/topics", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Topic(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationErrorSimple(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/pages/builds
    #
    def ReposRequestPagesBuild(self, owner:str, repo:str):
        """You can request that your site be built from the latest revision on the default branch. This has the same effect as pushing a commit to your default branch, but does not require an additional commit. Manually triggering page builds can be helpful when diagnosing build warnings and failures.

Build requests are limited to one concurrent build per repository and one concurrent build per requester. If you request a build while another is still in progress, the second request will be queued until the first completes.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#request-a-github-pages-build
        /repos/{owner}/{repo}/pages/builds
        
        arguments:
        owner -- 
        repo -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/pages/builds", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return PageBuildStatus(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins
    #
    def ReposSetAdminBranchProtection(self, owner:str, repo:str, branch:str):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Adding admin enforcement requires admin or owner permissions to the repository and branch protection to be enabled.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#set-admin-branch-protection
        /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return ProtectedBranchAdminEnforced(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps
    #
    def ReposSetAppAccessRestrictions(self, owner:str, repo:str, branch:str,object:object):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Replaces the list of apps that have push access to this branch. This removes all apps that previously had push access and grants push access to the new list of apps. Only installed GitHub Apps with `write` access to the `contents` permission can be added as authorized actors on a protected branch.

| Type    | Description                                                                                                                                                |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `array` | The GitHub Apps that have push access to this branch. Use the app's `slug`. **Note**: The list of users, apps, and teams in total is limited to 100 items. |
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#set-app-access-restrictions
        /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        object -- 
        

        """
    
        data = {
        'object': object,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return [ entry and Integration(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts
    #
    def ReposSetStatusCheckContexts(self, owner:str, repo:str, branch:str,object:object):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#set-status-check-contexts
        /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        object -- 
        

        """
    
        data = {
        'object': object,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return [ entry for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams
    #
    def ReposSetTeamAccessRestrictions(self, owner:str, repo:str, branch:str,object:object):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Replaces the list of teams that have push access to this branch. This removes all teams that previously had push access and grants push access to the new list of teams. Team restrictions include child teams.

| Type    | Description                                                                                                                                |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `array` | The teams that can have push access. Use the team's `slug`. **Note**: The list of users, apps, and teams in total is limited to 100 items. |
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#set-team-access-restrictions
        /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        object -- 
        

        """
    
        data = {
        'object': object,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return [ entry and Team(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users
    #
    def ReposSetUserAccessRestrictions(self, owner:str, repo:str, branch:str,object:object):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Replaces the list of people that have push access to this branch. This removes all people that previously had push access and grants push access to the new list of people.

| Type    | Description                                                                                                                   |
| ------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `array` | Usernames for people who can have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. |
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#set-user-access-restrictions
        /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        object -- 
        

        """
    
        data = {
        'object': object,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return [ entry and SimpleUser(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/hooks/{hook_id}/tests
    #
    def ReposTestPushWebhook(self, owner:str, repo:str, hook_id:int):
        """This will trigger the hook with the latest push to the current repository if the hook is subscribed to `push` events. If the hook is not subscribed to `push` events, the server will respond with 204 but no test POST will be generated.

**Note**: Previously `/repos/:owner/:repo/hooks/:hook_id/test`
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#test-the-push-repository-webhook
        /repos/{owner}/{repo}/hooks/{hook_id}/tests
        
        arguments:
        owner -- 
        repo -- 
        hook_id -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/hooks/{hook_id}/tests", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/transfer
    #
    def ReposTransfer(self, owner:str, repo:str,new_owner:str, team_ids:list=[]):
        """A transfer request will need to be accepted by the new owner when transferring a personal repository to another user. The response will contain the original `owner`, and the transfer will continue asynchronously. For more details on the requirements to transfer personal and organization-owned repositories, see [about repository transfers](https://help.github.com/articles/about-repository-transfers/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#transfer-a-repository
        /repos/{owner}/{repo}/transfer
        
        arguments:
        owner -- 
        repo -- 
        new_owner -- The username or organization name the repository will be transferred to.
        team_ids -- ID of the team or teams to add to the repository. Teams can only be added to organization-owned repositories.
        

        """
    
        data = {
        'new_owner': new_owner,
        'team_ids': team_ids,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/transfer", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 202:
            return MinimalRepository(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}
    #
    def ReposUpdate(self, owner:str, repo:str,name:str=None, description:str=None, homepage:str=None, private:bool=False, visibility:str=None, security_and_analysis:dict=None, has_issues:bool=True, has_projects:bool=True, has_wiki:bool=True, is_template:bool=False, default_branch:str=None, allow_squash_merge:bool=True, allow_merge_commit:bool=True, allow_rebase_merge:bool=True, allow_auto_merge:bool=False, delete_branch_on_merge:bool=False, archived:bool=False, allow_forking:bool=False):
        """**Note**: To edit a repository's topics, use the [Replace all repository topics](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#replace-all-repository-topics) endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos/#update-a-repository
        /repos/{owner}/{repo}
        
        arguments:
        owner -- 
        repo -- 
        name -- The name of the repository.
        description -- A short description of the repository.
        homepage -- A URL with more information about the repository.
        private -- Either `true` to make the repository private or `false` to make it public. Default: `false`.  
**Note**: You will get a `422` error if the organization restricts [changing repository visibility](https://help.github.com/articles/repository-permission-levels-for-an-organization#changing-the-visibility-of-repositories) to organization owners and a non-owner tries to change the value of private. **Note**: You will get a `422` error if the organization restricts [changing repository visibility](https://help.github.com/articles/repository-permission-levels-for-an-organization#changing-the-visibility-of-repositories) to organization owners and a non-owner tries to change the value of private.
        visibility -- Can be `public` or `private`. If your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+, `visibility` can also be `internal`."
        security_and_analysis -- Specify which security and analysis features to enable or disable. For example, to enable GitHub Advanced Security, use this data in the body of the PATCH request: `{"security_and_analysis": {"advanced_security": {"status": "enabled"}}}`. If you have admin permissions for a private repository covered by an Advanced Security license, you can check which security and analysis features are currently enabled by using a `GET /repos/{owner}/{repo}` request.
        has_issues -- Either `true` to enable issues for this repository or `false` to disable them.
        has_projects -- Either `true` to enable projects for this repository or `false` to disable them. **Note:** If you're creating a repository in an organization that has disabled repository projects, the default is `false`, and if you pass `true`, the API returns an error.
        has_wiki -- Either `true` to enable the wiki for this repository or `false` to disable it.
        is_template -- Either `true` to make this repo available as a template repository or `false` to prevent it.
        default_branch -- Updates the default branch for this repository.
        allow_squash_merge -- Either `true` to allow squash-merging pull requests, or `false` to prevent squash-merging.
        allow_merge_commit -- Either `true` to allow merging pull requests with a merge commit, or `false` to prevent merging pull requests with merge commits.
        allow_rebase_merge -- Either `true` to allow rebase-merging pull requests, or `false` to prevent rebase-merging.
        allow_auto_merge -- Either `true` to allow auto-merge on pull requests, or `false` to disallow auto-merge.
        delete_branch_on_merge -- Either `true` to allow automatically deleting head branches when pull requests are merged, or `false` to prevent automatic deletion.
        archived -- `true` to archive this repository. **Note**: You cannot unarchive repositories through the API.
        allow_forking -- Either `true` to allow private forks, or `false` to prevent private forks.
        

        """
    
        data = {
        'name': name,
        'description': description,
        'homepage': homepage,
        'private': private,
        'visibility': visibility,
        'security_and_analysis': security_and_analysis,
        'has_issues': has_issues,
        'has_projects': has_projects,
        'has_wiki': has_wiki,
        'is_template': is_template,
        'default_branch': default_branch,
        'allow_squash_merge': allow_squash_merge,
        'allow_merge_commit': allow_merge_commit,
        'allow_rebase_merge': allow_rebase_merge,
        'allow_auto_merge': allow_auto_merge,
        'delete_branch_on_merge': delete_branch_on_merge,
        'archived': archived,
        'allow_forking': allow_forking,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return FullRepository(**r.json())
            
        if r.status_code == 307:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/branches/{branch}/protection
    #
    def ReposUpdateBranchProtection(self, owner:str, repo:str, branch:str,restrictions:dict, required_pull_request_reviews:dict, enforce_admins:bool, required_status_checks:dict, required_linear_history:bool=None, allow_force_pushes:bool=None, allow_deletions:bool=None, required_conversation_resolution:bool=None, contexts:list=[]):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Protecting a branch requires admin or owner permissions to the repository.

**Note**: Passing new arrays of `users` and `teams` replaces their previous values.

**Note**: The list of users, apps, and teams in total is limited to 100 items.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#update-branch-protection
        /repos/{owner}/{repo}/branches/{branch}/protection
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        restrictions -- Restrict who can push to the protected branch. User, app, and team `restrictions` are only available for organization-owned repositories. Set to `null` to disable.
        required_pull_request_reviews -- Require at least one approving review on a pull request, before merging. Set to `null` to disable.
        enforce_admins -- Enforce all configured restrictions for administrators. Set to `true` to enforce required status checks for repository administrators. Set to `null` to disable.
        required_status_checks -- Require status checks to pass before merging. Set to `null` to disable.
        required_linear_history -- Enforces a linear commit Git history, which prevents anyone from pushing merge commits to a branch. Set to `true` to enforce a linear commit history. Set to `false` to disable a linear commit Git history. Your repository must allow squash merging or rebase merging before you can enable a linear commit history. Default: `false`. For more information, see "[Requiring a linear commit history](https://help.github.com/github/administering-a-repository/requiring-a-linear-commit-history)" in the GitHub Help documentation.
        allow_force_pushes -- Permits force pushes to the protected branch by anyone with write access to the repository. Set to `true` to allow force pushes. Set to `false` or `null` to block force pushes. Default: `false`. For more information, see "[Enabling force pushes to a protected branch](https://help.github.com/en/github/administering-a-repository/enabling-force-pushes-to-a-protected-branch)" in the GitHub Help documentation."
        allow_deletions -- Allows deletion of the protected branch by anyone with write access to the repository. Set to `false` to prevent deletion of the protected branch. Default: `false`. For more information, see "[Enabling force pushes to a protected branch](https://help.github.com/en/github/administering-a-repository/enabling-force-pushes-to-a-protected-branch)" in the GitHub Help documentation.
        required_conversation_resolution -- Requires all conversations on code to be resolved before a pull request can be merged into a branch that matches this rule. Set to `false` to disable. Default: `false`.
        contexts -- The list of status checks to require in order to merge into this branch.
        

        """
    
        data = {
        'restrictions': restrictions,
        'required_pull_request_reviews': required_pull_request_reviews,
        'enforce_admins': enforce_admins,
        'required_status_checks': required_status_checks,
        'required_linear_history': required_linear_history,
        'allow_force_pushes': allow_force_pushes,
        'allow_deletions': allow_deletions,
        'required_conversation_resolution': required_conversation_resolution,
        'contexts': contexts,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return ProtectedBranch(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationErrorSimple(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}/comments/{comment_id}
    #
    def ReposUpdateCommitComment(self, owner:str, repo:str, comment_id:int,body:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#update-a-commit-comment
        /repos/{owner}/{repo}/comments/{comment_id}
        
        arguments:
        owner -- 
        repo -- 
        comment_id -- comment_id parameter
        body -- The contents of the comment
        

        """
    
        data = {
        'body': body,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/comments/{comment_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return CommitComment(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/pages
    #
    def ReposUpdateInformationAboutPagesSite(self, owner:str, repo:str,cname:str=None, https_enforced:bool=None, public:bool=None, source=None):
        """Updates information for a GitHub Enterprise Server Pages site. For more information, see "[About GitHub Pages](/github/working-with-github-pages/about-github-pages).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#update-information-about-a-github-pages-site
        /repos/{owner}/{repo}/pages
        
        arguments:
        owner -- 
        repo -- 
        cname -- Specify a custom domain for the repository. Sending a `null` value will remove the custom domain. For more about custom domains, see "[Using a custom domain with GitHub Pages](https://help.github.com/articles/using-a-custom-domain-with-github-pages/)."
        https_enforced -- Specify whether HTTPS should be enforced for the repository.
        public -- Configures access controls for the GitHub Pages site. If public is set to `true`, the site is accessible to anyone on the internet. If set to `false`, the site will only be accessible to users who have at least `read` access to the repository that published the site. This includes anyone in your Enterprise if the repository is set to `internal` visibility. This feature is only available to repositories in an organization on an Enterprise plan.
        source -- 
        

        """
    
        data = {
        'cname': cname,
        'https_enforced': https_enforced,
        'public': public,
        'source': source,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/pages", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 400:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}/invitations/{invitation_id}
    #
    def ReposUpdateInvitation(self, owner:str, repo:str, invitation_id:int,permissions:str=None):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#update-a-repository-invitation
        /repos/{owner}/{repo}/invitations/{invitation_id}
        
        arguments:
        owner -- 
        repo -- 
        invitation_id -- invitation_id parameter
        permissions -- The permissions that the associated user will have on the repository. Valid values are `read`, `write`, `maintain`, `triage`, and `admin`.
        

        """
    
        data = {
        'permissions': permissions,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/invitations/{invitation_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return RepositoryInvitation(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews
    #
    def ReposUpdatePullRequestReviewProtection(self, owner:str, repo:str, branch:str,dismissal_restrictions:dict=None, dismiss_stale_reviews:bool=None, require_code_owner_reviews:bool=None, required_approving_review_count:int=None):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Updating pull request review enforcement requires admin or owner permissions to the repository and branch protection to be enabled.

**Note**: Passing new arrays of `users` and `teams` replaces their previous values.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#update-pull-request-review-protection
        /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        dismissal_restrictions -- Specify which users and teams can dismiss pull request reviews. Pass an empty `dismissal_restrictions` object to disable. User and team `dismissal_restrictions` are only available for organization-owned repositories. Omit this parameter for personal repositories.
        dismiss_stale_reviews -- Set to `true` if you want to automatically dismiss approving reviews when someone pushes a new commit.
        require_code_owner_reviews -- Blocks merging pull requests until [code owners](https://help.github.com/articles/about-code-owners/) have reviewed.
        required_approving_review_count -- Specifies the number of reviewers required to approve pull requests. Use a number between 1 and 6.
        

        """
    
        data = {
        'dismissal_restrictions': dismissal_restrictions,
        'dismiss_stale_reviews': dismiss_stale_reviews,
        'require_code_owner_reviews': require_code_owner_reviews,
        'required_approving_review_count': required_approving_review_count,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return ProtectedBranchPullRequestReview(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}/releases/{release_id}
    #
    def ReposUpdateRelease(self, owner:str, repo:str, release_id:int,tag_name:str=None, target_commitish:str=None, name:str=None, body:str=None, draft:bool=None, prerelease:bool=None):
        """Users with push access to the repository can edit a release.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#update-a-release
        /repos/{owner}/{repo}/releases/{release_id}
        
        arguments:
        owner -- 
        repo -- 
        release_id -- release_id parameter
        tag_name -- The name of the tag.
        target_commitish -- Specifies the commitish value that determines where the Git tag is created from. Can be any branch or commit SHA. Unused if the Git tag already exists. Default: the repository's default branch (usually `master`).
        name -- The name of the release.
        body -- Text describing the contents of the tag.
        draft -- `true` makes the release a draft, and `false` publishes the release.
        prerelease -- `true` to identify the release as a prerelease, `false` to identify the release as a full release.
        

        """
    
        data = {
        'tag_name': tag_name,
        'target_commitish': target_commitish,
        'name': name,
        'body': body,
        'draft': draft,
        'prerelease': prerelease,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/releases/{release_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Release(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}/releases/assets/{asset_id}
    #
    def ReposUpdateReleaseAsset(self, owner:str, repo:str, asset_id:int,name:str=None, label:str=None, state:str=None):
        """Users with push access to the repository can edit a release asset.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#update-a-release-asset
        /repos/{owner}/{repo}/releases/assets/{asset_id}
        
        arguments:
        owner -- 
        repo -- 
        asset_id -- asset_id parameter
        name -- The file name of the asset.
        label -- An alternate short description of the asset. Used in place of the filename.
        state -- 
        

        """
    
        data = {
        'name': name,
        'label': label,
        'state': state,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/releases/assets/{asset_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return ReleaseAsset(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks
    #
    def ReposUpdateStatusCheckProtection(self, owner:str, repo:str, branch:str,strict:bool=None, contexts=None):
        """Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Updating required status checks requires admin or owner permissions to the repository and branch protection to be enabled.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#update-status-check-protection
        /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks
        
        arguments:
        owner -- 
        repo -- 
        branch -- The name of the branch.
        strict -- Require branches to be up to date before merging.
        contexts -- The list of status checks to require in order to merge into this branch
        

        """
    
        data = {
        'strict': strict,
        'contexts': contexts,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return StatusCheckPolicy(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}/hooks/{hook_id}
    #
    def ReposUpdateWebhook(self, owner:str, repo:str, hook_id:int,config:dict=None, events:list=['push'], add_events:list=[], remove_events:list=[], active:bool=True):
        """Updates a webhook configured in a repository. If you previously had a `secret` set, you must provide the same `secret` or set a new `secret` or the secret will be removed. If you are only updating individual webhook `config` properties, use "[Update a webhook configuration for a repository](/rest/reference/repos#update-a-webhook-configuration-for-a-repository)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#update-a-repository-webhook
        /repos/{owner}/{repo}/hooks/{hook_id}
        
        arguments:
        owner -- 
        repo -- 
        hook_id -- 
        config -- Key/value pairs to provide settings for this webhook. [These are defined below](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-hook-config-params).
        events -- Determines what [events](https://docs.github.com/enterprise-server@3.3/webhooks/event-payloads) the hook is triggered for. This replaces the entire array of events.
        add_events -- Determines a list of events to be added to the list of events that the Hook triggers for.
        remove_events -- Determines a list of events to be removed from the list of events that the Hook triggers for.
        active -- Determines if notifications are sent when the webhook is triggered. Set to `true` to send notifications.
        

        """
    
        data = {
        'config': config,
        'events': events,
        'add_events': add_events,
        'remove_events': remove_events,
        'active': active,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/hooks/{hook_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Webhook(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}/hooks/{hook_id}/config
    #
    def ReposUpdateWebhookConfigForRepo(self, owner:str, repo:str, hook_id:int,url:str=None, content_type:str=None, secret:str=None, insecure_ssl=None):
        """Updates the webhook configuration for a repository. To update more information about the webhook, including the `active` state and `events`, use "[Update a repository webhook](/rest/reference/orgs#update-a-repository-webhook)."

Access tokens must have the `write:repo_hook` or `repo` scope, and GitHub Apps must have the `repository_hooks:write` permission.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#update-a-webhook-configuration-for-a-repository
        /repos/{owner}/{repo}/hooks/{hook_id}/config
        
        arguments:
        owner -- 
        repo -- 
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
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/hooks/{hook_id}/config", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return WebhookConfiguration(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/releases/{release_id}/assets
    #
    def ReposUploadReleaseAsset(self, owner:str, repo:str, release_id:int,data:bytes):
        """This endpoint makes use of [a Hypermedia relation](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#hypermedia) to determine which URL to access. The endpoint you call to upload release assets is specific to your release. Use the `upload_url` returned in
the response of the [Create a release endpoint](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-a-release) to upload a release asset.

You need to use an HTTP client which supports [SNI](http://en.wikipedia.org/wiki/Server_Name_Indication) to make calls to this endpoint.

Most libraries will set the required `Content-Length` header automatically. Use the required `Content-Type` header to provide the media type of the asset. For a list of media types, see [Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml). For example: 

`application/zip`

GitHub Enterprise Server expects the asset data in its raw binary form, rather than JSON. You will send the raw binary content of the asset as the request body. Everything else about the endpoint is the same as the rest of the API. For example,
you'll still need to pass your authentication to be able to upload an asset.

When an upstream failure occurs, you will receive a `502 Bad Gateway` status. This may leave an empty asset with a state of `starter`. It can be safely deleted.

**Notes:**
*   GitHub Enterprise Server renames asset filenames that have special characters, non-alphanumeric characters, and leading or trailing periods. The "[List assets for a release](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-assets-for-a-release)"
endpoint lists the renamed filenames. For more information and help, contact [GitHub Enterprise Server Support](https://support.github.com/contact?tags=dotcom-rest-api).
*   If you upload an asset with the same filename as another uploaded asset, you'll receive an error and must delete the old file before you can re-upload the new asset.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/repos#upload-a-release-asset
        /repos/{owner}/{repo}/releases/{release_id}/assets
        
        arguments:
        owner -- 
        repo -- 
        release_id -- release_id parameter
        name -- 
        label -- 
        data -- 
        

        """
    
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/releases/{release_id}/assets", 
                          data=data,
                          **self._requests_kwargs({'Content-Type':  '*/*'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return ReleaseAsset(**r.json())
            
        if r.status_code == 422:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
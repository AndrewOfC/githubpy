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

class Teams(object):


    #
    # put /teams/{team_id}/members/{username}
    #
    def TeamsAddMemberLegacy(self, team_id:int, username:str):
        """The "Add team member" endpoint (described below) is deprecated.

We recommend using the [Add or update team membership for a user](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#add-or-update-team-membership-for-a-user) endpoint instead. It allows you to invite new organization members to your teams.

Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

To add someone to a team, the authenticated user must be an organization owner or a team maintainer in the team they're changing. The person being added to the team must be a member of the team's organization.

**Note:** When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#http-verbs)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#add-team-member-legacy
        /teams/{team_id}/members/{username}
        
        arguments:
        team_id -- 
        username -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.put(f"{self._url}/teams/{team_id}/members/{username}", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        if r.status_code == 422:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /orgs/{org}/teams/{team_slug}/memberships/{username}
    #
    def TeamsAddOrUpdateMembershipForUserInOrg(self, org:str, team_slug:str, username:str,role:str='member'):
        """Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Adds an organization member to a team. An authenticated organization owner or team maintainer can add organization members to a team.

**Note:** When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

An organization owner can add someone who is not part of the team's organization to a team. When an organization owner adds someone to a team who is not an organization member, this endpoint will send an invitation to the person via email. This newly-created membership will be in the "pending" state until the person accepts the invitation, at which point the membership will transition to the "active" state and the user will be added as a member of the team.

If the user is already a member of the team, this endpoint will update the role of the team member's role. To update the membership of a team member, the authenticated user must be an organization owner or a team maintainer.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `PUT /organizations/{org_id}/team/{team_id}/memberships/{username}`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#add-or-update-team-membership-for-a-user
        /orgs/{org}/teams/{team_slug}/memberships/{username}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        username -- 
        role -- The role that this user should have in the team. Can be one of:  
\* `member` - a normal member of the team.  
\* `maintainer` - a team maintainer. Able to add/remove other team members, promote other team members to team maintainer, and edit the team's name and description.
        

        """
    
        data = {
        'role': role,
        
        }
        

        
        r = self._session.put(f"{self._url}/orgs/{org}/teams/{team_slug}/memberships/{username}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return TeamMembership(**r.json())
            
        if r.status_code == 403:
            return HttpResponse(r)
            
        if r.status_code == 422:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /teams/{team_id}/memberships/{username}
    #
    def TeamsAddOrUpdateMembershipForUserLegacy(self, team_id:int, username:str,role:str='member'):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Add or update team membership for a user](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#add-or-update-team-membership-for-a-user) endpoint.

Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

If the user is already a member of the team's organization, this endpoint will add the user to the team. To add a membership between an organization member and a team, the authenticated user must be an organization owner or a team maintainer.

**Note:** When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

If the user is unaffiliated with the team's organization, this endpoint will send an invitation to the user via email. This newly-created membership will be in the "pending" state until the user accepts the invitation, at which point the membership will transition to the "active" state and the user will be added as a member of the team. To add a membership between an unaffiliated user and a team, the authenticated user must be an organization owner.

If the user is already a member of the team, this endpoint will update the role of the team member's role. To update the membership of a team member, the authenticated user must be an organization owner or a team maintainer.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#add-or-update-team-membership-for-a-user-legacy
        /teams/{team_id}/memberships/{username}
        
        arguments:
        team_id -- 
        username -- 
        role -- The role that this user should have in the team. Can be one of:  
\* `member` - a normal member of the team.  
\* `maintainer` - a team maintainer. Able to add/remove other team members, promote other team members to team maintainer, and edit the team's name and description.
        

        """
    
        data = {
        'role': role,
        
        }
        

        
        r = self._session.put(f"{self._url}/teams/{team_id}/memberships/{username}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return TeamMembership(**r.json())
            
        if r.status_code == 403:
            return HttpResponse(r)
            
        if r.status_code == 422:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /orgs/{org}/teams/{team_slug}/projects/{project_id}
    #
    def TeamsAddOrUpdateProjectPermissionsInOrg(self, org:str, team_slug:str, project_id:int,permission:str=None):
        """Adds an organization project to a team. To add a project to a team or update the team's permission on a project, the authenticated user must have `admin` permissions for the project. The project and team must be part of the same organization.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `PUT /organizations/{org_id}/team/{team_id}/projects/{project_id}`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#add-or-update-team-project-permissions
        /orgs/{org}/teams/{team_slug}/projects/{project_id}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        project_id -- 
        permission -- The permission to grant to the team for this project. Can be one of:  
\* `read` - team members can read, but not write to or administer this project.  
\* `write` - team members can read and write, but not administer this project.  
\* `admin` - team members can read, write and administer this project.  
Default: the team's `permission` attribute will be used to determine what permission to grant the team on this project. Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#http-verbs)."
        

        """
    
        data = {
        'permission': permission,
        
        }
        

        
        r = self._session.put(f"{self._url}/orgs/{org}/teams/{team_slug}/projects/{project_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return TeamsAddOrUpdateProjectPermissionsInOrgForbidden(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /teams/{team_id}/projects/{project_id}
    #
    def TeamsAddOrUpdateProjectPermissionsLegacy(self, team_id:int, project_id:int,permission:str=None):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Add or update team project permissions](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#add-or-update-team-project-permissions) endpoint.

Adds an organization project to a team. To add a project to a team or update the team's permission on a project, the authenticated user must have `admin` permissions for the project. The project and team must be part of the same organization.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams/#add-or-update-team-project-permissions-legacy
        /teams/{team_id}/projects/{project_id}
        
        arguments:
        team_id -- 
        project_id -- 
        permission -- The permission to grant to the team for this project. Can be one of:  
\* `read` - team members can read, but not write to or administer this project.  
\* `write` - team members can read and write, but not administer this project.  
\* `admin` - team members can read, write and administer this project.  
Default: the team's `permission` attribute will be used to determine what permission to grant the team on this project. Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#http-verbs)."
        

        """
    
        data = {
        'permission': permission,
        
        }
        

        
        r = self._session.put(f"{self._url}/teams/{team_id}/projects/{project_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return TeamsAddOrUpdateProjectPermissionsLegacyForbidden(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}
    #
    def TeamsAddOrUpdateRepoPermissionsInOrg(self, org:str, team_slug:str, owner:str, repo:str,permission:str='push'):
        """To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization. Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#http-verbs)."

**Note:** You can also specify a team by `org_id` and `team_id` using the route `PUT /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`.

For more information about the permission levels, see "[Repository permission levels for an organization](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)".
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams/#add-or-update-team-repository-permissions
        /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        owner -- 
        repo -- 
        permission -- The permission to grant the team on this repository. Can be one of:  
\* `pull` - team members can pull, but not push to or administer this repository.  
\* `push` - team members can pull and push, but not administer this repository.  
\* `admin` - team members can pull, push and administer this repository.  
\* `maintain` - team members can manage the repository without access to sensitive or destructive actions. Recommended for project managers. Only applies to repositories owned by organizations.  
\* `triage` - team members can proactively manage issues and pull requests without write access. Recommended for contributors who triage a repository. Only applies to repositories owned by organizations.  
  
If no permission is specified, the team's `permission` attribute will be used to determine what permission to grant the team on this repository.
        

        """
    
        data = {
        'permission': permission,
        
        }
        

        
        r = self._session.put(f"{self._url}/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # put /teams/{team_id}/repos/{owner}/{repo}
    #
    def TeamsAddOrUpdateRepoPermissionsLegacy(self, team_id:int, owner:str, repo:str,permission:str=None):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new "[Add or update team repository permissions](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#add-or-update-team-repository-permissions)" endpoint.

To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization.

Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#http-verbs)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams/#add-or-update-team-repository-permissions-legacy
        /teams/{team_id}/repos/{owner}/{repo}
        
        arguments:
        team_id -- 
        owner -- 
        repo -- 
        permission -- The permission to grant the team on this repository. Can be one of:  
\* `pull` - team members can pull, but not push to or administer this repository.  
\* `push` - team members can pull and push, but not administer this repository.  
\* `admin` - team members can pull, push and administer this repository.  
  
If no permission is specified, the team's `permission` attribute will be used to determine what permission to grant the team on this repository.
        

        """
    
        data = {
        'permission': permission,
        
        }
        

        
        r = self._session.put(f"{self._url}/teams/{team_id}/repos/{owner}/{repo}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # get /orgs/{org}/teams/{team_slug}/projects/{project_id}
    #
    def TeamsCheckPermissionsForProjectInOrg(self, org:str, team_slug:str, project_id:int):
        """Checks whether a team has `read`, `write`, or `admin` permissions for an organization project. The response includes projects inherited from a parent team.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/projects/{project_id}`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#check-team-permissions-for-a-project
        /orgs/{org}/teams/{team_slug}/projects/{project_id}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        project_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/teams/{team_slug}/projects/{project_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return TeamProject(**r.json())
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # get /teams/{team_id}/projects/{project_id}
    #
    def TeamsCheckPermissionsForProjectLegacy(self, team_id:int, project_id:int):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a project](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#check-team-permissions-for-a-project) endpoint.

Checks whether a team has `read`, `write`, or `admin` permissions for an organization project. The response includes projects inherited from a parent team.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams/#check-team-permissions-for-a-project-legacy
        /teams/{team_id}/projects/{project_id}
        
        arguments:
        team_id -- 
        project_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/teams/{team_id}/projects/{project_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return TeamProject(**r.json())
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}
    #
    def TeamsCheckPermissionsForRepoInOrg(self, org:str, team_slug:str, owner:str, repo:str):
        """Checks whether a team has `admin`, `push`, `maintain`, `triage`, or `pull` permission for a repository. Repositories inherited through a parent team will also be checked.

You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/enterprise-server@3.3/rest/overview/media-types/) via the `application/vnd.github.v3.repository+json` accept header.

If a team doesn't have permission for the repository, you will receive a `404 Not Found` response status.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams/#check-team-permissions-for-a-repository
        /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return TeamRepository(**r.json())
            
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # get /teams/{team_id}/repos/{owner}/{repo}
    #
    def TeamsCheckPermissionsForRepoLegacy(self, team_id:int, owner:str, repo:str):
        """**Note**: Repositories inherited through a parent team will also be checked.

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a repository](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#check-team-permissions-for-a-repository) endpoint.

You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/enterprise-server@3.3/rest/overview/media-types/) via the `Accept` header:
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams/#check-team-permissions-for-a-repository-legacy
        /teams/{team_id}/repos/{owner}/{repo}
        
        arguments:
        team_id -- 
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/teams/{team_id}/repos/{owner}/{repo}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return TeamRepository(**r.json())
            
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # post /orgs/{org}/teams
    #
    def TeamsCreate(self, org:str,name:str, description:str=None, maintainers:list=[], repo_names:list=[], privacy:str=None, permission:str='pull', parent_team_id:int=None):
        """To create a team, the authenticated user must be a member or owner of `{org}`. By default, organization members can create teams. Organization owners can limit team creation to organization owners. For more information, see "[Setting team creation permissions](https://help.github.com/en/articles/setting-team-creation-permissions-in-your-organization)."

When you create a new team, you automatically become a team maintainer without explicitly adding yourself to the optional array of `maintainers`. For more information, see "[About teams](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/about-teams)".
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#create-a-team
        /orgs/{org}/teams
        
        arguments:
        org -- 
        name -- The name of the team.
        description -- The description of the team.
        maintainers -- List GitHub IDs for organization members who will become team maintainers.
        repo_names -- The full name (e.g., "organization-name/repository-name") of repositories to add the team to.
        privacy -- The level of privacy this team should have. The options are:  
**For a non-nested team:**  
\* `secret` - only visible to organization owners and members of this team.  
\* `closed` - visible to all members of this organization.  
Default: `secret`  
**For a parent or child team:**  
\* `closed` - visible to all members of this organization.  
Default for child team: `closed`
        permission -- **Deprecated**. The permission that new repositories will be added to the team with when none is specified. Can be one of:  
\* `pull` - team members can pull, but not push to or administer newly-added repositories.  
\* `push` - team members can pull and push, but not administer newly-added repositories.  
\* `admin` - team members can pull, push and administer newly-added repositories.
        parent_team_id -- The ID of a team to set as the parent team.
        

        """
    
        data = {
        'name': name,
        'description': description,
        'maintainers': maintainers,
        'repo_names': repo_names,
        'privacy': privacy,
        'permission': permission,
        'parent_team_id': parent_team_id,
        
        }
        

        
        r = self._session.post(f"{self._url}/orgs/{org}/teams", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return FullTeam(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments
    #
    def TeamsCreateDiscussionCommentInOrg(self, org:str, team_slug:str, discussion_number:int,body:str):
        """Creates a new comment on a team discussion. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `POST /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#create-a-discussion-comment
        /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        discussion_number -- 
        body -- The discussion comment's body text.
        

        """
    
        data = {
        'body': body,
        
        }
        

        
        r = self._session.post(f"{self._url}/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return TeamDiscussionComment(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /teams/{team_id}/discussions/{discussion_number}/comments
    #
    def TeamsCreateDiscussionCommentLegacy(self, team_id:int, discussion_number:int,body:str):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Create a discussion comment](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#create-a-discussion-comment) endpoint.

Creates a new comment on a team discussion. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#create-a-discussion-comment-legacy
        /teams/{team_id}/discussions/{discussion_number}/comments
        
        arguments:
        team_id -- 
        discussion_number -- 
        body -- The discussion comment's body text.
        

        """
    
        data = {
        'body': body,
        
        }
        

        
        r = self._session.post(f"{self._url}/teams/{team_id}/discussions/{discussion_number}/comments", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return TeamDiscussionComment(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /orgs/{org}/teams/{team_slug}/discussions
    #
    def TeamsCreateDiscussionInOrg(self, org:str, team_slug:str,body:str, title:str, private:bool=False):
        """Creates a new discussion post on a team's page. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `POST /organizations/{org_id}/team/{team_id}/discussions`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#create-a-discussion
        /orgs/{org}/teams/{team_slug}/discussions
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        body -- The discussion post's body text.
        title -- The discussion post's title.
        private -- Private posts are only visible to team members, organization owners, and team maintainers. Public posts are visible to all members of the organization. Set to `true` to create a private post.
        

        """
    
        data = {
        'body': body,
        'title': title,
        'private': private,
        
        }
        

        
        r = self._session.post(f"{self._url}/orgs/{org}/teams/{team_slug}/discussions", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return TeamDiscussion(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /teams/{team_id}/discussions
    #
    def TeamsCreateDiscussionLegacy(self, team_id:int,body:str, title:str, private:bool=False):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`Create a discussion`](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#create-a-discussion) endpoint.

Creates a new discussion post on a team's page. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#create-a-discussion-legacy
        /teams/{team_id}/discussions
        
        arguments:
        team_id -- 
        body -- The discussion post's body text.
        title -- The discussion post's title.
        private -- Private posts are only visible to team members, organization owners, and team maintainers. Public posts are visible to all members of the organization. Set to `true` to create a private post.
        

        """
    
        data = {
        'body': body,
        'title': title,
        'private': private,
        
        }
        

        
        r = self._session.post(f"{self._url}/teams/{team_id}/discussions", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return TeamDiscussion(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}
    #
    def TeamsDeleteDiscussionCommentInOrg(self, org:str, team_slug:str, discussion_number:int, comment_number:int):
        """Deletes a comment on a team discussion. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments/{comment_number}`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#delete-a-discussion-comment
        /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        discussion_number -- 
        comment_number -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}
    #
    def TeamsDeleteDiscussionCommentLegacy(self, team_id:int, discussion_number:int, comment_number:int):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Delete a discussion comment](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#delete-a-discussion-comment) endpoint.

Deletes a comment on a team discussion. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#delete-a-discussion-comment-legacy
        /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}
        
        arguments:
        team_id -- 
        discussion_number -- 
        comment_number -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}
    #
    def TeamsDeleteDiscussionInOrg(self, org:str, team_slug:str, discussion_number:int):
        """Delete a discussion from a team's page. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#delete-a-discussion
        /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        discussion_number -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /teams/{team_id}/discussions/{discussion_number}
    #
    def TeamsDeleteDiscussionLegacy(self, team_id:int, discussion_number:int):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`Delete a discussion`](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#delete-a-discussion) endpoint.

Delete a discussion from a team's page. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#delete-a-discussion-legacy
        /teams/{team_id}/discussions/{discussion_number}
        
        arguments:
        team_id -- 
        discussion_number -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/teams/{team_id}/discussions/{discussion_number}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/teams/{team_slug}
    #
    def TeamsDeleteInOrg(self, org:str, team_slug:str):
        """To delete a team, the authenticated user must be an organization owner or team maintainer.

If you are an organization owner, deleting a parent team will delete all of its child teams as well.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#delete-a-team
        /orgs/{org}/teams/{team_slug}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/teams/{team_slug}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /teams/{team_id}
    #
    def TeamsDeleteLegacy(self, team_id:int):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Delete a team](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#delete-a-team) endpoint.

To delete a team, the authenticated user must be an organization owner or team maintainer.

If you are an organization owner, deleting a parent team will delete all of its child teams as well.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams/#delete-a-team-legacy
        /teams/{team_id}
        
        arguments:
        team_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/teams/{team_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/teams/{team_slug}
    #
    def TeamsGetByName(self, org:str, team_slug:str):
        """Gets a team using the team's `slug`. GitHub Enterprise Server generates the `slug` from the team `name`.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#get-a-team-by-name
        /orgs/{org}/teams/{team_slug}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/teams/{team_slug}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return FullTeam(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}
    #
    def TeamsGetDiscussionCommentInOrg(self, org:str, team_slug:str, discussion_number:int, comment_number:int):
        """Get a specific comment on a team discussion. OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments/{comment_number}`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#get-a-discussion-comment
        /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        discussion_number -- 
        comment_number -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return TeamDiscussionComment(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}
    #
    def TeamsGetDiscussionCommentLegacy(self, team_id:int, discussion_number:int, comment_number:int):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Get a discussion comment](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#get-a-discussion-comment) endpoint.

Get a specific comment on a team discussion. OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#get-a-discussion-comment-legacy
        /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}
        
        arguments:
        team_id -- 
        discussion_number -- 
        comment_number -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return TeamDiscussionComment(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}
    #
    def TeamsGetDiscussionInOrg(self, org:str, team_slug:str, discussion_number:int):
        """Get a specific discussion on a team's page. OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#get-a-discussion
        /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        discussion_number -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return TeamDiscussion(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /teams/{team_id}/discussions/{discussion_number}
    #
    def TeamsGetDiscussionLegacy(self, team_id:int, discussion_number:int):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Get a discussion](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#get-a-discussion) endpoint.

Get a specific discussion on a team's page. OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#get-a-discussion-legacy
        /teams/{team_id}/discussions/{discussion_number}
        
        arguments:
        team_id -- 
        discussion_number -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/teams/{team_id}/discussions/{discussion_number}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return TeamDiscussion(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /teams/{team_id}
    #
    def TeamsGetLegacy(self, team_id:int):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the [Get a team by name](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#get-a-team-by-name) endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams/#get-a-team-legacy
        /teams/{team_id}
        
        arguments:
        team_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/teams/{team_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return FullTeam(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /teams/{team_id}/members/{username}
    #
    def TeamsGetMemberLegacy(self, team_id:int, username:str):
        """The "Get team member" endpoint (described below) is deprecated.

We recommend using the [Get team membership for a user](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#get-team-membership-for-a-user) endpoint instead. It allows you to get both active and pending memberships.

To list members in a team, the team must be visible to the authenticated user.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#get-team-member-legacy
        /teams/{team_id}/members/{username}
        
        arguments:
        team_id -- 
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/teams/{team_id}/members/{username}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/teams/{team_slug}/memberships/{username}
    #
    def TeamsGetMembershipForUserInOrg(self, org:str, team_slug:str, username:str):
        """Team members will include the members of child teams.

To get a user's membership with a team, the team must be visible to the authenticated user.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/memberships/{username}`.

**Note:**
The response contains the `state` of the membership and the member's `role`.

The `role` for organization owners is set to `maintainer`. For more information about `maintainer` roles, see see [Create a team](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#create-a-team).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#get-team-membership-for-a-user
        /orgs/{org}/teams/{team_slug}/memberships/{username}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/teams/{team_slug}/memberships/{username}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return TeamMembership(**r.json())
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # get /teams/{team_id}/memberships/{username}
    #
    def TeamsGetMembershipForUserLegacy(self, team_id:int, username:str):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Get team membership for a user](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#get-team-membership-for-a-user) endpoint.

Team members will include the members of child teams.

To get a user's membership with a team, the team must be visible to the authenticated user.

**Note:**
The response contains the `state` of the membership and the member's `role`.

The `role` for organization owners is set to `maintainer`. For more information about `maintainer` roles, see [Create a team](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#create-a-team).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#get-team-membership-for-a-user-legacy
        /teams/{team_id}/memberships/{username}
        
        arguments:
        team_id -- 
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/teams/{team_id}/memberships/{username}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return TeamMembership(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/teams
    #
    def TeamsList(self, org:str,per_page=30, page=1):
        """Lists all teams in an organization that are visible to the authenticated user.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#list-teams
        /orgs/{org}/teams
        
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
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/teams", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Team(**entry) for entry in r.json() ]
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/teams/{team_slug}/teams
    #
    def TeamsListChildInOrg(self, org:str, team_slug:str,per_page=30, page=1):
        """Lists the child teams of the team specified by `{team_slug}`.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/teams`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#list-child-teams
        /orgs/{org}/teams/{team_slug}/teams
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/teams/{team_slug}/teams", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Team(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /teams/{team_id}/teams
    #
    def TeamsListChildLegacy(self, team_id:int,per_page=30, page=1):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List child teams`](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#list-child-teams) endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams/#list-child-teams-legacy
        /teams/{team_id}/teams
        
        arguments:
        team_id -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/teams/{team_id}/teams", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Team(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments
    #
    def TeamsListDiscussionCommentsInOrg(self, org:str, team_slug:str, discussion_number:int,direction='desc', per_page=30, page=1):
        """List all comments on a team discussion. OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#list-discussion-comments
        /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        discussion_number -- 
        direction -- One of `asc` (ascending) or `desc` (descending).
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if direction is not None:
            data['direction'] = direction
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and TeamDiscussionComment(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /teams/{team_id}/discussions/{discussion_number}/comments
    #
    def TeamsListDiscussionCommentsLegacy(self, team_id:int, discussion_number:int,direction='desc', per_page=30, page=1):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [List discussion comments](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#list-discussion-comments) endpoint.

List all comments on a team discussion. OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#list-discussion-comments-legacy
        /teams/{team_id}/discussions/{discussion_number}/comments
        
        arguments:
        team_id -- 
        discussion_number -- 
        direction -- One of `asc` (ascending) or `desc` (descending).
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if direction is not None:
            data['direction'] = direction
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/teams/{team_id}/discussions/{discussion_number}/comments", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and TeamDiscussionComment(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/teams/{team_slug}/discussions
    #
    def TeamsListDiscussionsInOrg(self, org:str, team_slug:str,direction='desc', per_page=30, page=1, pinned:str=None):
        """List all discussions on a team's page. OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/discussions`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#list-discussions
        /orgs/{org}/teams/{team_slug}/discussions
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        direction -- One of `asc` (ascending) or `desc` (descending).
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        pinned -- Pinned discussions only filter
        
        """
        
        data = {}
        if direction is not None:
            data['direction'] = direction
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        if pinned is not None:
            data['pinned'] = pinned
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/teams/{team_slug}/discussions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and TeamDiscussion(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /teams/{team_id}/discussions
    #
    def TeamsListDiscussionsLegacy(self, team_id:int,direction='desc', per_page=30, page=1):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List discussions`](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#list-discussions) endpoint.

List all discussions on a team's page. OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#list-discussions-legacy
        /teams/{team_id}/discussions
        
        arguments:
        team_id -- 
        direction -- One of `asc` (ascending) or `desc` (descending).
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if direction is not None:
            data['direction'] = direction
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/teams/{team_id}/discussions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and TeamDiscussion(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /user/teams
    #
    def TeamsListForAuthenticatedUser(self, per_page=30, page=1):
        """List all of the teams across all of the organizations to which the authenticated user belongs. This method requires `user`, `repo`, or `read:org` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/) when authenticating via [OAuth](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#list-teams-for-the-authenticated-user
        /user/teams
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/user/teams", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and FullTeam(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/teams/{team_slug}/members
    #
    def TeamsListMembersInOrg(self, org:str, team_slug:str,role='all', per_page=30, page=1):
        """Team members will include the members of child teams.

To list members in a team, the team must be visible to the authenticated user.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#list-team-members
        /orgs/{org}/teams/{team_slug}/members
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        role -- Filters members returned by their role in the team. Can be one of:  
\* `member` - normal members of the team.  
\* `maintainer` - team maintainers.  
\* `all` - all members of the team.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if role is not None:
            data['role'] = role
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/teams/{team_slug}/members", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and SimpleUser(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /teams/{team_id}/members
    #
    def TeamsListMembersLegacy(self, team_id:int,role='all', per_page=30, page=1):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List team members`](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#list-team-members) endpoint.

Team members will include the members of child teams.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#list-team-members-legacy
        /teams/{team_id}/members
        
        arguments:
        team_id -- 
        role -- Filters members returned by their role in the team. Can be one of:  
\* `member` - normal members of the team.  
\* `maintainer` - team maintainers.  
\* `all` - all members of the team.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if role is not None:
            data['role'] = role
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/teams/{team_id}/members", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and SimpleUser(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/teams/{team_slug}/projects
    #
    def TeamsListProjectsInOrg(self, org:str, team_slug:str,per_page=30, page=1):
        """Lists the organization projects for a team.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/projects`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#list-team-projects
        /orgs/{org}/teams/{team_slug}/projects
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/teams/{team_slug}/projects", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and TeamProject(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /teams/{team_id}/projects
    #
    def TeamsListProjectsLegacy(self, team_id:int,per_page=30, page=1):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List team projects`](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#list-team-projects) endpoint.

Lists the organization projects for a team.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams/#list-team-projects-legacy
        /teams/{team_id}/projects
        
        arguments:
        team_id -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/teams/{team_id}/projects", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and TeamProject(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/teams/{team_slug}/repos
    #
    def TeamsListReposInOrg(self, org:str, team_slug:str,per_page=30, page=1):
        """Lists a team's repositories visible to the authenticated user.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/repos`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#list-team-repositories
        /orgs/{org}/teams/{team_slug}/repos
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/teams/{team_slug}/repos", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and MinimalRepository(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /teams/{team_id}/repos
    #
    def TeamsListReposLegacy(self, team_id:int,per_page=30, page=1):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [List team repositories](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#list-team-repositories) endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams/#list-team-repositories-legacy
        /teams/{team_id}/repos
        
        arguments:
        team_id -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/teams/{team_id}/repos", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and MinimalRepository(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /teams/{team_id}/members/{username}
    #
    def TeamsRemoveMemberLegacy(self, team_id:int, username:str):
        """The "Remove team member" endpoint (described below) is deprecated.

We recommend using the [Remove team membership for a user](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#remove-team-membership-for-a-user) endpoint instead. It allows you to remove both active and pending memberships.

Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

To remove a team member, the authenticated user must have 'admin' permissions to the team or be an owner of the org that the team is associated with. Removing a team member does not delete the user, it just removes them from the team.

**Note:** When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#remove-team-member-legacy
        /teams/{team_id}/members/{username}
        
        arguments:
        team_id -- 
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/teams/{team_id}/members/{username}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/teams/{team_slug}/memberships/{username}
    #
    def TeamsRemoveMembershipForUserInOrg(self, org:str, team_slug:str, username:str):
        """Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

To remove a membership between a user and a team, the authenticated user must have 'admin' permissions to the team or be an owner of the organization that the team is associated with. Removing team membership does not delete the user, it just removes their membership from the team.

**Note:** When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}/memberships/{username}`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#remove-team-membership-for-a-user
        /orgs/{org}/teams/{team_slug}/memberships/{username}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/teams/{team_slug}/memberships/{username}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /teams/{team_id}/memberships/{username}
    #
    def TeamsRemoveMembershipForUserLegacy(self, team_id:int, username:str):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove team membership for a user](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#remove-team-membership-for-a-user) endpoint.

Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

To remove a membership between a user and a team, the authenticated user must have 'admin' permissions to the team or be an owner of the organization that the team is associated with. Removing team membership does not delete the user, it just removes their membership from the team.

**Note:** When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#remove-team-membership-for-a-user-legacy
        /teams/{team_id}/memberships/{username}
        
        arguments:
        team_id -- 
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/teams/{team_id}/memberships/{username}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/teams/{team_slug}/projects/{project_id}
    #
    def TeamsRemoveProjectInOrg(self, org:str, team_slug:str, project_id:int):
        """Removes an organization project from a team. An organization owner or a team maintainer can remove any project from the team. To remove a project from a team as an organization member, the authenticated user must have `read` access to both the team and project, or `admin` access to the team or project. This endpoint removes the project from the team, but does not delete the project.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}/projects/{project_id}`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#remove-a-project-from-a-team
        /orgs/{org}/teams/{team_slug}/projects/{project_id}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        project_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/teams/{team_slug}/projects/{project_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /teams/{team_id}/projects/{project_id}
    #
    def TeamsRemoveProjectLegacy(self, team_id:int, project_id:int):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a project from a team](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#remove-a-project-from-a-team) endpoint.

Removes an organization project from a team. An organization owner or a team maintainer can remove any project from the team. To remove a project from a team as an organization member, the authenticated user must have `read` access to both the team and project, or `admin` access to the team or project. **Note:** This endpoint removes the project from the team, but does not delete it.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams/#remove-a-project-from-a-team-legacy
        /teams/{team_id}/projects/{project_id}
        
        arguments:
        team_id -- 
        project_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/teams/{team_id}/projects/{project_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 415:
            return Preview_header_missing(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}
    #
    def TeamsRemoveRepoInOrg(self, org:str, team_slug:str, owner:str, repo:str):
        """If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. This does not delete the repository, it just removes it from the team.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams/#remove-a-repository-from-a-team
        /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /teams/{team_id}/repos/{owner}/{repo}
    #
    def TeamsRemoveRepoLegacy(self, team_id:int, owner:str, repo:str):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a repository from a team](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#remove-a-repository-from-a-team) endpoint.

If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. NOTE: This does not delete the repository, it just removes it from the team.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams/#remove-a-repository-from-a-team-legacy
        /teams/{team_id}/repos/{owner}/{repo}
        
        arguments:
        team_id -- 
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/teams/{team_id}/repos/{owner}/{repo}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # patch /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}
    #
    def TeamsUpdateDiscussionCommentInOrg(self, org:str, team_slug:str, discussion_number:int, comment_number:int,body:str):
        """Edits the body text of a discussion comment. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `PATCH /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments/{comment_number}`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#update-a-discussion-comment
        /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        discussion_number -- 
        comment_number -- 
        body -- The discussion comment's body text.
        

        """
    
        data = {
        'body': body,
        
        }
        

        
        r = self._session.patch(f"{self._url}/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return TeamDiscussionComment(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}
    #
    def TeamsUpdateDiscussionCommentLegacy(self, team_id:int, discussion_number:int, comment_number:int,body:str):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a discussion comment](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#update-a-discussion-comment) endpoint.

Edits the body text of a discussion comment. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#update-a-discussion-comment-legacy
        /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}
        
        arguments:
        team_id -- 
        discussion_number -- 
        comment_number -- 
        body -- The discussion comment's body text.
        

        """
    
        data = {
        'body': body,
        
        }
        

        
        r = self._session.patch(f"{self._url}/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return TeamDiscussionComment(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}
    #
    def TeamsUpdateDiscussionInOrg(self, org:str, team_slug:str, discussion_number:int,title:str=None, body:str=None):
        """Edits the title and body text of a discussion post. Only the parameters you provide are updated. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `PATCH /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#update-a-discussion
        /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        discussion_number -- 
        title -- The discussion post's title.
        body -- The discussion post's body text.
        

        """
    
        data = {
        'title': title,
        'body': body,
        
        }
        

        
        r = self._session.patch(f"{self._url}/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return TeamDiscussion(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /teams/{team_id}/discussions/{discussion_number}
    #
    def TeamsUpdateDiscussionLegacy(self, team_id:int, discussion_number:int,title:str=None, body:str=None):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a discussion](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#update-a-discussion) endpoint.

Edits the title and body text of a discussion post. Only the parameters you provide are updated. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#update-a-discussion-legacy
        /teams/{team_id}/discussions/{discussion_number}
        
        arguments:
        team_id -- 
        discussion_number -- 
        title -- The discussion post's title.
        body -- The discussion post's body text.
        

        """
    
        data = {
        'title': title,
        'body': body,
        
        }
        

        
        r = self._session.patch(f"{self._url}/teams/{team_id}/discussions/{discussion_number}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return TeamDiscussion(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /orgs/{org}/teams/{team_slug}
    #
    def TeamsUpdateInOrg(self, org:str, team_slug:str,name:str=None, description:str=None, privacy:str=None, permission:str='pull', parent_team_id:int=None):
        """To edit a team, the authenticated user must either be an organization owner or a team maintainer.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `PATCH /organizations/{org_id}/team/{team_id}`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams#update-a-team
        /orgs/{org}/teams/{team_slug}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        name -- The name of the team.
        description -- The description of the team.
        privacy -- The level of privacy this team should have. Editing teams without specifying this parameter leaves `privacy` intact. When a team is nested, the `privacy` for parent teams cannot be `secret`. The options are:  
**For a non-nested team:**  
\* `secret` - only visible to organization owners and members of this team.  
\* `closed` - visible to all members of this organization.  
**For a parent or child team:**  
\* `closed` - visible to all members of this organization.
        permission -- **Deprecated**. The permission that new repositories will be added to the team with when none is specified. Can be one of:  
\* `pull` - team members can pull, but not push to or administer newly-added repositories.  
\* `push` - team members can pull and push, but not administer newly-added repositories.  
\* `admin` - team members can pull, push and administer newly-added repositories.
        parent_team_id -- The ID of a team to set as the parent team.
        

        """
    
        data = {
        'name': name,
        'description': description,
        'privacy': privacy,
        'permission': permission,
        'parent_team_id': parent_team_id,
        
        }
        

        
        r = self._session.patch(f"{self._url}/orgs/{org}/teams/{team_slug}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return FullTeam(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /teams/{team_id}
    #
    def TeamsUpdateLegacy(self, team_id:int,name:str, description:str=None, privacy:str=None, permission:str='pull', parent_team_id:int=None):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a team](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#update-a-team) endpoint.

To edit a team, the authenticated user must either be an organization owner or a team maintainer.

**Note:** With nested teams, the `privacy` for parent teams cannot be `secret`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/teams/#update-a-team-legacy
        /teams/{team_id}
        
        arguments:
        team_id -- 
        name -- The name of the team.
        description -- The description of the team.
        privacy -- The level of privacy this team should have. Editing teams without specifying this parameter leaves `privacy` intact. The options are:  
**For a non-nested team:**  
\* `secret` - only visible to organization owners and members of this team.  
\* `closed` - visible to all members of this organization.  
**For a parent or child team:**  
\* `closed` - visible to all members of this organization.
        permission -- **Deprecated**. The permission that new repositories will be added to the team with when none is specified. Can be one of:  
\* `pull` - team members can pull, but not push to or administer newly-added repositories.  
\* `push` - team members can pull and push, but not administer newly-added repositories.  
\* `admin` - team members can pull, push and administer newly-added repositories.
        parent_team_id -- The ID of a team to set as the parent team.
        

        """
    
        data = {
        'name': name,
        'description': description,
        'privacy': privacy,
        'permission': permission,
        'parent_team_id': parent_team_id,
        
        }
        

        
        r = self._session.patch(f"{self._url}/teams/{team_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return FullTeam(**r.json())
            
        if r.status_code == 201:
            return FullTeam(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
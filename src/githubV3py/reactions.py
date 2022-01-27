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

class Reactions(object):


    #
    # post /repos/{owner}/{repo}/comments/{comment_id}/reactions
    #
    def ReactionsCreateForCommitComment(self, owner:str, repo:str, comment_id:int,content:str):
        """Create a reaction to a [commit comment](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#comments). A response with an HTTP `200` status means that you already added the reaction type to this commit comment.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#create-reaction-for-a-commit-comment
        /repos/{owner}/{repo}/comments/{comment_id}/reactions
        
        arguments:
        owner -- 
        repo -- 
        comment_id -- comment_id parameter
        content -- The [reaction type](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#reaction-types) to add to the commit comment.
        

        """
    
        data = {
        'content': content,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/comments/{comment_id}/reactions", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Reaction(**r.json())
            
        if r.status_code == 201:
            return Reaction(**r.json())
            
        if r.status_code == 415:
            return Preview_header_missing(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/issues/{issue_number}/reactions
    #
    def ReactionsCreateForIssue(self, owner:str, repo:str, issue_number:int,content:str):
        """Create a reaction to an [issue](https://docs.github.com/enterprise-server@3.3/rest/reference/issues/). A response with an HTTP `200` status means that you already added the reaction type to this issue.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#create-reaction-for-an-issue
        /repos/{owner}/{repo}/issues/{issue_number}/reactions
        
        arguments:
        owner -- 
        repo -- 
        issue_number -- issue_number parameter
        content -- The [reaction type](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#reaction-types) to add to the issue.
        

        """
    
        data = {
        'content': content,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/reactions", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Reaction(**r.json())
            
        if r.status_code == 201:
            return Reaction(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions
    #
    def ReactionsCreateForIssueComment(self, owner:str, repo:str, comment_id:int,content:str):
        """Create a reaction to an [issue comment](https://docs.github.com/enterprise-server@3.3/rest/reference/issues#comments). A response with an HTTP `200` status means that you already added the reaction type to this issue comment.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#create-reaction-for-an-issue-comment
        /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions
        
        arguments:
        owner -- 
        repo -- 
        comment_id -- comment_id parameter
        content -- The [reaction type](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#reaction-types) to add to the issue comment.
        

        """
    
        data = {
        'content': content,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Reaction(**r.json())
            
        if r.status_code == 201:
            return Reaction(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions
    #
    def ReactionsCreateForPullRequestReviewComment(self, owner:str, repo:str, comment_id:int,content:str):
        """Create a reaction to a [pull request review comment](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#comments). A response with an HTTP `200` status means that you already added the reaction type to this pull request review comment.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#create-reaction-for-a-pull-request-review-comment
        /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions
        
        arguments:
        owner -- 
        repo -- 
        comment_id -- comment_id parameter
        content -- The [reaction type](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#reaction-types) to add to the pull request review comment.
        

        """
    
        data = {
        'content': content,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Reaction(**r.json())
            
        if r.status_code == 201:
            return Reaction(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/releases/{release_id}/reactions
    #
    def ReactionsCreateForRelease(self, owner:str, repo:str, release_id:int,content:str):
        """Create a reaction to a [release](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#releases). A response with a `Status: 200 OK` means that you already added the reaction type to this release.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions/#create-reaction-for-a-release
        /repos/{owner}/{repo}/releases/{release_id}/reactions
        
        arguments:
        owner -- 
        repo -- 
        release_id -- release_id parameter
        content -- The [reaction type](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#reaction-types) to add to the release.
        

        """
    
        data = {
        'content': content,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/releases/{release_id}/reactions", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Reaction(**r.json())
            
        if r.status_code == 201:
            return Reaction(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions
    #
    def ReactionsCreateForTeamDiscussionCommentInOrg(self, org:str, team_slug:str, discussion_number:int, comment_number:int,content:str):
        """Create a reaction to a [team discussion comment](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#discussion-comments). OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP `200` status means that you already added the reaction type to this team discussion comment.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `POST /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#create-reaction-for-a-team-discussion-comment
        /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        discussion_number -- 
        comment_number -- 
        content -- The [reaction type](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#reaction-types) to add to the team discussion comment.
        

        """
    
        data = {
        'content': content,
        
        }
        

        
        r = self._session.post(f"{self._url}/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Reaction(**r.json())
            
        if r.status_code == 201:
            return Reaction(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions
    #
    def ReactionsCreateForTeamDiscussionCommentLegacy(self, team_id:int, discussion_number:int, comment_number:int,content:str):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new "[Create reaction for a team discussion comment](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#create-reaction-for-a-team-discussion-comment)" endpoint.

Create a reaction to a [team discussion comment](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#discussion-comments). OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP `200` status means that you already added the reaction type to this team discussion comment.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions/#create-reaction-for-a-team-discussion-comment-legacy
        /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions
        
        arguments:
        team_id -- 
        discussion_number -- 
        comment_number -- 
        content -- The [reaction type](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#reaction-types) to add to the team discussion comment.
        

        """
    
        data = {
        'content': content,
        
        }
        

        
        r = self._session.post(f"{self._url}/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Reaction(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions
    #
    def ReactionsCreateForTeamDiscussionInOrg(self, org:str, team_slug:str, discussion_number:int,content:str):
        """Create a reaction to a [team discussion](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#discussions). OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP `200` status means that you already added the reaction type to this team discussion.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `POST /organizations/:org_id/team/:team_id/discussions/:discussion_number/reactions`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#create-reaction-for-a-team-discussion
        /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        discussion_number -- 
        content -- The [reaction type](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#reaction-types) to add to the team discussion.
        

        """
    
        data = {
        'content': content,
        
        }
        

        
        r = self._session.post(f"{self._url}/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Reaction(**r.json())
            
        if r.status_code == 201:
            return Reaction(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /teams/{team_id}/discussions/{discussion_number}/reactions
    #
    def ReactionsCreateForTeamDiscussionLegacy(self, team_id:int, discussion_number:int,content:str):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`Create reaction for a team discussion`](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#create-reaction-for-a-team-discussion) endpoint.

Create a reaction to a [team discussion](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#discussions). OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP `200` status means that you already added the reaction type to this team discussion.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions/#create-reaction-for-a-team-discussion-legacy
        /teams/{team_id}/discussions/{discussion_number}/reactions
        
        arguments:
        team_id -- 
        discussion_number -- 
        content -- The [reaction type](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#reaction-types) to add to the team discussion.
        

        """
    
        data = {
        'content': content,
        
        }
        

        
        r = self._session.post(f"{self._url}/teams/{team_id}/discussions/{discussion_number}/reactions", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Reaction(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/comments/{comment_id}/reactions/{reaction_id}
    #
    def ReactionsDeleteForCommitComment(self, owner:str, repo:str, comment_id:int, reaction_id:int):
        """**Note:** You can also specify a repository by `repository_id` using the route `DELETE /repositories/:repository_id/comments/:comment_id/reactions/:reaction_id`.

Delete a reaction to a [commit comment](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#comments).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#delete-a-commit-comment-reaction
        /repos/{owner}/{repo}/comments/{comment_id}/reactions/{reaction_id}
        
        arguments:
        owner -- 
        repo -- 
        comment_id -- comment_id parameter
        reaction_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/comments/{comment_id}/reactions/{reaction_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/issues/{issue_number}/reactions/{reaction_id}
    #
    def ReactionsDeleteForIssue(self, owner:str, repo:str, issue_number:int, reaction_id:int):
        """**Note:** You can also specify a repository by `repository_id` using the route `DELETE /repositories/:repository_id/issues/:issue_number/reactions/:reaction_id`.

Delete a reaction to an [issue](https://docs.github.com/enterprise-server@3.3/rest/reference/issues/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#delete-an-issue-reaction
        /repos/{owner}/{repo}/issues/{issue_number}/reactions/{reaction_id}
        
        arguments:
        owner -- 
        repo -- 
        issue_number -- issue_number parameter
        reaction_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/reactions/{reaction_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions/{reaction_id}
    #
    def ReactionsDeleteForIssueComment(self, owner:str, repo:str, comment_id:int, reaction_id:int):
        """**Note:** You can also specify a repository by `repository_id` using the route `DELETE delete /repositories/:repository_id/issues/comments/:comment_id/reactions/:reaction_id`.

Delete a reaction to an [issue comment](https://docs.github.com/enterprise-server@3.3/rest/reference/issues#comments).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#delete-an-issue-comment-reaction
        /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions/{reaction_id}
        
        arguments:
        owner -- 
        repo -- 
        comment_id -- comment_id parameter
        reaction_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions/{reaction_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions/{reaction_id}
    #
    def ReactionsDeleteForPullRequestComment(self, owner:str, repo:str, comment_id:int, reaction_id:int):
        """**Note:** You can also specify a repository by `repository_id` using the route `DELETE /repositories/:repository_id/pulls/comments/:comment_id/reactions/:reaction_id.`

Delete a reaction to a [pull request review comment](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#review-comments).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#delete-a-pull-request-comment-reaction
        /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions/{reaction_id}
        
        arguments:
        owner -- 
        repo -- 
        comment_id -- comment_id parameter
        reaction_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions/{reaction_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions/{reaction_id}
    #
    def ReactionsDeleteForTeamDiscussion(self, org:str, team_slug:str, discussion_number:int, reaction_id:int):
        """**Note:** You can also specify a team or organization with `team_id` and `org_id` using the route `DELETE /organizations/:org_id/team/:team_id/discussions/:discussion_number/reactions/:reaction_id`.

Delete a reaction to a [team discussion](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#discussions). OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#delete-team-discussion-reaction
        /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions/{reaction_id}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        discussion_number -- 
        reaction_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions/{reaction_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions/{reaction_id}
    #
    def ReactionsDeleteForTeamDiscussionComment(self, org:str, team_slug:str, discussion_number:int, comment_number:int, reaction_id:int):
        """**Note:** You can also specify a team or organization with `team_id` and `org_id` using the route `DELETE /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions/:reaction_id`.

Delete a reaction to a [team discussion comment](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#discussion-comments). OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#delete-team-discussion-comment-reaction
        /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions/{reaction_id}
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        discussion_number -- 
        comment_number -- 
        reaction_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions/{reaction_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /reactions/{reaction_id}
    #
    def ReactionsDeleteLegacy(self, reaction_id:int):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Reactions API. We recommend migrating your existing code to use the new delete reactions endpoints. For more information, see this [blog post](https://developer.github.com/changes/2020-02-26-new-delete-reactions-endpoints/).

OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), when deleting a [team discussion](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#discussions) or [team discussion comment](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#discussion-comments).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions/#delete-a-reaction-legacy
        /reactions/{reaction_id}
        
        arguments:
        reaction_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/reactions/{reaction_id}", 
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
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/comments/{comment_id}/reactions
    #
    def ReactionsListForCommitComment(self, owner:str, repo:str, comment_id:int,content=None, per_page=30, page=1):
        """List the reactions to a [commit comment](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#comments).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#list-reactions-for-a-commit-comment
        /repos/{owner}/{repo}/comments/{comment_id}/reactions
        
        arguments:
        owner -- 
        repo -- 
        comment_id -- comment_id parameter
        content -- Returns a single [reaction type](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion comment.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if content is not None:
            data['content'] = content
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/comments/{comment_id}/reactions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Reaction(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/issues/{issue_number}/reactions
    #
    def ReactionsListForIssue(self, owner:str, repo:str, issue_number:int,content=None, per_page=30, page=1):
        """List the reactions to an [issue](https://docs.github.com/enterprise-server@3.3/rest/reference/issues).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#list-reactions-for-an-issue
        /repos/{owner}/{repo}/issues/{issue_number}/reactions
        
        arguments:
        owner -- 
        repo -- 
        issue_number -- issue_number parameter
        content -- Returns a single [reaction type](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion comment.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if content is not None:
            data['content'] = content
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/reactions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Reaction(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions
    #
    def ReactionsListForIssueComment(self, owner:str, repo:str, comment_id:int,content=None, per_page=30, page=1):
        """List the reactions to an [issue comment](https://docs.github.com/enterprise-server@3.3/rest/reference/issues#comments).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#list-reactions-for-an-issue-comment
        /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions
        
        arguments:
        owner -- 
        repo -- 
        comment_id -- comment_id parameter
        content -- Returns a single [reaction type](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion comment.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if content is not None:
            data['content'] = content
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Reaction(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions
    #
    def ReactionsListForPullRequestReviewComment(self, owner:str, repo:str, comment_id:int,content=None, per_page=30, page=1):
        """List the reactions to a [pull request review comment](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#review-comments).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#list-reactions-for-a-pull-request-review-comment
        /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions
        
        arguments:
        owner -- 
        repo -- 
        comment_id -- comment_id parameter
        content -- Returns a single [reaction type](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion comment.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if content is not None:
            data['content'] = content
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Reaction(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions
    #
    def ReactionsListForTeamDiscussionCommentInOrg(self, org:str, team_slug:str, discussion_number:int, comment_number:int,content=None, per_page=30, page=1):
        """List the reactions to a [team discussion comment](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#discussion-comments/). OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#list-reactions-for-a-team-discussion-comment
        /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        discussion_number -- 
        comment_number -- 
        content -- Returns a single [reaction type](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion comment.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if content is not None:
            data['content'] = content
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Reaction(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions
    #
    def ReactionsListForTeamDiscussionCommentLegacy(self, team_id:int, discussion_number:int, comment_number:int,content=None, per_page=30, page=1):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List reactions for a team discussion comment`](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#list-reactions-for-a-team-discussion-comment) endpoint.

List the reactions to a [team discussion comment](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#discussion-comments). OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions/#list-reactions-for-a-team-discussion-comment-legacy
        /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions
        
        arguments:
        team_id -- 
        discussion_number -- 
        comment_number -- 
        content -- Returns a single [reaction type](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion comment.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if content is not None:
            data['content'] = content
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Reaction(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions
    #
    def ReactionsListForTeamDiscussionInOrg(self, org:str, team_slug:str, discussion_number:int,content=None, per_page=30, page=1):
        """List the reactions to a [team discussion](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#discussions). OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/:org_id/team/:team_id/discussions/:discussion_number/reactions`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#list-reactions-for-a-team-discussion
        /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions
        
        arguments:
        org -- 
        team_slug -- team_slug parameter
        discussion_number -- 
        content -- Returns a single [reaction type](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion comment.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if content is not None:
            data['content'] = content
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Reaction(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /teams/{team_id}/discussions/{discussion_number}/reactions
    #
    def ReactionsListForTeamDiscussionLegacy(self, team_id:int, discussion_number:int,content=None, per_page=30, page=1):
        """**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List reactions for a team discussion`](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#list-reactions-for-a-team-discussion) endpoint.

List the reactions to a [team discussion](https://docs.github.com/enterprise-server@3.3/rest/reference/teams#discussions). OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/enterprise-server@3.3/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/reactions/#list-reactions-for-a-team-discussion-legacy
        /teams/{team_id}/discussions/{discussion_number}/reactions
        
        arguments:
        team_id -- 
        discussion_number -- 
        content -- Returns a single [reaction type](https://docs.github.com/enterprise-server@3.3/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion comment.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if content is not None:
            data['content'] = content
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/teams/{team_id}/discussions/{discussion_number}/reactions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Reaction(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
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

class Issues(object):


    #
    # post /repos/{owner}/{repo}/issues/{issue_number}/assignees
    #
    def IssuesAddAssignees(self, owner:str, repo:str, issue_number:int,assignees:list=[]):
        """Adds up to 10 assignees to an issue. Users already assigned to an issue are not replaced.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#add-assignees-to-an-issue
        /repos/{owner}/{repo}/issues/{issue_number}/assignees
        
        arguments:
        owner -- 
        repo -- 
        issue_number -- issue_number parameter
        assignees -- Usernames of people to assign this issue to. _NOTE: Only users with push access can add assignees to an issue. Assignees are silently ignored otherwise._
        

        """
    
        data = {
        'assignees': assignees,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/assignees", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Issue(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/issues/{issue_number}/labels
    #
    def IssuesAddLabels(self, owner:str, repo:str, issue_number:int,object:object):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#add-labels-to-an-issue
        /repos/{owner}/{repo}/issues/{issue_number}/labels
        
        arguments:
        owner -- 
        repo -- 
        issue_number -- issue_number parameter
        object -- 
        

        """
    
        data = {
        'object': object,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/labels", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return [ entry and Label(**entry) for entry in r.json() ]
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/assignees/{assignee}
    #
    def IssuesCheckUserCanBeAssigned(self, owner:str, repo:str, assignee:str):
        """Checks if a user has permission to be assigned to an issue in this repository.

If the `assignee` can be assigned to issues in the repository, a `204` header with no content is returned.

Otherwise a `404` status code is returned.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#check-if-a-user-can-be-assigned
        /repos/{owner}/{repo}/assignees/{assignee}
        
        arguments:
        owner -- 
        repo -- 
        assignee -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/assignees/{assignee}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/issues
    #
    def IssuesCreate(self, owner:str, repo:str,title, body:str=None, assignee:str=None, milestone=None, labels:list=[], assignees:list=[]):
        """Any user with pull access to a repository can create an issue. If [issues are disabled in the repository](https://help.github.com/articles/disabling-issues/), the API returns a `410 Gone` status.

This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#create-an-issue
        /repos/{owner}/{repo}/issues
        
        arguments:
        owner -- 
        repo -- 
        title -- The title of the issue.
        body -- The contents of the issue.
        assignee -- Login for the user that this issue should be assigned to. _NOTE: Only users with push access can set the assignee for new issues. The assignee is silently dropped otherwise. **This field is deprecated.**_
        milestone -- 
        labels -- Labels to associate with this issue. _NOTE: Only users with push access can set labels for new issues. Labels are silently dropped otherwise._
        assignees -- Logins for Users to assign to this issue. _NOTE: Only users with push access can set assignees for new issues. Assignees are silently dropped otherwise._
        

        """
    
        data = {
        'title': title,
        'body': body,
        'assignee': assignee,
        'milestone': milestone,
        'labels': labels,
        'assignees': assignees,
        
        }
        

        #
        # one or the other must be specified but not
        # both, not even an empty list[] or string
        #
        if not data['assignees']:
            del data['assignees']
        if not data['assignee']:
            del data['assignee']
        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/issues", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Issue(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 503:
            return Service_unavailable(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 410:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/issues/{issue_number}/comments
    #
    def IssuesCreateComment(self, owner:str, repo:str, issue_number:int,body:str):
        """This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#create-an-issue-comment
        /repos/{owner}/{repo}/issues/{issue_number}/comments
        
        arguments:
        owner -- 
        repo -- 
        issue_number -- issue_number parameter
        body -- The contents of the comment.
        

        """
    
        data = {
        'body': body,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/comments", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return IssueComment(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/labels
    #
    def IssuesCreateLabel(self, owner:str, repo:str,name:str, color:str=None, description:str=None):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#create-a-label
        /repos/{owner}/{repo}/labels
        
        arguments:
        owner -- 
        repo -- 
        name -- The name of the label. Emoji can be added to label names, using either native emoji or colon-style markup. For example, typing `:strawberry:` will render the emoji ![:strawberry:](https://github.githubassets.com/images/icons/emoji/unicode/1f353.png ":strawberry:"). For a full list of available emoji and codes, see "[Emoji cheat sheet](https://github.com/ikatyang/emoji-cheat-sheet)."
        color -- The [hexadecimal color code](http://www.color-hex.com/) for the label, without the leading `#`.
        description -- A short description of the label. Must be 100 characters or fewer.
        

        """
    
        data = {
        'name': name,
        'color': color,
        'description': description,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/labels", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Label(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/milestones
    #
    def IssuesCreateMilestone(self, owner:str, repo:str,title:str, state:str='open', description:str=None, due_on:datetime=None):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#create-a-milestone
        /repos/{owner}/{repo}/milestones
        
        arguments:
        owner -- 
        repo -- 
        title -- The title of the milestone.
        state -- The state of the milestone. Either `open` or `closed`.
        description -- A description of the milestone.
        due_on -- The milestone due date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        

        """
    
        data = {
        'title': title,
        'state': state,
        'description': description,
        'due_on': due_on,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/milestones", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Milestone(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/issues/comments/{comment_id}
    #
    def IssuesDeleteComment(self, owner:str, repo:str, comment_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#delete-an-issue-comment
        /repos/{owner}/{repo}/issues/comments/{comment_id}
        
        arguments:
        owner -- 
        repo -- 
        comment_id -- comment_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/issues/comments/{comment_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/labels/{name}
    #
    def IssuesDeleteLabel(self, owner:str, repo:str, name:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#delete-a-label
        /repos/{owner}/{repo}/labels/{name}
        
        arguments:
        owner -- 
        repo -- 
        name -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/labels/{name}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/milestones/{milestone_number}
    #
    def IssuesDeleteMilestone(self, owner:str, repo:str, milestone_number:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#delete-a-milestone
        /repos/{owner}/{repo}/milestones/{milestone_number}
        
        arguments:
        owner -- 
        repo -- 
        milestone_number -- milestone_number parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/milestones/{milestone_number}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/issues/{issue_number}
    #
    def IssuesGet(self, owner:str, repo:str, issue_number:int):
        """The API returns a [`301 Moved Permanently` status](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#http-redirects-redirects) if the issue was
[transferred](https://help.github.com/articles/transferring-an-issue-to-another-repository/) to another repository. If
the issue was transferred to or deleted from a repository where the authenticated user lacks read access, the API
returns a `404 Not Found` status. If the issue was deleted from a repository where the authenticated user has read
access, the API returns a `410 Gone` status. To receive webhook events for transferred and deleted issues, subscribe
to the [`issues`](https://docs.github.com/enterprise-server@3.3/webhooks/event-payloads/#issues) webhook.

**Note**: GitHub's REST API v3 considers every pull request an issue, but not every issue is a pull request. For this
reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by
the `pull_request` key. Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull
request id, use the "[List pull requests](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#list-pull-requests)" endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#get-an-issue
        /repos/{owner}/{repo}/issues/{issue_number}
        
        arguments:
        owner -- 
        repo -- 
        issue_number -- issue_number parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Issue(**r.json())
            
        if r.status_code == 301:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/issues/comments/{comment_id}
    #
    def IssuesGetComment(self, owner:str, repo:str, comment_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#get-an-issue-comment
        /repos/{owner}/{repo}/issues/comments/{comment_id}
        
        arguments:
        owner -- 
        repo -- 
        comment_id -- comment_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/issues/comments/{comment_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return IssueComment(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/issues/events/{event_id}
    #
    def IssuesGetEvent(self, owner:str, repo:str, event_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#get-an-issue-event
        /repos/{owner}/{repo}/issues/events/{event_id}
        
        arguments:
        owner -- 
        repo -- 
        event_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/issues/events/{event_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return IssueEvent(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/labels/{name}
    #
    def IssuesGetLabel(self, owner:str, repo:str, name:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#get-a-label
        /repos/{owner}/{repo}/labels/{name}
        
        arguments:
        owner -- 
        repo -- 
        name -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/labels/{name}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Label(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/milestones/{milestone_number}
    #
    def IssuesGetMilestone(self, owner:str, repo:str, milestone_number:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#get-a-milestone
        /repos/{owner}/{repo}/milestones/{milestone_number}
        
        arguments:
        owner -- 
        repo -- 
        milestone_number -- milestone_number parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/milestones/{milestone_number}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Milestone(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /issues
    #
    def IssuesList(self, filter='assigned', state='open', labels:str=None, sort='created', direction='desc', since:datetime=None, collab:bool=None, orgs:bool=None, owned:bool=None, pulls:bool=None, per_page=30, page=1):
        """List issues assigned to the authenticated user across all visible repositories including owned repositories, member
repositories, and organization repositories. You can use the `filter` query parameter to fetch issues that are not
necessarily assigned to you.


**Note**: GitHub's REST API v3 considers every pull request an issue, but not every issue is a pull request. For this
reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by
the `pull_request` key. Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull
request id, use the "[List pull requests](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#list-pull-requests)" endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#list-issues-assigned-to-the-authenticated-user
        /issues
        
        arguments:
        filter -- Indicates which sorts of issues to return. Can be one of:  
\* `assigned`: Issues assigned to you  
\* `created`: Issues created by you  
\* `mentioned`: Issues mentioning you  
\* `subscribed`: Issues you're subscribed to updates for  
\* `all` or `repos`: All issues the authenticated user can see, regardless of participation or creation
        state -- Indicates the state of the issues to return. Can be either `open`, `closed`, or `all`.
        labels -- A list of comma separated label names. Example: `bug,ui,@high`
        sort -- What to sort results by. Can be either `created`, `updated`, `comments`.
        direction -- One of `asc` (ascending) or `desc` (descending).
        since -- Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        collab -- 
        orgs -- 
        owned -- 
        pulls -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if filter is not None:
            data['filter'] = filter
        if state is not None:
            data['state'] = state
        if labels is not None:
            data['labels'] = labels
        if sort is not None:
            data['sort'] = sort
        if direction is not None:
            data['direction'] = direction
        if since is not None:
            data['since'] = since.isoformat()
        if collab is not None:
            data['collab'] = collab
        if orgs is not None:
            data['orgs'] = orgs
        if owned is not None:
            data['owned'] = owned
        if pulls is not None:
            data['pulls'] = pulls
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/issues", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Issue(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/assignees
    #
    def IssuesListAssignees(self, owner:str, repo:str,per_page=30, page=1):
        """Lists the [available assignees](https://help.github.com/articles/assigning-issues-and-pull-requests-to-other-github-users/) for issues in a repository.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#list-assignees
        /repos/{owner}/{repo}/assignees
        
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
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/assignees", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and SimpleUser(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/issues/{issue_number}/comments
    #
    def IssuesListComments(self, owner:str, repo:str, issue_number:int,since:datetime=None, per_page=30, page=1):
        """Issue Comments are ordered by ascending ID.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#list-issue-comments
        /repos/{owner}/{repo}/issues/{issue_number}/comments
        
        arguments:
        owner -- 
        repo -- 
        issue_number -- issue_number parameter
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
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/comments", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and IssueComment(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/issues/comments
    #
    def IssuesListCommentsForRepo(self, owner:str, repo:str,sort='created', direction='desc', since:datetime=None, per_page=30, page=1):
        """By default, Issue Comments are ordered by ascending ID.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#list-issue-comments-for-a-repository
        /repos/{owner}/{repo}/issues/comments
        
        arguments:
        owner -- 
        repo -- 
        sort -- One of `created` (when the repository was starred) or `updated` (when it was last pushed to).
        direction -- One of `asc` (ascending) or `desc` (descending).
        since -- Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if sort is not None:
            data['sort'] = sort
        if direction is not None:
            data['direction'] = direction
        if since is not None:
            data['since'] = since.isoformat()
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/issues/comments", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and IssueComment(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/issues/{issue_number}/events
    #
    def IssuesListEvents(self, owner:str, repo:str, issue_number:int,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#list-issue-events
        /repos/{owner}/{repo}/issues/{issue_number}/events
        
        arguments:
        owner -- 
        repo -- 
        issue_number -- issue_number parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/events", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry for entry in r.json() ]
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/issues/events
    #
    def IssuesListEventsForRepo(self, owner:str, repo:str,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#list-issue-events-for-a-repository
        /repos/{owner}/{repo}/issues/events
        
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
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/issues/events", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and IssueEvent(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/issues/{issue_number}/timeline
    #
    def IssuesListEventsForTimeline(self, owner:str, repo:str, issue_number:int,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#list-timeline-events-for-an-issue
        /repos/{owner}/{repo}/issues/{issue_number}/timeline
        
        arguments:
        owner -- 
        repo -- 
        issue_number -- issue_number parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/timeline", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /user/issues
    #
    def IssuesListForAuthenticatedUser(self, filter='assigned', state='open', labels:str=None, sort='created', direction='desc', since:datetime=None, per_page=30, page=1):
        """List issues across owned and member repositories assigned to the authenticated user.

**Note**: GitHub's REST API v3 considers every pull request an issue, but not every issue is a pull request. For this
reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by
the `pull_request` key. Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull
request id, use the "[List pull requests](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#list-pull-requests)" endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#list-user-account-issues-assigned-to-the-authenticated-user
        /user/issues
        
        arguments:
        filter -- Indicates which sorts of issues to return. Can be one of:  
\* `assigned`: Issues assigned to you  
\* `created`: Issues created by you  
\* `mentioned`: Issues mentioning you  
\* `subscribed`: Issues you're subscribed to updates for  
\* `all` or `repos`: All issues the authenticated user can see, regardless of participation or creation
        state -- Indicates the state of the issues to return. Can be either `open`, `closed`, or `all`.
        labels -- A list of comma separated label names. Example: `bug,ui,@high`
        sort -- What to sort results by. Can be either `created`, `updated`, `comments`.
        direction -- One of `asc` (ascending) or `desc` (descending).
        since -- Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if filter is not None:
            data['filter'] = filter
        if state is not None:
            data['state'] = state
        if labels is not None:
            data['labels'] = labels
        if sort is not None:
            data['sort'] = sort
        if direction is not None:
            data['direction'] = direction
        if since is not None:
            data['since'] = since.isoformat()
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/user/issues", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Issue(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/issues
    #
    def IssuesListForOrg(self, org:str,filter='assigned', state='open', labels:str=None, sort='created', direction='desc', since:datetime=None, per_page=30, page=1):
        """List issues in an organization assigned to the authenticated user.

**Note**: GitHub's REST API v3 considers every pull request an issue, but not every issue is a pull request. For this
reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by
the `pull_request` key. Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull
request id, use the "[List pull requests](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#list-pull-requests)" endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#list-organization-issues-assigned-to-the-authenticated-user
        /orgs/{org}/issues
        
        arguments:
        org -- 
        filter -- Indicates which sorts of issues to return. Can be one of:  
\* `assigned`: Issues assigned to you  
\* `created`: Issues created by you  
\* `mentioned`: Issues mentioning you  
\* `subscribed`: Issues you're subscribed to updates for  
\* `all` or `repos`: All issues the authenticated user can see, regardless of participation or creation
        state -- Indicates the state of the issues to return. Can be either `open`, `closed`, or `all`.
        labels -- A list of comma separated label names. Example: `bug,ui,@high`
        sort -- What to sort results by. Can be either `created`, `updated`, `comments`.
        direction -- One of `asc` (ascending) or `desc` (descending).
        since -- Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if filter is not None:
            data['filter'] = filter
        if state is not None:
            data['state'] = state
        if labels is not None:
            data['labels'] = labels
        if sort is not None:
            data['sort'] = sort
        if direction is not None:
            data['direction'] = direction
        if since is not None:
            data['since'] = since.isoformat()
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/issues", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Issue(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/issues
    #
    def IssuesListForRepo(self, owner:str, repo:str,milestone:str=None, state='open', assignee:str=None, creator:str=None, mentioned:str=None, labels:str=None, sort='created', direction='desc', since:datetime=None, per_page=30, page=1):
        """List issues in a repository.

**Note**: GitHub's REST API v3 considers every pull request an issue, but not every issue is a pull request. For this
reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by
the `pull_request` key. Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull
request id, use the "[List pull requests](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#list-pull-requests)" endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#list-repository-issues
        /repos/{owner}/{repo}/issues
        
        arguments:
        owner -- 
        repo -- 
        milestone -- If an `integer` is passed, it should refer to a milestone by its `number` field. If the string `*` is passed, issues with any milestone are accepted. If the string `none` is passed, issues without milestones are returned.
        state -- Indicates the state of the issues to return. Can be either `open`, `closed`, or `all`.
        assignee -- Can be the name of a user. Pass in `none` for issues with no assigned user, and `*` for issues assigned to any user.
        creator -- The user that created the issue.
        mentioned -- A user that's mentioned in the issue.
        labels -- A list of comma separated label names. Example: `bug,ui,@high`
        sort -- What to sort results by. Can be either `created`, `updated`, `comments`.
        direction -- One of `asc` (ascending) or `desc` (descending).
        since -- Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if milestone is not None:
            data['milestone'] = milestone
        if state is not None:
            data['state'] = state
        if assignee is not None:
            data['assignee'] = assignee
        if creator is not None:
            data['creator'] = creator
        if mentioned is not None:
            data['mentioned'] = mentioned
        if labels is not None:
            data['labels'] = labels
        if sort is not None:
            data['sort'] = sort
        if direction is not None:
            data['direction'] = direction
        if since is not None:
            data['since'] = since.isoformat()
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/issues", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Issue(**entry) for entry in r.json() ]
            
        if r.status_code == 301:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/milestones/{milestone_number}/labels
    #
    def IssuesListLabelsForMilestone(self, owner:str, repo:str, milestone_number:int,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#list-labels-for-issues-in-a-milestone
        /repos/{owner}/{repo}/milestones/{milestone_number}/labels
        
        arguments:
        owner -- 
        repo -- 
        milestone_number -- milestone_number parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/milestones/{milestone_number}/labels", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Label(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/labels
    #
    def IssuesListLabelsForRepo(self, owner:str, repo:str,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#list-labels-for-a-repository
        /repos/{owner}/{repo}/labels
        
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
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/labels", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Label(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/issues/{issue_number}/labels
    #
    def IssuesListLabelsOnIssue(self, owner:str, repo:str, issue_number:int,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#list-labels-for-an-issue
        /repos/{owner}/{repo}/issues/{issue_number}/labels
        
        arguments:
        owner -- 
        repo -- 
        issue_number -- issue_number parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/labels", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Label(**entry) for entry in r.json() ]
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/milestones
    #
    def IssuesListMilestones(self, owner:str, repo:str,state='open', sort='due_on', direction='desc', per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#list-milestones
        /repos/{owner}/{repo}/milestones
        
        arguments:
        owner -- 
        repo -- 
        state -- Indicates the state of the issues to return. Can be either `open`, `closed`, or `all`.
        sort -- What to sort results by. Either `due_on` or `completeness`.
        direction -- One of `asc` (ascending) or `desc` (descending).
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if state is not None:
            data['state'] = state
        if sort is not None:
            data['sort'] = sort
        if direction is not None:
            data['direction'] = direction
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/milestones", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Milestone(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/issues/{issue_number}/lock
    #
    def IssuesLock(self, owner:str, repo:str, issue_number:int,lock_reason:str=None):
        """Users with push access can lock an issue or pull request's conversation.

Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#http-verbs)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#lock-an-issue
        /repos/{owner}/{repo}/issues/{issue_number}/lock
        
        arguments:
        owner -- 
        repo -- 
        issue_number -- issue_number parameter
        lock_reason -- The reason for locking the issue or pull request conversation. Lock will fail if you don't use one of these reasons:  
\* `off-topic`  
\* `too heated`  
\* `resolved`  
\* `spam`
        

        """
    
        data = {
        'lock_reason': lock_reason,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/lock", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/issues/{issue_number}/labels
    #
    def IssuesRemoveAllLabels(self, owner:str, repo:str, issue_number:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#remove-all-labels-from-an-issue
        /repos/{owner}/{repo}/issues/{issue_number}/labels
        
        arguments:
        owner -- 
        repo -- 
        issue_number -- issue_number parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/labels", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/issues/{issue_number}/assignees
    #
    def IssuesRemoveAssignees(self, owner:str, repo:str, issue_number:int):
        """Removes one or more assignees from an issue.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#remove-assignees-from-an-issue
        /repos/{owner}/{repo}/issues/{issue_number}/assignees
        
        arguments:
        owner -- 
        repo -- 
        issue_number -- issue_number parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/assignees", 
                           params=data,
                           **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Issue(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/issues/{issue_number}/labels/{name}
    #
    def IssuesRemoveLabel(self, owner:str, repo:str, issue_number:int, name:str):
        """Removes the specified label from the issue, and returns the remaining labels on the issue. This endpoint returns a `404 Not Found` status if the label does not exist.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#remove-a-label-from-an-issue
        /repos/{owner}/{repo}/issues/{issue_number}/labels/{name}
        
        arguments:
        owner -- 
        repo -- 
        issue_number -- issue_number parameter
        name -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/labels/{name}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Label(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/issues/{issue_number}/labels
    #
    def IssuesSetLabels(self, owner:str, repo:str, issue_number:int,object:object):
        """Removes any previous labels and sets the new labels for an issue.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#set-labels-for-an-issue
        /repos/{owner}/{repo}/issues/{issue_number}/labels
        
        arguments:
        owner -- 
        repo -- 
        issue_number -- issue_number parameter
        object -- 
        

        """
    
        data = {
        'object': object,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/labels", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return [ entry and Label(**entry) for entry in r.json() ]
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/issues/{issue_number}/lock
    #
    def IssuesUnlock(self, owner:str, repo:str, issue_number:int):
        """Users with push access can unlock an issue's conversation.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#unlock-an-issue
        /repos/{owner}/{repo}/issues/{issue_number}/lock
        
        arguments:
        owner -- 
        repo -- 
        issue_number -- issue_number parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/lock", 
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
    # patch /repos/{owner}/{repo}/issues/{issue_number}
    #
    def IssuesUpdate(self, owner:str, repo:str, issue_number:int,title=None, body:str=None, assignee:str=None, state:str=None, milestone=None, labels:list=[], assignees:list=[]):
        """Issue owners and users with push access can edit an issue.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues/#update-an-issue
        /repos/{owner}/{repo}/issues/{issue_number}
        
        arguments:
        owner -- 
        repo -- 
        issue_number -- issue_number parameter
        title -- The title of the issue.
        body -- The contents of the issue.
        assignee -- Login for the user that this issue should be assigned to. **This field is deprecated.**
        state -- State of the issue. Either `open` or `closed`.
        milestone -- 
        labels -- Labels to associate with this issue. Pass one or more Labels to _replace_ the set of Labels on this Issue. Send an empty array (`[]`) to clear all Labels from the Issue. _NOTE: Only users with push access can set labels for issues. Labels are silently dropped otherwise._
        assignees -- Logins for Users to assign to this issue. Pass one or more user logins to _replace_ the set of assignees on this Issue. Send an empty array (`[]`) to clear all assignees from the Issue. _NOTE: Only users with push access can set assignees for new issues. Assignees are silently dropped otherwise._
        

        """
    
        data = {
        'title': title,
        'body': body,
        'assignee': assignee,
        'state': state,
        'milestone': milestone,
        'labels': labels,
        'assignees': assignees,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Issue(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 503:
            return Service_unavailable(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 301:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 410:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}/issues/comments/{comment_id}
    #
    def IssuesUpdateComment(self, owner:str, repo:str, comment_id:int,body:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#update-an-issue-comment
        /repos/{owner}/{repo}/issues/comments/{comment_id}
        
        arguments:
        owner -- 
        repo -- 
        comment_id -- comment_id parameter
        body -- The contents of the comment.
        

        """
    
        data = {
        'body': body,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/issues/comments/{comment_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return IssueComment(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}/labels/{name}
    #
    def IssuesUpdateLabel(self, owner:str, repo:str, name:str,new_name:str=None, color:str=None, description:str=None):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#update-a-label
        /repos/{owner}/{repo}/labels/{name}
        
        arguments:
        owner -- 
        repo -- 
        name -- 
        new_name -- The new name of the label. Emoji can be added to label names, using either native emoji or colon-style markup. For example, typing `:strawberry:` will render the emoji ![:strawberry:](https://github.githubassets.com/images/icons/emoji/unicode/1f353.png ":strawberry:"). For a full list of available emoji and codes, see "[Emoji cheat sheet](https://github.com/ikatyang/emoji-cheat-sheet)."
        color -- The [hexadecimal color code](http://www.color-hex.com/) for the label, without the leading `#`.
        description -- A short description of the label. Must be 100 characters or fewer.
        

        """
    
        data = {
        'new_name': new_name,
        'color': color,
        'description': description,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/labels/{name}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Label(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}/milestones/{milestone_number}
    #
    def IssuesUpdateMilestone(self, owner:str, repo:str, milestone_number:int,title:str=None, state:str='open', description:str=None, due_on:datetime=None):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/issues#update-a-milestone
        /repos/{owner}/{repo}/milestones/{milestone_number}
        
        arguments:
        owner -- 
        repo -- 
        milestone_number -- milestone_number parameter
        title -- The title of the milestone.
        state -- The state of the milestone. Either `open` or `closed`.
        description -- A description of the milestone.
        due_on -- The milestone due date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        

        """
    
        data = {
        'title': title,
        'state': state,
        'description': description,
        'due_on': due_on,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/milestones/{milestone_number}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Milestone(**r.json())
            

        return UnexpectedResult(r)


        
        
        
    def IssuesDelete(self, issues):
        
        strm = io.StringIO() ;
        
        print("mutation {", file=strm)
        
        for i, issue in enumerate(issues):
            print(f"m{i}: deleteIssue( input: {{ issueId: \"{issue.node_id}\" }}) {{clientMutationId}} ",
                  file=strm)
        
        
        print("}", file=strm)
        
        js = {'query': strm.getvalue()}
        
        result = self._session.post(self._graphql_url, json=js,
                                    **self._requests_kwargs())
        
        return 'errors' not in result.json()
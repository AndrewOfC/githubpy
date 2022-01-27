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

class Activity(object):


    #
    # get /user/starred/{owner}/{repo}
    #
    def ActivityCheckRepoIsStarredByAuthenticatedUser(self, owner:str, repo:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#check-if-a-repository-is-starred-by-the-authenticated-user
        /user/starred/{owner}/{repo}
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/user/starred/{owner}/{repo}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/subscription
    #
    def ActivityDeleteRepoSubscription(self, owner:str, repo:str):
        """This endpoint should only be used to stop watching a repository. To control whether or not you wish to receive notifications from a repository, [set the repository's subscription manually](https://docs.github.com/enterprise-server@3.3/rest/reference/activity#set-a-repository-subscription).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#delete-a-repository-subscription
        /repos/{owner}/{repo}/subscription
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/subscription", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # delete /notifications/threads/{thread_id}/subscription
    #
    def ActivityDeleteThreadSubscription(self, thread_id:int):
        """Mutes all future notifications for a conversation until you comment on the thread or get an **@mention**. If you are watching the repository of the thread, you will still receive notifications. To ignore future notifications for a repository you are watching, use the [Set a thread subscription](https://docs.github.com/enterprise-server@3.3/rest/reference/activity#set-a-thread-subscription) endpoint and set `ignore` to `true`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#delete-a-thread-subscription
        /notifications/threads/{thread_id}/subscription
        
        arguments:
        thread_id -- thread_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/notifications/threads/{thread_id}/subscription", 
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
    # get /feeds
    #
    def ActivityGetFeeds(self, ):
        """GitHub Enterprise Server provides several timeline resources in [Atom](http://en.wikipedia.org/wiki/Atom_(standard)) format. The Feeds API lists all the feeds available to the authenticated user:

*   **Timeline**: The GitHub Enterprise Server global public timeline
*   **User**: The public timeline for any user, using [URI template](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#hypermedia)
*   **Current user public**: The public timeline for the authenticated user
*   **Current user**: The private timeline for the authenticated user
*   **Current user actor**: The private timeline for activity created by the authenticated user
*   **Current user organizations**: The private timeline for the organizations the authenticated user is a member of.
*   **Security advisories**: A collection of public announcements that provide information about security-related vulnerabilities in software on GitHub Enterprise Server.

**Note**: Private feeds are only returned when [authenticating via Basic Auth](https://docs.github.com/enterprise-server@3.3/rest/overview/other-authentication-methods#basic-authentication) since current feed URIs use the older, non revocable auth tokens.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#get-feeds
        /feeds
        
        arguments:
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/feeds", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Feed(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/subscription
    #
    def ActivityGetRepoSubscription(self, owner:str, repo:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#get-a-repository-subscription
        /repos/{owner}/{repo}/subscription
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/subscription", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return RepositorySubscription(**r.json())
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /notifications/threads/{thread_id}
    #
    def ActivityGetThread(self, thread_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#get-a-thread
        /notifications/threads/{thread_id}
        
        arguments:
        thread_id -- thread_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/notifications/threads/{thread_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Thread(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /notifications/threads/{thread_id}/subscription
    #
    def ActivityGetThreadSubscriptionForAuthenticatedUser(self, thread_id:int):
        """This checks to see if the current user is subscribed to a thread. You can also [get a repository subscription](https://docs.github.com/enterprise-server@3.3/rest/reference/activity#get-a-repository-subscription).

Note that subscriptions are only generated if a user is participating in a conversation--for example, they've replied to the thread, were **@mentioned**, or manually subscribe to a thread.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#get-a-thread-subscription-for-the-authenticated-user
        /notifications/threads/{thread_id}/subscription
        
        arguments:
        thread_id -- thread_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/notifications/threads/{thread_id}/subscription", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ThreadSubscription(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /users/{username}/events
    #
    def ActivityListEventsForAuthenticatedUser(self, username:str,per_page=30, page=1):
        """If you are authenticated as the given user, you will see your private events. Otherwise, you'll only see public events.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#list-events-for-the-authenticated-user
        /users/{username}/events
        
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
        
        
        r = self._session.get(f"{self._url}/users/{username}/events", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Event(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /notifications
    #
    def ActivityListNotificationsForAuthenticatedUser(self, all:bool=None, participating:bool=None, since:datetime=None, before:datetime=None, per_page=30, page=1):
        """List all notifications for the current user, sorted by most recently updated.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#list-notifications-for-the-authenticated-user
        /notifications
        
        arguments:
        all -- If `true`, show notifications marked as read.
        participating -- If `true`, only shows notifications in which the user is directly participating or mentioned.
        since -- Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        before -- Only show notifications updated before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if all is not None:
            data['all'] = all
        if participating is not None:
            data['participating'] = participating
        if since is not None:
            data['since'] = since.isoformat()
        if before is not None:
            data['before'] = before.isoformat()
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/notifications", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Thread(**entry) for entry in r.json() ]
            
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
    # get /users/{username}/events/orgs/{org}
    #
    def ActivityListOrgEventsForAuthenticatedUser(self, username:str, org:str,per_page=30, page=1):
        """This is the user's organization dashboard. You must be authenticated as the user to view this.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#list-organization-events-for-the-authenticated-user
        /users/{username}/events/orgs/{org}
        
        arguments:
        username -- 
        org -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/users/{username}/events/orgs/{org}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Event(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /events
    #
    def ActivityListPublicEvents(self, per_page=30, page=1):
        """We delay the public events feed by five minutes, which means the most recent event returned by the public events API actually occurred at least five minutes ago.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#list-public-events
        /events
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/events", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Event(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 503:
            return Service_unavailable(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /networks/{owner}/{repo}/events
    #
    def ActivityListPublicEventsForRepoNetwork(self, owner:str, repo:str,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#list-public-events-for-a-network-of-repositories
        /networks/{owner}/{repo}/events
        
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
        
        
        r = self._session.get(f"{self._url}/networks/{owner}/{repo}/events", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Event(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 301:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /users/{username}/events/public
    #
    def ActivityListPublicEventsForUser(self, username:str,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#list-public-events-for-a-user
        /users/{username}/events/public
        
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
        
        
        r = self._session.get(f"{self._url}/users/{username}/events/public", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Event(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/events
    #
    def ActivityListPublicOrgEvents(self, org:str,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#list-public-organization-events
        /orgs/{org}/events
        
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
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/events", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Event(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /users/{username}/received_events
    #
    def ActivityListReceivedEventsForUser(self, username:str,per_page=30, page=1):
        """These are events that you've received by watching repos and following users. If you are authenticated as the given user, you will see private events. Otherwise, you'll only see public events.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#list-events-received-by-the-authenticated-user
        /users/{username}/received_events
        
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
        
        
        r = self._session.get(f"{self._url}/users/{username}/received_events", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Event(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /users/{username}/received_events/public
    #
    def ActivityListReceivedPublicEventsForUser(self, username:str,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#list-public-events-received-by-a-user
        /users/{username}/received_events/public
        
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
        
        
        r = self._session.get(f"{self._url}/users/{username}/received_events/public", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Event(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/events
    #
    def ActivityListRepoEvents(self, owner:str, repo:str,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#list-repository-events
        /repos/{owner}/{repo}/events
        
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
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/events", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Event(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/notifications
    #
    def ActivityListRepoNotificationsForAuthenticatedUser(self, owner:str, repo:str,all:bool=None, participating:bool=None, since:datetime=None, before:datetime=None, per_page=30, page=1):
        """List all notifications for the current user.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#list-repository-notifications-for-the-authenticated-user
        /repos/{owner}/{repo}/notifications
        
        arguments:
        owner -- 
        repo -- 
        all -- If `true`, show notifications marked as read.
        participating -- If `true`, only shows notifications in which the user is directly participating or mentioned.
        since -- Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        before -- Only show notifications updated before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if all is not None:
            data['all'] = all
        if participating is not None:
            data['participating'] = participating
        if since is not None:
            data['since'] = since.isoformat()
        if before is not None:
            data['before'] = before.isoformat()
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/notifications", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Thread(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /user/starred
    #
    def ActivityListReposStarredByAuthenticatedUser(self, sort='created', direction='desc', per_page=30, page=1):
        """Lists repositories the authenticated user has starred.

You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/enterprise-server@3.3/rest/overview/media-types/) via the `Accept` header:
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#list-repositories-starred-by-the-authenticated-user
        /user/starred
        
        arguments:
        sort -- One of `created` (when the repository was starred) or `updated` (when it was last pushed to).
        direction -- One of `asc` (ascending) or `desc` (descending).
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if sort is not None:
            data['sort'] = sort
        if direction is not None:
            data['direction'] = direction
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/user/starred", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Repository(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /users/{username}/starred
    #
    def ActivityListReposStarredByUser(self, username:str,sort='created', direction='desc', per_page=30, page=1):
        """Lists repositories a user has starred.

You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/enterprise-server@3.3/rest/overview/media-types/) via the `Accept` header:
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#list-repositories-starred-by-a-user
        /users/{username}/starred
        
        arguments:
        username -- 
        sort -- One of `created` (when the repository was starred) or `updated` (when it was last pushed to).
        direction -- One of `asc` (ascending) or `desc` (descending).
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if sort is not None:
            data['sort'] = sort
        if direction is not None:
            data['direction'] = direction
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/users/{username}/starred", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return r.json()
            
        
        return UnexpectedResult(r)
    #
    # get /users/{username}/subscriptions
    #
    def ActivityListReposWatchedByUser(self, username:str,per_page=30, page=1):
        """Lists repositories a user is watching.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#list-repositories-watched-by-a-user
        /users/{username}/subscriptions
        
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
        
        
        r = self._session.get(f"{self._url}/users/{username}/subscriptions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and MinimalRepository(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/stargazers
    #
    def ActivityListStargazersForRepo(self, owner:str, repo:str,per_page=30, page=1):
        """Lists the people that have starred the repository.

You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/enterprise-server@3.3/rest/overview/media-types/) via the `Accept` header:
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#list-stargazers
        /repos/{owner}/{repo}/stargazers
        
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
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/stargazers", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return r.json()
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /user/subscriptions
    #
    def ActivityListWatchedReposForAuthenticatedUser(self, per_page=30, page=1):
        """Lists repositories the authenticated user is watching.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#list-repositories-watched-by-the-authenticated-user
        /user/subscriptions
        
        arguments:
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/user/subscriptions", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and MinimalRepository(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/subscribers
    #
    def ActivityListWatchersForRepo(self, owner:str, repo:str,per_page=30, page=1):
        """Lists the people watching the specified repository.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#list-watchers
        /repos/{owner}/{repo}/subscribers
        
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
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/subscribers", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and SimpleUser(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # put /notifications
    #
    def ActivityMarkNotificationsAsRead(self, last_read_at:datetime=None, read:bool=None):
        """Marks all notifications as "read" removes it from the [default view on GitHub Enterprise Server](https://github.com/notifications). If the number of notifications is too large to complete in one request, you will receive a `202 Accepted` status and GitHub Enterprise Server will run an asynchronous process to mark notifications as "read." To check whether any "unread" notifications remain, you can use the [List notifications for the authenticated user](https://docs.github.com/enterprise-server@3.3/rest/reference/activity#list-notifications-for-the-authenticated-user) endpoint and pass the query parameter `all=false`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#mark-notifications-as-read
        /notifications
        
        arguments:
        last_read_at -- Describes the last point that notifications were checked.
        read -- Whether the notification has been read.
        

        """
    
        data = {
        'last_read_at': last_read_at,
        'read': read,
        
        }
        

        
        r = self._session.put(f"{self._url}/notifications", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 202:
            return ActivityMarkNotificationsAsRead202(**r.json())
            
        if r.status_code == 205:
            return HttpResponse(r)
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/notifications
    #
    def ActivityMarkRepoNotificationsAsRead(self, owner:str, repo:str,last_read_at:datetime=None):
        """Marks all notifications in a repository as "read" removes them from the [default view on GitHub Enterprise Server](https://github.com/notifications). If the number of notifications is too large to complete in one request, you will receive a `202 Accepted` status and GitHub Enterprise Server will run an asynchronous process to mark notifications as "read." To check whether any "unread" notifications remain, you can use the [List repository notifications for the authenticated user](https://docs.github.com/enterprise-server@3.3/rest/reference/activity#list-repository-notifications-for-the-authenticated-user) endpoint and pass the query parameter `all=false`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#mark-repository-notifications-as-read
        /repos/{owner}/{repo}/notifications
        
        arguments:
        owner -- 
        repo -- 
        last_read_at -- Describes the last point that notifications were checked. Anything updated since this time will not be marked as read. If you omit this parameter, all notifications are marked as read. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. Default: The current timestamp.
        

        """
    
        data = {
        'last_read_at': last_read_at,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/notifications", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 202:
            return ActivityMarkRepoNotificationsAsRead202(**r.json())
            
        if r.status_code == 205:
            return HttpResponse(r)
            

        return UnexpectedResult(r)
    #
    # patch /notifications/threads/{thread_id}
    #
    def ActivityMarkThreadAsRead(self, thread_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#mark-a-thread-as-read
        /notifications/threads/{thread_id}
        
        arguments:
        thread_id -- thread_id parameter
        

        """
    
        data = {
        
        }
        

        
        r = self._session.patch(f"{self._url}/notifications/threads/{thread_id}", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 205:
            return HttpResponse(r)
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/subscription
    #
    def ActivitySetRepoSubscription(self, owner:str, repo:str,subscribed:bool=None, ignored:bool=None):
        """If you would like to watch a repository, set `subscribed` to `true`. If you would like to ignore notifications made within a repository, set `ignored` to `true`. If you would like to stop watching a repository, [delete the repository's subscription](https://docs.github.com/enterprise-server@3.3/rest/reference/activity#delete-a-repository-subscription) completely.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#set-a-repository-subscription
        /repos/{owner}/{repo}/subscription
        
        arguments:
        owner -- 
        repo -- 
        subscribed -- Determines if notifications should be received from this repository.
        ignored -- Determines if all notifications should be blocked from this repository.
        

        """
    
        data = {
        'subscribed': subscribed,
        'ignored': ignored,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/subscription", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return RepositorySubscription(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /notifications/threads/{thread_id}/subscription
    #
    def ActivitySetThreadSubscription(self, thread_id:int,ignored:bool=False):
        """If you are watching a repository, you receive notifications for all threads by default. Use this endpoint to ignore future notifications for threads until you comment on the thread or get an **@mention**.

You can also use this endpoint to subscribe to threads that you are currently not receiving notifications for or to subscribed to threads that you have previously ignored.

Unsubscribing from a conversation in a repository that you are not watching is functionally equivalent to the [Delete a thread subscription](https://docs.github.com/enterprise-server@3.3/rest/reference/activity#delete-a-thread-subscription) endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#set-a-thread-subscription
        /notifications/threads/{thread_id}/subscription
        
        arguments:
        thread_id -- thread_id parameter
        ignored -- Whether to block all notifications from a thread.
        

        """
    
        data = {
        'ignored': ignored,
        
        }
        

        
        r = self._session.put(f"{self._url}/notifications/threads/{thread_id}/subscription", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return ThreadSubscription(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /user/starred/{owner}/{repo}
    #
    def ActivityStarRepoForAuthenticatedUser(self, owner:str, repo:str):
        """Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#http-verbs)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#star-a-repository-for-the-authenticated-user
        /user/starred/{owner}/{repo}
        
        arguments:
        owner -- 
        repo -- 
        

        """
    
        data = {
        
        }
        

        
        r = self._session.put(f"{self._url}/user/starred/{owner}/{repo}", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /user/starred/{owner}/{repo}
    #
    def ActivityUnstarRepoForAuthenticatedUser(self, owner:str, repo:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/activity#unstar-a-repository-for-the-authenticated-user
        /user/starred/{owner}/{repo}
        
        arguments:
        owner -- 
        repo -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/user/starred/{owner}/{repo}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
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

class Checks(object):


    #
    # post /repos/{owner}/{repo}/check-runs
    #
    def ChecksCreate(self, owner:str, repo:str,head_sha:str, name:str, details_url:str=None, external_id:str=None, status:str='queued', started_at:datetime=None, conclusion:str=None, completed_at:datetime=None, output:dict=None, actions:list=[]):
        """**Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array.

Creates a new check run for a specific commit in a repository. Your GitHub App must have the `checks:write` permission to create check runs.

In a check suite, GitHub limits the number of check runs with the same name to 1000. Once these check runs exceed 1000, GitHub will start to automatically delete older check runs.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/checks#create-a-check-run
        /repos/{owner}/{repo}/check-runs
        
        arguments:
        owner -- 
        repo -- 
        head_sha -- The SHA of the commit.
        name -- The name of the check. For example, "code-coverage".
        details_url -- The URL of the integrator's site that has the full details of the check. If the integrator does not provide this, then the homepage of the GitHub app is used.
        external_id -- A reference for the run on the integrator's system.
        status -- The current status. Can be one of `queued`, `in_progress`, or `completed`.
        started_at -- The time that the check run began. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        conclusion -- **Required if you provide `completed_at` or a `status` of `completed`**. The final conclusion of the check. Can be one of `action_required`, `cancelled`, `failure`, `neutral`, `success`, `skipped`, `stale`, or `timed_out`. When the conclusion is `action_required`, additional details should be provided on the site specified by `details_url`.  
**Note:** Providing `conclusion` will automatically set the `status` parameter to `completed`. You cannot change a check run conclusion to `stale`, only GitHub can set this.
        completed_at -- The time the check completed. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        output -- Check runs can accept a variety of data in the `output` object, including a `title` and `summary` and can optionally provide descriptive details about the run. See the [`output` object](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#output-object) description.
        actions -- Displays a button on GitHub that can be clicked to alert your app to do additional tasks. For example, a code linting app can display a button that automatically fixes detected errors. The button created in this object is displayed after the check run completes. When a user clicks the button, GitHub sends the [`check_run.requested_action` webhook](https://docs.github.com/enterprise-server@3.3/webhooks/event-payloads/#check_run) to your app. Each action includes a `label`, `identifier` and `description`. A maximum of three actions are accepted. See the [`actions` object](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#actions-object) description. To learn more about check runs and requested actions, see "[Check runs and requested actions](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#check-runs-and-requested-actions)."
        

        """
    
        data = {
        'head_sha': head_sha,
        'name': name,
        'details_url': details_url,
        'external_id': external_id,
        'status': status,
        'started_at': started_at,
        'conclusion': conclusion,
        'completed_at': completed_at,
        'output': output,
        'actions': actions,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/check-runs", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Checkrun(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/check-suites
    #
    def ChecksCreateSuite(self, owner:str, repo:str,head_sha:str):
        """**Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array and a `null` value for `head_branch`.

By default, check suites are automatically created when you create a [check run](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#check-runs). You only need to use this endpoint for manually creating check suites when you've disabled automatic creation using "[Update repository preferences for check suites](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#update-repository-preferences-for-check-suites)". Your GitHub App must have the `checks:write` permission to create check suites.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/checks#create-a-check-suite
        /repos/{owner}/{repo}/check-suites
        
        arguments:
        owner -- 
        repo -- 
        head_sha -- The sha of the head commit.
        

        """
    
        data = {
        'head_sha': head_sha,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/check-suites", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Checksuite(**r.json())
            
        if r.status_code == 201:
            return Checksuite(**r.json())
            

        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/check-runs/{check_run_id}
    #
    def ChecksGet(self, owner:str, repo:str, check_run_id:int):
        """**Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array.

Gets a single check run using its `id`. GitHub Apps must have the `checks:read` permission on a private repository or pull access to a public repository to get check runs. OAuth Apps and authenticated users must have the `repo` scope to get check runs in a private repository.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/checks#get-a-check-run
        /repos/{owner}/{repo}/check-runs/{check_run_id}
        
        arguments:
        owner -- 
        repo -- 
        check_run_id -- check_run_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/check-runs/{check_run_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Checkrun(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/check-suites/{check_suite_id}
    #
    def ChecksGetSuite(self, owner:str, repo:str, check_suite_id:int):
        """**Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array and a `null` value for `head_branch`.

Gets a single check suite using its `id`. GitHub Apps must have the `checks:read` permission on a private repository or pull access to a public repository to get check suites. OAuth Apps and authenticated users must have the `repo` scope to get check suites in a private repository.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/checks#get-a-check-suite
        /repos/{owner}/{repo}/check-suites/{check_suite_id}
        
        arguments:
        owner -- 
        repo -- 
        check_suite_id -- check_suite_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/check-suites/{check_suite_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Checksuite(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/check-runs/{check_run_id}/annotations
    #
    def ChecksListAnnotations(self, owner:str, repo:str, check_run_id:int,per_page=30, page=1):
        """Lists annotations for a check run using the annotation `id`. GitHub Apps must have the `checks:read` permission on a private repository or pull access to a public repository to get annotations for a check run. OAuth Apps and authenticated users must have the `repo` scope to get annotations for a check run in a private repository.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/checks#list-check-run-annotations
        /repos/{owner}/{repo}/check-runs/{check_run_id}/annotations
        
        arguments:
        owner -- 
        repo -- 
        check_run_id -- check_run_id parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/check-runs/{check_run_id}/annotations", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and CheckAnnotation(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/commits/{ref}/check-runs
    #
    def ChecksListForRef(self, owner:str, repo:str, ref:str,check_name:str=None, status=None, filter='latest', per_page=30, page=1, app_id:int=None):
        """**Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array.

Lists check runs for a commit ref. The `ref` can be a SHA, branch name, or a tag name. GitHub Apps must have the `checks:read` permission on a private repository or pull access to a public repository to get check runs. OAuth Apps and authenticated users must have the `repo` scope to get check runs in a private repository.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/checks#list-check-runs-for-a-git-reference
        /repos/{owner}/{repo}/commits/{ref}/check-runs
        
        arguments:
        owner -- 
        repo -- 
        ref -- ref parameter
        check_name -- Returns check runs with the specified `name`.
        status -- Returns check runs with the specified `status`. Can be one of `queued`, `in_progress`, or `completed`.
        filter -- Filters jobs by their `completed_at` timestamp. Can be one of:  
\* `latest`: Returns jobs from the most recent execution of the workflow run.  
\* `all`: Returns all jobs for a workflow run, including from old executions of the workflow run.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        app_id -- 
        
        """
        
        data = {}
        if check_name is not None:
            data['check_name'] = check_name
        if status is not None:
            data['status'] = status
        if filter is not None:
            data['filter'] = filter
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        if app_id is not None:
            data['app_id'] = app_id
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/commits/{ref}/check-runs", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ChecksListForRefSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs
    #
    def ChecksListForSuite(self, owner:str, repo:str, check_suite_id:int,check_name:str=None, status=None, filter='latest', per_page=30, page=1):
        """**Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array.

Lists check runs for a check suite using its `id`. GitHub Apps must have the `checks:read` permission on a private repository or pull access to a public repository to get check runs. OAuth Apps and authenticated users must have the `repo` scope to get check runs in a private repository.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/checks#list-check-runs-in-a-check-suite
        /repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs
        
        arguments:
        owner -- 
        repo -- 
        check_suite_id -- check_suite_id parameter
        check_name -- Returns check runs with the specified `name`.
        status -- Returns check runs with the specified `status`. Can be one of `queued`, `in_progress`, or `completed`.
        filter -- Filters jobs by their `completed_at` timestamp. Can be one of:  
\* `latest`: Returns jobs from the most recent execution of the workflow run.  
\* `all`: Returns all jobs for a workflow run, including from old executions of the workflow run.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if check_name is not None:
            data['check_name'] = check_name
        if status is not None:
            data['status'] = status
        if filter is not None:
            data['filter'] = filter
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ChecksListForSuiteSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/commits/{ref}/check-suites
    #
    def ChecksListSuitesForRef(self, owner:str, repo:str, ref:str,app_id:int=None, check_name:str=None, per_page=30, page=1):
        """**Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array and a `null` value for `head_branch`.

Lists check suites for a commit `ref`. The `ref` can be a SHA, branch name, or a tag name. GitHub Apps must have the `checks:read` permission on a private repository or pull access to a public repository to list check suites. OAuth Apps and authenticated users must have the `repo` scope to get check suites in a private repository.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/checks#list-check-suites-for-a-git-reference
        /repos/{owner}/{repo}/commits/{ref}/check-suites
        
        arguments:
        owner -- 
        repo -- 
        ref -- ref parameter
        app_id -- Filters check suites by GitHub App `id`.
        check_name -- Returns check runs with the specified `name`.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if app_id is not None:
            data['app_id'] = app_id
        if check_name is not None:
            data['check_name'] = check_name
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/commits/{ref}/check-suites", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ChecksListSuitesForRefSuccess(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/check-runs/{check_run_id}/rerequest
    #
    def ChecksRerequestRun(self, owner:str, repo:str, check_run_id:int):
        """Triggers GitHub to rerequest an existing check run, without pushing new code to a repository. This endpoint will trigger the [`check_run` webhook](https://docs.github.com/enterprise-server@3.3/webhooks/event-payloads/#check_run) event with the action `rerequested`. When a check run is `rerequested`, its `status` is reset to `queued` and the `conclusion` is cleared.

To rerequest a check run, your GitHub App must have the `checks:read` permission on a private repository or pull access to a public repository.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/checks#rerequest-a-check-run
        /repos/{owner}/{repo}/check-runs/{check_run_id}/rerequest
        
        arguments:
        owner -- 
        repo -- 
        check_run_id -- check_run_id parameter
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/check-runs/{check_run_id}/rerequest", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return ChecksRerequestRunSuccess(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest
    #
    def ChecksRerequestSuite(self, owner:str, repo:str, check_suite_id:int):
        """Triggers GitHub to rerequest an existing check suite, without pushing new code to a repository. This endpoint will trigger the [`check_suite` webhook](https://docs.github.com/enterprise-server@3.3/webhooks/event-payloads/#check_suite) event with the action `rerequested`. When a check suite is `rerequested`, its `status` is reset to `queued` and the `conclusion` is cleared.

To rerequest a check suite, your GitHub App must have the `checks:read` permission on a private repository or pull access to a public repository.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/checks#rerequest-a-check-suite
        /repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest
        
        arguments:
        owner -- 
        repo -- 
        check_suite_id -- check_suite_id parameter
        

        """
    
        data = {
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest", 
                          json=data,
                          **self._requests_kwargs())
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return ChecksRerequestSuiteSuccess(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}/check-suites/preferences
    #
    def ChecksSetSuitesPreferences(self, owner:str, repo:str,auto_trigger_checks:list=[]):
        """Changes the default automatic flow when creating check suites. By default, a check suite is automatically created each time code is pushed to a repository. When you disable the automatic creation of check suites, you can manually [Create a check suite](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#create-a-check-suite). You must have admin permissions in the repository to set preferences for check suites.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/checks#update-repository-preferences-for-check-suites
        /repos/{owner}/{repo}/check-suites/preferences
        
        arguments:
        owner -- 
        repo -- 
        auto_trigger_checks -- Enables or disables automatic creation of CheckSuite events upon pushes to the repository. Enabled by default. See the [`auto_trigger_checks` object](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#auto_trigger_checks-object) description for details.
        

        """
    
        data = {
        'auto_trigger_checks': auto_trigger_checks,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/check-suites/preferences", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return CheckSuitePreference(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}/check-runs/{check_run_id}
    #
    def ChecksUpdate(self, owner:str, repo:str, check_run_id:int,name:str=None, details_url:str=None, external_id:str=None, started_at:datetime=None, status:str=None, conclusion:str=None, completed_at:datetime=None, output:dict=None, actions:list=[]):
        """**Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array.

Updates a check run for a specific commit in a repository. Your GitHub App must have the `checks:write` permission to edit check runs.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/checks#update-a-check-run
        /repos/{owner}/{repo}/check-runs/{check_run_id}
        
        arguments:
        owner -- 
        repo -- 
        check_run_id -- check_run_id parameter
        name -- The name of the check. For example, "code-coverage".
        details_url -- The URL of the integrator's site that has the full details of the check.
        external_id -- A reference for the run on the integrator's system.
        started_at -- This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        status -- The current status. Can be one of `queued`, `in_progress`, or `completed`.
        conclusion -- **Required if you provide `completed_at` or a `status` of `completed`**. The final conclusion of the check. Can be one of `action_required`, `cancelled`, `failure`, `neutral`, `success`, `skipped`, `stale`, or `timed_out`.  
**Note:** Providing `conclusion` will automatically set the `status` parameter to `completed`. You cannot change a check run conclusion to `stale`, only GitHub can set this.
        completed_at -- The time the check completed. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        output -- Check runs can accept a variety of data in the `output` object, including a `title` and `summary` and can optionally provide descriptive details about the run. See the [`output` object](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#output-object-1) description.
        actions -- Possible further actions the integrator can perform, which a user may trigger. Each action includes a `label`, `identifier` and `description`. A maximum of three actions are accepted. See the [`actions` object](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#actions-object) description. To learn more about check runs and requested actions, see "[Check runs and requested actions](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#check-runs-and-requested-actions)."
        

        """
    
        data = {
        'name': name,
        'details_url': details_url,
        'external_id': external_id,
        'started_at': started_at,
        'status': status,
        'conclusion': conclusion,
        'completed_at': completed_at,
        'output': output,
        'actions': actions,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/check-runs/{check_run_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Checkrun(**r.json())
            

        return UnexpectedResult(r)
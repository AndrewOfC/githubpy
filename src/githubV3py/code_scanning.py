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

class CodeScanning(object):


    #
    # delete /repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}
    #
    def CodeScanningDeleteAnalysis(self, owner:str, repo:str, analysis_id:int,confirm_delete:str=None):
        """Deletes a specified code scanning analysis from a repository. For
private repositories, you must use an access token with the `repo` scope. For public repositories,
you must use an access token with `public_repo` and `repo:security_events` scopes.
GitHub Apps must have the `security_events` write permission to use this endpoint.

You can delete one analysis at a time.
To delete a series of analyses, start with the most recent analysis and work backwards.
Conceptually, the process is similar to the undo function in a text editor.

**Note**: The ability to delete analyses was introduced in GitHub Enterprise Server 3.1.
You can delete analyses that were generated prior to installing this release,
however, if you do so, you will lose information about fixed alerts for all such analyses,
for the relevant code scanning tool.
We recommend that you only delete analyses that were generated with earlier releases
if you don't need the details of fixed alerts from pre-3.1 releases.

When you list the analyses for a repository,
one or more will be identified as deletable in the response:

```
"deletable": true
```

An analysis is deletable when it's the most recent in a set of analyses.
Typically, a repository will have multiple sets of analyses
for each enabled code scanning tool,
where a set is determined by a unique combination of analysis values:

* `ref`
* `tool`
* `analysis_key`
* `environment`

If you attempt to delete an analysis that is not the most recent in a set,
you'll get a 400 response with the message:

```
Analysis specified is not deletable.
```

The response from a successful `DELETE` operation provides you with
two alternative URLs for deleting the next analysis in the set
(see the example default response below).
Use the `next_analysis_url` URL if you want to avoid accidentally deleting the final analysis
in the set. This is a useful option if you want to preserve at least one analysis
for the specified tool in your repository.
Use the `confirm_delete_url` URL if you are content to remove all analyses for a tool.
When you delete the last analysis in a set the value of `next_analysis_url` and `confirm_delete_url`
in the 200 response is `null`.

As an example of the deletion process,
let's imagine that you added a workflow that configured a particular code scanning tool
to analyze the code in a repository. This tool has added 15 analyses:
10 on the default branch, and another 5 on a topic branch.
You therefore have two separate sets of analyses for this tool.
You've now decided that you want to remove all of the analyses for the tool.
To do this you must make 15 separate deletion requests.
To start, you must find the deletable analysis for one of the sets,
step through deleting the analyses in that set,
and then repeat the process for the second set.
The procedure therefore consists of a nested loop:

**Outer loop**:
* List the analyses for the repository, filtered by tool.
* Parse this list to find a deletable analysis. If found:

  **Inner loop**:
  * Delete the identified analysis.
  * Parse the response for the value of `confirm_delete_url` and, if found, use this in the next iteration.

The above process assumes that you want to remove all trace of the tool's analyses from the GitHub user interface, for the specified repository, and it therefore uses the `confirm_delete_url` value. Alternatively, you could use the `next_analysis_url` value, which would leave the last analysis in each set undeleted to avoid removing a tool's analysis entirely.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/code-scanning#delete-a-code-scanning-analysis-from-a-repository
        /repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}
        
        arguments:
        owner -- 
        repo -- 
        analysis_id -- The ID of the analysis, as returned from the `GET /repos/{owner}/{repo}/code-scanning/analyses` operation.
        confirm_delete -- Allow deletion if the specified analysis is the last in a set. If you attempt to delete the final analysis in a set without setting this parameter to `true`, you'll get a 400 response with the message: `Analysis is last of its type and deletion may result in the loss of historical alert data. Please specify confirm_delete.`
        
        """
        
        data = {}
        if confirm_delete is not None:
            data['confirm_delete'] = confirm_delete
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return CodeScanningAnalysisDeletion(**r.json())
            
        if r.status_code == 400:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 503:
            return Service_unavailable(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/code-scanning/alerts/{alert_number}
    #
    def CodeScanningGetAlert(self, owner:str, repo:str, alert_number:None):
        """Gets a single code scanning alert. You must use an access token with the `security_events` scope to use this endpoint. GitHub Apps must have the `security_events` read permission to use this endpoint.

**Deprecation notice**:
The instances field is deprecated and will, in future, not be included in the response for this endpoint. The example response reflects this change. The same information can now be retrieved via a GET request to the URL specified by `instances_url`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/code-scanning#get-a-code-scanning-alert
        /repos/{owner}/{repo}/code-scanning/alerts/{alert_number}
        
        arguments:
        owner -- 
        repo -- 
        alert_number -- The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return CodeScanningAlert(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 503:
            return Service_unavailable(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}
    #
    def CodeScanningGetAnalysis(self, owner:str, repo:str, analysis_id:int):
        """Gets a specified code scanning analysis for a repository.
You must use an access token with the `security_events` scope to use this endpoint.
GitHub Apps must have the `security_events` read permission to use this endpoint.

The default JSON response contains fields that describe the analysis.
This includes the Git reference and commit SHA to which the analysis relates,
the datetime of the analysis, the name of the code scanning tool,
and the number of alerts.

The `rules_count` field in the default response give the number of rules
that were run in the analysis.
For very old analyses this data is not available,
and `0` is returned in this field.

If you use the Accept header `application/sarif+json`,
the response contains the analysis data that was uploaded.
This is formatted as
[SARIF version 2.1.0](https://docs.oasis-open.org/sarif/sarif/v2.1.0/cs01/sarif-v2.1.0-cs01.html).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/code-scanning#get-a-code-scanning-analysis-for-a-repository
        /repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}
        
        arguments:
        owner -- 
        repo -- 
        analysis_id -- The ID of the analysis, as returned from the `GET /repos/{owner}/{repo}/code-scanning/analyses` operation.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return CodeScanningAnalysis(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 503:
            return Service_unavailable(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/code-scanning/sarifs/{sarif_id}
    #
    def CodeScanningGetSarif(self, owner:str, repo:str, sarif_id:str):
        """Gets information about a SARIF upload, including the status and the URL of the analysis that was uploaded so that you can retrieve details of the analysis. For more information, see "[Get a code scanning analysis for a repository](/rest/reference/code-scanning#get-a-code-scanning-analysis-for-a-repository)." You must use an access token with the `security_events` scope to use this endpoint. GitHub Apps must have the `security_events` read permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/code-scanning#list-recent-code-scanning-analyses-for-a-repository
        /repos/{owner}/{repo}/code-scanning/sarifs/{sarif_id}
        
        arguments:
        owner -- 
        repo -- 
        sarif_id -- The SARIF ID obtained after uploading.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/code-scanning/sarifs/{sarif_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return CodeScanningSarifsStatus(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        if r.status_code == 503:
            return Service_unavailable(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/instances
    #
    def CodeScanningListAlertInstances(self, owner:str, repo:str, alert_number:None,page=1, per_page=30, ref:None=None):
        """Lists all instances of the specified code scanning alert. You must use an access token with the `security_events` scope to use this endpoint. GitHub Apps must have the `security_events` read permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/code-scanning#list-instances-of-a-code-scanning-alert
        /repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/instances
        
        arguments:
        owner -- 
        repo -- 
        alert_number -- The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
        page -- Page number of the results to fetch.
        per_page -- Results per page (max 100)
        ref -- The Git reference for the results you want to list. The `ref` for a branch can be formatted either as `refs/heads/<branch name>` or simply `<branch name>`. To reference a pull request use `refs/pull/<number>/merge`.
        
        """
        
        data = {}
        if page is not None:
            data['page'] = page
        if per_page is not None:
            data['per_page'] = per_page
        if ref is not None:
            data['ref'] = ref
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/instances", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and CodeScanningAlertInstance(**entry) for entry in r.json() ]
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 503:
            return Service_unavailable(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/code-scanning/alerts
    #
    def CodeScanningListAlertsForRepo(self, owner:str, repo:str,tool_name:None=None, tool_guid:None=None, page=1, per_page=30, ref:None=None, state:None=None):
        """Lists all open code scanning alerts for the default branch (usually `main`
or `master`). You must use an access token with the `security_events` scope to use
this endpoint. GitHub Apps must have the `security_events` read permission to use
this endpoint.

The response includes a `most_recent_instance` object.
This provides details of the most recent instance of this alert
for the default branch or for the specified Git reference
(if you used `ref` in the request).
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/code-scanning#list-code-scanning-alerts-for-a-repository
        /repos/{owner}/{repo}/code-scanning/alerts
        
        arguments:
        owner -- 
        repo -- 
        tool_name -- The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using either `tool_name` or `tool_guid`, but not both.
        tool_guid -- The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using either `tool_guid` or `tool_name`, but not both.
        page -- Page number of the results to fetch.
        per_page -- Results per page (max 100)
        ref -- The Git reference for the results you want to list. The `ref` for a branch can be formatted either as `refs/heads/<branch name>` or simply `<branch name>`. To reference a pull request use `refs/pull/<number>/merge`.
        state -- Set to `open`, `fixed`, or `dismissed` to list code scanning alerts in a specific state.
        
        """
        
        data = {}
        if tool_name is not None:
            data['tool_name'] = tool_name
        if tool_guid is not None:
            data['tool_guid'] = tool_guid
        if page is not None:
            data['page'] = page
        if per_page is not None:
            data['per_page'] = per_page
        if ref is not None:
            data['ref'] = ref
        if state is not None:
            data['state'] = state
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/code-scanning/alerts", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and CodeScanningAlertItems(**entry) for entry in r.json() ]
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 503:
            return Service_unavailable(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/code-scanning/analyses
    #
    def CodeScanningListRecentAnalyses(self, owner:str, repo:str,tool_name:None=None, tool_guid:None=None, page=1, per_page=30, ref:None=None, sarif_id:None=None):
        """Lists the details of all code scanning analyses for a repository,
starting with the most recent.
The response is paginated and you can use the `page` and `per_page` parameters
to list the analyses you're interested in.
By default 30 analyses are listed per page.

The `rules_count` field in the response give the number of rules
that were run in the analysis.
For very old analyses this data is not available,
and `0` is returned in this field.

You must use an access token with the `security_events` scope to use this endpoint.
GitHub Apps must have the `security_events` read permission to use this endpoint.

**Deprecation notice**:
The `tool_name` field is deprecated and will, in future, not be included in the response for this endpoint. The example response reflects this change. The tool name can now be found inside the `tool` field.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/code-scanning#list-code-scanning-analyses-for-a-repository
        /repos/{owner}/{repo}/code-scanning/analyses
        
        arguments:
        owner -- 
        repo -- 
        tool_name -- The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using either `tool_name` or `tool_guid`, but not both.
        tool_guid -- The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using either `tool_guid` or `tool_name`, but not both.
        page -- Page number of the results to fetch.
        per_page -- Results per page (max 100)
        ref -- The Git reference for the analyses you want to list. The `ref` for a branch can be formatted either as `refs/heads/<branch name>` or simply `<branch name>`. To reference a pull request use `refs/pull/<number>/merge`.
        sarif_id -- Filter analyses belonging to the same SARIF upload.
        
        """
        
        data = {}
        if tool_name is not None:
            data['tool_name'] = tool_name
        if tool_guid is not None:
            data['tool_guid'] = tool_guid
        if page is not None:
            data['page'] = page
        if per_page is not None:
            data['per_page'] = per_page
        if ref is not None:
            data['ref'] = ref
        if sarif_id is not None:
            data['sarif_id'] = sarif_id
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/code-scanning/analyses", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and CodeScanningAnalysis(**entry) for entry in r.json() ]
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 503:
            return Service_unavailable(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}/code-scanning/alerts/{alert_number}
    #
    def CodeScanningUpdateAlert(self, owner:str, repo:str, alert_number:None,state:str, dismissed_reason:str=None):
        """Updates the status of a single code scanning alert. You must use an access token with the `security_events` scope to use this endpoint. GitHub Apps must have the `security_events` write permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/code-scanning#update-a-code-scanning-alert
        /repos/{owner}/{repo}/code-scanning/alerts/{alert_number}
        
        arguments:
        owner -- 
        repo -- 
        alert_number -- The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
        state -- 
        dismissed_reason -- 
        

        """
    
        data = {
        'state': state,
        'dismissed_reason': dismissed_reason,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return CodeScanningAlert(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 503:
            return Service_unavailable(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/code-scanning/sarifs
    #
    def CodeScanningUploadSarif(self, owner:str, repo:str,sarif:str, ref:str, commit_sha:str, checkout_uri:str=None, started_at:datetime=None, tool_name:str=None):
        """Uploads SARIF data containing the results of a code scanning analysis to make the results available in a repository. You must use an access token with the `security_events` scope to use this endpoint. GitHub Apps must have the `security_events` write permission to use this endpoint.

There are two places where you can upload code scanning results.
 - If you upload to a pull request, for example `--ref refs/pull/42/merge` or `--ref refs/pull/42/head`, then the results appear as alerts in a pull request check. For more information, see "[Triaging code scanning alerts in pull requests](/code-security/secure-coding/triaging-code-scanning-alerts-in-pull-requests)."
 - If you upload to a branch, for example `--ref refs/heads/my-branch`, then the results appear in the **Security** tab for your repository. For more information, see "[Managing code scanning alerts for your repository](/code-security/secure-coding/managing-code-scanning-alerts-for-your-repository#viewing-the-alerts-for-a-repository)."

You must compress the SARIF-formatted analysis data that you want to upload, using `gzip`, and then encode it as a Base64 format string. For example:

```
gzip -c analysis-data.sarif | base64 -w0
```

SARIF upload supports a maximum of 5000 results per analysis run. Any results over this limit are ignored and any SARIF uploads with more than 25,000 results are rejected. Typically, but not necessarily, a SARIF file contains a single run of a single tool. If a code scanning tool generates too many results, you should update the analysis configuration to run only the most important rules or queries.

The `202 Accepted`, response includes an `id` value.
You can use this ID to check the status of the upload by using this for the `/sarifs/{sarif_id}` endpoint.
For more information, see "[Get information about a SARIF upload](/rest/reference/code-scanning#get-information-about-a-sarif-upload)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/code-scanning#upload-a-sarif-file
        /repos/{owner}/{repo}/code-scanning/sarifs
        
        arguments:
        owner -- 
        repo -- 
        sarif -- 
        ref -- 
        commit_sha -- 
        checkout_uri -- The base directory used in the analysis, as it appears in the SARIF file.
This property is used to convert file paths from absolute to relative, so that alerts can be mapped to their correct location in the repository.
        started_at -- The time that the analysis run began. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        tool_name -- The name of the tool used to generate the code scanning analysis. If this parameter is not used, the tool name defaults to "API". If the uploaded SARIF contains a tool GUID, this will be available for filtering using the `tool_guid` parameter of operations such as `GET /repos/{owner}/{repo}/code-scanning/alerts`.
        

        """
    
        data = {
        'sarif': sarif,
        'ref': ref,
        'commit_sha': commit_sha,
        'checkout_uri': checkout_uri,
        'started_at': started_at,
        'tool_name': tool_name,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/code-scanning/sarifs", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 202:
            return CodeScanningSarifsReceipt(**r.json())
            
        if r.status_code == 400:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 413:
            return HttpResponse(r)
            
        if r.status_code == 503:
            return Service_unavailable(**r.json())
            

        return UnexpectedResult(r)
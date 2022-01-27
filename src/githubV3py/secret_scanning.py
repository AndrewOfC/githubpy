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

class SecretScanning(object):


    #
    # get /repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}
    #
    def SecretScanningGetAlert(self, owner:str, repo:str, alert_number:None):
        """Gets a single secret scanning alert detected in a private repository. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the `repo` scope or `security_events` scope.

GitHub Apps must have the `secret_scanning_alerts` read permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/secret-scanning#get-a-secret-scanning-alert
        /repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}
        
        arguments:
        owner -- 
        repo -- 
        alert_number -- The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return SecretScanningAlert(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        if r.status_code == 503:
            return Service_unavailable(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/secret-scanning/alerts
    #
    def SecretScanningListAlertsForOrg(self, org:str,state=None, secret_type:str=None, resolution:str=None, page=1, per_page=30):
        """Lists secret scanning alerts for eligible repositories in an organization, from newest to oldest.
To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the `repo` scope or `security_events` scope.

GitHub Apps must have the `secret_scanning_alerts` read permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/secret-scanning#list-secret-scanning-alerts-for-an-organization
        /orgs/{org}/secret-scanning/alerts
        
        arguments:
        org -- 
        state -- Set to `open` or `resolved` to only list secret scanning alerts in a specific state.
        secret_type -- A comma-separated list of secret types to return. By default all secret types are returned.
See "[About secret scanning for private repositories](https://docs.github.com/enterprise-server@3.3/code-security/secret-security/about-secret-scanning#about-secret-scanning-for-private-repositories)"
for a complete list of secret types (API slug).
        resolution -- A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are `false_positive`, `wont_fix`, `revoked`, `pattern_edited`, `pattern_deleted` or `used_in_tests`.
        page -- Page number of the results to fetch.
        per_page -- Results per page (max 100)
        
        """
        
        data = {}
        if state is not None:
            data['state'] = state
        if secret_type is not None:
            data['secret_type'] = secret_type
        if resolution is not None:
            data['resolution'] = resolution
        if page is not None:
            data['page'] = page
        if per_page is not None:
            data['per_page'] = per_page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/secret-scanning/alerts", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and OrganizationSecretScanningAlert(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 503:
            return Service_unavailable(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/secret-scanning/alerts
    #
    def SecretScanningListAlertsForRepo(self, owner:str, repo:str,state=None, secret_type:str=None, resolution:str=None, page=1, per_page=30):
        """Lists secret scanning alerts for a private repository, from newest to oldest. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the `repo` scope or `security_events` scope.

GitHub Apps must have the `secret_scanning_alerts` read permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/secret-scanning#list-secret-scanning-alerts-for-a-repository
        /repos/{owner}/{repo}/secret-scanning/alerts
        
        arguments:
        owner -- 
        repo -- 
        state -- Set to `open` or `resolved` to only list secret scanning alerts in a specific state.
        secret_type -- A comma-separated list of secret types to return. By default all secret types are returned.
See "[About secret scanning for private repositories](https://docs.github.com/enterprise-server@3.3/code-security/secret-security/about-secret-scanning#about-secret-scanning-for-private-repositories)"
for a complete list of secret types (API slug).
        resolution -- A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are `false_positive`, `wont_fix`, `revoked`, `pattern_edited`, `pattern_deleted` or `used_in_tests`.
        page -- Page number of the results to fetch.
        per_page -- Results per page (max 100)
        
        """
        
        data = {}
        if state is not None:
            data['state'] = state
        if secret_type is not None:
            data['secret_type'] = secret_type
        if resolution is not None:
            data['resolution'] = resolution
        if page is not None:
            data['page'] = page
        if per_page is not None:
            data['per_page'] = per_page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/secret-scanning/alerts", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and SecretScanningAlert(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        if r.status_code == 503:
            return Service_unavailable(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations
    #
    def SecretScanningListLocationsForAlert(self, owner:str, repo:str, alert_number:None,page=1, per_page=30):
        """Lists all locations for a given secret scanning alert for a private repository. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the `repo` scope or `security_events` scope.

GitHub Apps must have the `secret_scanning_alerts` read permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/secret-scanning#list-locations-for-a-secret-scanning-alert
        /repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations
        
        arguments:
        owner -- 
        repo -- 
        alert_number -- The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
        page -- Page number of the results to fetch.
        per_page -- Results per page (max 100)
        
        """
        
        data = {}
        if page is not None:
            data['page'] = page
        if per_page is not None:
            data['per_page'] = per_page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and SecretScanningLocation(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        if r.status_code == 503:
            return Service_unavailable(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}
    #
    def SecretScanningUpdateAlert(self, owner:str, repo:str, alert_number:None,state:str, resolution:str=None):
        """Updates the status of a secret scanning alert in a private repository. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the `repo` scope or `security_events` scope.

GitHub Apps must have the `secret_scanning_alerts` write permission to use this endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/secret-scanning#update-a-secret-scanning-alert
        /repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}
        
        arguments:
        owner -- 
        repo -- 
        alert_number -- The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
        state -- 
        resolution -- 
        

        """
    
        data = {
        'state': state,
        'resolution': resolution,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return SecretScanningAlert(**r.json())
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        if r.status_code == 422:
            return HttpResponse(r)
            
        if r.status_code == 503:
            return Service_unavailable(**r.json())
            

        return UnexpectedResult(r)
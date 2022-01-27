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

class Projects(object):


    #
    # put /projects/{project_id}/collaborators/{username}
    #
    def ProjectsAddCollaborator(self, project_id:int, username:str,permission:str='write'):
        """Adds a collaborator to an organization project and sets their permission level. You must be an organization owner or a project `admin` to add a collaborator.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#add-project-collaborator
        /projects/{project_id}/collaborators/{username}
        
        arguments:
        project_id -- 
        username -- 
        permission -- The permission to grant the collaborator.
        

        """
    
        data = {
        'permission': permission,
        
        }
        

        
        r = self._session.put(f"{self._url}/projects/{project_id}/collaborators/{username}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
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
    # post /projects/columns/{column_id}/cards
    #
    def ProjectsCreateCard(self, column_id:int,object:object):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#create-a-project-card
        /projects/columns/{column_id}/cards
        
        arguments:
        column_id -- column_id parameter
        object -- 
        

        """
    
        data = {
        'object': object,
        
        }
        

        
        r = self._session.post(f"{self._url}/projects/columns/{column_id}/cards", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return ProjectCard(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return r.json()
            
        if r.status_code == 503:
            return ProjectsCreateCard503(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /projects/{project_id}/columns
    #
    def ProjectsCreateColumn(self, project_id:int,name:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#create-a-project-column
        /projects/{project_id}/columns
        
        arguments:
        project_id -- 
        name -- Name of the project column
        

        """
    
        data = {
        'name': name,
        
        }
        

        
        r = self._session.post(f"{self._url}/projects/{project_id}/columns", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return ProjectColumn(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationErrorSimple(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /user/projects
    #
    def ProjectsCreateForAuthenticatedUser(self, name:str, body:str=None):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#create-a-user-project
        /user/projects
        
        arguments:
        name -- Name of the project
        body -- Body of the project
        

        """
    
        data = {
        'name': name,
        'body': body,
        
        }
        

        
        r = self._session.post(f"{self._url}/user/projects", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Project(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 415:
            return Preview_header_missing(**r.json())
            
        if r.status_code == 422:
            return ValidationErrorSimple(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /orgs/{org}/projects
    #
    def ProjectsCreateForOrg(self, org:str,name:str, body:str=None):
        """Creates an organization project board. Returns a `404 Not Found` status if projects are disabled in the organization. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#create-an-organization-project
        /orgs/{org}/projects
        
        arguments:
        org -- 
        name -- The name of the project.
        body -- The description of the project.
        

        """
    
        data = {
        'name': name,
        'body': body,
        
        }
        

        
        r = self._session.post(f"{self._url}/orgs/{org}/projects", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Project(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationErrorSimple(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/projects
    #
    def ProjectsCreateForRepo(self, owner:str, repo:str,name:str, body:str=None):
        """Creates a repository project board. Returns a `404 Not Found` status if projects are disabled in the repository. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#create-a-repository-project
        /repos/{owner}/{repo}/projects
        
        arguments:
        owner -- 
        repo -- 
        name -- The name of the project.
        body -- The description of the project.
        

        """
    
        data = {
        'name': name,
        'body': body,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/projects", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return Project(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationErrorSimple(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /projects/{project_id}
    #
    def ProjectsDelete(self, project_id:int):
        """Deletes a project board. Returns a `404 Not Found` status if projects are disabled.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#delete-a-project
        /projects/{project_id}
        
        arguments:
        project_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/projects/{project_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return ProjectsDeleteForbidden(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /projects/columns/cards/{card_id}
    #
    def ProjectsDeleteCard(self, card_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#delete-a-project-card
        /projects/columns/cards/{card_id}
        
        arguments:
        card_id -- card_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/projects/columns/cards/{card_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return ProjectsDeleteCardForbidden(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /projects/columns/{column_id}
    #
    def ProjectsDeleteColumn(self, column_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#delete-a-project-column
        /projects/columns/{column_id}
        
        arguments:
        column_id -- column_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/projects/columns/{column_id}", 
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
    # get /projects/{project_id}
    #
    def ProjectsGet(self, project_id:int):
        """Gets a project by its `id`. Returns a `404 Not Found` status if projects are disabled. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#get-a-project
        /projects/{project_id}
        
        arguments:
        project_id -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/projects/{project_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Project(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /projects/columns/cards/{card_id}
    #
    def ProjectsGetCard(self, card_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#get-a-project-card
        /projects/columns/cards/{card_id}
        
        arguments:
        card_id -- card_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/projects/columns/cards/{card_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ProjectCard(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /projects/columns/{column_id}
    #
    def ProjectsGetColumn(self, column_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#get-a-project-column
        /projects/columns/{column_id}
        
        arguments:
        column_id -- column_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/projects/columns/{column_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ProjectColumn(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /projects/{project_id}/collaborators/{username}/permission
    #
    def ProjectsGetPermissionForUser(self, project_id:int, username:str):
        """Returns the collaborator's permission level for an organization project. Possible values for the `permission` key: `admin`, `write`, `read`, `none`. You must be an organization owner or a project `admin` to review a user's permission level.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#get-project-permission-for-a-user
        /projects/{project_id}/collaborators/{username}/permission
        
        arguments:
        project_id -- 
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/projects/{project_id}/collaborators/{username}/permission", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return ProjectCollaboratorPermission(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
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
    # get /projects/columns/{column_id}/cards
    #
    def ProjectsListCards(self, column_id:int,archived_state='not_archived', per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#list-project-cards
        /projects/columns/{column_id}/cards
        
        arguments:
        column_id -- column_id parameter
        archived_state -- Filters the project cards that are returned by the card's state. Can be one of `all`,`archived`, or `not_archived`.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if archived_state is not None:
            data['archived_state'] = archived_state
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/projects/columns/{column_id}/cards", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and ProjectCard(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /projects/{project_id}/collaborators
    #
    def ProjectsListCollaborators(self, project_id:int,affiliation='all', per_page=30, page=1):
        """Lists the collaborators for an organization project. For a project, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners. You must be an organization owner or a project `admin` to list collaborators.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#list-project-collaborators
        /projects/{project_id}/collaborators
        
        arguments:
        project_id -- 
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
        
        
        r = self._session.get(f"{self._url}/projects/{project_id}/collaborators", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and SimpleUser(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
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
    # get /projects/{project_id}/columns
    #
    def ProjectsListColumns(self, project_id:int,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#list-project-columns
        /projects/{project_id}/columns
        
        arguments:
        project_id -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/projects/{project_id}/columns", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and ProjectColumn(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /orgs/{org}/projects
    #
    def ProjectsListForOrg(self, org:str,state='open', per_page=30, page=1):
        """Lists the projects in an organization. Returns a `404 Not Found` status if projects are disabled in the organization. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#list-organization-projects
        /orgs/{org}/projects
        
        arguments:
        org -- 
        state -- Indicates the state of the issues to return. Can be either `open`, `closed`, or `all`.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if state is not None:
            data['state'] = state
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/orgs/{org}/projects", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Project(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationErrorSimple(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/projects
    #
    def ProjectsListForRepo(self, owner:str, repo:str,state='open', per_page=30, page=1):
        """Lists the projects in a repository. Returns a `404 Not Found` status if projects are disabled in the repository. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#list-repository-projects
        /repos/{owner}/{repo}/projects
        
        arguments:
        owner -- 
        repo -- 
        state -- Indicates the state of the issues to return. Can be either `open`, `closed`, or `all`.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if state is not None:
            data['state'] = state
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/projects", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Project(**entry) for entry in r.json() ]
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationErrorSimple(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /users/{username}/projects
    #
    def ProjectsListForUser(self, username:str,state='open', per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#list-user-projects
        /users/{username}/projects
        
        arguments:
        username -- 
        state -- Indicates the state of the issues to return. Can be either `open`, `closed`, or `all`.
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if state is not None:
            data['state'] = state
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/users/{username}/projects", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Project(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # post /projects/columns/cards/{card_id}/moves
    #
    def ProjectsMoveCard(self, card_id:int,position:str, column_id:int=None):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#move-a-project-card
        /projects/columns/cards/{card_id}/moves
        
        arguments:
        card_id -- card_id parameter
        position -- The position of the card in a column. Can be one of: `top`, `bottom`, or `after:<card_id>` to place after the specified card.
        column_id -- The unique identifier of the column the card should be moved to
        

        """
    
        data = {
        'position': position,
        'column_id': column_id,
        
        }
        

        
        r = self._session.post(f"{self._url}/projects/columns/cards/{card_id}/moves", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return ProjectsMoveCardSuccess(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return ProjectsMoveCardForbidden(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 503:
            return ProjectsMoveCard503(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /projects/columns/{column_id}/moves
    #
    def ProjectsMoveColumn(self, column_id:int,position:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#move-a-project-column
        /projects/columns/{column_id}/moves
        
        arguments:
        column_id -- column_id parameter
        position -- The position of the column in a project. Can be one of: `first`, `last`, or `after:<column_id>` to place after the specified column.
        

        """
    
        data = {
        'position': position,
        
        }
        

        
        r = self._session.post(f"{self._url}/projects/columns/{column_id}/moves", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return ProjectsMoveColumnSuccess(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationErrorSimple(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /projects/{project_id}/collaborators/{username}
    #
    def ProjectsRemoveCollaborator(self, project_id:int, username:str):
        """Removes a collaborator from an organization project. You must be an organization owner or a project `admin` to remove a collaborator.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#remove-project-collaborator
        /projects/{project_id}/collaborators/{username}
        
        arguments:
        project_id -- 
        username -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/projects/{project_id}/collaborators/{username}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # patch /projects/{project_id}
    #
    def ProjectsUpdate(self, project_id:int,name:str=None, body:str=None, state:str=None, organization_permission:str=None, private:bool=None):
        """Updates a project board's information. Returns a `404 Not Found` status if projects are disabled. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#update-a-project
        /projects/{project_id}
        
        arguments:
        project_id -- 
        name -- Name of the project
        body -- Body of the project
        state -- State of the project; either 'open' or 'closed'
        organization_permission -- The baseline permission that all organization members have on this project
        private -- Whether or not this project can be seen by everyone.
        

        """
    
        data = {
        'name': name,
        'body': body,
        'state': state,
        'organization_permission': organization_permission,
        'private': private,
        
        }
        

        
        r = self._session.patch(f"{self._url}/projects/{project_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return Project(**r.json())
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return ProjectsUpdateForbidden(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 410:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationErrorSimple(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /projects/columns/cards/{card_id}
    #
    def ProjectsUpdateCard(self, card_id:int,note:str=None, archived:bool=None):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#update-a-project-card
        /projects/columns/cards/{card_id}
        
        arguments:
        card_id -- card_id parameter
        note -- The project card's note
        archived -- Whether or not the card is archived
        

        """
    
        data = {
        'note': note,
        'archived': archived,
        
        }
        

        
        r = self._session.patch(f"{self._url}/projects/columns/cards/{card_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return ProjectCard(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationErrorSimple(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /projects/columns/{column_id}
    #
    def ProjectsUpdateColumn(self, column_id:int,name:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/projects#update-a-project-column
        /projects/columns/{column_id}
        
        arguments:
        column_id -- column_id parameter
        name -- Name of the project column
        

        """
    
        data = {
        'name': name,
        
        }
        

        
        r = self._session.patch(f"{self._url}/projects/columns/{column_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return ProjectColumn(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 401:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
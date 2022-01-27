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



from .githubclientbase import GitHubClientBase
from .githubclientclasses import *




from .meta import Meta
from .enterprise_admin import EnterpriseAdmin
from .apps import Apps
from .oauth_authorizations import OauthAuthorizations
from .codes_of_conduct import CodesOfConduct
from .emojis import Emojis
from .activity import Activity
from .gists import Gists
from .gitignore import Gitignore
from .issues import Issues
from .licenses import Licenses
from .markdown import Markdown
from .orgs import Orgs
from .actions import Actions
from .projects import Projects
from .repos import Repos
from .secret_scanning import SecretScanning
from .teams import Teams
from .reactions import Reactions
from .rate_limit import RateLimit
from .checks import Checks
from .code_scanning import CodeScanning
from .git import Git
from .pulls import Pulls
from .search import Search
from .users import Users


class GitHubClient(GitHubClientBase, 
  Meta,
  EnterpriseAdmin,
  Apps,
  OauthAuthorizations,
  CodesOfConduct,
  Emojis,
  Activity,
  Gists,
  Gitignore,
  Issues,
  Licenses,
  Markdown,
  Orgs,
  Actions,
  Projects,
  Repos,
  SecretScanning,
  Teams,
  Reactions,
  RateLimit,
  Checks,
  CodeScanning,
  Git,
  Pulls,
  Search,
  Users):
    def __init__(self, username=None, password=None, token=None, usesession=False):
        GitHubClientBase.__init__(self, username=username, 
        password=password, 
        token=token, 
        usesession=usesession)

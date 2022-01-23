


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

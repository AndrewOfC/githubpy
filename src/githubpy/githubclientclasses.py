

import enum
import datetime

class EnumParameter(enum.Enum):
    def __str__(self):
        return self.name
    def __eq__(self, o):
        if isinstance(o, str):
            return self.name == o
        return self is o
        
        
class ResponseBase(object):
    def __init__(self, extra_params=None):
        self.__extra_params = extra_params
        return

    def __ok(o):
        return True
        
    def __status_code(o):
        return 200

        
    ok = property(__ok, doc="Response is good")
    
    status_code = property(__status_code)
    
    def _get_extra_params(self):
        return self._extra_params
        
    extra_params = property(_get_extra_params, doc='extra parameters')

class HttpResponse(ResponseBase):
    def __init__(self, request):
        ResponseBase.__init__(self)
        self._message = ''
        self._ok = request.ok
        self._status_code = request.status_code
        if 'Content-Type' in request.headers and request.headers['Content-Type'].startswith('application/json'):
            json = request.json()
            if 'message' in json:
                self._message = json['message']
            
        
    def _get_status_code(self):
        return self._status_code
        
    status_code = property(_get_status_code, doc="request status code")

    def _get_message(self):
        return self._message
        
    message = property(_get_message)
    
    def _get_ok(self):
        return self._ok
        
    ok = property(_get_ok)
        
    def __repr__(self):
        return f"HttpResponse({self._status_code})"
        

class UnexpectedResult(HttpResponse):
    def __init__(self, request):
        HttpResponse.__init__(self, request)
        
        

#
# direction
#
class direction(EnumParameter):
    """One of `asc` (ascending) or `desc` (descending).
    """
    asc = enum.auto()
    desc = enum.auto()
    

#
# audit-log-order
#
class direction(EnumParameter):
    """One of `asc` (ascending) or `desc` (descending).
    """
    asc = enum.auto()
    desc = enum.auto()
    

#
# secret-scanning-alert-state
#
class state(EnumParameter):
    """Set to `open` or `resolved` to only list secret scanning alerts in a specific state.
    """
    open = enum.auto()
    resolved = enum.auto()
    

#
# workflow-run-status
#
class status(EnumParameter):
    """Returns workflow runs with the check run `status` or `conclusion` that you specify. For example, a conclusion can be `success` or a status can be `in_progress`. Only GitHub can set a status of `waiting` or `requested`. For a list of the possible `status` and `conclusion` options, see "[Create a check run](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#create-a-check-run)."
    """
    completed = enum.auto()
    action_required = enum.auto()
    cancelled = enum.auto()
    failure = enum.auto()
    neutral = enum.auto()
    skipped = enum.auto()
    stale = enum.auto()
    success = enum.auto()
    timed_out = enum.auto()
    in_progress = enum.auto()
    queued = enum.auto()
    requested = enum.auto()
    waiting = enum.auto()
    

#
# status
#
class status(EnumParameter):
    """Returns check runs with the specified `status`. Can be one of `queued`, `in_progress`, or `completed`.
    """
    queued = enum.auto()
    in_progress = enum.auto()
    completed = enum.auto()
    

#
# sort
#
class sort(EnumParameter):
    """One of `created` (when the repository was starred) or `updated` (when it was last pushed to).
    """
    created = enum.auto()
    updated = enum.auto()
    

#
# order
#
class direction(EnumParameter):
    """One of `asc` (ascending) or `desc` (descending).
    """
    asc = enum.auto()
    desc = enum.auto()
    ##
##
##
class DataResponse(ResponseBase):
    def __init__(self, data:object, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._data = data
        return
        
    def __str__(self):
        return self.data
    def __repr__(self):
        return f"""DataResponse(\"""{self.data}\""")"""
    

    
    def _getdata(self):
        return self._data
        
    data = property(_getdata, doc="""Response Data """)


    
##
##
##
class Globalhook_config(ResponseBase):
    def __init__(self, url:str=None, content_type:str=None, insecure_ssl:str=None, secret:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._content_type = content_type
        self._insecure_ssl = insecure_ssl
        self._secret = secret
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getcontent_type(self):
        return self._content_type
        
    content_type = property(_getcontent_type)

    def _getinsecure_ssl(self):
        return self._insecure_ssl
        
    insecure_ssl = property(_getinsecure_ssl)

    def _getsecret(self):
        return self._secret
        
    secret = property(_getsecret)


    
##
##
##
class GlobalHook(ResponseBase):
    def __init__(self, type:str=None, id:int=None, name:str=None, active:bool=None, events:list=[], config:dict=None, updated_at:str=None, created_at:str=None, url:str=None, ping_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._type = type
        self._id = id
        self._name = name
        self._active = active
        self._events = events
        self._config = config
        self._updated_at = updated_at
        self._created_at = created_at
        self._url = url
        self._ping_url = ping_url
        return
        
    

    
    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getactive(self):
        return self._active
        
    active = property(_getactive)

    def _getevents(self):
        return self._events and [ entry for entry in self._events ]
        
    events = property(_getevents)

    def _getconfig(self):
        return self._config and Globalhook_config(**self._config)
        
    config = property(_getconfig)

    def _getupdated_at(self):
        return self._updated_at
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getping_url(self):
        return self._ping_url
        
    ping_url = property(_getping_url)


    
##
##
##
class Globalhook2_config(ResponseBase):
    def __init__(self, url:str=None, content_type:str=None, insecure_ssl:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._content_type = content_type
        self._insecure_ssl = insecure_ssl
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getcontent_type(self):
        return self._content_type
        
    content_type = property(_getcontent_type)

    def _getinsecure_ssl(self):
        return self._insecure_ssl
        
    insecure_ssl = property(_getinsecure_ssl)


    
##
##
##
class GlobalHook2(ResponseBase):
    def __init__(self, type:str=None, id:int=None, name:str=None, active:bool=None, events:list=[], config:dict=None, updated_at:str=None, created_at:str=None, url:str=None, ping_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._type = type
        self._id = id
        self._name = name
        self._active = active
        self._events = events
        self._config = config
        self._updated_at = updated_at
        self._created_at = created_at
        self._url = url
        self._ping_url = ping_url
        return
        
    

    
    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getactive(self):
        return self._active
        
    active = property(_getactive)

    def _getevents(self):
        return self._events and [ entry for entry in self._events ]
        
    events = property(_getevents)

    def _getconfig(self):
        return self._config and Globalhook2_config(**self._config)
        
    config = property(_getconfig)

    def _getupdated_at(self):
        return self._updated_at
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getping_url(self):
        return self._ping_url
        
    ping_url = property(_getping_url)


    
##
##
##
class PublicKeyFull(ResponseBase):
    def __init__(self, last_used:datetime, created_at:datetime, verified:bool, read_only:bool, title:str, url:str, repository_id:int, user_id:int, key:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._last_used = last_used
        self._created_at = created_at
        self._verified = verified
        self._read_only = read_only
        self._title = title
        self._url = url
        self._repository_id = repository_id
        self._user_id = user_id
        self._key = key
        self._id = id
        return
        
    

    
    def _getlast_used(self):
        return self._last_used and datetime.datetime.fromisoformat(self._last_used[0:-1])
        
    last_used = property(_getlast_used)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getverified(self):
        return self._verified
        
    verified = property(_getverified)

    def _getread_only(self):
        return self._read_only
        
    read_only = property(_getread_only)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getrepository_id(self):
        return self._repository_id
        
    repository_id = property(_getrepository_id)

    def _getuser_id(self):
        return self._user_id
        
    user_id = property(_getuser_id)

    def _getkey(self):
        return self._key
        
    key = property(_getkey)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class LdapMappingTeam(ResponseBase):
    def __init__(self, ldap_dn:str=None, id:int=None, node_id:str=None, url:str=None, html_url:str=None, name:str=None, slug:str=None, description:str=None, privacy:str=None, permission:str=None, members_url:str=None, repositories_url:str=None, parent:object=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._ldap_dn = ldap_dn
        self._id = id
        self._node_id = node_id
        self._url = url
        self._html_url = html_url
        self._name = name
        self._slug = slug
        self._description = description
        self._privacy = privacy
        self._permission = permission
        self._members_url = members_url
        self._repositories_url = repositories_url
        self._parent = parent
        return
        
    

    
    def _getldap_dn(self):
        return self._ldap_dn
        
    ldap_dn = property(_getldap_dn)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getslug(self):
        return self._slug
        
    slug = property(_getslug)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getprivacy(self):
        return self._privacy
        
    privacy = property(_getprivacy)

    def _getpermission(self):
        return self._permission
        
    permission = property(_getpermission)

    def _getmembers_url(self):
        return self._members_url
        
    members_url = property(_getmembers_url)

    def _getrepositories_url(self):
        return self._repositories_url
        
    repositories_url = property(_getrepositories_url)

    def _getparent(self):
        return self._parent
        
    parent = property(_getparent)


    
##
##
##
class Ldapprivateuser_plan(ResponseBase):
    def __init__(self, private_repos:int, space:int, name:str, collaborators:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._private_repos = private_repos
        self._space = space
        self._name = name
        self._collaborators = collaborators
        return
        
    

    
    def _getprivate_repos(self):
        return self._private_repos
        
    private_repos = property(_getprivate_repos)

    def _getspace(self):
        return self._space
        
    space = property(_getspace)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getcollaborators(self):
        return self._collaborators
        
    collaborators = property(_getcollaborators)


    
##
##
##
class LdapPrivateUser(ResponseBase):
    """Ldap Private User """
    def __init__(self, two_factor_authentication:bool, collaborators:int, disk_usage:int, owned_private_repos:int, total_private_repos:int, private_gists:int, updated_at:datetime, created_at:datetime, following:int, followers:int, public_gists:int, public_repos:int, bio:str, hireable:bool, email:str, location:str, blog:str, company:str, name:str, site_admin:bool, type:str, received_events_url:str, events_url:str, repos_url:str, organizations_url:str, subscriptions_url:str, starred_url:str, gists_url:str, following_url:str, followers_url:str, html_url:str, url:str, gravatar_id:str, avatar_url:str, node_id:str, id:int, login:str, ldap_dn:str=None, twitter_username:str=None, plan:dict=None, suspended_at:datetime=None, business_plus:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._two_factor_authentication = two_factor_authentication
        self._collaborators = collaborators
        self._disk_usage = disk_usage
        self._owned_private_repos = owned_private_repos
        self._total_private_repos = total_private_repos
        self._private_gists = private_gists
        self._updated_at = updated_at
        self._created_at = created_at
        self._following = following
        self._followers = followers
        self._public_gists = public_gists
        self._public_repos = public_repos
        self._bio = bio
        self._hireable = hireable
        self._email = email
        self._location = location
        self._blog = blog
        self._company = company
        self._name = name
        self._site_admin = site_admin
        self._type = type
        self._received_events_url = received_events_url
        self._events_url = events_url
        self._repos_url = repos_url
        self._organizations_url = organizations_url
        self._subscriptions_url = subscriptions_url
        self._starred_url = starred_url
        self._gists_url = gists_url
        self._following_url = following_url
        self._followers_url = followers_url
        self._html_url = html_url
        self._url = url
        self._gravatar_id = gravatar_id
        self._avatar_url = avatar_url
        self._node_id = node_id
        self._id = id
        self._login = login
        self._ldap_dn = ldap_dn
        self._twitter_username = twitter_username
        self._plan = plan
        self._suspended_at = suspended_at
        self._business_plus = business_plus
        return
        
    

    
    def _gettwo_factor_authentication(self):
        return self._two_factor_authentication
        
    two_factor_authentication = property(_gettwo_factor_authentication)

    def _getcollaborators(self):
        return self._collaborators
        
    collaborators = property(_getcollaborators)

    def _getdisk_usage(self):
        return self._disk_usage
        
    disk_usage = property(_getdisk_usage)

    def _getowned_private_repos(self):
        return self._owned_private_repos
        
    owned_private_repos = property(_getowned_private_repos)

    def _gettotal_private_repos(self):
        return self._total_private_repos
        
    total_private_repos = property(_gettotal_private_repos)

    def _getprivate_gists(self):
        return self._private_gists
        
    private_gists = property(_getprivate_gists)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getfollowing(self):
        return self._following
        
    following = property(_getfollowing)

    def _getfollowers(self):
        return self._followers
        
    followers = property(_getfollowers)

    def _getpublic_gists(self):
        return self._public_gists
        
    public_gists = property(_getpublic_gists)

    def _getpublic_repos(self):
        return self._public_repos
        
    public_repos = property(_getpublic_repos)

    def _getbio(self):
        return self._bio
        
    bio = property(_getbio)

    def _gethireable(self):
        return self._hireable
        
    hireable = property(_gethireable)

    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _getlocation(self):
        return self._location
        
    location = property(_getlocation)

    def _getblog(self):
        return self._blog
        
    blog = property(_getblog)

    def _getcompany(self):
        return self._company
        
    company = property(_getcompany)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getsite_admin(self):
        return self._site_admin
        
    site_admin = property(_getsite_admin)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getreceived_events_url(self):
        return self._received_events_url
        
    received_events_url = property(_getreceived_events_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getrepos_url(self):
        return self._repos_url
        
    repos_url = property(_getrepos_url)

    def _getorganizations_url(self):
        return self._organizations_url
        
    organizations_url = property(_getorganizations_url)

    def _getsubscriptions_url(self):
        return self._subscriptions_url
        
    subscriptions_url = property(_getsubscriptions_url)

    def _getstarred_url(self):
        return self._starred_url
        
    starred_url = property(_getstarred_url)

    def _getgists_url(self):
        return self._gists_url
        
    gists_url = property(_getgists_url)

    def _getfollowing_url(self):
        return self._following_url
        
    following_url = property(_getfollowing_url)

    def _getfollowers_url(self):
        return self._followers_url
        
    followers_url = property(_getfollowers_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getgravatar_id(self):
        return self._gravatar_id
        
    gravatar_id = property(_getgravatar_id)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)

    def _getldap_dn(self):
        return self._ldap_dn
        
    ldap_dn = property(_getldap_dn)

    def _gettwitter_username(self):
        return self._twitter_username
        
    twitter_username = property(_gettwitter_username)

    def _getplan(self):
        return self._plan and Ldapprivateuser_plan(**self._plan)
        
    plan = property(_getplan)

    def _getsuspended_at(self):
        return self._suspended_at and datetime.datetime.fromisoformat(self._suspended_at[0:-1])
        
    suspended_at = property(_getsuspended_at)

    def _getbusiness_plus(self):
        return self._business_plus
        
    business_plus = property(_getbusiness_plus)


    
##
##
##
class OrganizationSimple(ResponseBase):
    """Organization Simple """
    def __init__(self, description:str, avatar_url:str, public_members_url:str, members_url:str, issues_url:str, hooks_url:str, events_url:str, repos_url:str, url:str, node_id:str, id:int, login:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._description = description
        self._avatar_url = avatar_url
        self._public_members_url = public_members_url
        self._members_url = members_url
        self._issues_url = issues_url
        self._hooks_url = hooks_url
        self._events_url = events_url
        self._repos_url = repos_url
        self._url = url
        self._node_id = node_id
        self._id = id
        self._login = login
        return
        
    

    
    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)

    def _getpublic_members_url(self):
        return self._public_members_url
        
    public_members_url = property(_getpublic_members_url)

    def _getmembers_url(self):
        return self._members_url
        
    members_url = property(_getmembers_url)

    def _getissues_url(self):
        return self._issues_url
        
    issues_url = property(_getissues_url)

    def _gethooks_url(self):
        return self._hooks_url
        
    hooks_url = property(_gethooks_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getrepos_url(self):
        return self._repos_url
        
    repos_url = property(_getrepos_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)


    
##
##
##
class Prereceiveenvironment_download(ResponseBase):
    def __init__(self, url:str=None, state:str=None, downloaded_at:str=None, message:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._state = state
        self._downloaded_at = downloaded_at
        self._message = message
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)

    def _getdownloaded_at(self):
        return self._downloaded_at
        
    downloaded_at = property(_getdownloaded_at)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)


    
##
##
##
class PreReceiveEnvironment(ResponseBase):
    def __init__(self, id:int=None, name:str=None, image_url:str=None, url:str=None, html_url:str=None, default_environment:bool=None, created_at:str=None, hooks_count:int=None, download:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._name = name
        self._image_url = image_url
        self._url = url
        self._html_url = html_url
        self._default_environment = default_environment
        self._created_at = created_at
        self._hooks_count = hooks_count
        self._download = download
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getimage_url(self):
        return self._image_url
        
    image_url = property(_getimage_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getdefault_environment(self):
        return self._default_environment
        
    default_environment = property(_getdefault_environment)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _gethooks_count(self):
        return self._hooks_count
        
    hooks_count = property(_gethooks_count)

    def _getdownload(self):
        return self._download and Prereceiveenvironment_download(**self._download)
        
    download = property(_getdownload)


    
##
##
##
class PreReceiveEnvironmentDownloadStatus(ResponseBase):
    def __init__(self, url:str=None, state:str=None, downloaded_at:str=None, message:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._state = state
        self._downloaded_at = downloaded_at
        self._message = message
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)

    def _getdownloaded_at(self):
        return self._downloaded_at
        
    downloaded_at = property(_getdownloaded_at)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)


    
##
##
##
class Prereceivehook_script_repository(ResponseBase):
    def __init__(self, id:int=None, full_name:str=None, url:str=None, html_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._full_name = full_name
        self._url = url
        self._html_url = html_url
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getfull_name(self):
        return self._full_name
        
    full_name = property(_getfull_name)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)


    
##
##
##
class Prereceivehook_environment_download(ResponseBase):
    def __init__(self, url:str=None, state:str=None, downloaded_at:str=None, message:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._state = state
        self._downloaded_at = downloaded_at
        self._message = message
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)

    def _getdownloaded_at(self):
        return self._downloaded_at
        
    downloaded_at = property(_getdownloaded_at)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)


    
##
##
##
class Prereceivehook_environment(ResponseBase):
    def __init__(self, id:int=None, name:str=None, image_url:str=None, url:str=None, html_url:str=None, default_environment:bool=None, created_at:str=None, hooks_count:int=None, download:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._name = name
        self._image_url = image_url
        self._url = url
        self._html_url = html_url
        self._default_environment = default_environment
        self._created_at = created_at
        self._hooks_count = hooks_count
        self._download = download
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getimage_url(self):
        return self._image_url
        
    image_url = property(_getimage_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getdefault_environment(self):
        return self._default_environment
        
    default_environment = property(_getdefault_environment)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _gethooks_count(self):
        return self._hooks_count
        
    hooks_count = property(_gethooks_count)

    def _getdownload(self):
        return self._download and Prereceivehook_environment_download(**self._download)
        
    download = property(_getdownload)


    
##
##
##
class PreReceiveHook(ResponseBase):
    def __init__(self, id:int=None, name:str=None, enforcement:str=None, script:str=None, script_repository:dict=None, environment:dict=None, allow_downstream_configuration:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._name = name
        self._enforcement = enforcement
        self._script = script
        self._script_repository = script_repository
        self._environment = environment
        self._allow_downstream_configuration = allow_downstream_configuration
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getenforcement(self):
        return self._enforcement
        
    enforcement = property(_getenforcement)

    def _getscript(self):
        return self._script
        
    script = property(_getscript)

    def _getscript_repository(self):
        return self._script_repository and Prereceivehook_script_repository(**self._script_repository)
        
    script_repository = property(_getscript_repository)

    def _getenvironment(self):
        return self._environment and Prereceivehook_environment(**self._environment)
        
    environment = property(_getenvironment)

    def _getallow_downstream_configuration(self):
        return self._allow_downstream_configuration
        
    allow_downstream_configuration = property(_getallow_downstream_configuration)


    
##
##
##
class NullableSimpleUser(ResponseBase):
    """Simple User """
    def __init__(self, site_admin:bool, type:str, received_events_url:str, events_url:str, repos_url:str, organizations_url:str, subscriptions_url:str, starred_url:str, gists_url:str, following_url:str, followers_url:str, html_url:str, url:str, gravatar_id:str, avatar_url:str, node_id:str, id:int, login:str, name:str=None, email:str=None, starred_at:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._site_admin = site_admin
        self._type = type
        self._received_events_url = received_events_url
        self._events_url = events_url
        self._repos_url = repos_url
        self._organizations_url = organizations_url
        self._subscriptions_url = subscriptions_url
        self._starred_url = starred_url
        self._gists_url = gists_url
        self._following_url = following_url
        self._followers_url = followers_url
        self._html_url = html_url
        self._url = url
        self._gravatar_id = gravatar_id
        self._avatar_url = avatar_url
        self._node_id = node_id
        self._id = id
        self._login = login
        self._name = name
        self._email = email
        self._starred_at = starred_at
        return
        
    

    
    def _getsite_admin(self):
        return self._site_admin
        
    site_admin = property(_getsite_admin)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getreceived_events_url(self):
        return self._received_events_url
        
    received_events_url = property(_getreceived_events_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getrepos_url(self):
        return self._repos_url
        
    repos_url = property(_getrepos_url)

    def _getorganizations_url(self):
        return self._organizations_url
        
    organizations_url = property(_getorganizations_url)

    def _getsubscriptions_url(self):
        return self._subscriptions_url
        
    subscriptions_url = property(_getsubscriptions_url)

    def _getstarred_url(self):
        return self._starred_url
        
    starred_url = property(_getstarred_url)

    def _getgists_url(self):
        return self._gists_url
        
    gists_url = property(_getgists_url)

    def _getfollowing_url(self):
        return self._following_url
        
    following_url = property(_getfollowing_url)

    def _getfollowers_url(self):
        return self._followers_url
        
    followers_url = property(_getfollowers_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getgravatar_id(self):
        return self._gravatar_id
        
    gravatar_id = property(_getgravatar_id)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _getstarred_at(self):
        return self._starred_at
        
    starred_at = property(_getstarred_at)


    
##
##
##
class AppPermissions(ResponseBase):
    """The permissions granted to the user-to-server access token. """
    def __init__(self, actions:str=None, administration:str=None, checks:str=None, contents:str=None, deployments:str=None, environments:str=None, issues:str=None, metadata:str=None, packages:str=None, pages:str=None, pull_requests:str=None, repository_hooks:str=None, repository_projects:str=None, secret_scanning_alerts:str=None, secrets:str=None, security_events:str=None, single_file:str=None, statuses:str=None, vulnerability_alerts:str=None, workflows:str=None, members:str=None, organization_administration:str=None, organization_hooks:str=None, organization_plan:str=None, organization_projects:str=None, organization_packages:str=None, organization_secrets:str=None, organization_self_hosted_runners:str=None, organization_user_blocking:str=None, team_discussions:str=None, content_references:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._actions = actions
        self._administration = administration
        self._checks = checks
        self._contents = contents
        self._deployments = deployments
        self._environments = environments
        self._issues = issues
        self._metadata = metadata
        self._packages = packages
        self._pages = pages
        self._pull_requests = pull_requests
        self._repository_hooks = repository_hooks
        self._repository_projects = repository_projects
        self._secret_scanning_alerts = secret_scanning_alerts
        self._secrets = secrets
        self._security_events = security_events
        self._single_file = single_file
        self._statuses = statuses
        self._vulnerability_alerts = vulnerability_alerts
        self._workflows = workflows
        self._members = members
        self._organization_administration = organization_administration
        self._organization_hooks = organization_hooks
        self._organization_plan = organization_plan
        self._organization_projects = organization_projects
        self._organization_packages = organization_packages
        self._organization_secrets = organization_secrets
        self._organization_self_hosted_runners = organization_self_hosted_runners
        self._organization_user_blocking = organization_user_blocking
        self._team_discussions = team_discussions
        self._content_references = content_references
        return
        
    

    
    def _getactions(self):
        return self._actions
        
    actions = property(_getactions, doc="""The level of permission to grant the access token for GitHub Actions workflows, workflow runs, and artifacts. Can be one of: `read` or `write`. """)

    def _getadministration(self):
        return self._administration
        
    administration = property(_getadministration, doc="""The level of permission to grant the access token for repository creation, deletion, settings, teams, and collaborators creation. Can be one of: `read` or `write`. """)

    def _getchecks(self):
        return self._checks
        
    checks = property(_getchecks, doc="""The level of permission to grant the access token for checks on code. Can be one of: `read` or `write`. """)

    def _getcontents(self):
        return self._contents
        
    contents = property(_getcontents, doc="""The level of permission to grant the access token for repository contents, commits, branches, downloads, releases, and merges. Can be one of: `read` or `write`. """)

    def _getdeployments(self):
        return self._deployments
        
    deployments = property(_getdeployments, doc="""The level of permission to grant the access token for deployments and deployment statuses. Can be one of: `read` or `write`. """)

    def _getenvironments(self):
        return self._environments
        
    environments = property(_getenvironments, doc="""The level of permission to grant the access token for managing repository environments. Can be one of: `read` or `write`. """)

    def _getissues(self):
        return self._issues
        
    issues = property(_getissues, doc="""The level of permission to grant the access token for issues and related comments, assignees, labels, and milestones. Can be one of: `read` or `write`. """)

    def _getmetadata(self):
        return self._metadata
        
    metadata = property(_getmetadata, doc="""The level of permission to grant the access token to search repositories, list collaborators, and access repository metadata. Can be one of: `read` or `write`. """)

    def _getpackages(self):
        return self._packages
        
    packages = property(_getpackages, doc="""The level of permission to grant the access token for packages published to GitHub Packages. Can be one of: `read` or `write`. """)

    def _getpages(self):
        return self._pages
        
    pages = property(_getpages, doc="""The level of permission to grant the access token to retrieve Pages statuses, configuration, and builds, as well as create new builds. Can be one of: `read` or `write`. """)

    def _getpull_requests(self):
        return self._pull_requests
        
    pull_requests = property(_getpull_requests, doc="""The level of permission to grant the access token for pull requests and related comments, assignees, labels, milestones, and merges. Can be one of: `read` or `write`. """)

    def _getrepository_hooks(self):
        return self._repository_hooks
        
    repository_hooks = property(_getrepository_hooks, doc="""The level of permission to grant the access token to manage the post-receive hooks for a repository. Can be one of: `read` or `write`. """)

    def _getrepository_projects(self):
        return self._repository_projects
        
    repository_projects = property(_getrepository_projects, doc="""The level of permission to grant the access token to manage repository projects, columns, and cards. Can be one of: `read`, `write`, or `admin`. """)

    def _getsecret_scanning_alerts(self):
        return self._secret_scanning_alerts
        
    secret_scanning_alerts = property(_getsecret_scanning_alerts, doc="""The level of permission to grant the access token to view and manage secret scanning alerts. Can be one of: `read` or `write`. """)

    def _getsecrets(self):
        return self._secrets
        
    secrets = property(_getsecrets, doc="""The level of permission to grant the access token to manage repository secrets. Can be one of: `read` or `write`. """)

    def _getsecurity_events(self):
        return self._security_events
        
    security_events = property(_getsecurity_events, doc="""The level of permission to grant the access token to view and manage security events like code scanning alerts. Can be one of: `read` or `write`. """)

    def _getsingle_file(self):
        return self._single_file
        
    single_file = property(_getsingle_file, doc="""The level of permission to grant the access token to manage just a single file. Can be one of: `read` or `write`. """)

    def _getstatuses(self):
        return self._statuses
        
    statuses = property(_getstatuses, doc="""The level of permission to grant the access token for commit statuses. Can be one of: `read` or `write`. """)

    def _getvulnerability_alerts(self):
        return self._vulnerability_alerts
        
    vulnerability_alerts = property(_getvulnerability_alerts, doc="""The level of permission to grant the access token to manage Dependabot alerts. Can be one of: `read` or `write`. """)

    def _getworkflows(self):
        return self._workflows
        
    workflows = property(_getworkflows, doc="""The level of permission to grant the access token to update GitHub Actions workflow files. Can be one of: `write`. """)

    def _getmembers(self):
        return self._members
        
    members = property(_getmembers, doc="""The level of permission to grant the access token for organization teams and members. Can be one of: `read` or `write`. """)

    def _getorganization_administration(self):
        return self._organization_administration
        
    organization_administration = property(_getorganization_administration, doc="""The level of permission to grant the access token to manage access to an organization. Can be one of: `read` or `write`. """)

    def _getorganization_hooks(self):
        return self._organization_hooks
        
    organization_hooks = property(_getorganization_hooks, doc="""The level of permission to grant the access token to manage the post-receive hooks for an organization. Can be one of: `read` or `write`. """)

    def _getorganization_plan(self):
        return self._organization_plan
        
    organization_plan = property(_getorganization_plan, doc="""The level of permission to grant the access token for viewing an organization's plan. Can be one of: `read`. """)

    def _getorganization_projects(self):
        return self._organization_projects
        
    organization_projects = property(_getorganization_projects, doc="""The level of permission to grant the access token to manage organization projects and projects beta (where available). Can be one of: `read`, `write`, or `admin`. """)

    def _getorganization_packages(self):
        return self._organization_packages
        
    organization_packages = property(_getorganization_packages, doc="""The level of permission to grant the access token for organization packages published to GitHub Packages. Can be one of: `read` or `write`. """)

    def _getorganization_secrets(self):
        return self._organization_secrets
        
    organization_secrets = property(_getorganization_secrets, doc="""The level of permission to grant the access token to manage organization secrets. Can be one of: `read` or `write`. """)

    def _getorganization_self_hosted_runners(self):
        return self._organization_self_hosted_runners
        
    organization_self_hosted_runners = property(_getorganization_self_hosted_runners, doc="""The level of permission to grant the access token to view and manage GitHub Actions self-hosted runners available to an organization. Can be one of: `read` or `write`. """)

    def _getorganization_user_blocking(self):
        return self._organization_user_blocking
        
    organization_user_blocking = property(_getorganization_user_blocking, doc="""The level of permission to grant the access token to view and manage users blocked by the organization. Can be one of: `read` or `write`. """)

    def _getteam_discussions(self):
        return self._team_discussions
        
    team_discussions = property(_getteam_discussions, doc="""The level of permission to grant the access token to manage team discussions and related comments. Can be one of: `read` or `write`. """)

    def _getcontent_references(self):
        return self._content_references
        
    content_references = property(_getcontent_references, doc="""The level of permission to grant the access token for notification of content references and creation content attachments. Can be one of: `read` or `write`. """)


    
##
##
##
class SimpleUser(ResponseBase):
    """Simple User """
    def __init__(self, site_admin:bool, type:str, received_events_url:str, events_url:str, repos_url:str, organizations_url:str, subscriptions_url:str, starred_url:str, gists_url:str, following_url:str, followers_url:str, html_url:str, url:str, gravatar_id:str, avatar_url:str, node_id:str, id:int, login:str, name:str=None, email:str=None, starred_at:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._site_admin = site_admin
        self._type = type
        self._received_events_url = received_events_url
        self._events_url = events_url
        self._repos_url = repos_url
        self._organizations_url = organizations_url
        self._subscriptions_url = subscriptions_url
        self._starred_url = starred_url
        self._gists_url = gists_url
        self._following_url = following_url
        self._followers_url = followers_url
        self._html_url = html_url
        self._url = url
        self._gravatar_id = gravatar_id
        self._avatar_url = avatar_url
        self._node_id = node_id
        self._id = id
        self._login = login
        self._name = name
        self._email = email
        self._starred_at = starred_at
        return
        
    

    
    def _getsite_admin(self):
        return self._site_admin
        
    site_admin = property(_getsite_admin)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getreceived_events_url(self):
        return self._received_events_url
        
    received_events_url = property(_getreceived_events_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getrepos_url(self):
        return self._repos_url
        
    repos_url = property(_getrepos_url)

    def _getorganizations_url(self):
        return self._organizations_url
        
    organizations_url = property(_getorganizations_url)

    def _getsubscriptions_url(self):
        return self._subscriptions_url
        
    subscriptions_url = property(_getsubscriptions_url)

    def _getstarred_url(self):
        return self._starred_url
        
    starred_url = property(_getstarred_url)

    def _getgists_url(self):
        return self._gists_url
        
    gists_url = property(_getgists_url)

    def _getfollowing_url(self):
        return self._following_url
        
    following_url = property(_getfollowing_url)

    def _getfollowers_url(self):
        return self._followers_url
        
    followers_url = property(_getfollowers_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getgravatar_id(self):
        return self._gravatar_id
        
    gravatar_id = property(_getgravatar_id)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _getstarred_at(self):
        return self._starred_at
        
    starred_at = property(_getstarred_at)


    
##
##
##
class NullableScopedInstallation(ResponseBase):
    def __init__(self, account:dict, repositories_url:str, single_file_name:str, repository_selection:str, permissions:dict, has_multiple_single_files:bool=None, single_file_paths:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._account = account
        self._repositories_url = repositories_url
        self._single_file_name = single_file_name
        self._repository_selection = repository_selection
        self._permissions = permissions
        self._has_multiple_single_files = has_multiple_single_files
        self._single_file_paths = single_file_paths
        return
        
    

    
    def _getaccount(self):
        return self._account and SimpleUser(**self._account)
        
    account = property(_getaccount)

    def _getrepositories_url(self):
        return self._repositories_url
        
    repositories_url = property(_getrepositories_url)

    def _getsingle_file_name(self):
        return self._single_file_name
        
    single_file_name = property(_getsingle_file_name)

    def _getrepository_selection(self):
        return self._repository_selection
        
    repository_selection = property(_getrepository_selection, doc="""Describe whether all repositories have been selected or there's a selection involved """)

    def _getpermissions(self):
        return self._permissions and AppPermissions(**self._permissions)
        
    permissions = property(_getpermissions)

    def _gethas_multiple_single_files(self):
        return self._has_multiple_single_files
        
    has_multiple_single_files = property(_gethas_multiple_single_files)

    def _getsingle_file_paths(self):
        return self._single_file_paths and [ entry for entry in self._single_file_paths ]
        
    single_file_paths = property(_getsingle_file_paths)


    
##
##
##
class Authorization_app(ResponseBase):
    def __init__(self, url:str, name:str, client_id:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._name = name
        self._client_id = client_id
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getclient_id(self):
        return self._client_id
        
    client_id = property(_getclient_id)


    
##
##
##
class Authorization(ResponseBase):
    """The authorization for an OAuth app, GitHub App, or a Personal Access Token. """
    def __init__(self, expires_at:datetime, fingerprint:str, created_at:datetime, updated_at:datetime, note_url:str, note:str, app:dict, hashed_token:str, token_last_eight:str, token:str, scopes:list, url:str, id:int, user:dict=None, installation:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._expires_at = expires_at
        self._fingerprint = fingerprint
        self._created_at = created_at
        self._updated_at = updated_at
        self._note_url = note_url
        self._note = note
        self._app = app
        self._hashed_token = hashed_token
        self._token_last_eight = token_last_eight
        self._token = token
        self._scopes = scopes
        self._url = url
        self._id = id
        self._user = user
        self._installation = installation
        return
        
    

    
    def _getexpires_at(self):
        return self._expires_at and datetime.datetime.fromisoformat(self._expires_at[0:-1])
        
    expires_at = property(_getexpires_at)

    def _getfingerprint(self):
        return self._fingerprint
        
    fingerprint = property(_getfingerprint)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getnote_url(self):
        return self._note_url
        
    note_url = property(_getnote_url)

    def _getnote(self):
        return self._note
        
    note = property(_getnote)

    def _getapp(self):
        return self._app and Authorization_app(**self._app)
        
    app = property(_getapp)

    def _gethashed_token(self):
        return self._hashed_token
        
    hashed_token = property(_gethashed_token)

    def _gettoken_last_eight(self):
        return self._token_last_eight
        
    token_last_eight = property(_gettoken_last_eight)

    def _gettoken(self):
        return self._token
        
    token = property(_gettoken)

    def _getscopes(self):
        return self._scopes and [ entry for entry in self._scopes ]
        
    scopes = property(_getscopes, doc="""A list of scopes that this authorization is in. """)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _getinstallation(self):
        return self._installation and NullableScopedInstallation(**self._installation)
        
    installation = property(_getinstallation)


    
##
##
##
class Integration_permissions(ResponseBase):
    """The set of permissions for the GitHub app """
    def __init__(self, issues:str=None, checks:str=None, metadata:str=None, contents:str=None, deployments:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._issues = issues
        self._checks = checks
        self._metadata = metadata
        self._contents = contents
        self._deployments = deployments
        return
        
    

    
    def _getissues(self):
        return self._issues
        
    issues = property(_getissues)

    def _getchecks(self):
        return self._checks
        
    checks = property(_getchecks)

    def _getmetadata(self):
        return self._metadata
        
    metadata = property(_getmetadata)

    def _getcontents(self):
        return self._contents
        
    contents = property(_getcontents)

    def _getdeployments(self):
        return self._deployments
        
    deployments = property(_getdeployments)


    
##
##
##
class Integration(ResponseBase):
    """GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. """
    def __init__(self, events:list, permissions:dict, updated_at:datetime, created_at:datetime, html_url:str, external_url:str, description:str, name:str, owner:dict, node_id:str, id:int, slug:str=None, installations_count:int=None, client_id:str=None, client_secret:str=None, webhook_secret:str=None, pem:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._events = events
        self._permissions = permissions
        self._updated_at = updated_at
        self._created_at = created_at
        self._html_url = html_url
        self._external_url = external_url
        self._description = description
        self._name = name
        self._owner = owner
        self._node_id = node_id
        self._id = id
        self._slug = slug
        self._installations_count = installations_count
        self._client_id = client_id
        self._client_secret = client_secret
        self._webhook_secret = webhook_secret
        self._pem = pem
        return
        
    

    
    def _getevents(self):
        return self._events and [ entry for entry in self._events ]
        
    events = property(_getevents, doc="""The list of events for the GitHub app """)

    def _getpermissions(self):
        return self._permissions and Integration_permissions(**self._permissions)
        
    permissions = property(_getpermissions, doc="""The set of permissions for the GitHub app """)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getexternal_url(self):
        return self._external_url
        
    external_url = property(_getexternal_url)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the GitHub app """)

    def _getowner(self):
        return self._owner and NullableSimpleUser(**self._owner)
        
    owner = property(_getowner)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the GitHub app """)

    def _getslug(self):
        return self._slug
        
    slug = property(_getslug, doc="""The slug name of the GitHub app """)

    def _getinstallations_count(self):
        return self._installations_count
        
    installations_count = property(_getinstallations_count, doc="""The number of installations associated with the GitHub app """)

    def _getclient_id(self):
        return self._client_id
        
    client_id = property(_getclient_id)

    def _getclient_secret(self):
        return self._client_secret
        
    client_secret = property(_getclient_secret)

    def _getwebhook_secret(self):
        return self._webhook_secret
        
    webhook_secret = property(_getwebhook_secret)

    def _getpem(self):
        return self._pem
        
    pem = property(_getpem)


    
##
##
##
class BasicError(ResponseBase):
    """Basic Error """
    def __init__(self, message:str=None, documentation_url:str=None, url:str=None, status:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._documentation_url = documentation_url
        self._url = url
        self._status = status
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getdocumentation_url(self):
        return self._documentation_url
        
    documentation_url = property(_getdocumentation_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getstatus(self):
        return self._status
        
    status = property(_getstatus)


    def _ok(self):
        return False

    ok = property(_ok, doc='not ok')

    def __repr__(self):
        return f"BasicError({self.status_code}, \"{self.message}\")"

##
##
##
class ValidationErrorSimple(ResponseBase):
    """Validation Error Simple """
    def __init__(self, documentation_url:str, message:str, errors:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._documentation_url = documentation_url
        self._message = message
        self._errors = errors
        return
        
    

    
    def _getdocumentation_url(self):
        return self._documentation_url
        
    documentation_url = property(_getdocumentation_url)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _geterrors(self):
        return self._errors and [ entry for entry in self._errors ]
        
    errors = property(_geterrors)


    
##
##
##
class WebhookConfiguration(ResponseBase):
    """Configuration object of the webhook """
    def __init__(self, url:str=None, content_type:str=None, secret:str=None, insecure_ssl=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._content_type = content_type
        self._secret = secret
        self._insecure_ssl = insecure_ssl
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getcontent_type(self):
        return self._content_type
        
    content_type = property(_getcontent_type)

    def _getsecret(self):
        return self._secret
        
    secret = property(_getsecret)

    def _getinsecure_ssl(self):
        return self._insecure_ssl
        
    insecure_ssl = property(_getinsecure_ssl)


    
##
##
##
class SimpleWebhookDelivery(ResponseBase):
    """Delivery made by a webhook, without request and response information. """
    def __init__(self, repository_id:int, installation_id:int, action:str, event:str, status_code:int, status:str, duration:int, redelivery:bool, delivered_at:datetime, guid:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._repository_id = repository_id
        self._installation_id = installation_id
        self._action = action
        self._event = event
        self._status_code = status_code
        self._status = status
        self._duration = duration
        self._redelivery = redelivery
        self._delivered_at = delivered_at
        self._guid = guid
        self._id = id
        return
        
    

    
    def _getrepository_id(self):
        return self._repository_id
        
    repository_id = property(_getrepository_id, doc="""The id of the repository associated with this event. """)

    def _getinstallation_id(self):
        return self._installation_id
        
    installation_id = property(_getinstallation_id, doc="""The id of the GitHub App installation associated with this event. """)

    def _getaction(self):
        return self._action
        
    action = property(_getaction, doc="""The type of activity for the event that triggered the delivery. """)

    def _getevent(self):
        return self._event
        
    event = property(_getevent, doc="""The event that triggered the delivery. """)

    def _getstatus_code(self):
        return self._status_code
        
    status_code = property(_getstatus_code, doc="""Status code received when delivery was made. """)

    def _getstatus(self):
        return self._status
        
    status = property(_getstatus, doc="""Describes the response returned after attempting the delivery. """)

    def _getduration(self):
        return self._duration
        
    duration = property(_getduration, doc="""Time spent delivering. """)

    def _getredelivery(self):
        return self._redelivery
        
    redelivery = property(_getredelivery, doc="""Whether the webhook delivery is a redelivery. """)

    def _getdelivered_at(self):
        return self._delivered_at and datetime.datetime.fromisoformat(self._delivered_at[0:-1])
        
    delivered_at = property(_getdelivered_at, doc="""Time when the webhook delivery occurred. """)

    def _getguid(self):
        return self._guid
        
    guid = property(_getguid, doc="""Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event). """)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the webhook delivery. """)


    
##
##
##
class ScimError(ResponseBase):
    """Scim Error """
    def __init__(self, message:str=None, documentation_url:str=None, detail:str=None, status:int=None, scimType:str=None, schemas:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._documentation_url = documentation_url
        self._detail = detail
        self._status = status
        self._scimType = scimType
        self._schemas = schemas
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getdocumentation_url(self):
        return self._documentation_url
        
    documentation_url = property(_getdocumentation_url)

    def _getdetail(self):
        return self._detail
        
    detail = property(_getdetail)

    def _getstatus(self):
        return self._status
        
    status = property(_getstatus)

    def _getscimType(self):
        return self._scimType
        
    scimType = property(_getscimType)

    def _getschemas(self):
        return self._schemas and [ entry for entry in self._schemas ]
        
    schemas = property(_getschemas)


    
##
##
##
class Validationerror_errors(ResponseBase):
    def __init__(self, code:str, resource:str=None, field:str=None, message:str=None, index:int=None, value=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._code = code
        self._resource = resource
        self._field = field
        self._message = message
        self._index = index
        self._value = value
        return
        
    

    
    def _getcode(self):
        return self._code
        
    code = property(_getcode)

    def _getresource(self):
        return self._resource
        
    resource = property(_getresource)

    def _getfield(self):
        return self._field
        
    field = property(_getfield)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getindex(self):
        return self._index
        
    index = property(_getindex)

    def _getvalue(self):
        return self._value
        
    value = property(_getvalue)


    
##
##
##
class ValidationError(ResponseBase):
    """Validation Error """
    def __init__(self, documentation_url:str, message:str, errors:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._documentation_url = documentation_url
        self._message = message
        self._errors = errors
        return
        
    

    
    def _getdocumentation_url(self):
        return self._documentation_url
        
    documentation_url = property(_getdocumentation_url)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _geterrors(self):
        return self._errors and [ entry and Validationerror_errors(**entry) for entry in self._errors ]
        
    errors = property(_geterrors)


    def _ok(self):
        return False

    ok = property(_ok, doc='not ok')

##
##
##
class Webhookdelivery_request(ResponseBase):
    def __init__(self, payload:object, headers:object, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._payload = payload
        self._headers = headers
        return
        
    

    
    def _getpayload(self):
        return self._payload
        
    payload = property(_getpayload, doc="""The webhook payload. """)

    def _getheaders(self):
        return self._headers
        
    headers = property(_getheaders, doc="""The request headers sent with the webhook delivery. """)


    
##
##
##
class Webhookdelivery_response(ResponseBase):
    def __init__(self, payload:str, headers:object, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._payload = payload
        self._headers = headers
        return
        
    

    
    def _getpayload(self):
        return self._payload
        
    payload = property(_getpayload, doc="""The response payload received. """)

    def _getheaders(self):
        return self._headers
        
    headers = property(_getheaders, doc="""The response headers received when the delivery was made. """)


    
##
##
##
class WebhookDelivery(ResponseBase):
    """Delivery made by a webhook. """
    def __init__(self, response:dict, request:dict, repository_id:int, installation_id:int, action:str, event:str, status_code:int, status:str, duration:int, redelivery:bool, delivered_at:datetime, guid:str, id:int, url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._response = response
        self._request = request
        self._repository_id = repository_id
        self._installation_id = installation_id
        self._action = action
        self._event = event
        self._status_code = status_code
        self._status = status
        self._duration = duration
        self._redelivery = redelivery
        self._delivered_at = delivered_at
        self._guid = guid
        self._id = id
        self._url = url
        return
        
    

    
    def _getresponse(self):
        return self._response and Webhookdelivery_response(**self._response)
        
    response = property(_getresponse)

    def _getrequest(self):
        return self._request and Webhookdelivery_request(**self._request)
        
    request = property(_getrequest)

    def _getrepository_id(self):
        return self._repository_id
        
    repository_id = property(_getrepository_id, doc="""The id of the repository associated with this event. """)

    def _getinstallation_id(self):
        return self._installation_id
        
    installation_id = property(_getinstallation_id, doc="""The id of the GitHub App installation associated with this event. """)

    def _getaction(self):
        return self._action
        
    action = property(_getaction, doc="""The type of activity for the event that triggered the delivery. """)

    def _getevent(self):
        return self._event
        
    event = property(_getevent, doc="""The event that triggered the delivery. """)

    def _getstatus_code(self):
        return self._status_code
        
    status_code = property(_getstatus_code, doc="""Status code received when delivery was made. """)

    def _getstatus(self):
        return self._status
        
    status = property(_getstatus, doc="""Description of the status of the attempted delivery """)

    def _getduration(self):
        return self._duration
        
    duration = property(_getduration, doc="""Time spent delivering. """)

    def _getredelivery(self):
        return self._redelivery
        
    redelivery = property(_getredelivery, doc="""Whether the delivery is a redelivery. """)

    def _getdelivered_at(self):
        return self._delivered_at and datetime.datetime.fromisoformat(self._delivered_at[0:-1])
        
    delivered_at = property(_getdelivered_at, doc="""Time when the delivery was delivered. """)

    def _getguid(self):
        return self._guid
        
    guid = property(_getguid, doc="""Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event). """)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the delivery. """)

    def _geturl(self):
        return self._url
        
    url = property(_geturl, doc="""The URL target of the delivery. """)


    
##
##
##
class Enterprise(ResponseBase):
    """An enterprise account """
    def __init__(self, avatar_url:str, updated_at:datetime, created_at:datetime, slug:str, name:str, node_id:str, id:int, html_url:str, description:str=None, website_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._avatar_url = avatar_url
        self._updated_at = updated_at
        self._created_at = created_at
        self._slug = slug
        self._name = name
        self._node_id = node_id
        self._id = id
        self._html_url = html_url
        self._description = description
        self._website_url = website_url
        return
        
    

    
    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getslug(self):
        return self._slug
        
    slug = property(_getslug, doc="""The slug url identifier for the enterprise. """)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the enterprise. """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the enterprise """)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription, doc="""A short description of the enterprise. """)

    def _getwebsite_url(self):
        return self._website_url
        
    website_url = property(_getwebsite_url, doc="""The enterprise's website URL. """)


    
##
##
##
class Installation(ResponseBase):
    """Installation """
    def __init__(self, suspended_at:datetime, suspended_by:dict, app_slug:str, single_file_name:str, updated_at:datetime, created_at:datetime, events:list, permissions:dict, target_type:str, target_id:int, app_id:int, html_url:str, repositories_url:str, access_tokens_url:str, repository_selection:str, account, id:int, has_multiple_single_files:bool=None, single_file_paths:list=[], contact_email:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._suspended_at = suspended_at
        self._suspended_by = suspended_by
        self._app_slug = app_slug
        self._single_file_name = single_file_name
        self._updated_at = updated_at
        self._created_at = created_at
        self._events = events
        self._permissions = permissions
        self._target_type = target_type
        self._target_id = target_id
        self._app_id = app_id
        self._html_url = html_url
        self._repositories_url = repositories_url
        self._access_tokens_url = access_tokens_url
        self._repository_selection = repository_selection
        self._account = account
        self._id = id
        self._has_multiple_single_files = has_multiple_single_files
        self._single_file_paths = single_file_paths
        self._contact_email = contact_email
        return
        
    

    
    def _getsuspended_at(self):
        return self._suspended_at and datetime.datetime.fromisoformat(self._suspended_at[0:-1])
        
    suspended_at = property(_getsuspended_at)

    def _getsuspended_by(self):
        return self._suspended_by and NullableSimpleUser(**self._suspended_by)
        
    suspended_by = property(_getsuspended_by)

    def _getapp_slug(self):
        return self._app_slug
        
    app_slug = property(_getapp_slug)

    def _getsingle_file_name(self):
        return self._single_file_name
        
    single_file_name = property(_getsingle_file_name)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getevents(self):
        return self._events and [ entry for entry in self._events ]
        
    events = property(_getevents)

    def _getpermissions(self):
        return self._permissions and AppPermissions(**self._permissions)
        
    permissions = property(_getpermissions)

    def _gettarget_type(self):
        return self._target_type
        
    target_type = property(_gettarget_type)

    def _gettarget_id(self):
        return self._target_id
        
    target_id = property(_gettarget_id, doc="""The ID of the user or organization this token is being scoped to. """)

    def _getapp_id(self):
        return self._app_id
        
    app_id = property(_getapp_id)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getrepositories_url(self):
        return self._repositories_url
        
    repositories_url = property(_getrepositories_url)

    def _getaccess_tokens_url(self):
        return self._access_tokens_url
        
    access_tokens_url = property(_getaccess_tokens_url)

    def _getrepository_selection(self):
        return self._repository_selection
        
    repository_selection = property(_getrepository_selection, doc="""Describe whether all repositories have been selected or there's a selection involved """)

    def _getaccount(self):
        return self._account
        
    account = property(_getaccount)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""The ID of the installation. """)

    def _gethas_multiple_single_files(self):
        return self._has_multiple_single_files
        
    has_multiple_single_files = property(_gethas_multiple_single_files)

    def _getsingle_file_paths(self):
        return self._single_file_paths and [ entry for entry in self._single_file_paths ]
        
    single_file_paths = property(_getsingle_file_paths)

    def _getcontact_email(self):
        return self._contact_email
        
    contact_email = property(_getcontact_email)


    
##
##
##
class NullableLicenseSimple(ResponseBase):
    """License Simple """
    def __init__(self, node_id:str, spdx_id:str, url:str, name:str, key:str, html_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._node_id = node_id
        self._spdx_id = spdx_id
        self._url = url
        self._name = name
        self._key = key
        self._html_url = html_url
        return
        
    

    
    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getspdx_id(self):
        return self._spdx_id
        
    spdx_id = property(_getspdx_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getkey(self):
        return self._key
        
    key = property(_getkey)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)


    
##
##
##
class Repository_permissions(ResponseBase):
    def __init__(self, push:bool, pull:bool, admin:bool, triage:bool=None, maintain:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._push = push
        self._pull = pull
        self._admin = admin
        self._triage = triage
        self._maintain = maintain
        return
        
    

    
    def _getpush(self):
        return self._push
        
    push = property(_getpush)

    def _getpull(self):
        return self._pull
        
    pull = property(_getpull)

    def _getadmin(self):
        return self._admin
        
    admin = property(_getadmin)

    def _gettriage(self):
        return self._triage
        
    triage = property(_gettriage)

    def _getmaintain(self):
        return self._maintain
        
    maintain = property(_getmaintain)


    
##
##
##
class Repository_template_repository_owner(ResponseBase):
    def __init__(self, login:str=None, id:int=None, node_id:str=None, avatar_url:str=None, gravatar_id:str=None, url:str=None, html_url:str=None, followers_url:str=None, following_url:str=None, gists_url:str=None, starred_url:str=None, subscriptions_url:str=None, organizations_url:str=None, repos_url:str=None, events_url:str=None, received_events_url:str=None, type:str=None, site_admin:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._login = login
        self._id = id
        self._node_id = node_id
        self._avatar_url = avatar_url
        self._gravatar_id = gravatar_id
        self._url = url
        self._html_url = html_url
        self._followers_url = followers_url
        self._following_url = following_url
        self._gists_url = gists_url
        self._starred_url = starred_url
        self._subscriptions_url = subscriptions_url
        self._organizations_url = organizations_url
        self._repos_url = repos_url
        self._events_url = events_url
        self._received_events_url = received_events_url
        self._type = type
        self._site_admin = site_admin
        return
        
    

    
    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)

    def _getgravatar_id(self):
        return self._gravatar_id
        
    gravatar_id = property(_getgravatar_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getfollowers_url(self):
        return self._followers_url
        
    followers_url = property(_getfollowers_url)

    def _getfollowing_url(self):
        return self._following_url
        
    following_url = property(_getfollowing_url)

    def _getgists_url(self):
        return self._gists_url
        
    gists_url = property(_getgists_url)

    def _getstarred_url(self):
        return self._starred_url
        
    starred_url = property(_getstarred_url)

    def _getsubscriptions_url(self):
        return self._subscriptions_url
        
    subscriptions_url = property(_getsubscriptions_url)

    def _getorganizations_url(self):
        return self._organizations_url
        
    organizations_url = property(_getorganizations_url)

    def _getrepos_url(self):
        return self._repos_url
        
    repos_url = property(_getrepos_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getreceived_events_url(self):
        return self._received_events_url
        
    received_events_url = property(_getreceived_events_url)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getsite_admin(self):
        return self._site_admin
        
    site_admin = property(_getsite_admin)


    
##
##
##
class Repository_template_repository_permissions(ResponseBase):
    def __init__(self, admin:bool=None, maintain:bool=None, push:bool=None, triage:bool=None, pull:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._admin = admin
        self._maintain = maintain
        self._push = push
        self._triage = triage
        self._pull = pull
        return
        
    

    
    def _getadmin(self):
        return self._admin
        
    admin = property(_getadmin)

    def _getmaintain(self):
        return self._maintain
        
    maintain = property(_getmaintain)

    def _getpush(self):
        return self._push
        
    push = property(_getpush)

    def _gettriage(self):
        return self._triage
        
    triage = property(_gettriage)

    def _getpull(self):
        return self._pull
        
    pull = property(_getpull)


    
##
##
##
class Repository_template_repository(ResponseBase):
    def __init__(self, id:int=None, node_id:str=None, name:str=None, full_name:str=None, owner:dict=None, private:bool=None, html_url:str=None, description:str=None, fork:bool=None, url:str=None, archive_url:str=None, assignees_url:str=None, blobs_url:str=None, branches_url:str=None, collaborators_url:str=None, comments_url:str=None, commits_url:str=None, compare_url:str=None, contents_url:str=None, contributors_url:str=None, deployments_url:str=None, downloads_url:str=None, events_url:str=None, forks_url:str=None, git_commits_url:str=None, git_refs_url:str=None, git_tags_url:str=None, git_url:str=None, issue_comment_url:str=None, issue_events_url:str=None, issues_url:str=None, keys_url:str=None, labels_url:str=None, languages_url:str=None, merges_url:str=None, milestones_url:str=None, notifications_url:str=None, pulls_url:str=None, releases_url:str=None, ssh_url:str=None, stargazers_url:str=None, statuses_url:str=None, subscribers_url:str=None, subscription_url:str=None, tags_url:str=None, teams_url:str=None, trees_url:str=None, clone_url:str=None, mirror_url:str=None, hooks_url:str=None, svn_url:str=None, homepage:str=None, language:str=None, forks_count:int=None, stargazers_count:int=None, watchers_count:int=None, size:int=None, default_branch:str=None, open_issues_count:int=None, is_template:bool=None, topics:list=[], has_issues:bool=None, has_projects:bool=None, has_wiki:bool=None, has_pages:bool=None, has_downloads:bool=None, archived:bool=None, disabled:bool=None, visibility:str=None, pushed_at:str=None, created_at:str=None, updated_at:str=None, permissions:dict=None, allow_rebase_merge:bool=None, temp_clone_token:str=None, allow_squash_merge:bool=None, allow_auto_merge:bool=None, delete_branch_on_merge:bool=None, allow_update_branch:bool=None, allow_merge_commit:bool=None, subscribers_count:int=None, network_count:int=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._node_id = node_id
        self._name = name
        self._full_name = full_name
        self._owner = owner
        self._private = private
        self._html_url = html_url
        self._description = description
        self._fork = fork
        self._url = url
        self._archive_url = archive_url
        self._assignees_url = assignees_url
        self._blobs_url = blobs_url
        self._branches_url = branches_url
        self._collaborators_url = collaborators_url
        self._comments_url = comments_url
        self._commits_url = commits_url
        self._compare_url = compare_url
        self._contents_url = contents_url
        self._contributors_url = contributors_url
        self._deployments_url = deployments_url
        self._downloads_url = downloads_url
        self._events_url = events_url
        self._forks_url = forks_url
        self._git_commits_url = git_commits_url
        self._git_refs_url = git_refs_url
        self._git_tags_url = git_tags_url
        self._git_url = git_url
        self._issue_comment_url = issue_comment_url
        self._issue_events_url = issue_events_url
        self._issues_url = issues_url
        self._keys_url = keys_url
        self._labels_url = labels_url
        self._languages_url = languages_url
        self._merges_url = merges_url
        self._milestones_url = milestones_url
        self._notifications_url = notifications_url
        self._pulls_url = pulls_url
        self._releases_url = releases_url
        self._ssh_url = ssh_url
        self._stargazers_url = stargazers_url
        self._statuses_url = statuses_url
        self._subscribers_url = subscribers_url
        self._subscription_url = subscription_url
        self._tags_url = tags_url
        self._teams_url = teams_url
        self._trees_url = trees_url
        self._clone_url = clone_url
        self._mirror_url = mirror_url
        self._hooks_url = hooks_url
        self._svn_url = svn_url
        self._homepage = homepage
        self._language = language
        self._forks_count = forks_count
        self._stargazers_count = stargazers_count
        self._watchers_count = watchers_count
        self._size = size
        self._default_branch = default_branch
        self._open_issues_count = open_issues_count
        self._is_template = is_template
        self._topics = topics
        self._has_issues = has_issues
        self._has_projects = has_projects
        self._has_wiki = has_wiki
        self._has_pages = has_pages
        self._has_downloads = has_downloads
        self._archived = archived
        self._disabled = disabled
        self._visibility = visibility
        self._pushed_at = pushed_at
        self._created_at = created_at
        self._updated_at = updated_at
        self._permissions = permissions
        self._allow_rebase_merge = allow_rebase_merge
        self._temp_clone_token = temp_clone_token
        self._allow_squash_merge = allow_squash_merge
        self._allow_auto_merge = allow_auto_merge
        self._delete_branch_on_merge = delete_branch_on_merge
        self._allow_update_branch = allow_update_branch
        self._allow_merge_commit = allow_merge_commit
        self._subscribers_count = subscribers_count
        self._network_count = network_count
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getfull_name(self):
        return self._full_name
        
    full_name = property(_getfull_name)

    def _getowner(self):
        return self._owner and Repository_template_repository_owner(**self._owner)
        
    owner = property(_getowner)

    def _getprivate(self):
        return self._private
        
    private = property(_getprivate)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getfork(self):
        return self._fork
        
    fork = property(_getfork)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getarchive_url(self):
        return self._archive_url
        
    archive_url = property(_getarchive_url)

    def _getassignees_url(self):
        return self._assignees_url
        
    assignees_url = property(_getassignees_url)

    def _getblobs_url(self):
        return self._blobs_url
        
    blobs_url = property(_getblobs_url)

    def _getbranches_url(self):
        return self._branches_url
        
    branches_url = property(_getbranches_url)

    def _getcollaborators_url(self):
        return self._collaborators_url
        
    collaborators_url = property(_getcollaborators_url)

    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _getcommits_url(self):
        return self._commits_url
        
    commits_url = property(_getcommits_url)

    def _getcompare_url(self):
        return self._compare_url
        
    compare_url = property(_getcompare_url)

    def _getcontents_url(self):
        return self._contents_url
        
    contents_url = property(_getcontents_url)

    def _getcontributors_url(self):
        return self._contributors_url
        
    contributors_url = property(_getcontributors_url)

    def _getdeployments_url(self):
        return self._deployments_url
        
    deployments_url = property(_getdeployments_url)

    def _getdownloads_url(self):
        return self._downloads_url
        
    downloads_url = property(_getdownloads_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getforks_url(self):
        return self._forks_url
        
    forks_url = property(_getforks_url)

    def _getgit_commits_url(self):
        return self._git_commits_url
        
    git_commits_url = property(_getgit_commits_url)

    def _getgit_refs_url(self):
        return self._git_refs_url
        
    git_refs_url = property(_getgit_refs_url)

    def _getgit_tags_url(self):
        return self._git_tags_url
        
    git_tags_url = property(_getgit_tags_url)

    def _getgit_url(self):
        return self._git_url
        
    git_url = property(_getgit_url)

    def _getissue_comment_url(self):
        return self._issue_comment_url
        
    issue_comment_url = property(_getissue_comment_url)

    def _getissue_events_url(self):
        return self._issue_events_url
        
    issue_events_url = property(_getissue_events_url)

    def _getissues_url(self):
        return self._issues_url
        
    issues_url = property(_getissues_url)

    def _getkeys_url(self):
        return self._keys_url
        
    keys_url = property(_getkeys_url)

    def _getlabels_url(self):
        return self._labels_url
        
    labels_url = property(_getlabels_url)

    def _getlanguages_url(self):
        return self._languages_url
        
    languages_url = property(_getlanguages_url)

    def _getmerges_url(self):
        return self._merges_url
        
    merges_url = property(_getmerges_url)

    def _getmilestones_url(self):
        return self._milestones_url
        
    milestones_url = property(_getmilestones_url)

    def _getnotifications_url(self):
        return self._notifications_url
        
    notifications_url = property(_getnotifications_url)

    def _getpulls_url(self):
        return self._pulls_url
        
    pulls_url = property(_getpulls_url)

    def _getreleases_url(self):
        return self._releases_url
        
    releases_url = property(_getreleases_url)

    def _getssh_url(self):
        return self._ssh_url
        
    ssh_url = property(_getssh_url)

    def _getstargazers_url(self):
        return self._stargazers_url
        
    stargazers_url = property(_getstargazers_url)

    def _getstatuses_url(self):
        return self._statuses_url
        
    statuses_url = property(_getstatuses_url)

    def _getsubscribers_url(self):
        return self._subscribers_url
        
    subscribers_url = property(_getsubscribers_url)

    def _getsubscription_url(self):
        return self._subscription_url
        
    subscription_url = property(_getsubscription_url)

    def _gettags_url(self):
        return self._tags_url
        
    tags_url = property(_gettags_url)

    def _getteams_url(self):
        return self._teams_url
        
    teams_url = property(_getteams_url)

    def _gettrees_url(self):
        return self._trees_url
        
    trees_url = property(_gettrees_url)

    def _getclone_url(self):
        return self._clone_url
        
    clone_url = property(_getclone_url)

    def _getmirror_url(self):
        return self._mirror_url
        
    mirror_url = property(_getmirror_url)

    def _gethooks_url(self):
        return self._hooks_url
        
    hooks_url = property(_gethooks_url)

    def _getsvn_url(self):
        return self._svn_url
        
    svn_url = property(_getsvn_url)

    def _gethomepage(self):
        return self._homepage
        
    homepage = property(_gethomepage)

    def _getlanguage(self):
        return self._language
        
    language = property(_getlanguage)

    def _getforks_count(self):
        return self._forks_count
        
    forks_count = property(_getforks_count)

    def _getstargazers_count(self):
        return self._stargazers_count
        
    stargazers_count = property(_getstargazers_count)

    def _getwatchers_count(self):
        return self._watchers_count
        
    watchers_count = property(_getwatchers_count)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _getdefault_branch(self):
        return self._default_branch
        
    default_branch = property(_getdefault_branch)

    def _getopen_issues_count(self):
        return self._open_issues_count
        
    open_issues_count = property(_getopen_issues_count)

    def _getis_template(self):
        return self._is_template
        
    is_template = property(_getis_template)

    def _gettopics(self):
        return self._topics and [ entry for entry in self._topics ]
        
    topics = property(_gettopics)

    def _gethas_issues(self):
        return self._has_issues
        
    has_issues = property(_gethas_issues)

    def _gethas_projects(self):
        return self._has_projects
        
    has_projects = property(_gethas_projects)

    def _gethas_wiki(self):
        return self._has_wiki
        
    has_wiki = property(_gethas_wiki)

    def _gethas_pages(self):
        return self._has_pages
        
    has_pages = property(_gethas_pages)

    def _gethas_downloads(self):
        return self._has_downloads
        
    has_downloads = property(_gethas_downloads)

    def _getarchived(self):
        return self._archived
        
    archived = property(_getarchived)

    def _getdisabled(self):
        return self._disabled
        
    disabled = property(_getdisabled)

    def _getvisibility(self):
        return self._visibility
        
    visibility = property(_getvisibility)

    def _getpushed_at(self):
        return self._pushed_at
        
    pushed_at = property(_getpushed_at)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getupdated_at(self):
        return self._updated_at
        
    updated_at = property(_getupdated_at)

    def _getpermissions(self):
        return self._permissions and Repository_template_repository_permissions(**self._permissions)
        
    permissions = property(_getpermissions)

    def _getallow_rebase_merge(self):
        return self._allow_rebase_merge
        
    allow_rebase_merge = property(_getallow_rebase_merge)

    def _gettemp_clone_token(self):
        return self._temp_clone_token
        
    temp_clone_token = property(_gettemp_clone_token)

    def _getallow_squash_merge(self):
        return self._allow_squash_merge
        
    allow_squash_merge = property(_getallow_squash_merge)

    def _getallow_auto_merge(self):
        return self._allow_auto_merge
        
    allow_auto_merge = property(_getallow_auto_merge)

    def _getdelete_branch_on_merge(self):
        return self._delete_branch_on_merge
        
    delete_branch_on_merge = property(_getdelete_branch_on_merge)

    def _getallow_update_branch(self):
        return self._allow_update_branch
        
    allow_update_branch = property(_getallow_update_branch)

    def _getallow_merge_commit(self):
        return self._allow_merge_commit
        
    allow_merge_commit = property(_getallow_merge_commit)

    def _getsubscribers_count(self):
        return self._subscribers_count
        
    subscribers_count = property(_getsubscribers_count)

    def _getnetwork_count(self):
        return self._network_count
        
    network_count = property(_getnetwork_count)


    
##
##
##
class Repository(ResponseBase):
    """A git repository """
    def __init__(self, watchers:int, open_issues:int, updated_at:datetime, created_at:datetime, pushed_at:datetime, disabled:bool, has_pages:bool, open_issues_count:int, default_branch:str, size:int, watchers_count:int, stargazers_count:int, forks_count:int, language:str, homepage:str, svn_url:str, hooks_url:str, mirror_url:str, clone_url:str, trees_url:str, teams_url:str, tags_url:str, subscription_url:str, subscribers_url:str, statuses_url:str, stargazers_url:str, ssh_url:str, releases_url:str, pulls_url:str, notifications_url:str, milestones_url:str, merges_url:str, languages_url:str, labels_url:str, keys_url:str, issues_url:str, issue_events_url:str, issue_comment_url:str, git_url:str, git_tags_url:str, git_refs_url:str, git_commits_url:str, forks_url:str, events_url:str, downloads_url:str, deployments_url:str, contributors_url:str, contents_url:str, compare_url:str, commits_url:str, comments_url:str, collaborators_url:str, branches_url:str, blobs_url:str, assignees_url:str, archive_url:str, url:str, fork:bool, description:str, html_url:str, owner:dict, forks:int, license:dict, full_name:str, name:str, node_id:str, id:int, organization:dict=None, permissions:dict=None, private:bool=False, is_template:bool=False, topics:list=[], has_issues:bool=True, has_projects:bool=True, has_wiki:bool=True, has_downloads:bool=True, archived:bool=False, visibility:str='public', allow_rebase_merge:bool=True, template_repository:dict=None, temp_clone_token:str=None, allow_squash_merge:bool=True, allow_auto_merge:bool=False, delete_branch_on_merge:bool=False, allow_merge_commit:bool=True, allow_forking:bool=None, subscribers_count:int=None, network_count:int=None, master_branch:str=None, starred_at:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._watchers = watchers
        self._open_issues = open_issues
        self._updated_at = updated_at
        self._created_at = created_at
        self._pushed_at = pushed_at
        self._disabled = disabled
        self._has_pages = has_pages
        self._open_issues_count = open_issues_count
        self._default_branch = default_branch
        self._size = size
        self._watchers_count = watchers_count
        self._stargazers_count = stargazers_count
        self._forks_count = forks_count
        self._language = language
        self._homepage = homepage
        self._svn_url = svn_url
        self._hooks_url = hooks_url
        self._mirror_url = mirror_url
        self._clone_url = clone_url
        self._trees_url = trees_url
        self._teams_url = teams_url
        self._tags_url = tags_url
        self._subscription_url = subscription_url
        self._subscribers_url = subscribers_url
        self._statuses_url = statuses_url
        self._stargazers_url = stargazers_url
        self._ssh_url = ssh_url
        self._releases_url = releases_url
        self._pulls_url = pulls_url
        self._notifications_url = notifications_url
        self._milestones_url = milestones_url
        self._merges_url = merges_url
        self._languages_url = languages_url
        self._labels_url = labels_url
        self._keys_url = keys_url
        self._issues_url = issues_url
        self._issue_events_url = issue_events_url
        self._issue_comment_url = issue_comment_url
        self._git_url = git_url
        self._git_tags_url = git_tags_url
        self._git_refs_url = git_refs_url
        self._git_commits_url = git_commits_url
        self._forks_url = forks_url
        self._events_url = events_url
        self._downloads_url = downloads_url
        self._deployments_url = deployments_url
        self._contributors_url = contributors_url
        self._contents_url = contents_url
        self._compare_url = compare_url
        self._commits_url = commits_url
        self._comments_url = comments_url
        self._collaborators_url = collaborators_url
        self._branches_url = branches_url
        self._blobs_url = blobs_url
        self._assignees_url = assignees_url
        self._archive_url = archive_url
        self._url = url
        self._fork = fork
        self._description = description
        self._html_url = html_url
        self._owner = owner
        self._forks = forks
        self._license = license
        self._full_name = full_name
        self._name = name
        self._node_id = node_id
        self._id = id
        self._organization = organization
        self._permissions = permissions
        self._private = private
        self._is_template = is_template
        self._topics = topics
        self._has_issues = has_issues
        self._has_projects = has_projects
        self._has_wiki = has_wiki
        self._has_downloads = has_downloads
        self._archived = archived
        self._visibility = visibility
        self._allow_rebase_merge = allow_rebase_merge
        self._template_repository = template_repository
        self._temp_clone_token = temp_clone_token
        self._allow_squash_merge = allow_squash_merge
        self._allow_auto_merge = allow_auto_merge
        self._delete_branch_on_merge = delete_branch_on_merge
        self._allow_merge_commit = allow_merge_commit
        self._allow_forking = allow_forking
        self._subscribers_count = subscribers_count
        self._network_count = network_count
        self._master_branch = master_branch
        self._starred_at = starred_at
        return
        
    

    
    def _getwatchers(self):
        return self._watchers
        
    watchers = property(_getwatchers)

    def _getopen_issues(self):
        return self._open_issues
        
    open_issues = property(_getopen_issues)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getpushed_at(self):
        return self._pushed_at and datetime.datetime.fromisoformat(self._pushed_at[0:-1])
        
    pushed_at = property(_getpushed_at)

    def _getdisabled(self):
        return self._disabled
        
    disabled = property(_getdisabled, doc="""Returns whether or not this repository disabled. """)

    def _gethas_pages(self):
        return self._has_pages
        
    has_pages = property(_gethas_pages)

    def _getopen_issues_count(self):
        return self._open_issues_count
        
    open_issues_count = property(_getopen_issues_count)

    def _getdefault_branch(self):
        return self._default_branch
        
    default_branch = property(_getdefault_branch, doc="""The default branch of the repository. """)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _getwatchers_count(self):
        return self._watchers_count
        
    watchers_count = property(_getwatchers_count)

    def _getstargazers_count(self):
        return self._stargazers_count
        
    stargazers_count = property(_getstargazers_count)

    def _getforks_count(self):
        return self._forks_count
        
    forks_count = property(_getforks_count)

    def _getlanguage(self):
        return self._language
        
    language = property(_getlanguage)

    def _gethomepage(self):
        return self._homepage
        
    homepage = property(_gethomepage)

    def _getsvn_url(self):
        return self._svn_url
        
    svn_url = property(_getsvn_url)

    def _gethooks_url(self):
        return self._hooks_url
        
    hooks_url = property(_gethooks_url)

    def _getmirror_url(self):
        return self._mirror_url
        
    mirror_url = property(_getmirror_url)

    def _getclone_url(self):
        return self._clone_url
        
    clone_url = property(_getclone_url)

    def _gettrees_url(self):
        return self._trees_url
        
    trees_url = property(_gettrees_url)

    def _getteams_url(self):
        return self._teams_url
        
    teams_url = property(_getteams_url)

    def _gettags_url(self):
        return self._tags_url
        
    tags_url = property(_gettags_url)

    def _getsubscription_url(self):
        return self._subscription_url
        
    subscription_url = property(_getsubscription_url)

    def _getsubscribers_url(self):
        return self._subscribers_url
        
    subscribers_url = property(_getsubscribers_url)

    def _getstatuses_url(self):
        return self._statuses_url
        
    statuses_url = property(_getstatuses_url)

    def _getstargazers_url(self):
        return self._stargazers_url
        
    stargazers_url = property(_getstargazers_url)

    def _getssh_url(self):
        return self._ssh_url
        
    ssh_url = property(_getssh_url)

    def _getreleases_url(self):
        return self._releases_url
        
    releases_url = property(_getreleases_url)

    def _getpulls_url(self):
        return self._pulls_url
        
    pulls_url = property(_getpulls_url)

    def _getnotifications_url(self):
        return self._notifications_url
        
    notifications_url = property(_getnotifications_url)

    def _getmilestones_url(self):
        return self._milestones_url
        
    milestones_url = property(_getmilestones_url)

    def _getmerges_url(self):
        return self._merges_url
        
    merges_url = property(_getmerges_url)

    def _getlanguages_url(self):
        return self._languages_url
        
    languages_url = property(_getlanguages_url)

    def _getlabels_url(self):
        return self._labels_url
        
    labels_url = property(_getlabels_url)

    def _getkeys_url(self):
        return self._keys_url
        
    keys_url = property(_getkeys_url)

    def _getissues_url(self):
        return self._issues_url
        
    issues_url = property(_getissues_url)

    def _getissue_events_url(self):
        return self._issue_events_url
        
    issue_events_url = property(_getissue_events_url)

    def _getissue_comment_url(self):
        return self._issue_comment_url
        
    issue_comment_url = property(_getissue_comment_url)

    def _getgit_url(self):
        return self._git_url
        
    git_url = property(_getgit_url)

    def _getgit_tags_url(self):
        return self._git_tags_url
        
    git_tags_url = property(_getgit_tags_url)

    def _getgit_refs_url(self):
        return self._git_refs_url
        
    git_refs_url = property(_getgit_refs_url)

    def _getgit_commits_url(self):
        return self._git_commits_url
        
    git_commits_url = property(_getgit_commits_url)

    def _getforks_url(self):
        return self._forks_url
        
    forks_url = property(_getforks_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getdownloads_url(self):
        return self._downloads_url
        
    downloads_url = property(_getdownloads_url)

    def _getdeployments_url(self):
        return self._deployments_url
        
    deployments_url = property(_getdeployments_url)

    def _getcontributors_url(self):
        return self._contributors_url
        
    contributors_url = property(_getcontributors_url)

    def _getcontents_url(self):
        return self._contents_url
        
    contents_url = property(_getcontents_url)

    def _getcompare_url(self):
        return self._compare_url
        
    compare_url = property(_getcompare_url)

    def _getcommits_url(self):
        return self._commits_url
        
    commits_url = property(_getcommits_url)

    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _getcollaborators_url(self):
        return self._collaborators_url
        
    collaborators_url = property(_getcollaborators_url)

    def _getbranches_url(self):
        return self._branches_url
        
    branches_url = property(_getbranches_url)

    def _getblobs_url(self):
        return self._blobs_url
        
    blobs_url = property(_getblobs_url)

    def _getassignees_url(self):
        return self._assignees_url
        
    assignees_url = property(_getassignees_url)

    def _getarchive_url(self):
        return self._archive_url
        
    archive_url = property(_getarchive_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getfork(self):
        return self._fork
        
    fork = property(_getfork)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getowner(self):
        return self._owner and SimpleUser(**self._owner)
        
    owner = property(_getowner)

    def _getforks(self):
        return self._forks
        
    forks = property(_getforks)

    def _getlicense(self):
        return self._license and NullableLicenseSimple(**self._license)
        
    license = property(_getlicense)

    def _getfull_name(self):
        return self._full_name
        
    full_name = property(_getfull_name)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the repository. """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the repository """)

    def _getorganization(self):
        return self._organization and NullableSimpleUser(**self._organization)
        
    organization = property(_getorganization)

    def _getpermissions(self):
        return self._permissions and Repository_permissions(**self._permissions)
        
    permissions = property(_getpermissions)

    def _getprivate(self):
        return self._private
        
    private = property(_getprivate, doc="""Whether the repository is private or public. """)

    def _getis_template(self):
        return self._is_template
        
    is_template = property(_getis_template, doc="""Whether this repository acts as a template that can be used to generate new repositories. """)

    def _gettopics(self):
        return self._topics and [ entry for entry in self._topics ]
        
    topics = property(_gettopics)

    def _gethas_issues(self):
        return self._has_issues
        
    has_issues = property(_gethas_issues, doc="""Whether issues are enabled. """)

    def _gethas_projects(self):
        return self._has_projects
        
    has_projects = property(_gethas_projects, doc="""Whether projects are enabled. """)

    def _gethas_wiki(self):
        return self._has_wiki
        
    has_wiki = property(_gethas_wiki, doc="""Whether the wiki is enabled. """)

    def _gethas_downloads(self):
        return self._has_downloads
        
    has_downloads = property(_gethas_downloads, doc="""Whether downloads are enabled. """)

    def _getarchived(self):
        return self._archived
        
    archived = property(_getarchived, doc="""Whether the repository is archived. """)

    def _getvisibility(self):
        return self._visibility
        
    visibility = property(_getvisibility, doc="""The repository visibility: public, private, or internal. """)

    def _getallow_rebase_merge(self):
        return self._allow_rebase_merge
        
    allow_rebase_merge = property(_getallow_rebase_merge, doc="""Whether to allow rebase merges for pull requests. """)

    def _gettemplate_repository(self):
        return self._template_repository and Repository_template_repository(**self._template_repository)
        
    template_repository = property(_gettemplate_repository)

    def _gettemp_clone_token(self):
        return self._temp_clone_token
        
    temp_clone_token = property(_gettemp_clone_token)

    def _getallow_squash_merge(self):
        return self._allow_squash_merge
        
    allow_squash_merge = property(_getallow_squash_merge, doc="""Whether to allow squash merges for pull requests. """)

    def _getallow_auto_merge(self):
        return self._allow_auto_merge
        
    allow_auto_merge = property(_getallow_auto_merge, doc="""Whether to allow Auto-merge to be used on pull requests. """)

    def _getdelete_branch_on_merge(self):
        return self._delete_branch_on_merge
        
    delete_branch_on_merge = property(_getdelete_branch_on_merge, doc="""Whether to delete head branches when pull requests are merged """)

    def _getallow_merge_commit(self):
        return self._allow_merge_commit
        
    allow_merge_commit = property(_getallow_merge_commit, doc="""Whether to allow merge commits for pull requests. """)

    def _getallow_forking(self):
        return self._allow_forking
        
    allow_forking = property(_getallow_forking, doc="""Whether to allow forking this repo """)

    def _getsubscribers_count(self):
        return self._subscribers_count
        
    subscribers_count = property(_getsubscribers_count)

    def _getnetwork_count(self):
        return self._network_count
        
    network_count = property(_getnetwork_count)

    def _getmaster_branch(self):
        return self._master_branch
        
    master_branch = property(_getmaster_branch)

    def _getstarred_at(self):
        return self._starred_at
        
    starred_at = property(_getstarred_at)


    
##
##
##
class InstallationToken(ResponseBase):
    """Authentication token for a GitHub App installed on a user or org. """
    def __init__(self, expires_at:str, token:str, permissions:dict=None, repository_selection:str=None, repositories:list=[], single_file:str=None, has_multiple_single_files:bool=None, single_file_paths:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._expires_at = expires_at
        self._token = token
        self._permissions = permissions
        self._repository_selection = repository_selection
        self._repositories = repositories
        self._single_file = single_file
        self._has_multiple_single_files = has_multiple_single_files
        self._single_file_paths = single_file_paths
        return
        
    

    
    def _getexpires_at(self):
        return self._expires_at
        
    expires_at = property(_getexpires_at)

    def _gettoken(self):
        return self._token
        
    token = property(_gettoken)

    def _getpermissions(self):
        return self._permissions and AppPermissions(**self._permissions)
        
    permissions = property(_getpermissions)

    def _getrepository_selection(self):
        return self._repository_selection
        
    repository_selection = property(_getrepository_selection)

    def _getrepositories(self):
        return self._repositories and [ entry and Repository(**entry) for entry in self._repositories ]
        
    repositories = property(_getrepositories)

    def _getsingle_file(self):
        return self._single_file
        
    single_file = property(_getsingle_file)

    def _gethas_multiple_single_files(self):
        return self._has_multiple_single_files
        
    has_multiple_single_files = property(_gethas_multiple_single_files)

    def _getsingle_file_paths(self):
        return self._single_file_paths and [ entry for entry in self._single_file_paths ]
        
    single_file_paths = property(_getsingle_file_paths)


    
##
##
##
class Applicationgrant_app(ResponseBase):
    def __init__(self, url:str, name:str, client_id:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._name = name
        self._client_id = client_id
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getclient_id(self):
        return self._client_id
        
    client_id = property(_getclient_id)


    
##
##
##
class ApplicationGrant(ResponseBase):
    """The authorization associated with an OAuth Access. """
    def __init__(self, scopes:list, updated_at:datetime, created_at:datetime, app:dict, url:str, id:int, user:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._scopes = scopes
        self._updated_at = updated_at
        self._created_at = created_at
        self._app = app
        self._url = url
        self._id = id
        self._user = user
        return
        
    

    
    def _getscopes(self):
        return self._scopes and [ entry for entry in self._scopes ]
        
    scopes = property(_getscopes)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getapp(self):
        return self._app and Applicationgrant_app(**self._app)
        
    app = property(_getapp)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)


    
##
##
##
class Nullableauthorization_app(ResponseBase):
    def __init__(self, url:str, name:str, client_id:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._name = name
        self._client_id = client_id
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getclient_id(self):
        return self._client_id
        
    client_id = property(_getclient_id)


    
##
##
##
class NullableAuthorization(ResponseBase):
    """The authorization for an OAuth app, GitHub App, or a Personal Access Token. """
    def __init__(self, expires_at:datetime, fingerprint:str, created_at:datetime, updated_at:datetime, note_url:str, note:str, app:dict, hashed_token:str, token_last_eight:str, token:str, scopes:list, url:str, id:int, user:dict=None, installation:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._expires_at = expires_at
        self._fingerprint = fingerprint
        self._created_at = created_at
        self._updated_at = updated_at
        self._note_url = note_url
        self._note = note
        self._app = app
        self._hashed_token = hashed_token
        self._token_last_eight = token_last_eight
        self._token = token
        self._scopes = scopes
        self._url = url
        self._id = id
        self._user = user
        self._installation = installation
        return
        
    

    
    def _getexpires_at(self):
        return self._expires_at and datetime.datetime.fromisoformat(self._expires_at[0:-1])
        
    expires_at = property(_getexpires_at)

    def _getfingerprint(self):
        return self._fingerprint
        
    fingerprint = property(_getfingerprint)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getnote_url(self):
        return self._note_url
        
    note_url = property(_getnote_url)

    def _getnote(self):
        return self._note
        
    note = property(_getnote)

    def _getapp(self):
        return self._app and Nullableauthorization_app(**self._app)
        
    app = property(_getapp)

    def _gethashed_token(self):
        return self._hashed_token
        
    hashed_token = property(_gethashed_token)

    def _gettoken_last_eight(self):
        return self._token_last_eight
        
    token_last_eight = property(_gettoken_last_eight)

    def _gettoken(self):
        return self._token
        
    token = property(_gettoken)

    def _getscopes(self):
        return self._scopes and [ entry for entry in self._scopes ]
        
    scopes = property(_getscopes, doc="""A list of scopes that this authorization is in. """)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _getinstallation(self):
        return self._installation and NullableScopedInstallation(**self._installation)
        
    installation = property(_getinstallation)


    
##
##
##
class CodeOfConduct(ResponseBase):
    """Code Of Conduct """
    def __init__(self, html_url:str, url:str, name:str, key:str, body:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._html_url = html_url
        self._url = url
        self._name = name
        self._key = key
        self._body = body
        return
        
    

    
    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getkey(self):
        return self._key
        
    key = property(_getkey)

    def _getbody(self):
        return self._body
        
    body = property(_getbody)


    
##
##
##
class EnterpriseAnnouncement(ResponseBase):
    """Enterprise global announcement """
    def __init__(self, announcement:str, expires_at:datetime=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._announcement = announcement
        self._expires_at = expires_at
        return
        
    

    
    def _getannouncement(self):
        return self._announcement
        
    announcement = property(_getannouncement)

    def _getexpires_at(self):
        return self._expires_at and datetime.datetime.fromisoformat(self._expires_at[0:-1])
        
    expires_at = property(_getexpires_at)


    
##
##
##
class LicenseInfo(ResponseBase):
    def __init__(self, seats=None, seats_used:int=None, seats_available=None, kind:str=None, days_until_expiration:int=None, expire_at:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._seats = seats
        self._seats_used = seats_used
        self._seats_available = seats_available
        self._kind = kind
        self._days_until_expiration = days_until_expiration
        self._expire_at = expire_at
        return
        
    

    
    def _getseats(self):
        return self._seats
        
    seats = property(_getseats)

    def _getseats_used(self):
        return self._seats_used
        
    seats_used = property(_getseats_used)

    def _getseats_available(self):
        return self._seats_available
        
    seats_available = property(_getseats_available)

    def _getkind(self):
        return self._kind
        
    kind = property(_getkind)

    def _getdays_until_expiration(self):
        return self._days_until_expiration
        
    days_until_expiration = property(_getdays_until_expiration)

    def _getexpire_at(self):
        return self._expire_at
        
    expire_at = property(_getexpire_at)


    
##
##
##
class EnterpriseRepositoryOverview(ResponseBase):
    def __init__(self, total_wikis:int, total_pushes:int, org_repos:int, fork_repos:int, root_repos:int, total_repos:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._total_wikis = total_wikis
        self._total_pushes = total_pushes
        self._org_repos = org_repos
        self._fork_repos = fork_repos
        self._root_repos = root_repos
        self._total_repos = total_repos
        return
        
    

    
    def _gettotal_wikis(self):
        return self._total_wikis
        
    total_wikis = property(_gettotal_wikis)

    def _gettotal_pushes(self):
        return self._total_pushes
        
    total_pushes = property(_gettotal_pushes)

    def _getorg_repos(self):
        return self._org_repos
        
    org_repos = property(_getorg_repos)

    def _getfork_repos(self):
        return self._fork_repos
        
    fork_repos = property(_getfork_repos)

    def _getroot_repos(self):
        return self._root_repos
        
    root_repos = property(_getroot_repos)

    def _gettotal_repos(self):
        return self._total_repos
        
    total_repos = property(_gettotal_repos)


    
##
##
##
class EnterpriseHookOverview(ResponseBase):
    def __init__(self, inactive_hooks:int, active_hooks:int, total_hooks:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._inactive_hooks = inactive_hooks
        self._active_hooks = active_hooks
        self._total_hooks = total_hooks
        return
        
    

    
    def _getinactive_hooks(self):
        return self._inactive_hooks
        
    inactive_hooks = property(_getinactive_hooks)

    def _getactive_hooks(self):
        return self._active_hooks
        
    active_hooks = property(_getactive_hooks)

    def _gettotal_hooks(self):
        return self._total_hooks
        
    total_hooks = property(_gettotal_hooks)


    
##
##
##
class EnterprisePageOverview(ResponseBase):
    def __init__(self, total_pages:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._total_pages = total_pages
        return
        
    

    
    def _gettotal_pages(self):
        return self._total_pages
        
    total_pages = property(_gettotal_pages)


    
##
##
##
class EnterpriseOrganizationOverview(ResponseBase):
    def __init__(self, total_team_members:int, total_teams:int, disabled_orgs:int, total_orgs:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._total_team_members = total_team_members
        self._total_teams = total_teams
        self._disabled_orgs = disabled_orgs
        self._total_orgs = total_orgs
        return
        
    

    
    def _gettotal_team_members(self):
        return self._total_team_members
        
    total_team_members = property(_gettotal_team_members)

    def _gettotal_teams(self):
        return self._total_teams
        
    total_teams = property(_gettotal_teams)

    def _getdisabled_orgs(self):
        return self._disabled_orgs
        
    disabled_orgs = property(_getdisabled_orgs)

    def _gettotal_orgs(self):
        return self._total_orgs
        
    total_orgs = property(_gettotal_orgs)


    
##
##
##
class EnterpriseUserOverview(ResponseBase):
    def __init__(self, suspended_users:int, admin_users:int, total_users:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._suspended_users = suspended_users
        self._admin_users = admin_users
        self._total_users = total_users
        return
        
    

    
    def _getsuspended_users(self):
        return self._suspended_users
        
    suspended_users = property(_getsuspended_users)

    def _getadmin_users(self):
        return self._admin_users
        
    admin_users = property(_getadmin_users)

    def _gettotal_users(self):
        return self._total_users
        
    total_users = property(_gettotal_users)


    
##
##
##
class EnterprisePullRequestOverview(ResponseBase):
    def __init__(self, unmergeable_pulls:int, mergeable_pulls:int, merged_pulls:int, total_pulls:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._unmergeable_pulls = unmergeable_pulls
        self._mergeable_pulls = mergeable_pulls
        self._merged_pulls = merged_pulls
        self._total_pulls = total_pulls
        return
        
    

    
    def _getunmergeable_pulls(self):
        return self._unmergeable_pulls
        
    unmergeable_pulls = property(_getunmergeable_pulls)

    def _getmergeable_pulls(self):
        return self._mergeable_pulls
        
    mergeable_pulls = property(_getmergeable_pulls)

    def _getmerged_pulls(self):
        return self._merged_pulls
        
    merged_pulls = property(_getmerged_pulls)

    def _gettotal_pulls(self):
        return self._total_pulls
        
    total_pulls = property(_gettotal_pulls)


    
##
##
##
class EnterpriseIssueOverview(ResponseBase):
    def __init__(self, closed_issues:int, open_issues:int, total_issues:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._closed_issues = closed_issues
        self._open_issues = open_issues
        self._total_issues = total_issues
        return
        
    

    
    def _getclosed_issues(self):
        return self._closed_issues
        
    closed_issues = property(_getclosed_issues)

    def _getopen_issues(self):
        return self._open_issues
        
    open_issues = property(_getopen_issues)

    def _gettotal_issues(self):
        return self._total_issues
        
    total_issues = property(_gettotal_issues)


    
##
##
##
class EnterpriseMilestoneOverview(ResponseBase):
    def __init__(self, closed_milestones:int, open_milestones:int, total_milestones:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._closed_milestones = closed_milestones
        self._open_milestones = open_milestones
        self._total_milestones = total_milestones
        return
        
    

    
    def _getclosed_milestones(self):
        return self._closed_milestones
        
    closed_milestones = property(_getclosed_milestones)

    def _getopen_milestones(self):
        return self._open_milestones
        
    open_milestones = property(_getopen_milestones)

    def _gettotal_milestones(self):
        return self._total_milestones
        
    total_milestones = property(_gettotal_milestones)


    
##
##
##
class EnterpriseGistOverview(ResponseBase):
    def __init__(self, public_gists:int, private_gists:int, total_gists:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._public_gists = public_gists
        self._private_gists = private_gists
        self._total_gists = total_gists
        return
        
    

    
    def _getpublic_gists(self):
        return self._public_gists
        
    public_gists = property(_getpublic_gists)

    def _getprivate_gists(self):
        return self._private_gists
        
    private_gists = property(_getprivate_gists)

    def _gettotal_gists(self):
        return self._total_gists
        
    total_gists = property(_gettotal_gists)


    
##
##
##
class EnterpriseCommentOverview(ResponseBase):
    def __init__(self, total_pull_request_comments:int, total_issue_comments:int, total_gist_comments:int, total_commit_comments:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._total_pull_request_comments = total_pull_request_comments
        self._total_issue_comments = total_issue_comments
        self._total_gist_comments = total_gist_comments
        self._total_commit_comments = total_commit_comments
        return
        
    

    
    def _gettotal_pull_request_comments(self):
        return self._total_pull_request_comments
        
    total_pull_request_comments = property(_gettotal_pull_request_comments)

    def _gettotal_issue_comments(self):
        return self._total_issue_comments
        
    total_issue_comments = property(_gettotal_issue_comments)

    def _gettotal_gist_comments(self):
        return self._total_gist_comments
        
    total_gist_comments = property(_gettotal_gist_comments)

    def _gettotal_commit_comments(self):
        return self._total_commit_comments
        
    total_commit_comments = property(_gettotal_commit_comments)


    
##
##
##
class EnterpriseOverview(ResponseBase):
    def __init__(self, repos:dict=None, hooks:dict=None, pages:dict=None, orgs:dict=None, users:dict=None, pulls:dict=None, issues:dict=None, milestones:dict=None, gists:dict=None, comments:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._repos = repos
        self._hooks = hooks
        self._pages = pages
        self._orgs = orgs
        self._users = users
        self._pulls = pulls
        self._issues = issues
        self._milestones = milestones
        self._gists = gists
        self._comments = comments
        return
        
    

    
    def _getrepos(self):
        return self._repos and EnterpriseRepositoryOverview(**self._repos)
        
    repos = property(_getrepos)

    def _gethooks(self):
        return self._hooks and EnterpriseHookOverview(**self._hooks)
        
    hooks = property(_gethooks)

    def _getpages(self):
        return self._pages and EnterprisePageOverview(**self._pages)
        
    pages = property(_getpages)

    def _getorgs(self):
        return self._orgs and EnterpriseOrganizationOverview(**self._orgs)
        
    orgs = property(_getorgs)

    def _getusers(self):
        return self._users and EnterpriseUserOverview(**self._users)
        
    users = property(_getusers)

    def _getpulls(self):
        return self._pulls and EnterprisePullRequestOverview(**self._pulls)
        
    pulls = property(_getpulls)

    def _getissues(self):
        return self._issues and EnterpriseIssueOverview(**self._issues)
        
    issues = property(_getissues)

    def _getmilestones(self):
        return self._milestones and EnterpriseMilestoneOverview(**self._milestones)
        
    milestones = property(_getmilestones)

    def _getgists(self):
        return self._gists and EnterpriseGistOverview(**self._gists)
        
    gists = property(_getgists)

    def _getcomments(self):
        return self._comments and EnterpriseCommentOverview(**self._comments)
        
    comments = property(_getcomments)


    
##
##
##
class ActionsEnterprisePermissions(ResponseBase):
    def __init__(self, enabled_organizations:str, selected_organizations_url:str=None, allowed_actions:str=None, selected_actions_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled_organizations = enabled_organizations
        self._selected_organizations_url = selected_organizations_url
        self._allowed_actions = allowed_actions
        self._selected_actions_url = selected_actions_url
        return
        
    

    
    def _getenabled_organizations(self):
        return self._enabled_organizations
        
    enabled_organizations = property(_getenabled_organizations)

    def _getselected_organizations_url(self):
        return self._selected_organizations_url
        
    selected_organizations_url = property(_getselected_organizations_url, doc="""The API URL to use to get or set the selected organizations that are allowed to run GitHub Actions, when `enabled_organizations` is set to `selected`. """)

    def _getallowed_actions(self):
        return self._allowed_actions
        
    allowed_actions = property(_getallowed_actions)

    def _getselected_actions_url(self):
        return self._selected_actions_url
        
    selected_actions_url = property(_getselected_actions_url)


    
##
##
##
class SelectedActions(ResponseBase):
    def __init__(self, patterns_allowed:list, github_owned_allowed:bool, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._patterns_allowed = patterns_allowed
        self._github_owned_allowed = github_owned_allowed
        return
        
    

    
    def _getpatterns_allowed(self):
        return self._patterns_allowed and [ entry for entry in self._patterns_allowed ]
        
    patterns_allowed = property(_getpatterns_allowed, doc="""Specifies a list of string-matching patterns to allow specific action(s). Wildcards, tags, and SHAs are allowed. For example, `monalisa/octocat@*`, `monalisa/octocat@v2`, `monalisa/*`." """)

    def _getgithub_owned_allowed(self):
        return self._github_owned_allowed
        
    github_owned_allowed = property(_getgithub_owned_allowed, doc="""Whether GitHub-owned actions are allowed. For example, this includes the actions in the `actions` organization. """)


    
##
##
##
class RunnerGroupsEnterprise(ResponseBase):
    def __init__(self, allows_public_repositories:bool, runners_url:str, default:bool, visibility:str, name:str, id:int, selected_organizations_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._allows_public_repositories = allows_public_repositories
        self._runners_url = runners_url
        self._default = default
        self._visibility = visibility
        self._name = name
        self._id = id
        self._selected_organizations_url = selected_organizations_url
        return
        
    

    
    def _getallows_public_repositories(self):
        return self._allows_public_repositories
        
    allows_public_repositories = property(_getallows_public_repositories)

    def _getrunners_url(self):
        return self._runners_url
        
    runners_url = property(_getrunners_url)

    def _getdefault(self):
        return self._default
        
    default = property(_getdefault)

    def _getvisibility(self):
        return self._visibility
        
    visibility = property(_getvisibility)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getselected_organizations_url(self):
        return self._selected_organizations_url
        
    selected_organizations_url = property(_getselected_organizations_url)


    
##
##
##
class SelfHostedRunnerLabel(ResponseBase):
    """A label for a self hosted runner """
    def __init__(self, name:str, id:int=None, type:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._name = name
        self._id = id
        self._type = type
        return
        
    

    
    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""Name of the label. """)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the label. """)

    def _gettype(self):
        return self._type
        
    type = property(_gettype, doc="""The type of label. Read-only labels are applied automatically when the runner is configured. """)


    
##
##
##
class SelfHostedRunners(ResponseBase):
    """A self hosted runner """
    def __init__(self, labels:list, busy:bool, status:str, os:str, name:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._labels = labels
        self._busy = busy
        self._status = status
        self._os = os
        self._name = name
        self._id = id
        return
        
    

    
    def _getlabels(self):
        return self._labels and [ entry and SelfHostedRunnerLabel(**entry) for entry in self._labels ]
        
    labels = property(_getlabels)

    def _getbusy(self):
        return self._busy
        
    busy = property(_getbusy)

    def _getstatus(self):
        return self._status
        
    status = property(_getstatus, doc="""The status of the runner. """)

    def _getos(self):
        return self._os
        
    os = property(_getos, doc="""The Operating System of the runner. """)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the runner. """)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""The id of the runner. """)


    
##
##
##
class RunnerApplication(ResponseBase):
    """Runner Application """
    def __init__(self, filename:str, download_url:str, architecture:str, os:str, temp_download_token:str=None, sha256_checksum:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._filename = filename
        self._download_url = download_url
        self._architecture = architecture
        self._os = os
        self._temp_download_token = temp_download_token
        self._sha256_checksum = sha256_checksum
        return
        
    

    
    def _getfilename(self):
        return self._filename
        
    filename = property(_getfilename)

    def _getdownload_url(self):
        return self._download_url
        
    download_url = property(_getdownload_url)

    def _getarchitecture(self):
        return self._architecture
        
    architecture = property(_getarchitecture)

    def _getos(self):
        return self._os
        
    os = property(_getos)

    def _gettemp_download_token(self):
        return self._temp_download_token
        
    temp_download_token = property(_gettemp_download_token, doc="""A short lived bearer token used to download the runner, if needed. """)

    def _getsha256_checksum(self):
        return self._sha256_checksum
        
    sha256_checksum = property(_getsha256_checksum)


    
##
##
##
class AuthenticationToken(ResponseBase):
    """Authentication Token """
    def __init__(self, expires_at:datetime, token:str, permissions:object=None, repositories:list=[], single_file:str=None, repository_selection:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._expires_at = expires_at
        self._token = token
        self._permissions = permissions
        self._repositories = repositories
        self._single_file = single_file
        self._repository_selection = repository_selection
        return
        
    

    
    def _getexpires_at(self):
        return self._expires_at and datetime.datetime.fromisoformat(self._expires_at[0:-1])
        
    expires_at = property(_getexpires_at, doc="""The time this token expires """)

    def _gettoken(self):
        return self._token
        
    token = property(_gettoken, doc="""The token used for authentication """)

    def _getpermissions(self):
        return self._permissions
        
    permissions = property(_getpermissions)

    def _getrepositories(self):
        return self._repositories and [ entry and Repository(**entry) for entry in self._repositories ]
        
    repositories = property(_getrepositories, doc="""The repositories this token has access to """)

    def _getsingle_file(self):
        return self._single_file
        
    single_file = property(_getsingle_file)

    def _getrepository_selection(self):
        return self._repository_selection
        
    repository_selection = property(_getrepository_selection, doc="""Describe whether all repositories have been selected or there's a selection involved """)


    
##
##
##
class Auditlogevent_actor_location(ResponseBase):
    def __init__(self, country_name:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._country_name = country_name
        return
        
    

    
    def _getcountry_name(self):
        return self._country_name
        
    country_name = property(_getcountry_name)


    
##
##
##
class AuditLogEvent(ResponseBase):
    def __init__(self, timestamp:int=None, action:str=None, active:bool=None, active_was:bool=None, actor:str=None, actor_id:int=None, actor_location:dict=None, data:object=None, org_id:int=None, blocked_user:str=None, business:str=None, config:list=[], config_was:list=[], content_type:str=None, created_at:int=None, deploy_key_fingerprint:str=None, _document_id:str=None, emoji:str=None, events:list=[], events_were:list=[], explanation:str=None, fingerprint:str=None, hook_id:int=None, limited_availability:bool=None, message:str=None, name:str=None, old_user:str=None, openssh_public_key:str=None, org:str=None, previous_visibility:str=None, read_only:bool=None, repo:str=None, repository:str=None, repository_public:bool=None, target_login:str=None, team:str=None, transport_protocol:int=None, transport_protocol_name:str=None, user:str=None, visibility:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._timestamp = timestamp
        self._action = action
        self._active = active
        self._active_was = active_was
        self._actor = actor
        self._actor_id = actor_id
        self._actor_location = actor_location
        self._data = data
        self._org_id = org_id
        self._blocked_user = blocked_user
        self._business = business
        self._config = config
        self._config_was = config_was
        self._content_type = content_type
        self._created_at = created_at
        self._deploy_key_fingerprint = deploy_key_fingerprint
        self.__document_id = _document_id
        self._emoji = emoji
        self._events = events
        self._events_were = events_were
        self._explanation = explanation
        self._fingerprint = fingerprint
        self._hook_id = hook_id
        self._limited_availability = limited_availability
        self._message = message
        self._name = name
        self._old_user = old_user
        self._openssh_public_key = openssh_public_key
        self._org = org
        self._previous_visibility = previous_visibility
        self._read_only = read_only
        self._repo = repo
        self._repository = repository
        self._repository_public = repository_public
        self._target_login = target_login
        self._team = team
        self._transport_protocol = transport_protocol
        self._transport_protocol_name = transport_protocol_name
        self._user = user
        self._visibility = visibility
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['timestamp'] = entry.pop('@timestamp')
        return entry
    

    
    def _gettimestamp(self):
        return self._timestamp
        
    timestamp = property(_gettimestamp, doc="""The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). """)

    def _getaction(self):
        return self._action
        
    action = property(_getaction, doc="""The name of the action that was performed, for example `user.login` or `repo.create`. """)

    def _getactive(self):
        return self._active
        
    active = property(_getactive)

    def _getactive_was(self):
        return self._active_was
        
    active_was = property(_getactive_was)

    def _getactor(self):
        return self._actor
        
    actor = property(_getactor, doc="""The actor who performed the action. """)

    def _getactor_id(self):
        return self._actor_id
        
    actor_id = property(_getactor_id, doc="""The id of the actor who performed the action. """)

    def _getactor_location(self):
        return self._actor_location and Auditlogevent_actor_location(**self._actor_location)
        
    actor_location = property(_getactor_location)

    def _getdata(self):
        return self._data
        
    data = property(_getdata)

    def _getorg_id(self):
        return self._org_id
        
    org_id = property(_getorg_id)

    def _getblocked_user(self):
        return self._blocked_user
        
    blocked_user = property(_getblocked_user, doc="""The username of the account being blocked. """)

    def _getbusiness(self):
        return self._business
        
    business = property(_getbusiness)

    def _getconfig(self):
        return self._config and [ entry for entry in self._config ]
        
    config = property(_getconfig)

    def _getconfig_was(self):
        return self._config_was and [ entry for entry in self._config_was ]
        
    config_was = property(_getconfig_was)

    def _getcontent_type(self):
        return self._content_type
        
    content_type = property(_getcontent_type)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at, doc="""The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). """)

    def _getdeploy_key_fingerprint(self):
        return self._deploy_key_fingerprint
        
    deploy_key_fingerprint = property(_getdeploy_key_fingerprint)

    def _get_document_id(self):
        return self.__document_id
        
    _document_id = property(_get_document_id, doc="""A unique identifier for an audit event. """)

    def _getemoji(self):
        return self._emoji
        
    emoji = property(_getemoji)

    def _getevents(self):
        return self._events and [ entry for entry in self._events ]
        
    events = property(_getevents)

    def _getevents_were(self):
        return self._events_were and [ entry for entry in self._events_were ]
        
    events_were = property(_getevents_were)

    def _getexplanation(self):
        return self._explanation
        
    explanation = property(_getexplanation)

    def _getfingerprint(self):
        return self._fingerprint
        
    fingerprint = property(_getfingerprint)

    def _gethook_id(self):
        return self._hook_id
        
    hook_id = property(_gethook_id)

    def _getlimited_availability(self):
        return self._limited_availability
        
    limited_availability = property(_getlimited_availability)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getold_user(self):
        return self._old_user
        
    old_user = property(_getold_user)

    def _getopenssh_public_key(self):
        return self._openssh_public_key
        
    openssh_public_key = property(_getopenssh_public_key)

    def _getorg(self):
        return self._org
        
    org = property(_getorg)

    def _getprevious_visibility(self):
        return self._previous_visibility
        
    previous_visibility = property(_getprevious_visibility)

    def _getread_only(self):
        return self._read_only
        
    read_only = property(_getread_only)

    def _getrepo(self):
        return self._repo
        
    repo = property(_getrepo, doc="""The name of the repository. """)

    def _getrepository(self):
        return self._repository
        
    repository = property(_getrepository, doc="""The name of the repository. """)

    def _getrepository_public(self):
        return self._repository_public
        
    repository_public = property(_getrepository_public)

    def _gettarget_login(self):
        return self._target_login
        
    target_login = property(_gettarget_login)

    def _getteam(self):
        return self._team
        
    team = property(_getteam)

    def _gettransport_protocol(self):
        return self._transport_protocol
        
    transport_protocol = property(_gettransport_protocol, doc="""The type of protocol (for example, HTTP or SSH) used to transfer Git data. """)

    def _gettransport_protocol_name(self):
        return self._transport_protocol_name
        
    transport_protocol_name = property(_gettransport_protocol_name, doc="""A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. """)

    def _getuser(self):
        return self._user
        
    user = property(_getuser, doc="""The user that was affected by the action performed (if available). """)

    def _getvisibility(self):
        return self._visibility
        
    visibility = property(_getvisibility, doc="""The repository visibility, for example `public` or `private`. """)


    
    ##
    ##
    def _gettimestamp(self):
        return self._timestamp
        
    timestamp = property(_gettimestamp, doc="""The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). """)

##
##
##
class Actor(ResponseBase):
    """Actor """
    def __init__(self, avatar_url:str, url:str, gravatar_id:str, login:str, id:int, display_login:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._avatar_url = avatar_url
        self._url = url
        self._gravatar_id = gravatar_id
        self._login = login
        self._id = id
        self._display_login = display_login
        return
        
    

    
    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getgravatar_id(self):
        return self._gravatar_id
        
    gravatar_id = property(_getgravatar_id)

    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getdisplay_login(self):
        return self._display_login
        
    display_login = property(_getdisplay_login)


    
##
##
##
class NullableMilestone(ResponseBase):
    """A collection of related issues and pull requests. """
    def __init__(self, due_on:datetime, closed_at:datetime, updated_at:datetime, created_at:datetime, closed_issues:int, open_issues:int, creator:dict, description:str, title:str, number:int, node_id:str, id:int, labels_url:str, html_url:str, url:str, state:str='open', **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._due_on = due_on
        self._closed_at = closed_at
        self._updated_at = updated_at
        self._created_at = created_at
        self._closed_issues = closed_issues
        self._open_issues = open_issues
        self._creator = creator
        self._description = description
        self._title = title
        self._number = number
        self._node_id = node_id
        self._id = id
        self._labels_url = labels_url
        self._html_url = html_url
        self._url = url
        self._state = state
        return
        
    

    
    def _getdue_on(self):
        return self._due_on and datetime.datetime.fromisoformat(self._due_on[0:-1])
        
    due_on = property(_getdue_on)

    def _getclosed_at(self):
        return self._closed_at and datetime.datetime.fromisoformat(self._closed_at[0:-1])
        
    closed_at = property(_getclosed_at)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getclosed_issues(self):
        return self._closed_issues
        
    closed_issues = property(_getclosed_issues)

    def _getopen_issues(self):
        return self._open_issues
        
    open_issues = property(_getopen_issues)

    def _getcreator(self):
        return self._creator and NullableSimpleUser(**self._creator)
        
    creator = property(_getcreator)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle, doc="""The title of the milestone. """)

    def _getnumber(self):
        return self._number
        
    number = property(_getnumber, doc="""The number of the milestone. """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getlabels_url(self):
        return self._labels_url
        
    labels_url = property(_getlabels_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getstate(self):
        return self._state
        
    state = property(_getstate, doc="""The state of the milestone. """)


    
##
##
##
class Nullableintegration_permissions(ResponseBase):
    """The set of permissions for the GitHub app """
    def __init__(self, issues:str=None, checks:str=None, metadata:str=None, contents:str=None, deployments:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._issues = issues
        self._checks = checks
        self._metadata = metadata
        self._contents = contents
        self._deployments = deployments
        return
        
    

    
    def _getissues(self):
        return self._issues
        
    issues = property(_getissues)

    def _getchecks(self):
        return self._checks
        
    checks = property(_getchecks)

    def _getmetadata(self):
        return self._metadata
        
    metadata = property(_getmetadata)

    def _getcontents(self):
        return self._contents
        
    contents = property(_getcontents)

    def _getdeployments(self):
        return self._deployments
        
    deployments = property(_getdeployments)


    
##
##
##
class NullableIntegration(ResponseBase):
    """GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. """
    def __init__(self, events:list, permissions:dict, updated_at:datetime, created_at:datetime, html_url:str, external_url:str, description:str, name:str, owner:dict, node_id:str, id:int, slug:str=None, installations_count:int=None, client_id:str=None, client_secret:str=None, webhook_secret:str=None, pem:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._events = events
        self._permissions = permissions
        self._updated_at = updated_at
        self._created_at = created_at
        self._html_url = html_url
        self._external_url = external_url
        self._description = description
        self._name = name
        self._owner = owner
        self._node_id = node_id
        self._id = id
        self._slug = slug
        self._installations_count = installations_count
        self._client_id = client_id
        self._client_secret = client_secret
        self._webhook_secret = webhook_secret
        self._pem = pem
        return
        
    

    
    def _getevents(self):
        return self._events and [ entry for entry in self._events ]
        
    events = property(_getevents, doc="""The list of events for the GitHub app """)

    def _getpermissions(self):
        return self._permissions and Nullableintegration_permissions(**self._permissions)
        
    permissions = property(_getpermissions, doc="""The set of permissions for the GitHub app """)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getexternal_url(self):
        return self._external_url
        
    external_url = property(_getexternal_url)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the GitHub app """)

    def _getowner(self):
        return self._owner and NullableSimpleUser(**self._owner)
        
    owner = property(_getowner)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the GitHub app """)

    def _getslug(self):
        return self._slug
        
    slug = property(_getslug, doc="""The slug name of the GitHub app """)

    def _getinstallations_count(self):
        return self._installations_count
        
    installations_count = property(_getinstallations_count, doc="""The number of installations associated with the GitHub app """)

    def _getclient_id(self):
        return self._client_id
        
    client_id = property(_getclient_id)

    def _getclient_secret(self):
        return self._client_secret
        
    client_secret = property(_getclient_secret)

    def _getwebhook_secret(self):
        return self._webhook_secret
        
    webhook_secret = property(_getwebhook_secret)

    def _getpem(self):
        return self._pem
        
    pem = property(_getpem)


    
##
##
##
class ReactionRollup(ResponseBase):
    def __init__(self, rocket:int, eyes:int, hooray:int, heart:int, confused:int, laugh:int, minusone:int, plusone:int, total_count:int, url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._rocket = rocket
        self._eyes = eyes
        self._hooray = hooray
        self._heart = heart
        self._confused = confused
        self._laugh = laugh
        self._minusone = minusone
        self._plusone = plusone
        self._total_count = total_count
        self._url = url
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['minusone'] = entry.pop('-1')
        entry['plusone'] = entry.pop('+1')
        return entry
    

    
    def _getrocket(self):
        return self._rocket
        
    rocket = property(_getrocket)

    def _geteyes(self):
        return self._eyes
        
    eyes = property(_geteyes)

    def _gethooray(self):
        return self._hooray
        
    hooray = property(_gethooray)

    def _getheart(self):
        return self._heart
        
    heart = property(_getheart)

    def _getconfused(self):
        return self._confused
        
    confused = property(_getconfused)

    def _getlaugh(self):
        return self._laugh
        
    laugh = property(_getlaugh)

    def _getminusone(self):
        return self._minusone
        
    minusone = property(_getminusone)

    def _getplusone(self):
        return self._plusone
        
    plusone = property(_getplusone)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
    ##
    ##
    def _getminusone(self):
        return self._minusone
        
    minusone = property(_getminusone)

    ##
    ##
    def _getplusone(self):
        return self._plusone
        
    plusone = property(_getplusone)

##
##
##
class Issue_labels(ResponseBase):
    def __init__(self, id:int=None, node_id:str=None, url:str=None, name:str=None, description:str=None, color:str=None, default:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._node_id = node_id
        self._url = url
        self._name = name
        self._description = description
        self._color = color
        self._default = default
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getcolor(self):
        return self._color
        
    color = property(_getcolor)

    def _getdefault(self):
        return self._default
        
    default = property(_getdefault)


    
##
##
##
class Issue_pull_request(ResponseBase):
    def __init__(self, url:str, patch_url:str, html_url:str, diff_url:str, merged_at:datetime=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._patch_url = patch_url
        self._html_url = html_url
        self._diff_url = diff_url
        self._merged_at = merged_at
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getpatch_url(self):
        return self._patch_url
        
    patch_url = property(_getpatch_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getdiff_url(self):
        return self._diff_url
        
    diff_url = property(_getdiff_url)

    def _getmerged_at(self):
        return self._merged_at and datetime.datetime.fromisoformat(self._merged_at[0:-1])
        
    merged_at = property(_getmerged_at)


    
##
##
##
class Issue(ResponseBase):
    """Issues are a great way to keep track of tasks, enhancements, and bugs for your projects. """
    def __init__(self, author_association:str, updated_at:datetime, created_at:datetime, closed_at:datetime, comments:int, locked:bool, milestone:dict, assignee:dict, labels:list, user:dict, title:str, state:str, number:int, html_url:str, events_url:str, comments_url:str, labels_url:str, repository_url:str, url:str, node_id:str, id:int, body:str=None, assignees:list=[], active_lock_reason:str=None, pull_request:dict=None, draft:bool=None, closed_by:dict=None, body_html:str=None, body_text:str=None, timeline_url:str=None, repository:dict=None, performed_via_github_app:dict=None, reactions:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._author_association = author_association
        self._updated_at = updated_at
        self._created_at = created_at
        self._closed_at = closed_at
        self._comments = comments
        self._locked = locked
        self._milestone = milestone
        self._assignee = assignee
        self._labels = labels
        self._user = user
        self._title = title
        self._state = state
        self._number = number
        self._html_url = html_url
        self._events_url = events_url
        self._comments_url = comments_url
        self._labels_url = labels_url
        self._repository_url = repository_url
        self._url = url
        self._node_id = node_id
        self._id = id
        self._body = body
        self._assignees = assignees
        self._active_lock_reason = active_lock_reason
        self._pull_request = pull_request
        self._draft = draft
        self._closed_by = closed_by
        self._body_html = body_html
        self._body_text = body_text
        self._timeline_url = timeline_url
        self._repository = repository
        self._performed_via_github_app = performed_via_github_app
        self._reactions = reactions
        return
        
    

    
    def _getauthor_association(self):
        return self._author_association
        
    author_association = property(_getauthor_association)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getclosed_at(self):
        return self._closed_at and datetime.datetime.fromisoformat(self._closed_at[0:-1])
        
    closed_at = property(_getclosed_at)

    def _getcomments(self):
        return self._comments
        
    comments = property(_getcomments)

    def _getlocked(self):
        return self._locked
        
    locked = property(_getlocked)

    def _getmilestone(self):
        return self._milestone and NullableMilestone(**self._milestone)
        
    milestone = property(_getmilestone)

    def _getassignee(self):
        return self._assignee and NullableSimpleUser(**self._assignee)
        
    assignee = property(_getassignee)

    def _getlabels(self):
        return self._labels and [ entry for entry in self._labels ]
        
    labels = property(_getlabels, doc="""Labels to associate with this issue; pass one or more label names to replace the set of labels on this issue; send an empty array to clear all labels from the issue; note that the labels are silently dropped for users without push access to the repository """)

    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle, doc="""Title of the issue """)

    def _getstate(self):
        return self._state
        
    state = property(_getstate, doc="""State of the issue; either 'open' or 'closed' """)

    def _getnumber(self):
        return self._number
        
    number = property(_getnumber, doc="""Number uniquely identifying the issue within its repository """)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _getlabels_url(self):
        return self._labels_url
        
    labels_url = property(_getlabels_url)

    def _getrepository_url(self):
        return self._repository_url
        
    repository_url = property(_getrepository_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl, doc="""URL for the issue """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getbody(self):
        return self._body
        
    body = property(_getbody, doc="""Contents of the issue """)

    def _getassignees(self):
        return self._assignees and [ entry and SimpleUser(**entry) for entry in self._assignees ]
        
    assignees = property(_getassignees)

    def _getactive_lock_reason(self):
        return self._active_lock_reason
        
    active_lock_reason = property(_getactive_lock_reason)

    def _getpull_request(self):
        return self._pull_request and Issue_pull_request(**self._pull_request)
        
    pull_request = property(_getpull_request)

    def _getdraft(self):
        return self._draft
        
    draft = property(_getdraft)

    def _getclosed_by(self):
        return self._closed_by and NullableSimpleUser(**self._closed_by)
        
    closed_by = property(_getclosed_by)

    def _getbody_html(self):
        return self._body_html
        
    body_html = property(_getbody_html)

    def _getbody_text(self):
        return self._body_text
        
    body_text = property(_getbody_text)

    def _gettimeline_url(self):
        return self._timeline_url
        
    timeline_url = property(_gettimeline_url)

    def _getrepository(self):
        return self._repository and Repository(**self._repository)
        
    repository = property(_getrepository)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getreactions(self):
        return self._reactions and ReactionRollup(**ReactionRollup.patchEntry(self._reactions))
        
    reactions = property(_getreactions)


    
##
##
##
class IssueComment(ResponseBase):
    """Comments provide a way for people to collaborate on an issue. """
    def __init__(self, author_association:str, issue_url:str, updated_at:datetime, created_at:datetime, user:dict, html_url:str, url:str, node_id:str, id:int, body:str=None, body_text:str=None, body_html:str=None, performed_via_github_app:dict=None, reactions:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._author_association = author_association
        self._issue_url = issue_url
        self._updated_at = updated_at
        self._created_at = created_at
        self._user = user
        self._html_url = html_url
        self._url = url
        self._node_id = node_id
        self._id = id
        self._body = body
        self._body_text = body_text
        self._body_html = body_html
        self._performed_via_github_app = performed_via_github_app
        self._reactions = reactions
        return
        
    

    
    def _getauthor_association(self):
        return self._author_association
        
    author_association = property(_getauthor_association)

    def _getissue_url(self):
        return self._issue_url
        
    issue_url = property(_getissue_url)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl, doc="""URL for the issue comment """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the issue comment """)

    def _getbody(self):
        return self._body
        
    body = property(_getbody, doc="""Contents of the issue comment """)

    def _getbody_text(self):
        return self._body_text
        
    body_text = property(_getbody_text)

    def _getbody_html(self):
        return self._body_html
        
    body_html = property(_getbody_html)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getreactions(self):
        return self._reactions and ReactionRollup(**ReactionRollup.patchEntry(self._reactions))
        
    reactions = property(_getreactions)


    
##
##
##
class Event_repo(ResponseBase):
    def __init__(self, url:str, name:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._name = name
        self._id = id
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class Event_payload_pages(ResponseBase):
    def __init__(self, page_name:str=None, title:str=None, summary:str=None, action:str=None, sha:str=None, html_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._page_name = page_name
        self._title = title
        self._summary = summary
        self._action = action
        self._sha = sha
        self._html_url = html_url
        return
        
    

    
    def _getpage_name(self):
        return self._page_name
        
    page_name = property(_getpage_name)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle)

    def _getsummary(self):
        return self._summary
        
    summary = property(_getsummary)

    def _getaction(self):
        return self._action
        
    action = property(_getaction)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)


    
##
##
##
class Event_payload(ResponseBase):
    def __init__(self, action:str=None, issue:dict=None, comment:dict=None, pages:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._action = action
        self._issue = issue
        self._comment = comment
        self._pages = pages
        return
        
    

    
    def _getaction(self):
        return self._action
        
    action = property(_getaction)

    def _getissue(self):
        return self._issue and Issue(**self._issue)
        
    issue = property(_getissue)

    def _getcomment(self):
        return self._comment and IssueComment(**self._comment)
        
    comment = property(_getcomment)

    def _getpages(self):
        return self._pages and [ entry and Event_payload_pages(**entry) for entry in self._pages ]
        
    pages = property(_getpages)


    
##
##
##
class Event(ResponseBase):
    """Event """
    def __init__(self, created_at:datetime, public:bool, payload:dict, repo:dict, actor:dict, type:str, id:str, org:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._created_at = created_at
        self._public = public
        self._payload = payload
        self._repo = repo
        self._actor = actor
        self._type = type
        self._id = id
        self._org = org
        return
        
    

    
    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getpublic(self):
        return self._public
        
    public = property(_getpublic)

    def _getpayload(self):
        return self._payload and Event_payload(**self._payload)
        
    payload = property(_getpayload)

    def _getrepo(self):
        return self._repo and Event_repo(**self._repo)
        
    repo = property(_getrepo)

    def _getactor(self):
        return self._actor and Actor(**self._actor)
        
    actor = property(_getactor)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getorg(self):
        return self._org and Actor(**self._org)
        
    org = property(_getorg)


    
##
##
##
class LinkWithType(ResponseBase):
    """Hypermedia Link with Type """
    def __init__(self, type:str, href:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._type = type
        self._href = href
        return
        
    

    
    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _gethref(self):
        return self._href
        
    href = property(_gethref)


    
##
##
##
class Feed__links(ResponseBase):
    def __init__(self, user:dict, timeline:dict, security_advisories:dict=None, current_user:dict=None, current_user_public:dict=None, current_user_actor:dict=None, current_user_organization:dict=None, current_user_organizations:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._user = user
        self._timeline = timeline
        self._security_advisories = security_advisories
        self._current_user = current_user
        self._current_user_public = current_user_public
        self._current_user_actor = current_user_actor
        self._current_user_organization = current_user_organization
        self._current_user_organizations = current_user_organizations
        return
        
    

    
    def _getuser(self):
        return self._user and LinkWithType(**self._user)
        
    user = property(_getuser)

    def _gettimeline(self):
        return self._timeline and LinkWithType(**self._timeline)
        
    timeline = property(_gettimeline)

    def _getsecurity_advisories(self):
        return self._security_advisories and LinkWithType(**self._security_advisories)
        
    security_advisories = property(_getsecurity_advisories)

    def _getcurrent_user(self):
        return self._current_user and LinkWithType(**self._current_user)
        
    current_user = property(_getcurrent_user)

    def _getcurrent_user_public(self):
        return self._current_user_public and LinkWithType(**self._current_user_public)
        
    current_user_public = property(_getcurrent_user_public)

    def _getcurrent_user_actor(self):
        return self._current_user_actor and LinkWithType(**self._current_user_actor)
        
    current_user_actor = property(_getcurrent_user_actor)

    def _getcurrent_user_organization(self):
        return self._current_user_organization and LinkWithType(**self._current_user_organization)
        
    current_user_organization = property(_getcurrent_user_organization)

    def _getcurrent_user_organizations(self):
        return self._current_user_organizations and [ entry and LinkWithType(**entry) for entry in self._current_user_organizations ]
        
    current_user_organizations = property(_getcurrent_user_organizations)


    
##
##
##
class Feed(ResponseBase):
    """Feed """
    def __init__(self, _links:dict, user_url:str, timeline_url:str, current_user_public_url:str=None, current_user_url:str=None, current_user_actor_url:str=None, current_user_organization_url:str=None, current_user_organization_urls:list=[], security_advisories_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self.__links = _links
        self._user_url = user_url
        self._timeline_url = timeline_url
        self._current_user_public_url = current_user_public_url
        self._current_user_url = current_user_url
        self._current_user_actor_url = current_user_actor_url
        self._current_user_organization_url = current_user_organization_url
        self._current_user_organization_urls = current_user_organization_urls
        self._security_advisories_url = security_advisories_url
        return
        
    

    
    def _get_links(self):
        return self.__links and Feed__links(**self.__links)
        
    _links = property(_get_links)

    def _getuser_url(self):
        return self._user_url
        
    user_url = property(_getuser_url)

    def _gettimeline_url(self):
        return self._timeline_url
        
    timeline_url = property(_gettimeline_url)

    def _getcurrent_user_public_url(self):
        return self._current_user_public_url
        
    current_user_public_url = property(_getcurrent_user_public_url)

    def _getcurrent_user_url(self):
        return self._current_user_url
        
    current_user_url = property(_getcurrent_user_url)

    def _getcurrent_user_actor_url(self):
        return self._current_user_actor_url
        
    current_user_actor_url = property(_getcurrent_user_actor_url)

    def _getcurrent_user_organization_url(self):
        return self._current_user_organization_url
        
    current_user_organization_url = property(_getcurrent_user_organization_url)

    def _getcurrent_user_organization_urls(self):
        return self._current_user_organization_urls and [ entry for entry in self._current_user_organization_urls ]
        
    current_user_organization_urls = property(_getcurrent_user_organization_urls)

    def _getsecurity_advisories_url(self):
        return self._security_advisories_url
        
    security_advisories_url = property(_getsecurity_advisories_url)


    
##
##
##
class BaseGist(ResponseBase):
    """Base Gist """
    def __init__(self, comments_url:str, user:dict, comments:int, description:str, updated_at:datetime, created_at:datetime, public:bool, files:object, html_url:str, git_push_url:str, git_pull_url:str, node_id:str, id:str, commits_url:str, forks_url:str, url:str, owner:dict=None, truncated:bool=None, forks:list=[], history:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._comments_url = comments_url
        self._user = user
        self._comments = comments
        self._description = description
        self._updated_at = updated_at
        self._created_at = created_at
        self._public = public
        self._files = files
        self._html_url = html_url
        self._git_push_url = git_push_url
        self._git_pull_url = git_pull_url
        self._node_id = node_id
        self._id = id
        self._commits_url = commits_url
        self._forks_url = forks_url
        self._url = url
        self._owner = owner
        self._truncated = truncated
        self._forks = forks
        self._history = history
        return
        
    

    
    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _getcomments(self):
        return self._comments
        
    comments = property(_getcomments)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getpublic(self):
        return self._public
        
    public = property(_getpublic)

    def _getfiles(self):
        return self._files
        
    files = property(_getfiles)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getgit_push_url(self):
        return self._git_push_url
        
    git_push_url = property(_getgit_push_url)

    def _getgit_pull_url(self):
        return self._git_pull_url
        
    git_pull_url = property(_getgit_pull_url)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getcommits_url(self):
        return self._commits_url
        
    commits_url = property(_getcommits_url)

    def _getforks_url(self):
        return self._forks_url
        
    forks_url = property(_getforks_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getowner(self):
        return self._owner and SimpleUser(**self._owner)
        
    owner = property(_getowner)

    def _gettruncated(self):
        return self._truncated
        
    truncated = property(_gettruncated)

    def _getforks(self):
        return self._forks and [ entry for entry in self._forks ]
        
    forks = property(_getforks)

    def _gethistory(self):
        return self._history and [ entry for entry in self._history ]
        
    history = property(_gethistory)


    
##
##
##
class Publicuser_plan(ResponseBase):
    def __init__(self, private_repos:int, space:int, name:str, collaborators:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._private_repos = private_repos
        self._space = space
        self._name = name
        self._collaborators = collaborators
        return
        
    

    
    def _getprivate_repos(self):
        return self._private_repos
        
    private_repos = property(_getprivate_repos)

    def _getspace(self):
        return self._space
        
    space = property(_getspace)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getcollaborators(self):
        return self._collaborators
        
    collaborators = property(_getcollaborators)


    
##
##
##
class PublicUser(ResponseBase):
    """Public User """
    def __init__(self, updated_at:datetime, created_at:datetime, following:int, followers:int, public_gists:int, public_repos:int, bio:str, hireable:bool, email:str, location:str, blog:str, company:str, name:str, site_admin:bool, type:str, received_events_url:str, events_url:str, repos_url:str, organizations_url:str, subscriptions_url:str, starred_url:str, gists_url:str, following_url:str, followers_url:str, html_url:str, url:str, gravatar_id:str, avatar_url:str, node_id:str, id:int, login:str, twitter_username:str=None, plan:dict=None, suspended_at:datetime=None, private_gists:int=None, total_private_repos:int=None, owned_private_repos:int=None, disk_usage:int=None, collaborators:int=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._updated_at = updated_at
        self._created_at = created_at
        self._following = following
        self._followers = followers
        self._public_gists = public_gists
        self._public_repos = public_repos
        self._bio = bio
        self._hireable = hireable
        self._email = email
        self._location = location
        self._blog = blog
        self._company = company
        self._name = name
        self._site_admin = site_admin
        self._type = type
        self._received_events_url = received_events_url
        self._events_url = events_url
        self._repos_url = repos_url
        self._organizations_url = organizations_url
        self._subscriptions_url = subscriptions_url
        self._starred_url = starred_url
        self._gists_url = gists_url
        self._following_url = following_url
        self._followers_url = followers_url
        self._html_url = html_url
        self._url = url
        self._gravatar_id = gravatar_id
        self._avatar_url = avatar_url
        self._node_id = node_id
        self._id = id
        self._login = login
        self._twitter_username = twitter_username
        self._plan = plan
        self._suspended_at = suspended_at
        self._private_gists = private_gists
        self._total_private_repos = total_private_repos
        self._owned_private_repos = owned_private_repos
        self._disk_usage = disk_usage
        self._collaborators = collaborators
        return
        
    

    
    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getfollowing(self):
        return self._following
        
    following = property(_getfollowing)

    def _getfollowers(self):
        return self._followers
        
    followers = property(_getfollowers)

    def _getpublic_gists(self):
        return self._public_gists
        
    public_gists = property(_getpublic_gists)

    def _getpublic_repos(self):
        return self._public_repos
        
    public_repos = property(_getpublic_repos)

    def _getbio(self):
        return self._bio
        
    bio = property(_getbio)

    def _gethireable(self):
        return self._hireable
        
    hireable = property(_gethireable)

    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _getlocation(self):
        return self._location
        
    location = property(_getlocation)

    def _getblog(self):
        return self._blog
        
    blog = property(_getblog)

    def _getcompany(self):
        return self._company
        
    company = property(_getcompany)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getsite_admin(self):
        return self._site_admin
        
    site_admin = property(_getsite_admin)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getreceived_events_url(self):
        return self._received_events_url
        
    received_events_url = property(_getreceived_events_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getrepos_url(self):
        return self._repos_url
        
    repos_url = property(_getrepos_url)

    def _getorganizations_url(self):
        return self._organizations_url
        
    organizations_url = property(_getorganizations_url)

    def _getsubscriptions_url(self):
        return self._subscriptions_url
        
    subscriptions_url = property(_getsubscriptions_url)

    def _getstarred_url(self):
        return self._starred_url
        
    starred_url = property(_getstarred_url)

    def _getgists_url(self):
        return self._gists_url
        
    gists_url = property(_getgists_url)

    def _getfollowing_url(self):
        return self._following_url
        
    following_url = property(_getfollowing_url)

    def _getfollowers_url(self):
        return self._followers_url
        
    followers_url = property(_getfollowers_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getgravatar_id(self):
        return self._gravatar_id
        
    gravatar_id = property(_getgravatar_id)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)

    def _gettwitter_username(self):
        return self._twitter_username
        
    twitter_username = property(_gettwitter_username)

    def _getplan(self):
        return self._plan and Publicuser_plan(**self._plan)
        
    plan = property(_getplan)

    def _getsuspended_at(self):
        return self._suspended_at and datetime.datetime.fromisoformat(self._suspended_at[0:-1])
        
    suspended_at = property(_getsuspended_at)

    def _getprivate_gists(self):
        return self._private_gists
        
    private_gists = property(_getprivate_gists)

    def _gettotal_private_repos(self):
        return self._total_private_repos
        
    total_private_repos = property(_gettotal_private_repos)

    def _getowned_private_repos(self):
        return self._owned_private_repos
        
    owned_private_repos = property(_getowned_private_repos)

    def _getdisk_usage(self):
        return self._disk_usage
        
    disk_usage = property(_getdisk_usage)

    def _getcollaborators(self):
        return self._collaborators
        
    collaborators = property(_getcollaborators)


    
##
##
##
class Gisthistory_change_status(ResponseBase):
    def __init__(self, total:int=None, additions:int=None, deletions:int=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._total = total
        self._additions = additions
        self._deletions = deletions
        return
        
    

    
    def _gettotal(self):
        return self._total
        
    total = property(_gettotal)

    def _getadditions(self):
        return self._additions
        
    additions = property(_getadditions)

    def _getdeletions(self):
        return self._deletions
        
    deletions = property(_getdeletions)


    
##
##
##
class GistHistory(ResponseBase):
    """Gist History """
    def __init__(self, user:dict=None, version:str=None, committed_at:datetime=None, change_status:dict=None, url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._user = user
        self._version = version
        self._committed_at = committed_at
        self._change_status = change_status
        self._url = url
        return
        
    

    
    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _getversion(self):
        return self._version
        
    version = property(_getversion)

    def _getcommitted_at(self):
        return self._committed_at and datetime.datetime.fromisoformat(self._committed_at[0:-1])
        
    committed_at = property(_getcommitted_at)

    def _getchange_status(self):
        return self._change_status and Gisthistory_change_status(**self._change_status)
        
    change_status = property(_getchange_status)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class Gistsimple_fork_of(ResponseBase):
    """Gist """
    def __init__(self, comments_url:str, user:dict, comments:int, description:str, updated_at:datetime, created_at:datetime, public:bool, files:object, html_url:str, git_push_url:str, git_pull_url:str, node_id:str, id:str, commits_url:str, forks_url:str, url:str, owner:dict=None, truncated:bool=None, forks:list=[], history:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._comments_url = comments_url
        self._user = user
        self._comments = comments
        self._description = description
        self._updated_at = updated_at
        self._created_at = created_at
        self._public = public
        self._files = files
        self._html_url = html_url
        self._git_push_url = git_push_url
        self._git_pull_url = git_pull_url
        self._node_id = node_id
        self._id = id
        self._commits_url = commits_url
        self._forks_url = forks_url
        self._url = url
        self._owner = owner
        self._truncated = truncated
        self._forks = forks
        self._history = history
        return
        
    

    
    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _getcomments(self):
        return self._comments
        
    comments = property(_getcomments)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getpublic(self):
        return self._public
        
    public = property(_getpublic)

    def _getfiles(self):
        return self._files
        
    files = property(_getfiles)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getgit_push_url(self):
        return self._git_push_url
        
    git_push_url = property(_getgit_push_url)

    def _getgit_pull_url(self):
        return self._git_pull_url
        
    git_pull_url = property(_getgit_pull_url)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getcommits_url(self):
        return self._commits_url
        
    commits_url = property(_getcommits_url)

    def _getforks_url(self):
        return self._forks_url
        
    forks_url = property(_getforks_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getowner(self):
        return self._owner and NullableSimpleUser(**self._owner)
        
    owner = property(_getowner)

    def _gettruncated(self):
        return self._truncated
        
    truncated = property(_gettruncated)

    def _getforks(self):
        return self._forks and [ entry for entry in self._forks ]
        
    forks = property(_getforks)

    def _gethistory(self):
        return self._history and [ entry for entry in self._history ]
        
    history = property(_gethistory)


    
##
##
##
class GistSimple(ResponseBase):
    """Gist Simple """
    def __init__(self, forks=None, history=None, fork_of:dict=None, url:str=None, forks_url:str=None, commits_url:str=None, id:str=None, node_id:str=None, git_pull_url:str=None, git_push_url:str=None, html_url:str=None, files:object=None, public:bool=None, created_at:str=None, updated_at:str=None, description:str=None, comments:int=None, user:str=None, comments_url:str=None, owner:dict=None, truncated:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._forks = forks
        self._history = history
        self._fork_of = fork_of
        self._url = url
        self._forks_url = forks_url
        self._commits_url = commits_url
        self._id = id
        self._node_id = node_id
        self._git_pull_url = git_pull_url
        self._git_push_url = git_push_url
        self._html_url = html_url
        self._files = files
        self._public = public
        self._created_at = created_at
        self._updated_at = updated_at
        self._description = description
        self._comments = comments
        self._user = user
        self._comments_url = comments_url
        self._owner = owner
        self._truncated = truncated
        return
        
    

    
    def _getforks(self):
        return self._forks # deprecated
        
    forks = property(_getforks)

    def _gethistory(self):
        return self._history # deprecated
        
    history = property(_gethistory)

    def _getfork_of(self):
        return self._fork_of and Gistsimple_fork_of(**self._fork_of)
        
    fork_of = property(_getfork_of, doc="""Gist """)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getforks_url(self):
        return self._forks_url
        
    forks_url = property(_getforks_url)

    def _getcommits_url(self):
        return self._commits_url
        
    commits_url = property(_getcommits_url)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getgit_pull_url(self):
        return self._git_pull_url
        
    git_pull_url = property(_getgit_pull_url)

    def _getgit_push_url(self):
        return self._git_push_url
        
    git_push_url = property(_getgit_push_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getfiles(self):
        return self._files
        
    files = property(_getfiles)

    def _getpublic(self):
        return self._public
        
    public = property(_getpublic)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getupdated_at(self):
        return self._updated_at
        
    updated_at = property(_getupdated_at)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getcomments(self):
        return self._comments
        
    comments = property(_getcomments)

    def _getuser(self):
        return self._user
        
    user = property(_getuser)

    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _getowner(self):
        return self._owner and SimpleUser(**self._owner)
        
    owner = property(_getowner)

    def _gettruncated(self):
        return self._truncated
        
    truncated = property(_gettruncated)


    
##
##
##
class GistComment(ResponseBase):
    """A comment made to a gist. """
    def __init__(self, author_association:str, updated_at:datetime, created_at:datetime, user:dict, body:str, url:str, node_id:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._author_association = author_association
        self._updated_at = updated_at
        self._created_at = created_at
        self._user = user
        self._body = body
        self._url = url
        self._node_id = node_id
        self._id = id
        return
        
    

    
    def _getauthor_association(self):
        return self._author_association
        
    author_association = property(_getauthor_association)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _getbody(self):
        return self._body
        
    body = property(_getbody, doc="""The comment text. """)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class Gistcommit_change_status(ResponseBase):
    def __init__(self, total:int=None, additions:int=None, deletions:int=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._total = total
        self._additions = additions
        self._deletions = deletions
        return
        
    

    
    def _gettotal(self):
        return self._total
        
    total = property(_gettotal)

    def _getadditions(self):
        return self._additions
        
    additions = property(_getadditions)

    def _getdeletions(self):
        return self._deletions
        
    deletions = property(_getdeletions)


    
##
##
##
class GistCommit(ResponseBase):
    """Gist Commit """
    def __init__(self, committed_at:datetime, change_status:dict, user:dict, version:str, url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._committed_at = committed_at
        self._change_status = change_status
        self._user = user
        self._version = version
        self._url = url
        return
        
    

    
    def _getcommitted_at(self):
        return self._committed_at and datetime.datetime.fromisoformat(self._committed_at[0:-1])
        
    committed_at = property(_getcommitted_at)

    def _getchange_status(self):
        return self._change_status and Gistcommit_change_status(**self._change_status)
        
    change_status = property(_getchange_status)

    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _getversion(self):
        return self._version
        
    version = property(_getversion)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class GitignoreTemplate(ResponseBase):
    """Gitignore Template """
    def __init__(self, source:str, name:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._source = source
        self._name = name
        return
        
    

    
    def _getsource(self):
        return self._source
        
    source = property(_getsource)

    def _getname(self):
        return self._name
        
    name = property(_getname)


    
##
##
##
class LicenseSimple(ResponseBase):
    """License Simple """
    def __init__(self, node_id:str, spdx_id:str, url:str, name:str, key:str, html_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._node_id = node_id
        self._spdx_id = spdx_id
        self._url = url
        self._name = name
        self._key = key
        self._html_url = html_url
        return
        
    

    
    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getspdx_id(self):
        return self._spdx_id
        
    spdx_id = property(_getspdx_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getkey(self):
        return self._key
        
    key = property(_getkey)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)


    
##
##
##
class License(ResponseBase):
    """License """
    def __init__(self, featured:bool, body:str, limitations:list, conditions:list, permissions:list, implementation:str, description:str, html_url:str, node_id:str, url:str, spdx_id:str, name:str, key:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._featured = featured
        self._body = body
        self._limitations = limitations
        self._conditions = conditions
        self._permissions = permissions
        self._implementation = implementation
        self._description = description
        self._html_url = html_url
        self._node_id = node_id
        self._url = url
        self._spdx_id = spdx_id
        self._name = name
        self._key = key
        return
        
    

    
    def _getfeatured(self):
        return self._featured
        
    featured = property(_getfeatured)

    def _getbody(self):
        return self._body
        
    body = property(_getbody)

    def _getlimitations(self):
        return self._limitations and [ entry for entry in self._limitations ]
        
    limitations = property(_getlimitations)

    def _getconditions(self):
        return self._conditions and [ entry for entry in self._conditions ]
        
    conditions = property(_getconditions)

    def _getpermissions(self):
        return self._permissions and [ entry for entry in self._permissions ]
        
    permissions = property(_getpermissions)

    def _getimplementation(self):
        return self._implementation
        
    implementation = property(_getimplementation)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getspdx_id(self):
        return self._spdx_id
        
    spdx_id = property(_getspdx_id)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getkey(self):
        return self._key
        
    key = property(_getkey)


    
##
##
##
class ApiOverview(ResponseBase):
    """Api Overview """
    def __init__(self, verifiable_password_authentication:bool, packages:list=[], dependabot:list=[], installed_version:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._verifiable_password_authentication = verifiable_password_authentication
        self._packages = packages
        self._dependabot = dependabot
        self._installed_version = installed_version
        return
        
    

    
    def _getverifiable_password_authentication(self):
        return self._verifiable_password_authentication
        
    verifiable_password_authentication = property(_getverifiable_password_authentication)

    def _getpackages(self):
        return self._packages and [ entry for entry in self._packages ]
        
    packages = property(_getpackages)

    def _getdependabot(self):
        return self._dependabot and [ entry for entry in self._dependabot ]
        
    dependabot = property(_getdependabot)

    def _getinstalled_version(self):
        return self._installed_version
        
    installed_version = property(_getinstalled_version)


    
##
##
##
class Nullablerepository_permissions(ResponseBase):
    def __init__(self, push:bool, pull:bool, admin:bool, triage:bool=None, maintain:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._push = push
        self._pull = pull
        self._admin = admin
        self._triage = triage
        self._maintain = maintain
        return
        
    

    
    def _getpush(self):
        return self._push
        
    push = property(_getpush)

    def _getpull(self):
        return self._pull
        
    pull = property(_getpull)

    def _getadmin(self):
        return self._admin
        
    admin = property(_getadmin)

    def _gettriage(self):
        return self._triage
        
    triage = property(_gettriage)

    def _getmaintain(self):
        return self._maintain
        
    maintain = property(_getmaintain)


    
##
##
##
class Nullablerepository_template_repository_owner(ResponseBase):
    def __init__(self, login:str=None, id:int=None, node_id:str=None, avatar_url:str=None, gravatar_id:str=None, url:str=None, html_url:str=None, followers_url:str=None, following_url:str=None, gists_url:str=None, starred_url:str=None, subscriptions_url:str=None, organizations_url:str=None, repos_url:str=None, events_url:str=None, received_events_url:str=None, type:str=None, site_admin:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._login = login
        self._id = id
        self._node_id = node_id
        self._avatar_url = avatar_url
        self._gravatar_id = gravatar_id
        self._url = url
        self._html_url = html_url
        self._followers_url = followers_url
        self._following_url = following_url
        self._gists_url = gists_url
        self._starred_url = starred_url
        self._subscriptions_url = subscriptions_url
        self._organizations_url = organizations_url
        self._repos_url = repos_url
        self._events_url = events_url
        self._received_events_url = received_events_url
        self._type = type
        self._site_admin = site_admin
        return
        
    

    
    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)

    def _getgravatar_id(self):
        return self._gravatar_id
        
    gravatar_id = property(_getgravatar_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getfollowers_url(self):
        return self._followers_url
        
    followers_url = property(_getfollowers_url)

    def _getfollowing_url(self):
        return self._following_url
        
    following_url = property(_getfollowing_url)

    def _getgists_url(self):
        return self._gists_url
        
    gists_url = property(_getgists_url)

    def _getstarred_url(self):
        return self._starred_url
        
    starred_url = property(_getstarred_url)

    def _getsubscriptions_url(self):
        return self._subscriptions_url
        
    subscriptions_url = property(_getsubscriptions_url)

    def _getorganizations_url(self):
        return self._organizations_url
        
    organizations_url = property(_getorganizations_url)

    def _getrepos_url(self):
        return self._repos_url
        
    repos_url = property(_getrepos_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getreceived_events_url(self):
        return self._received_events_url
        
    received_events_url = property(_getreceived_events_url)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getsite_admin(self):
        return self._site_admin
        
    site_admin = property(_getsite_admin)


    
##
##
##
class Nullablerepository_template_repository_permissions(ResponseBase):
    def __init__(self, admin:bool=None, maintain:bool=None, push:bool=None, triage:bool=None, pull:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._admin = admin
        self._maintain = maintain
        self._push = push
        self._triage = triage
        self._pull = pull
        return
        
    

    
    def _getadmin(self):
        return self._admin
        
    admin = property(_getadmin)

    def _getmaintain(self):
        return self._maintain
        
    maintain = property(_getmaintain)

    def _getpush(self):
        return self._push
        
    push = property(_getpush)

    def _gettriage(self):
        return self._triage
        
    triage = property(_gettriage)

    def _getpull(self):
        return self._pull
        
    pull = property(_getpull)


    
##
##
##
class Nullablerepository_template_repository(ResponseBase):
    def __init__(self, id:int=None, node_id:str=None, name:str=None, full_name:str=None, owner:dict=None, private:bool=None, html_url:str=None, description:str=None, fork:bool=None, url:str=None, archive_url:str=None, assignees_url:str=None, blobs_url:str=None, branches_url:str=None, collaborators_url:str=None, comments_url:str=None, commits_url:str=None, compare_url:str=None, contents_url:str=None, contributors_url:str=None, deployments_url:str=None, downloads_url:str=None, events_url:str=None, forks_url:str=None, git_commits_url:str=None, git_refs_url:str=None, git_tags_url:str=None, git_url:str=None, issue_comment_url:str=None, issue_events_url:str=None, issues_url:str=None, keys_url:str=None, labels_url:str=None, languages_url:str=None, merges_url:str=None, milestones_url:str=None, notifications_url:str=None, pulls_url:str=None, releases_url:str=None, ssh_url:str=None, stargazers_url:str=None, statuses_url:str=None, subscribers_url:str=None, subscription_url:str=None, tags_url:str=None, teams_url:str=None, trees_url:str=None, clone_url:str=None, mirror_url:str=None, hooks_url:str=None, svn_url:str=None, homepage:str=None, language:str=None, forks_count:int=None, stargazers_count:int=None, watchers_count:int=None, size:int=None, default_branch:str=None, open_issues_count:int=None, is_template:bool=None, topics:list=[], has_issues:bool=None, has_projects:bool=None, has_wiki:bool=None, has_pages:bool=None, has_downloads:bool=None, archived:bool=None, disabled:bool=None, visibility:str=None, pushed_at:str=None, created_at:str=None, updated_at:str=None, permissions:dict=None, allow_rebase_merge:bool=None, temp_clone_token:str=None, allow_squash_merge:bool=None, allow_auto_merge:bool=None, delete_branch_on_merge:bool=None, allow_update_branch:bool=None, allow_merge_commit:bool=None, subscribers_count:int=None, network_count:int=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._node_id = node_id
        self._name = name
        self._full_name = full_name
        self._owner = owner
        self._private = private
        self._html_url = html_url
        self._description = description
        self._fork = fork
        self._url = url
        self._archive_url = archive_url
        self._assignees_url = assignees_url
        self._blobs_url = blobs_url
        self._branches_url = branches_url
        self._collaborators_url = collaborators_url
        self._comments_url = comments_url
        self._commits_url = commits_url
        self._compare_url = compare_url
        self._contents_url = contents_url
        self._contributors_url = contributors_url
        self._deployments_url = deployments_url
        self._downloads_url = downloads_url
        self._events_url = events_url
        self._forks_url = forks_url
        self._git_commits_url = git_commits_url
        self._git_refs_url = git_refs_url
        self._git_tags_url = git_tags_url
        self._git_url = git_url
        self._issue_comment_url = issue_comment_url
        self._issue_events_url = issue_events_url
        self._issues_url = issues_url
        self._keys_url = keys_url
        self._labels_url = labels_url
        self._languages_url = languages_url
        self._merges_url = merges_url
        self._milestones_url = milestones_url
        self._notifications_url = notifications_url
        self._pulls_url = pulls_url
        self._releases_url = releases_url
        self._ssh_url = ssh_url
        self._stargazers_url = stargazers_url
        self._statuses_url = statuses_url
        self._subscribers_url = subscribers_url
        self._subscription_url = subscription_url
        self._tags_url = tags_url
        self._teams_url = teams_url
        self._trees_url = trees_url
        self._clone_url = clone_url
        self._mirror_url = mirror_url
        self._hooks_url = hooks_url
        self._svn_url = svn_url
        self._homepage = homepage
        self._language = language
        self._forks_count = forks_count
        self._stargazers_count = stargazers_count
        self._watchers_count = watchers_count
        self._size = size
        self._default_branch = default_branch
        self._open_issues_count = open_issues_count
        self._is_template = is_template
        self._topics = topics
        self._has_issues = has_issues
        self._has_projects = has_projects
        self._has_wiki = has_wiki
        self._has_pages = has_pages
        self._has_downloads = has_downloads
        self._archived = archived
        self._disabled = disabled
        self._visibility = visibility
        self._pushed_at = pushed_at
        self._created_at = created_at
        self._updated_at = updated_at
        self._permissions = permissions
        self._allow_rebase_merge = allow_rebase_merge
        self._temp_clone_token = temp_clone_token
        self._allow_squash_merge = allow_squash_merge
        self._allow_auto_merge = allow_auto_merge
        self._delete_branch_on_merge = delete_branch_on_merge
        self._allow_update_branch = allow_update_branch
        self._allow_merge_commit = allow_merge_commit
        self._subscribers_count = subscribers_count
        self._network_count = network_count
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getfull_name(self):
        return self._full_name
        
    full_name = property(_getfull_name)

    def _getowner(self):
        return self._owner and Nullablerepository_template_repository_owner(**self._owner)
        
    owner = property(_getowner)

    def _getprivate(self):
        return self._private
        
    private = property(_getprivate)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getfork(self):
        return self._fork
        
    fork = property(_getfork)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getarchive_url(self):
        return self._archive_url
        
    archive_url = property(_getarchive_url)

    def _getassignees_url(self):
        return self._assignees_url
        
    assignees_url = property(_getassignees_url)

    def _getblobs_url(self):
        return self._blobs_url
        
    blobs_url = property(_getblobs_url)

    def _getbranches_url(self):
        return self._branches_url
        
    branches_url = property(_getbranches_url)

    def _getcollaborators_url(self):
        return self._collaborators_url
        
    collaborators_url = property(_getcollaborators_url)

    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _getcommits_url(self):
        return self._commits_url
        
    commits_url = property(_getcommits_url)

    def _getcompare_url(self):
        return self._compare_url
        
    compare_url = property(_getcompare_url)

    def _getcontents_url(self):
        return self._contents_url
        
    contents_url = property(_getcontents_url)

    def _getcontributors_url(self):
        return self._contributors_url
        
    contributors_url = property(_getcontributors_url)

    def _getdeployments_url(self):
        return self._deployments_url
        
    deployments_url = property(_getdeployments_url)

    def _getdownloads_url(self):
        return self._downloads_url
        
    downloads_url = property(_getdownloads_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getforks_url(self):
        return self._forks_url
        
    forks_url = property(_getforks_url)

    def _getgit_commits_url(self):
        return self._git_commits_url
        
    git_commits_url = property(_getgit_commits_url)

    def _getgit_refs_url(self):
        return self._git_refs_url
        
    git_refs_url = property(_getgit_refs_url)

    def _getgit_tags_url(self):
        return self._git_tags_url
        
    git_tags_url = property(_getgit_tags_url)

    def _getgit_url(self):
        return self._git_url
        
    git_url = property(_getgit_url)

    def _getissue_comment_url(self):
        return self._issue_comment_url
        
    issue_comment_url = property(_getissue_comment_url)

    def _getissue_events_url(self):
        return self._issue_events_url
        
    issue_events_url = property(_getissue_events_url)

    def _getissues_url(self):
        return self._issues_url
        
    issues_url = property(_getissues_url)

    def _getkeys_url(self):
        return self._keys_url
        
    keys_url = property(_getkeys_url)

    def _getlabels_url(self):
        return self._labels_url
        
    labels_url = property(_getlabels_url)

    def _getlanguages_url(self):
        return self._languages_url
        
    languages_url = property(_getlanguages_url)

    def _getmerges_url(self):
        return self._merges_url
        
    merges_url = property(_getmerges_url)

    def _getmilestones_url(self):
        return self._milestones_url
        
    milestones_url = property(_getmilestones_url)

    def _getnotifications_url(self):
        return self._notifications_url
        
    notifications_url = property(_getnotifications_url)

    def _getpulls_url(self):
        return self._pulls_url
        
    pulls_url = property(_getpulls_url)

    def _getreleases_url(self):
        return self._releases_url
        
    releases_url = property(_getreleases_url)

    def _getssh_url(self):
        return self._ssh_url
        
    ssh_url = property(_getssh_url)

    def _getstargazers_url(self):
        return self._stargazers_url
        
    stargazers_url = property(_getstargazers_url)

    def _getstatuses_url(self):
        return self._statuses_url
        
    statuses_url = property(_getstatuses_url)

    def _getsubscribers_url(self):
        return self._subscribers_url
        
    subscribers_url = property(_getsubscribers_url)

    def _getsubscription_url(self):
        return self._subscription_url
        
    subscription_url = property(_getsubscription_url)

    def _gettags_url(self):
        return self._tags_url
        
    tags_url = property(_gettags_url)

    def _getteams_url(self):
        return self._teams_url
        
    teams_url = property(_getteams_url)

    def _gettrees_url(self):
        return self._trees_url
        
    trees_url = property(_gettrees_url)

    def _getclone_url(self):
        return self._clone_url
        
    clone_url = property(_getclone_url)

    def _getmirror_url(self):
        return self._mirror_url
        
    mirror_url = property(_getmirror_url)

    def _gethooks_url(self):
        return self._hooks_url
        
    hooks_url = property(_gethooks_url)

    def _getsvn_url(self):
        return self._svn_url
        
    svn_url = property(_getsvn_url)

    def _gethomepage(self):
        return self._homepage
        
    homepage = property(_gethomepage)

    def _getlanguage(self):
        return self._language
        
    language = property(_getlanguage)

    def _getforks_count(self):
        return self._forks_count
        
    forks_count = property(_getforks_count)

    def _getstargazers_count(self):
        return self._stargazers_count
        
    stargazers_count = property(_getstargazers_count)

    def _getwatchers_count(self):
        return self._watchers_count
        
    watchers_count = property(_getwatchers_count)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _getdefault_branch(self):
        return self._default_branch
        
    default_branch = property(_getdefault_branch)

    def _getopen_issues_count(self):
        return self._open_issues_count
        
    open_issues_count = property(_getopen_issues_count)

    def _getis_template(self):
        return self._is_template
        
    is_template = property(_getis_template)

    def _gettopics(self):
        return self._topics and [ entry for entry in self._topics ]
        
    topics = property(_gettopics)

    def _gethas_issues(self):
        return self._has_issues
        
    has_issues = property(_gethas_issues)

    def _gethas_projects(self):
        return self._has_projects
        
    has_projects = property(_gethas_projects)

    def _gethas_wiki(self):
        return self._has_wiki
        
    has_wiki = property(_gethas_wiki)

    def _gethas_pages(self):
        return self._has_pages
        
    has_pages = property(_gethas_pages)

    def _gethas_downloads(self):
        return self._has_downloads
        
    has_downloads = property(_gethas_downloads)

    def _getarchived(self):
        return self._archived
        
    archived = property(_getarchived)

    def _getdisabled(self):
        return self._disabled
        
    disabled = property(_getdisabled)

    def _getvisibility(self):
        return self._visibility
        
    visibility = property(_getvisibility)

    def _getpushed_at(self):
        return self._pushed_at
        
    pushed_at = property(_getpushed_at)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getupdated_at(self):
        return self._updated_at
        
    updated_at = property(_getupdated_at)

    def _getpermissions(self):
        return self._permissions and Nullablerepository_template_repository_permissions(**self._permissions)
        
    permissions = property(_getpermissions)

    def _getallow_rebase_merge(self):
        return self._allow_rebase_merge
        
    allow_rebase_merge = property(_getallow_rebase_merge)

    def _gettemp_clone_token(self):
        return self._temp_clone_token
        
    temp_clone_token = property(_gettemp_clone_token)

    def _getallow_squash_merge(self):
        return self._allow_squash_merge
        
    allow_squash_merge = property(_getallow_squash_merge)

    def _getallow_auto_merge(self):
        return self._allow_auto_merge
        
    allow_auto_merge = property(_getallow_auto_merge)

    def _getdelete_branch_on_merge(self):
        return self._delete_branch_on_merge
        
    delete_branch_on_merge = property(_getdelete_branch_on_merge)

    def _getallow_update_branch(self):
        return self._allow_update_branch
        
    allow_update_branch = property(_getallow_update_branch)

    def _getallow_merge_commit(self):
        return self._allow_merge_commit
        
    allow_merge_commit = property(_getallow_merge_commit)

    def _getsubscribers_count(self):
        return self._subscribers_count
        
    subscribers_count = property(_getsubscribers_count)

    def _getnetwork_count(self):
        return self._network_count
        
    network_count = property(_getnetwork_count)


    
##
##
##
class NullableRepository(ResponseBase):
    """A git repository """
    def __init__(self, watchers:int, open_issues:int, updated_at:datetime, created_at:datetime, pushed_at:datetime, disabled:bool, has_pages:bool, open_issues_count:int, default_branch:str, size:int, watchers_count:int, stargazers_count:int, forks_count:int, language:str, homepage:str, svn_url:str, hooks_url:str, mirror_url:str, clone_url:str, trees_url:str, teams_url:str, tags_url:str, subscription_url:str, subscribers_url:str, statuses_url:str, stargazers_url:str, ssh_url:str, releases_url:str, pulls_url:str, notifications_url:str, milestones_url:str, merges_url:str, languages_url:str, labels_url:str, keys_url:str, issues_url:str, issue_events_url:str, issue_comment_url:str, git_url:str, git_tags_url:str, git_refs_url:str, git_commits_url:str, forks_url:str, events_url:str, downloads_url:str, deployments_url:str, contributors_url:str, contents_url:str, compare_url:str, commits_url:str, comments_url:str, collaborators_url:str, branches_url:str, blobs_url:str, assignees_url:str, archive_url:str, url:str, fork:bool, description:str, html_url:str, owner:dict, forks:int, license:dict, full_name:str, name:str, node_id:str, id:int, organization:dict=None, permissions:dict=None, private:bool=False, is_template:bool=False, topics:list=[], has_issues:bool=True, has_projects:bool=True, has_wiki:bool=True, has_downloads:bool=True, archived:bool=False, visibility:str='public', allow_rebase_merge:bool=True, template_repository:dict=None, temp_clone_token:str=None, allow_squash_merge:bool=True, allow_auto_merge:bool=False, delete_branch_on_merge:bool=False, allow_merge_commit:bool=True, allow_forking:bool=None, subscribers_count:int=None, network_count:int=None, master_branch:str=None, starred_at:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._watchers = watchers
        self._open_issues = open_issues
        self._updated_at = updated_at
        self._created_at = created_at
        self._pushed_at = pushed_at
        self._disabled = disabled
        self._has_pages = has_pages
        self._open_issues_count = open_issues_count
        self._default_branch = default_branch
        self._size = size
        self._watchers_count = watchers_count
        self._stargazers_count = stargazers_count
        self._forks_count = forks_count
        self._language = language
        self._homepage = homepage
        self._svn_url = svn_url
        self._hooks_url = hooks_url
        self._mirror_url = mirror_url
        self._clone_url = clone_url
        self._trees_url = trees_url
        self._teams_url = teams_url
        self._tags_url = tags_url
        self._subscription_url = subscription_url
        self._subscribers_url = subscribers_url
        self._statuses_url = statuses_url
        self._stargazers_url = stargazers_url
        self._ssh_url = ssh_url
        self._releases_url = releases_url
        self._pulls_url = pulls_url
        self._notifications_url = notifications_url
        self._milestones_url = milestones_url
        self._merges_url = merges_url
        self._languages_url = languages_url
        self._labels_url = labels_url
        self._keys_url = keys_url
        self._issues_url = issues_url
        self._issue_events_url = issue_events_url
        self._issue_comment_url = issue_comment_url
        self._git_url = git_url
        self._git_tags_url = git_tags_url
        self._git_refs_url = git_refs_url
        self._git_commits_url = git_commits_url
        self._forks_url = forks_url
        self._events_url = events_url
        self._downloads_url = downloads_url
        self._deployments_url = deployments_url
        self._contributors_url = contributors_url
        self._contents_url = contents_url
        self._compare_url = compare_url
        self._commits_url = commits_url
        self._comments_url = comments_url
        self._collaborators_url = collaborators_url
        self._branches_url = branches_url
        self._blobs_url = blobs_url
        self._assignees_url = assignees_url
        self._archive_url = archive_url
        self._url = url
        self._fork = fork
        self._description = description
        self._html_url = html_url
        self._owner = owner
        self._forks = forks
        self._license = license
        self._full_name = full_name
        self._name = name
        self._node_id = node_id
        self._id = id
        self._organization = organization
        self._permissions = permissions
        self._private = private
        self._is_template = is_template
        self._topics = topics
        self._has_issues = has_issues
        self._has_projects = has_projects
        self._has_wiki = has_wiki
        self._has_downloads = has_downloads
        self._archived = archived
        self._visibility = visibility
        self._allow_rebase_merge = allow_rebase_merge
        self._template_repository = template_repository
        self._temp_clone_token = temp_clone_token
        self._allow_squash_merge = allow_squash_merge
        self._allow_auto_merge = allow_auto_merge
        self._delete_branch_on_merge = delete_branch_on_merge
        self._allow_merge_commit = allow_merge_commit
        self._allow_forking = allow_forking
        self._subscribers_count = subscribers_count
        self._network_count = network_count
        self._master_branch = master_branch
        self._starred_at = starred_at
        return
        
    

    
    def _getwatchers(self):
        return self._watchers
        
    watchers = property(_getwatchers)

    def _getopen_issues(self):
        return self._open_issues
        
    open_issues = property(_getopen_issues)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getpushed_at(self):
        return self._pushed_at and datetime.datetime.fromisoformat(self._pushed_at[0:-1])
        
    pushed_at = property(_getpushed_at)

    def _getdisabled(self):
        return self._disabled
        
    disabled = property(_getdisabled, doc="""Returns whether or not this repository disabled. """)

    def _gethas_pages(self):
        return self._has_pages
        
    has_pages = property(_gethas_pages)

    def _getopen_issues_count(self):
        return self._open_issues_count
        
    open_issues_count = property(_getopen_issues_count)

    def _getdefault_branch(self):
        return self._default_branch
        
    default_branch = property(_getdefault_branch, doc="""The default branch of the repository. """)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _getwatchers_count(self):
        return self._watchers_count
        
    watchers_count = property(_getwatchers_count)

    def _getstargazers_count(self):
        return self._stargazers_count
        
    stargazers_count = property(_getstargazers_count)

    def _getforks_count(self):
        return self._forks_count
        
    forks_count = property(_getforks_count)

    def _getlanguage(self):
        return self._language
        
    language = property(_getlanguage)

    def _gethomepage(self):
        return self._homepage
        
    homepage = property(_gethomepage)

    def _getsvn_url(self):
        return self._svn_url
        
    svn_url = property(_getsvn_url)

    def _gethooks_url(self):
        return self._hooks_url
        
    hooks_url = property(_gethooks_url)

    def _getmirror_url(self):
        return self._mirror_url
        
    mirror_url = property(_getmirror_url)

    def _getclone_url(self):
        return self._clone_url
        
    clone_url = property(_getclone_url)

    def _gettrees_url(self):
        return self._trees_url
        
    trees_url = property(_gettrees_url)

    def _getteams_url(self):
        return self._teams_url
        
    teams_url = property(_getteams_url)

    def _gettags_url(self):
        return self._tags_url
        
    tags_url = property(_gettags_url)

    def _getsubscription_url(self):
        return self._subscription_url
        
    subscription_url = property(_getsubscription_url)

    def _getsubscribers_url(self):
        return self._subscribers_url
        
    subscribers_url = property(_getsubscribers_url)

    def _getstatuses_url(self):
        return self._statuses_url
        
    statuses_url = property(_getstatuses_url)

    def _getstargazers_url(self):
        return self._stargazers_url
        
    stargazers_url = property(_getstargazers_url)

    def _getssh_url(self):
        return self._ssh_url
        
    ssh_url = property(_getssh_url)

    def _getreleases_url(self):
        return self._releases_url
        
    releases_url = property(_getreleases_url)

    def _getpulls_url(self):
        return self._pulls_url
        
    pulls_url = property(_getpulls_url)

    def _getnotifications_url(self):
        return self._notifications_url
        
    notifications_url = property(_getnotifications_url)

    def _getmilestones_url(self):
        return self._milestones_url
        
    milestones_url = property(_getmilestones_url)

    def _getmerges_url(self):
        return self._merges_url
        
    merges_url = property(_getmerges_url)

    def _getlanguages_url(self):
        return self._languages_url
        
    languages_url = property(_getlanguages_url)

    def _getlabels_url(self):
        return self._labels_url
        
    labels_url = property(_getlabels_url)

    def _getkeys_url(self):
        return self._keys_url
        
    keys_url = property(_getkeys_url)

    def _getissues_url(self):
        return self._issues_url
        
    issues_url = property(_getissues_url)

    def _getissue_events_url(self):
        return self._issue_events_url
        
    issue_events_url = property(_getissue_events_url)

    def _getissue_comment_url(self):
        return self._issue_comment_url
        
    issue_comment_url = property(_getissue_comment_url)

    def _getgit_url(self):
        return self._git_url
        
    git_url = property(_getgit_url)

    def _getgit_tags_url(self):
        return self._git_tags_url
        
    git_tags_url = property(_getgit_tags_url)

    def _getgit_refs_url(self):
        return self._git_refs_url
        
    git_refs_url = property(_getgit_refs_url)

    def _getgit_commits_url(self):
        return self._git_commits_url
        
    git_commits_url = property(_getgit_commits_url)

    def _getforks_url(self):
        return self._forks_url
        
    forks_url = property(_getforks_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getdownloads_url(self):
        return self._downloads_url
        
    downloads_url = property(_getdownloads_url)

    def _getdeployments_url(self):
        return self._deployments_url
        
    deployments_url = property(_getdeployments_url)

    def _getcontributors_url(self):
        return self._contributors_url
        
    contributors_url = property(_getcontributors_url)

    def _getcontents_url(self):
        return self._contents_url
        
    contents_url = property(_getcontents_url)

    def _getcompare_url(self):
        return self._compare_url
        
    compare_url = property(_getcompare_url)

    def _getcommits_url(self):
        return self._commits_url
        
    commits_url = property(_getcommits_url)

    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _getcollaborators_url(self):
        return self._collaborators_url
        
    collaborators_url = property(_getcollaborators_url)

    def _getbranches_url(self):
        return self._branches_url
        
    branches_url = property(_getbranches_url)

    def _getblobs_url(self):
        return self._blobs_url
        
    blobs_url = property(_getblobs_url)

    def _getassignees_url(self):
        return self._assignees_url
        
    assignees_url = property(_getassignees_url)

    def _getarchive_url(self):
        return self._archive_url
        
    archive_url = property(_getarchive_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getfork(self):
        return self._fork
        
    fork = property(_getfork)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getowner(self):
        return self._owner and SimpleUser(**self._owner)
        
    owner = property(_getowner)

    def _getforks(self):
        return self._forks
        
    forks = property(_getforks)

    def _getlicense(self):
        return self._license and NullableLicenseSimple(**self._license)
        
    license = property(_getlicense)

    def _getfull_name(self):
        return self._full_name
        
    full_name = property(_getfull_name)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the repository. """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the repository """)

    def _getorganization(self):
        return self._organization and NullableSimpleUser(**self._organization)
        
    organization = property(_getorganization)

    def _getpermissions(self):
        return self._permissions and Nullablerepository_permissions(**self._permissions)
        
    permissions = property(_getpermissions)

    def _getprivate(self):
        return self._private
        
    private = property(_getprivate, doc="""Whether the repository is private or public. """)

    def _getis_template(self):
        return self._is_template
        
    is_template = property(_getis_template, doc="""Whether this repository acts as a template that can be used to generate new repositories. """)

    def _gettopics(self):
        return self._topics and [ entry for entry in self._topics ]
        
    topics = property(_gettopics)

    def _gethas_issues(self):
        return self._has_issues
        
    has_issues = property(_gethas_issues, doc="""Whether issues are enabled. """)

    def _gethas_projects(self):
        return self._has_projects
        
    has_projects = property(_gethas_projects, doc="""Whether projects are enabled. """)

    def _gethas_wiki(self):
        return self._has_wiki
        
    has_wiki = property(_gethas_wiki, doc="""Whether the wiki is enabled. """)

    def _gethas_downloads(self):
        return self._has_downloads
        
    has_downloads = property(_gethas_downloads, doc="""Whether downloads are enabled. """)

    def _getarchived(self):
        return self._archived
        
    archived = property(_getarchived, doc="""Whether the repository is archived. """)

    def _getvisibility(self):
        return self._visibility
        
    visibility = property(_getvisibility, doc="""The repository visibility: public, private, or internal. """)

    def _getallow_rebase_merge(self):
        return self._allow_rebase_merge
        
    allow_rebase_merge = property(_getallow_rebase_merge, doc="""Whether to allow rebase merges for pull requests. """)

    def _gettemplate_repository(self):
        return self._template_repository and Nullablerepository_template_repository(**self._template_repository)
        
    template_repository = property(_gettemplate_repository)

    def _gettemp_clone_token(self):
        return self._temp_clone_token
        
    temp_clone_token = property(_gettemp_clone_token)

    def _getallow_squash_merge(self):
        return self._allow_squash_merge
        
    allow_squash_merge = property(_getallow_squash_merge, doc="""Whether to allow squash merges for pull requests. """)

    def _getallow_auto_merge(self):
        return self._allow_auto_merge
        
    allow_auto_merge = property(_getallow_auto_merge, doc="""Whether to allow Auto-merge to be used on pull requests. """)

    def _getdelete_branch_on_merge(self):
        return self._delete_branch_on_merge
        
    delete_branch_on_merge = property(_getdelete_branch_on_merge, doc="""Whether to delete head branches when pull requests are merged """)

    def _getallow_merge_commit(self):
        return self._allow_merge_commit
        
    allow_merge_commit = property(_getallow_merge_commit, doc="""Whether to allow merge commits for pull requests. """)

    def _getallow_forking(self):
        return self._allow_forking
        
    allow_forking = property(_getallow_forking, doc="""Whether to allow forking this repo """)

    def _getsubscribers_count(self):
        return self._subscribers_count
        
    subscribers_count = property(_getsubscribers_count)

    def _getnetwork_count(self):
        return self._network_count
        
    network_count = property(_getnetwork_count)

    def _getmaster_branch(self):
        return self._master_branch
        
    master_branch = property(_getmaster_branch)

    def _getstarred_at(self):
        return self._starred_at
        
    starred_at = property(_getstarred_at)


    
##
##
##
class Minimalrepository_permissions(ResponseBase):
    def __init__(self, admin:bool=None, maintain:bool=None, push:bool=None, triage:bool=None, pull:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._admin = admin
        self._maintain = maintain
        self._push = push
        self._triage = triage
        self._pull = pull
        return
        
    

    
    def _getadmin(self):
        return self._admin
        
    admin = property(_getadmin)

    def _getmaintain(self):
        return self._maintain
        
    maintain = property(_getmaintain)

    def _getpush(self):
        return self._push
        
    push = property(_getpush)

    def _gettriage(self):
        return self._triage
        
    triage = property(_gettriage)

    def _getpull(self):
        return self._pull
        
    pull = property(_getpull)


    
##
##
##
class Minimalrepository_license(ResponseBase):
    def __init__(self, key:str=None, name:str=None, spdx_id:str=None, url:str=None, node_id:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._key = key
        self._name = name
        self._spdx_id = spdx_id
        self._url = url
        self._node_id = node_id
        return
        
    

    
    def _getkey(self):
        return self._key
        
    key = property(_getkey)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getspdx_id(self):
        return self._spdx_id
        
    spdx_id = property(_getspdx_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)


    
##
##
##
class MinimalRepository(ResponseBase):
    """Minimal Repository """
    def __init__(self, hooks_url:str, trees_url:str, teams_url:str, tags_url:str, subscription_url:str, subscribers_url:str, statuses_url:str, stargazers_url:str, releases_url:str, pulls_url:str, notifications_url:str, milestones_url:str, merges_url:str, languages_url:str, labels_url:str, keys_url:str, issues_url:str, issue_events_url:str, issue_comment_url:str, git_tags_url:str, git_refs_url:str, git_commits_url:str, forks_url:str, events_url:str, downloads_url:str, deployments_url:str, contributors_url:str, contents_url:str, compare_url:str, commits_url:str, comments_url:str, collaborators_url:str, branches_url:str, blobs_url:str, assignees_url:str, archive_url:str, url:str, fork:bool, description:str, html_url:str, private:bool, owner:dict, full_name:str, name:str, node_id:str, id:int, git_url:str=None, ssh_url:str=None, clone_url:str=None, mirror_url:str=None, svn_url:str=None, homepage:str=None, language:str=None, forks_count:int=None, stargazers_count:int=None, watchers_count:int=None, size:int=None, default_branch:str=None, open_issues_count:int=None, is_template:bool=None, topics:list=[], has_issues:bool=None, has_projects:bool=None, has_wiki:bool=None, has_pages:bool=None, has_downloads:bool=None, archived:bool=None, disabled:bool=None, visibility:str=None, pushed_at:datetime=None, created_at:datetime=None, updated_at:datetime=None, permissions:dict=None, template_repository:dict=None, temp_clone_token:str=None, delete_branch_on_merge:bool=None, subscribers_count:int=None, network_count:int=None, code_of_conduct:dict=None, license:dict=None, forks:int=None, open_issues:int=None, watchers:int=None, allow_forking:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._hooks_url = hooks_url
        self._trees_url = trees_url
        self._teams_url = teams_url
        self._tags_url = tags_url
        self._subscription_url = subscription_url
        self._subscribers_url = subscribers_url
        self._statuses_url = statuses_url
        self._stargazers_url = stargazers_url
        self._releases_url = releases_url
        self._pulls_url = pulls_url
        self._notifications_url = notifications_url
        self._milestones_url = milestones_url
        self._merges_url = merges_url
        self._languages_url = languages_url
        self._labels_url = labels_url
        self._keys_url = keys_url
        self._issues_url = issues_url
        self._issue_events_url = issue_events_url
        self._issue_comment_url = issue_comment_url
        self._git_tags_url = git_tags_url
        self._git_refs_url = git_refs_url
        self._git_commits_url = git_commits_url
        self._forks_url = forks_url
        self._events_url = events_url
        self._downloads_url = downloads_url
        self._deployments_url = deployments_url
        self._contributors_url = contributors_url
        self._contents_url = contents_url
        self._compare_url = compare_url
        self._commits_url = commits_url
        self._comments_url = comments_url
        self._collaborators_url = collaborators_url
        self._branches_url = branches_url
        self._blobs_url = blobs_url
        self._assignees_url = assignees_url
        self._archive_url = archive_url
        self._url = url
        self._fork = fork
        self._description = description
        self._html_url = html_url
        self._private = private
        self._owner = owner
        self._full_name = full_name
        self._name = name
        self._node_id = node_id
        self._id = id
        self._git_url = git_url
        self._ssh_url = ssh_url
        self._clone_url = clone_url
        self._mirror_url = mirror_url
        self._svn_url = svn_url
        self._homepage = homepage
        self._language = language
        self._forks_count = forks_count
        self._stargazers_count = stargazers_count
        self._watchers_count = watchers_count
        self._size = size
        self._default_branch = default_branch
        self._open_issues_count = open_issues_count
        self._is_template = is_template
        self._topics = topics
        self._has_issues = has_issues
        self._has_projects = has_projects
        self._has_wiki = has_wiki
        self._has_pages = has_pages
        self._has_downloads = has_downloads
        self._archived = archived
        self._disabled = disabled
        self._visibility = visibility
        self._pushed_at = pushed_at
        self._created_at = created_at
        self._updated_at = updated_at
        self._permissions = permissions
        self._template_repository = template_repository
        self._temp_clone_token = temp_clone_token
        self._delete_branch_on_merge = delete_branch_on_merge
        self._subscribers_count = subscribers_count
        self._network_count = network_count
        self._code_of_conduct = code_of_conduct
        self._license = license
        self._forks = forks
        self._open_issues = open_issues
        self._watchers = watchers
        self._allow_forking = allow_forking
        return
        
    

    
    def _gethooks_url(self):
        return self._hooks_url
        
    hooks_url = property(_gethooks_url)

    def _gettrees_url(self):
        return self._trees_url
        
    trees_url = property(_gettrees_url)

    def _getteams_url(self):
        return self._teams_url
        
    teams_url = property(_getteams_url)

    def _gettags_url(self):
        return self._tags_url
        
    tags_url = property(_gettags_url)

    def _getsubscription_url(self):
        return self._subscription_url
        
    subscription_url = property(_getsubscription_url)

    def _getsubscribers_url(self):
        return self._subscribers_url
        
    subscribers_url = property(_getsubscribers_url)

    def _getstatuses_url(self):
        return self._statuses_url
        
    statuses_url = property(_getstatuses_url)

    def _getstargazers_url(self):
        return self._stargazers_url
        
    stargazers_url = property(_getstargazers_url)

    def _getreleases_url(self):
        return self._releases_url
        
    releases_url = property(_getreleases_url)

    def _getpulls_url(self):
        return self._pulls_url
        
    pulls_url = property(_getpulls_url)

    def _getnotifications_url(self):
        return self._notifications_url
        
    notifications_url = property(_getnotifications_url)

    def _getmilestones_url(self):
        return self._milestones_url
        
    milestones_url = property(_getmilestones_url)

    def _getmerges_url(self):
        return self._merges_url
        
    merges_url = property(_getmerges_url)

    def _getlanguages_url(self):
        return self._languages_url
        
    languages_url = property(_getlanguages_url)

    def _getlabels_url(self):
        return self._labels_url
        
    labels_url = property(_getlabels_url)

    def _getkeys_url(self):
        return self._keys_url
        
    keys_url = property(_getkeys_url)

    def _getissues_url(self):
        return self._issues_url
        
    issues_url = property(_getissues_url)

    def _getissue_events_url(self):
        return self._issue_events_url
        
    issue_events_url = property(_getissue_events_url)

    def _getissue_comment_url(self):
        return self._issue_comment_url
        
    issue_comment_url = property(_getissue_comment_url)

    def _getgit_tags_url(self):
        return self._git_tags_url
        
    git_tags_url = property(_getgit_tags_url)

    def _getgit_refs_url(self):
        return self._git_refs_url
        
    git_refs_url = property(_getgit_refs_url)

    def _getgit_commits_url(self):
        return self._git_commits_url
        
    git_commits_url = property(_getgit_commits_url)

    def _getforks_url(self):
        return self._forks_url
        
    forks_url = property(_getforks_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getdownloads_url(self):
        return self._downloads_url
        
    downloads_url = property(_getdownloads_url)

    def _getdeployments_url(self):
        return self._deployments_url
        
    deployments_url = property(_getdeployments_url)

    def _getcontributors_url(self):
        return self._contributors_url
        
    contributors_url = property(_getcontributors_url)

    def _getcontents_url(self):
        return self._contents_url
        
    contents_url = property(_getcontents_url)

    def _getcompare_url(self):
        return self._compare_url
        
    compare_url = property(_getcompare_url)

    def _getcommits_url(self):
        return self._commits_url
        
    commits_url = property(_getcommits_url)

    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _getcollaborators_url(self):
        return self._collaborators_url
        
    collaborators_url = property(_getcollaborators_url)

    def _getbranches_url(self):
        return self._branches_url
        
    branches_url = property(_getbranches_url)

    def _getblobs_url(self):
        return self._blobs_url
        
    blobs_url = property(_getblobs_url)

    def _getassignees_url(self):
        return self._assignees_url
        
    assignees_url = property(_getassignees_url)

    def _getarchive_url(self):
        return self._archive_url
        
    archive_url = property(_getarchive_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getfork(self):
        return self._fork
        
    fork = property(_getfork)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getprivate(self):
        return self._private
        
    private = property(_getprivate)

    def _getowner(self):
        return self._owner and SimpleUser(**self._owner)
        
    owner = property(_getowner)

    def _getfull_name(self):
        return self._full_name
        
    full_name = property(_getfull_name)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getgit_url(self):
        return self._git_url
        
    git_url = property(_getgit_url)

    def _getssh_url(self):
        return self._ssh_url
        
    ssh_url = property(_getssh_url)

    def _getclone_url(self):
        return self._clone_url
        
    clone_url = property(_getclone_url)

    def _getmirror_url(self):
        return self._mirror_url
        
    mirror_url = property(_getmirror_url)

    def _getsvn_url(self):
        return self._svn_url
        
    svn_url = property(_getsvn_url)

    def _gethomepage(self):
        return self._homepage
        
    homepage = property(_gethomepage)

    def _getlanguage(self):
        return self._language
        
    language = property(_getlanguage)

    def _getforks_count(self):
        return self._forks_count
        
    forks_count = property(_getforks_count)

    def _getstargazers_count(self):
        return self._stargazers_count
        
    stargazers_count = property(_getstargazers_count)

    def _getwatchers_count(self):
        return self._watchers_count
        
    watchers_count = property(_getwatchers_count)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _getdefault_branch(self):
        return self._default_branch
        
    default_branch = property(_getdefault_branch)

    def _getopen_issues_count(self):
        return self._open_issues_count
        
    open_issues_count = property(_getopen_issues_count)

    def _getis_template(self):
        return self._is_template
        
    is_template = property(_getis_template)

    def _gettopics(self):
        return self._topics and [ entry for entry in self._topics ]
        
    topics = property(_gettopics)

    def _gethas_issues(self):
        return self._has_issues
        
    has_issues = property(_gethas_issues)

    def _gethas_projects(self):
        return self._has_projects
        
    has_projects = property(_gethas_projects)

    def _gethas_wiki(self):
        return self._has_wiki
        
    has_wiki = property(_gethas_wiki)

    def _gethas_pages(self):
        return self._has_pages
        
    has_pages = property(_gethas_pages)

    def _gethas_downloads(self):
        return self._has_downloads
        
    has_downloads = property(_gethas_downloads)

    def _getarchived(self):
        return self._archived
        
    archived = property(_getarchived)

    def _getdisabled(self):
        return self._disabled
        
    disabled = property(_getdisabled)

    def _getvisibility(self):
        return self._visibility
        
    visibility = property(_getvisibility)

    def _getpushed_at(self):
        return self._pushed_at and datetime.datetime.fromisoformat(self._pushed_at[0:-1])
        
    pushed_at = property(_getpushed_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getpermissions(self):
        return self._permissions and Minimalrepository_permissions(**self._permissions)
        
    permissions = property(_getpermissions)

    def _gettemplate_repository(self):
        return self._template_repository and NullableRepository(**self._template_repository)
        
    template_repository = property(_gettemplate_repository)

    def _gettemp_clone_token(self):
        return self._temp_clone_token
        
    temp_clone_token = property(_gettemp_clone_token)

    def _getdelete_branch_on_merge(self):
        return self._delete_branch_on_merge
        
    delete_branch_on_merge = property(_getdelete_branch_on_merge)

    def _getsubscribers_count(self):
        return self._subscribers_count
        
    subscribers_count = property(_getsubscribers_count)

    def _getnetwork_count(self):
        return self._network_count
        
    network_count = property(_getnetwork_count)

    def _getcode_of_conduct(self):
        return self._code_of_conduct and CodeOfConduct(**self._code_of_conduct)
        
    code_of_conduct = property(_getcode_of_conduct)

    def _getlicense(self):
        return self._license and Minimalrepository_license(**self._license)
        
    license = property(_getlicense)

    def _getforks(self):
        return self._forks
        
    forks = property(_getforks)

    def _getopen_issues(self):
        return self._open_issues
        
    open_issues = property(_getopen_issues)

    def _getwatchers(self):
        return self._watchers
        
    watchers = property(_getwatchers)

    def _getallow_forking(self):
        return self._allow_forking
        
    allow_forking = property(_getallow_forking)


    
##
##
##
class Thread_subject(ResponseBase):
    def __init__(self, type:str, latest_comment_url:str, url:str, title:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._type = type
        self._latest_comment_url = latest_comment_url
        self._url = url
        self._title = title
        return
        
    

    
    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getlatest_comment_url(self):
        return self._latest_comment_url
        
    latest_comment_url = property(_getlatest_comment_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle)


    
##
##
##
class Thread(ResponseBase):
    """Thread """
    def __init__(self, subscription_url:str, url:str, last_read_at:str, updated_at:str, unread:bool, reason:str, subject:dict, repository:dict, id:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._subscription_url = subscription_url
        self._url = url
        self._last_read_at = last_read_at
        self._updated_at = updated_at
        self._unread = unread
        self._reason = reason
        self._subject = subject
        self._repository = repository
        self._id = id
        return
        
    

    
    def _getsubscription_url(self):
        return self._subscription_url
        
    subscription_url = property(_getsubscription_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getlast_read_at(self):
        return self._last_read_at
        
    last_read_at = property(_getlast_read_at)

    def _getupdated_at(self):
        return self._updated_at
        
    updated_at = property(_getupdated_at)

    def _getunread(self):
        return self._unread
        
    unread = property(_getunread)

    def _getreason(self):
        return self._reason
        
    reason = property(_getreason)

    def _getsubject(self):
        return self._subject and Thread_subject(**self._subject)
        
    subject = property(_getsubject)

    def _getrepository(self):
        return self._repository and MinimalRepository(**self._repository)
        
    repository = property(_getrepository)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class ThreadSubscription(ResponseBase):
    """Thread Subscription """
    def __init__(self, url:str, created_at:datetime, reason:str, ignored:bool, subscribed:bool, thread_url:str=None, repository_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._created_at = created_at
        self._reason = reason
        self._ignored = ignored
        self._subscribed = subscribed
        self._thread_url = thread_url
        self._repository_url = repository_url
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getreason(self):
        return self._reason
        
    reason = property(_getreason)

    def _getignored(self):
        return self._ignored
        
    ignored = property(_getignored)

    def _getsubscribed(self):
        return self._subscribed
        
    subscribed = property(_getsubscribed)

    def _getthread_url(self):
        return self._thread_url
        
    thread_url = property(_getthread_url)

    def _getrepository_url(self):
        return self._repository_url
        
    repository_url = property(_getrepository_url)


    
##
##
##
class Organizationfull_plan(ResponseBase):
    def __init__(self, private_repos:int, space:int, name:str, filled_seats:int=None, seats:int=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._private_repos = private_repos
        self._space = space
        self._name = name
        self._filled_seats = filled_seats
        self._seats = seats
        return
        
    

    
    def _getprivate_repos(self):
        return self._private_repos
        
    private_repos = property(_getprivate_repos)

    def _getspace(self):
        return self._space
        
    space = property(_getspace)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getfilled_seats(self):
        return self._filled_seats
        
    filled_seats = property(_getfilled_seats)

    def _getseats(self):
        return self._seats
        
    seats = property(_getseats)


    
##
##
##
class OrganizationFull(ResponseBase):
    """Organization Full """
    def __init__(self, updated_at:datetime, type:str, created_at:datetime, html_url:str, following:int, followers:int, public_gists:int, public_repos:int, has_repository_projects:bool, has_organization_projects:bool, description:str, avatar_url:str, public_members_url:str, members_url:str, issues_url:str, hooks_url:str, events_url:str, repos_url:str, url:str, node_id:str, id:int, login:str, name:str=None, company:str=None, blog:str=None, location:str=None, email:str=None, twitter_username:str=None, is_verified:bool=None, total_private_repos:int=None, owned_private_repos:int=None, private_gists:int=None, disk_usage:int=None, collaborators:int=None, billing_email:str=None, plan:dict=None, default_repository_permission:str=None, members_can_create_repositories:bool=None, two_factor_requirement_enabled:bool=None, members_allowed_repository_creation_type:str=None, members_can_create_public_repositories:bool=None, members_can_create_private_repositories:bool=None, members_can_create_internal_repositories:bool=None, members_can_create_pages:bool=None, members_can_create_public_pages:bool=None, members_can_create_private_pages:bool=None, members_can_fork_private_repositories:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._updated_at = updated_at
        self._type = type
        self._created_at = created_at
        self._html_url = html_url
        self._following = following
        self._followers = followers
        self._public_gists = public_gists
        self._public_repos = public_repos
        self._has_repository_projects = has_repository_projects
        self._has_organization_projects = has_organization_projects
        self._description = description
        self._avatar_url = avatar_url
        self._public_members_url = public_members_url
        self._members_url = members_url
        self._issues_url = issues_url
        self._hooks_url = hooks_url
        self._events_url = events_url
        self._repos_url = repos_url
        self._url = url
        self._node_id = node_id
        self._id = id
        self._login = login
        self._name = name
        self._company = company
        self._blog = blog
        self._location = location
        self._email = email
        self._twitter_username = twitter_username
        self._is_verified = is_verified
        self._total_private_repos = total_private_repos
        self._owned_private_repos = owned_private_repos
        self._private_gists = private_gists
        self._disk_usage = disk_usage
        self._collaborators = collaborators
        self._billing_email = billing_email
        self._plan = plan
        self._default_repository_permission = default_repository_permission
        self._members_can_create_repositories = members_can_create_repositories
        self._two_factor_requirement_enabled = two_factor_requirement_enabled
        self._members_allowed_repository_creation_type = members_allowed_repository_creation_type
        self._members_can_create_public_repositories = members_can_create_public_repositories
        self._members_can_create_private_repositories = members_can_create_private_repositories
        self._members_can_create_internal_repositories = members_can_create_internal_repositories
        self._members_can_create_pages = members_can_create_pages
        self._members_can_create_public_pages = members_can_create_public_pages
        self._members_can_create_private_pages = members_can_create_private_pages
        self._members_can_fork_private_repositories = members_can_fork_private_repositories
        return
        
    

    
    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getfollowing(self):
        return self._following
        
    following = property(_getfollowing)

    def _getfollowers(self):
        return self._followers
        
    followers = property(_getfollowers)

    def _getpublic_gists(self):
        return self._public_gists
        
    public_gists = property(_getpublic_gists)

    def _getpublic_repos(self):
        return self._public_repos
        
    public_repos = property(_getpublic_repos)

    def _gethas_repository_projects(self):
        return self._has_repository_projects
        
    has_repository_projects = property(_gethas_repository_projects)

    def _gethas_organization_projects(self):
        return self._has_organization_projects
        
    has_organization_projects = property(_gethas_organization_projects)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)

    def _getpublic_members_url(self):
        return self._public_members_url
        
    public_members_url = property(_getpublic_members_url)

    def _getmembers_url(self):
        return self._members_url
        
    members_url = property(_getmembers_url)

    def _getissues_url(self):
        return self._issues_url
        
    issues_url = property(_getissues_url)

    def _gethooks_url(self):
        return self._hooks_url
        
    hooks_url = property(_gethooks_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getrepos_url(self):
        return self._repos_url
        
    repos_url = property(_getrepos_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getcompany(self):
        return self._company
        
    company = property(_getcompany)

    def _getblog(self):
        return self._blog
        
    blog = property(_getblog)

    def _getlocation(self):
        return self._location
        
    location = property(_getlocation)

    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _gettwitter_username(self):
        return self._twitter_username
        
    twitter_username = property(_gettwitter_username)

    def _getis_verified(self):
        return self._is_verified
        
    is_verified = property(_getis_verified)

    def _gettotal_private_repos(self):
        return self._total_private_repos
        
    total_private_repos = property(_gettotal_private_repos)

    def _getowned_private_repos(self):
        return self._owned_private_repos
        
    owned_private_repos = property(_getowned_private_repos)

    def _getprivate_gists(self):
        return self._private_gists
        
    private_gists = property(_getprivate_gists)

    def _getdisk_usage(self):
        return self._disk_usage
        
    disk_usage = property(_getdisk_usage)

    def _getcollaborators(self):
        return self._collaborators
        
    collaborators = property(_getcollaborators)

    def _getbilling_email(self):
        return self._billing_email
        
    billing_email = property(_getbilling_email)

    def _getplan(self):
        return self._plan and Organizationfull_plan(**self._plan)
        
    plan = property(_getplan)

    def _getdefault_repository_permission(self):
        return self._default_repository_permission
        
    default_repository_permission = property(_getdefault_repository_permission)

    def _getmembers_can_create_repositories(self):
        return self._members_can_create_repositories
        
    members_can_create_repositories = property(_getmembers_can_create_repositories)

    def _gettwo_factor_requirement_enabled(self):
        return self._two_factor_requirement_enabled
        
    two_factor_requirement_enabled = property(_gettwo_factor_requirement_enabled)

    def _getmembers_allowed_repository_creation_type(self):
        return self._members_allowed_repository_creation_type
        
    members_allowed_repository_creation_type = property(_getmembers_allowed_repository_creation_type)

    def _getmembers_can_create_public_repositories(self):
        return self._members_can_create_public_repositories
        
    members_can_create_public_repositories = property(_getmembers_can_create_public_repositories)

    def _getmembers_can_create_private_repositories(self):
        return self._members_can_create_private_repositories
        
    members_can_create_private_repositories = property(_getmembers_can_create_private_repositories)

    def _getmembers_can_create_internal_repositories(self):
        return self._members_can_create_internal_repositories
        
    members_can_create_internal_repositories = property(_getmembers_can_create_internal_repositories)

    def _getmembers_can_create_pages(self):
        return self._members_can_create_pages
        
    members_can_create_pages = property(_getmembers_can_create_pages)

    def _getmembers_can_create_public_pages(self):
        return self._members_can_create_public_pages
        
    members_can_create_public_pages = property(_getmembers_can_create_public_pages)

    def _getmembers_can_create_private_pages(self):
        return self._members_can_create_private_pages
        
    members_can_create_private_pages = property(_getmembers_can_create_private_pages)

    def _getmembers_can_fork_private_repositories(self):
        return self._members_can_fork_private_repositories
        
    members_can_fork_private_repositories = property(_getmembers_can_fork_private_repositories)


    
##
##
##
class ActionsOrganizationPermissions(ResponseBase):
    def __init__(self, enabled_repositories:str, selected_repositories_url:str=None, allowed_actions:str=None, selected_actions_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled_repositories = enabled_repositories
        self._selected_repositories_url = selected_repositories_url
        self._allowed_actions = allowed_actions
        self._selected_actions_url = selected_actions_url
        return
        
    

    
    def _getenabled_repositories(self):
        return self._enabled_repositories
        
    enabled_repositories = property(_getenabled_repositories)

    def _getselected_repositories_url(self):
        return self._selected_repositories_url
        
    selected_repositories_url = property(_getselected_repositories_url, doc="""The API URL to use to get or set the selected repositories that are allowed to run GitHub Actions, when `enabled_repositories` is set to `selected`. """)

    def _getallowed_actions(self):
        return self._allowed_actions
        
    allowed_actions = property(_getallowed_actions)

    def _getselected_actions_url(self):
        return self._selected_actions_url
        
    selected_actions_url = property(_getselected_actions_url)


    
##
##
##
class RunnerGroupsOrg(ResponseBase):
    def __init__(self, allows_public_repositories:bool, inherited:bool, runners_url:str, default:bool, visibility:str, name:str, id:int, selected_repositories_url:str=None, inherited_allows_public_repositories:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._allows_public_repositories = allows_public_repositories
        self._inherited = inherited
        self._runners_url = runners_url
        self._default = default
        self._visibility = visibility
        self._name = name
        self._id = id
        self._selected_repositories_url = selected_repositories_url
        self._inherited_allows_public_repositories = inherited_allows_public_repositories
        return
        
    

    
    def _getallows_public_repositories(self):
        return self._allows_public_repositories
        
    allows_public_repositories = property(_getallows_public_repositories)

    def _getinherited(self):
        return self._inherited
        
    inherited = property(_getinherited)

    def _getrunners_url(self):
        return self._runners_url
        
    runners_url = property(_getrunners_url)

    def _getdefault(self):
        return self._default
        
    default = property(_getdefault)

    def _getvisibility(self):
        return self._visibility
        
    visibility = property(_getvisibility)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getselected_repositories_url(self):
        return self._selected_repositories_url
        
    selected_repositories_url = property(_getselected_repositories_url, doc="""Link to the selected repositories resource for this runner group. Not present unless visibility was set to `selected` """)

    def _getinherited_allows_public_repositories(self):
        return self._inherited_allows_public_repositories
        
    inherited_allows_public_repositories = property(_getinherited_allows_public_repositories)


    
##
##
##
class ActionsSecretForAnOrganization(ResponseBase):
    """Secrets for GitHub Actions for an organization. """
    def __init__(self, visibility:str, updated_at:datetime, created_at:datetime, name:str, selected_repositories_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._visibility = visibility
        self._updated_at = updated_at
        self._created_at = created_at
        self._name = name
        self._selected_repositories_url = selected_repositories_url
        return
        
    

    
    def _getvisibility(self):
        return self._visibility
        
    visibility = property(_getvisibility, doc="""Visibility of a secret """)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the secret. """)

    def _getselected_repositories_url(self):
        return self._selected_repositories_url
        
    selected_repositories_url = property(_getselected_repositories_url)


    
##
##
##
class Actionspublickey(ResponseBase):
    """The public key used for setting Actions Secrets. """
    def __init__(self, key:str, key_id:str, id:int=None, url:str=None, title:str=None, created_at:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._key = key
        self._key_id = key_id
        self._id = id
        self._url = url
        self._title = title
        self._created_at = created_at
        return
        
    

    
    def _getkey(self):
        return self._key
        
    key = property(_getkey, doc="""The Base64 encoded public key. """)

    def _getkey_id(self):
        return self._key_id
        
    key_id = property(_getkey_id, doc="""The identifier for the key. """)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)


    
##
##
##
class EmptyObject(ResponseBase):
    """An object without any properties. """
    def __init__(self, **kwargs):
        ResponseBase.__init__(self, kwargs)
        return
        
    

    

    
##
##
##
class Orghook_config(ResponseBase):
    def __init__(self, url:str=None, insecure_ssl:str=None, content_type:str=None, secret:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._insecure_ssl = insecure_ssl
        self._content_type = content_type
        self._secret = secret
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getinsecure_ssl(self):
        return self._insecure_ssl
        
    insecure_ssl = property(_getinsecure_ssl)

    def _getcontent_type(self):
        return self._content_type
        
    content_type = property(_getcontent_type)

    def _getsecret(self):
        return self._secret
        
    secret = property(_getsecret)


    
##
##
##
class OrgHook(ResponseBase):
    """Org Hook """
    def __init__(self, type:str, created_at:datetime, updated_at:datetime, config:dict, active:bool, events:list, name:str, ping_url:str, url:str, id:int, deliveries_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._type = type
        self._created_at = created_at
        self._updated_at = updated_at
        self._config = config
        self._active = active
        self._events = events
        self._name = name
        self._ping_url = ping_url
        self._url = url
        self._id = id
        self._deliveries_url = deliveries_url
        return
        
    

    
    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getconfig(self):
        return self._config and Orghook_config(**self._config)
        
    config = property(_getconfig)

    def _getactive(self):
        return self._active
        
    active = property(_getactive)

    def _getevents(self):
        return self._events and [ entry for entry in self._events ]
        
    events = property(_getevents)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getping_url(self):
        return self._ping_url
        
    ping_url = property(_getping_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getdeliveries_url(self):
        return self._deliveries_url
        
    deliveries_url = property(_getdeliveries_url)


    
##
##
##
class Orgmembership_permissions(ResponseBase):
    def __init__(self, can_create_repository:bool, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._can_create_repository = can_create_repository
        return
        
    

    
    def _getcan_create_repository(self):
        return self._can_create_repository
        
    can_create_repository = property(_getcan_create_repository)


    
##
##
##
class OrgMembership(ResponseBase):
    """Org Membership """
    def __init__(self, user:dict, organization:dict, organization_url:str, role:str, state:str, url:str, permissions:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._user = user
        self._organization = organization
        self._organization_url = organization_url
        self._role = role
        self._state = state
        self._url = url
        self._permissions = permissions
        return
        
    

    
    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _getorganization(self):
        return self._organization and OrganizationSimple(**self._organization)
        
    organization = property(_getorganization)

    def _getorganization_url(self):
        return self._organization_url
        
    organization_url = property(_getorganization_url)

    def _getrole(self):
        return self._role
        
    role = property(_getrole, doc="""The user's membership type in the organization. """)

    def _getstate(self):
        return self._state
        
    state = property(_getstate, doc="""The state of the member in the organization. The `pending` state indicates the user has not yet accepted an invitation. """)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getpermissions(self):
        return self._permissions and Orgmembership_permissions(**self._permissions)
        
    permissions = property(_getpermissions)


    
##
##
##
class OrgPreReceiveHook(ResponseBase):
    def __init__(self, id:int=None, name:str=None, enforcement:str=None, configuration_url:str=None, allow_downstream_configuration:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._name = name
        self._enforcement = enforcement
        self._configuration_url = configuration_url
        self._allow_downstream_configuration = allow_downstream_configuration
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getenforcement(self):
        return self._enforcement
        
    enforcement = property(_getenforcement)

    def _getconfiguration_url(self):
        return self._configuration_url
        
    configuration_url = property(_getconfiguration_url)

    def _getallow_downstream_configuration(self):
        return self._allow_downstream_configuration
        
    allow_downstream_configuration = property(_getallow_downstream_configuration)


    
##
##
##
class Project(ResponseBase):
    """Projects are a way to organize columns and cards of work. """
    def __init__(self, updated_at:datetime, created_at:datetime, creator:dict, state:str, number:int, body:str, name:str, node_id:str, id:int, columns_url:str, html_url:str, url:str, owner_url:str, organization_permission:str=None, private:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._updated_at = updated_at
        self._created_at = created_at
        self._creator = creator
        self._state = state
        self._number = number
        self._body = body
        self._name = name
        self._node_id = node_id
        self._id = id
        self._columns_url = columns_url
        self._html_url = html_url
        self._url = url
        self._owner_url = owner_url
        self._organization_permission = organization_permission
        self._private = private
        return
        
    

    
    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getcreator(self):
        return self._creator and NullableSimpleUser(**self._creator)
        
    creator = property(_getcreator)

    def _getstate(self):
        return self._state
        
    state = property(_getstate, doc="""State of the project; either 'open' or 'closed' """)

    def _getnumber(self):
        return self._number
        
    number = property(_getnumber)

    def _getbody(self):
        return self._body
        
    body = property(_getbody, doc="""Body of the project """)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""Name of the project """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getcolumns_url(self):
        return self._columns_url
        
    columns_url = property(_getcolumns_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getowner_url(self):
        return self._owner_url
        
    owner_url = property(_getowner_url)

    def _getorganization_permission(self):
        return self._organization_permission
        
    organization_permission = property(_getorganization_permission, doc="""The baseline permission that all organization members have on this project. Only present if owner is an organization. """)

    def _getprivate(self):
        return self._private
        
    private = property(_getprivate, doc="""Whether or not this project can be seen by everyone. Only present if owner is an organization. """)


    
##
##
##
class OrganizationSecretScanningAlert(ResponseBase):
    def __init__(self, number:int=None, created_at:datetime=None, url:str=None, html_url:str=None, locations_url:str=None, state:str=None, resolution:str=None, resolved_at:datetime=None, resolved_by:dict=None, secret_type:str=None, secret:str=None, repository:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._number = number
        self._created_at = created_at
        self._url = url
        self._html_url = html_url
        self._locations_url = locations_url
        self._state = state
        self._resolution = resolution
        self._resolved_at = resolved_at
        self._resolved_by = resolved_by
        self._secret_type = secret_type
        self._secret = secret
        self._repository = repository
        return
        
    

    
    def _getnumber(self):
        return self._number
        
    number = property(_getnumber)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getlocations_url(self):
        return self._locations_url
        
    locations_url = property(_getlocations_url, doc="""The REST API URL of the code locations for this alert. """)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)

    def _getresolution(self):
        return self._resolution
        
    resolution = property(_getresolution)

    def _getresolved_at(self):
        return self._resolved_at and datetime.datetime.fromisoformat(self._resolved_at[0:-1])
        
    resolved_at = property(_getresolved_at, doc="""The time that the alert was resolved in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. """)

    def _getresolved_by(self):
        return self._resolved_by and NullableSimpleUser(**self._resolved_by)
        
    resolved_by = property(_getresolved_by)

    def _getsecret_type(self):
        return self._secret_type
        
    secret_type = property(_getsecret_type, doc="""The type of secret that secret scanning detected. """)

    def _getsecret(self):
        return self._secret
        
    secret = property(_getsecret, doc="""The secret that was detected. """)

    def _getrepository(self):
        return self._repository and MinimalRepository(**self._repository)
        
    repository = property(_getrepository)


    
##
##
##
class NullableTeamSimple(ResponseBase):
    """Groups of organization members that gives permissions on specified repositories. """
    def __init__(self, slug:str, repositories_url:str, html_url:str, permission:str, description:str, name:str, members_url:str, url:str, node_id:str, id:int, privacy:str=None, ldap_dn:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._slug = slug
        self._repositories_url = repositories_url
        self._html_url = html_url
        self._permission = permission
        self._description = description
        self._name = name
        self._members_url = members_url
        self._url = url
        self._node_id = node_id
        self._id = id
        self._privacy = privacy
        self._ldap_dn = ldap_dn
        return
        
    

    
    def _getslug(self):
        return self._slug
        
    slug = property(_getslug)

    def _getrepositories_url(self):
        return self._repositories_url
        
    repositories_url = property(_getrepositories_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getpermission(self):
        return self._permission
        
    permission = property(_getpermission, doc="""Permission that the team will have for its repositories """)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription, doc="""Description of the team """)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""Name of the team """)

    def _getmembers_url(self):
        return self._members_url
        
    members_url = property(_getmembers_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl, doc="""URL for the team """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the team """)

    def _getprivacy(self):
        return self._privacy
        
    privacy = property(_getprivacy, doc="""The level of privacy this team should have """)

    def _getldap_dn(self):
        return self._ldap_dn
        
    ldap_dn = property(_getldap_dn, doc="""Distinguished Name (DN) that team maps to within LDAP environment """)


    
##
##
##
class Team_permissions(ResponseBase):
    def __init__(self, admin:bool, maintain:bool, push:bool, triage:bool, pull:bool, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._admin = admin
        self._maintain = maintain
        self._push = push
        self._triage = triage
        self._pull = pull
        return
        
    

    
    def _getadmin(self):
        return self._admin
        
    admin = property(_getadmin)

    def _getmaintain(self):
        return self._maintain
        
    maintain = property(_getmaintain)

    def _getpush(self):
        return self._push
        
    push = property(_getpush)

    def _gettriage(self):
        return self._triage
        
    triage = property(_gettriage)

    def _getpull(self):
        return self._pull
        
    pull = property(_getpull)


    
##
##
##
class Team(ResponseBase):
    """Groups of organization members that gives permissions on specified repositories. """
    def __init__(self, parent:dict, repositories_url:str, members_url:str, html_url:str, url:str, permission:str, description:str, slug:str, name:str, node_id:str, id:int, privacy:str=None, permissions:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._parent = parent
        self._repositories_url = repositories_url
        self._members_url = members_url
        self._html_url = html_url
        self._url = url
        self._permission = permission
        self._description = description
        self._slug = slug
        self._name = name
        self._node_id = node_id
        self._id = id
        self._privacy = privacy
        self._permissions = permissions
        return
        
    

    
    def _getparent(self):
        return self._parent and NullableTeamSimple(**self._parent)
        
    parent = property(_getparent)

    def _getrepositories_url(self):
        return self._repositories_url
        
    repositories_url = property(_getrepositories_url)

    def _getmembers_url(self):
        return self._members_url
        
    members_url = property(_getmembers_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getpermission(self):
        return self._permission
        
    permission = property(_getpermission)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getslug(self):
        return self._slug
        
    slug = property(_getslug)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getprivacy(self):
        return self._privacy
        
    privacy = property(_getprivacy)

    def _getpermissions(self):
        return self._permissions and Team_permissions(**self._permissions)
        
    permissions = property(_getpermissions)


    
##
##
##
class FullTeam(ResponseBase):
    """Groups of organization members that gives permissions on specified repositories. """
    def __init__(self, organization:dict, updated_at:datetime, created_at:datetime, repos_count:int, members_count:int, repositories_url:str, members_url:str, permission:str, description:str, slug:str, name:str, html_url:str, url:str, node_id:str, id:int, privacy:str=None, parent:dict=None, ldap_dn:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._organization = organization
        self._updated_at = updated_at
        self._created_at = created_at
        self._repos_count = repos_count
        self._members_count = members_count
        self._repositories_url = repositories_url
        self._members_url = members_url
        self._permission = permission
        self._description = description
        self._slug = slug
        self._name = name
        self._html_url = html_url
        self._url = url
        self._node_id = node_id
        self._id = id
        self._privacy = privacy
        self._parent = parent
        self._ldap_dn = ldap_dn
        return
        
    

    
    def _getorganization(self):
        return self._organization and OrganizationFull(**self._organization)
        
    organization = property(_getorganization)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getrepos_count(self):
        return self._repos_count
        
    repos_count = property(_getrepos_count)

    def _getmembers_count(self):
        return self._members_count
        
    members_count = property(_getmembers_count)

    def _getrepositories_url(self):
        return self._repositories_url
        
    repositories_url = property(_getrepositories_url)

    def _getmembers_url(self):
        return self._members_url
        
    members_url = property(_getmembers_url)

    def _getpermission(self):
        return self._permission
        
    permission = property(_getpermission, doc="""Permission that the team will have for its repositories """)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getslug(self):
        return self._slug
        
    slug = property(_getslug)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""Name of the team """)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl, doc="""URL for the team """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the team """)

    def _getprivacy(self):
        return self._privacy
        
    privacy = property(_getprivacy, doc="""The level of privacy this team should have """)

    def _getparent(self):
        return self._parent and NullableTeamSimple(**self._parent)
        
    parent = property(_getparent)

    def _getldap_dn(self):
        return self._ldap_dn
        
    ldap_dn = property(_getldap_dn, doc="""Distinguished Name (DN) that team maps to within LDAP environment """)


    
##
##
##
class TeamDiscussion(ResponseBase):
    """A team discussion is a persistent record of a free-form conversation within a team. """
    def __init__(self, url:str, updated_at:datetime, title:str, team_url:str, private:bool, pinned:bool, number:int, node_id:str, html_url:str, last_edited_at:datetime, created_at:datetime, comments_url:str, comments_count:int, body_version:str, body_html:str, body:str, author:dict, reactions:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._updated_at = updated_at
        self._title = title
        self._team_url = team_url
        self._private = private
        self._pinned = pinned
        self._number = number
        self._node_id = node_id
        self._html_url = html_url
        self._last_edited_at = last_edited_at
        self._created_at = created_at
        self._comments_url = comments_url
        self._comments_count = comments_count
        self._body_version = body_version
        self._body_html = body_html
        self._body = body
        self._author = author
        self._reactions = reactions
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle, doc="""The title of the discussion. """)

    def _getteam_url(self):
        return self._team_url
        
    team_url = property(_getteam_url)

    def _getprivate(self):
        return self._private
        
    private = property(_getprivate, doc="""Whether or not this discussion should be restricted to team members and organization administrators. """)

    def _getpinned(self):
        return self._pinned
        
    pinned = property(_getpinned, doc="""Whether or not this discussion should be pinned for easy retrieval. """)

    def _getnumber(self):
        return self._number
        
    number = property(_getnumber, doc="""The unique sequence number of a team discussion. """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getlast_edited_at(self):
        return self._last_edited_at and datetime.datetime.fromisoformat(self._last_edited_at[0:-1])
        
    last_edited_at = property(_getlast_edited_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _getcomments_count(self):
        return self._comments_count
        
    comments_count = property(_getcomments_count)

    def _getbody_version(self):
        return self._body_version
        
    body_version = property(_getbody_version, doc="""The current version of the body content. If provided, this update operation will be rejected if the given version does not match the latest version on the server. """)

    def _getbody_html(self):
        return self._body_html
        
    body_html = property(_getbody_html)

    def _getbody(self):
        return self._body
        
    body = property(_getbody, doc="""The main text of the discussion. """)

    def _getauthor(self):
        return self._author and NullableSimpleUser(**self._author)
        
    author = property(_getauthor)

    def _getreactions(self):
        return self._reactions and ReactionRollup(**ReactionRollup.patchEntry(self._reactions))
        
    reactions = property(_getreactions)


    
##
##
##
class TeamDiscussionComment(ResponseBase):
    """A reply to a discussion within a team. """
    def __init__(self, url:str, updated_at:datetime, number:int, node_id:str, html_url:str, discussion_url:str, last_edited_at:datetime, created_at:datetime, body_version:str, body_html:str, body:str, author:dict, reactions:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._updated_at = updated_at
        self._number = number
        self._node_id = node_id
        self._html_url = html_url
        self._discussion_url = discussion_url
        self._last_edited_at = last_edited_at
        self._created_at = created_at
        self._body_version = body_version
        self._body_html = body_html
        self._body = body
        self._author = author
        self._reactions = reactions
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getnumber(self):
        return self._number
        
    number = property(_getnumber, doc="""The unique sequence number of a team discussion comment. """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getdiscussion_url(self):
        return self._discussion_url
        
    discussion_url = property(_getdiscussion_url)

    def _getlast_edited_at(self):
        return self._last_edited_at and datetime.datetime.fromisoformat(self._last_edited_at[0:-1])
        
    last_edited_at = property(_getlast_edited_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getbody_version(self):
        return self._body_version
        
    body_version = property(_getbody_version, doc="""The current version of the body content. If provided, this update operation will be rejected if the given version does not match the latest version on the server. """)

    def _getbody_html(self):
        return self._body_html
        
    body_html = property(_getbody_html)

    def _getbody(self):
        return self._body
        
    body = property(_getbody, doc="""The main text of the comment. """)

    def _getauthor(self):
        return self._author and NullableSimpleUser(**self._author)
        
    author = property(_getauthor)

    def _getreactions(self):
        return self._reactions and ReactionRollup(**ReactionRollup.patchEntry(self._reactions))
        
    reactions = property(_getreactions)


    
##
##
##
class Reaction(ResponseBase):
    """Reactions to conversations provide a way to help people express their feelings more simply and effectively. """
    def __init__(self, created_at:datetime, content:str, user:dict, node_id:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._created_at = created_at
        self._content = content
        self._user = user
        self._node_id = node_id
        self._id = id
        return
        
    

    
    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getcontent(self):
        return self._content
        
    content = property(_getcontent, doc="""The reaction to use """)

    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class TeamMembership(ResponseBase):
    """Team Membership """
    def __init__(self, state:str, url:str, role:str='member', **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._state = state
        self._url = url
        self._role = role
        return
        
    

    
    def _getstate(self):
        return self._state
        
    state = property(_getstate, doc="""The state of the user's membership in the team. """)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getrole(self):
        return self._role
        
    role = property(_getrole, doc="""The role of the user in the team. """)


    
##
##
##
class Teamproject_permissions(ResponseBase):
    def __init__(self, admin:bool, write:bool, read:bool, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._admin = admin
        self._write = write
        self._read = read
        return
        
    

    
    def _getadmin(self):
        return self._admin
        
    admin = property(_getadmin)

    def _getwrite(self):
        return self._write
        
    write = property(_getwrite)

    def _getread(self):
        return self._read
        
    read = property(_getread)


    
##
##
##
class TeamProject(ResponseBase):
    """A team's access to a project. """
    def __init__(self, permissions:dict, updated_at:str, created_at:str, creator:dict, state:str, number:int, body:str, name:str, node_id:str, id:int, columns_url:str, html_url:str, url:str, owner_url:str, organization_permission:str=None, private:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._permissions = permissions
        self._updated_at = updated_at
        self._created_at = created_at
        self._creator = creator
        self._state = state
        self._number = number
        self._body = body
        self._name = name
        self._node_id = node_id
        self._id = id
        self._columns_url = columns_url
        self._html_url = html_url
        self._url = url
        self._owner_url = owner_url
        self._organization_permission = organization_permission
        self._private = private
        return
        
    

    
    def _getpermissions(self):
        return self._permissions and Teamproject_permissions(**self._permissions)
        
    permissions = property(_getpermissions)

    def _getupdated_at(self):
        return self._updated_at
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getcreator(self):
        return self._creator and SimpleUser(**self._creator)
        
    creator = property(_getcreator)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)

    def _getnumber(self):
        return self._number
        
    number = property(_getnumber)

    def _getbody(self):
        return self._body
        
    body = property(_getbody)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getcolumns_url(self):
        return self._columns_url
        
    columns_url = property(_getcolumns_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getowner_url(self):
        return self._owner_url
        
    owner_url = property(_getowner_url)

    def _getorganization_permission(self):
        return self._organization_permission
        
    organization_permission = property(_getorganization_permission, doc="""The organization permission for this project. Only present when owner is an organization. """)

    def _getprivate(self):
        return self._private
        
    private = property(_getprivate, doc="""Whether the project is private or not. Only present when owner is an organization. """)


    
##
##
##
class Teamrepository_permissions(ResponseBase):
    def __init__(self, push:bool, pull:bool, admin:bool, triage:bool=None, maintain:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._push = push
        self._pull = pull
        self._admin = admin
        self._triage = triage
        self._maintain = maintain
        return
        
    

    
    def _getpush(self):
        return self._push
        
    push = property(_getpush)

    def _getpull(self):
        return self._pull
        
    pull = property(_getpull)

    def _getadmin(self):
        return self._admin
        
    admin = property(_getadmin)

    def _gettriage(self):
        return self._triage
        
    triage = property(_gettriage)

    def _getmaintain(self):
        return self._maintain
        
    maintain = property(_getmaintain)


    
##
##
##
class TeamRepository(ResponseBase):
    """A team's access to a repository. """
    def __init__(self, watchers:int, open_issues:int, updated_at:datetime, created_at:datetime, pushed_at:datetime, disabled:bool, has_pages:bool, open_issues_count:int, default_branch:str, size:int, watchers_count:int, stargazers_count:int, forks_count:int, language:str, homepage:str, svn_url:str, hooks_url:str, mirror_url:str, clone_url:str, trees_url:str, teams_url:str, tags_url:str, subscription_url:str, subscribers_url:str, statuses_url:str, stargazers_url:str, ssh_url:str, releases_url:str, pulls_url:str, notifications_url:str, milestones_url:str, merges_url:str, languages_url:str, labels_url:str, keys_url:str, issues_url:str, issue_events_url:str, issue_comment_url:str, git_url:str, git_tags_url:str, git_refs_url:str, git_commits_url:str, forks_url:str, events_url:str, downloads_url:str, deployments_url:str, contributors_url:str, contents_url:str, compare_url:str, commits_url:str, comments_url:str, collaborators_url:str, branches_url:str, blobs_url:str, assignees_url:str, archive_url:str, url:str, fork:bool, description:str, html_url:str, owner:dict, forks:int, license:dict, full_name:str, name:str, node_id:str, id:int, permissions:dict=None, private:bool=False, is_template:bool=False, topics:list=[], has_issues:bool=True, has_projects:bool=True, has_wiki:bool=True, has_downloads:bool=True, archived:bool=False, visibility:str='public', allow_rebase_merge:bool=True, template_repository:dict=None, temp_clone_token:str=None, allow_squash_merge:bool=True, allow_auto_merge:bool=False, delete_branch_on_merge:bool=False, allow_merge_commit:bool=True, allow_forking:bool=False, subscribers_count:int=None, network_count:int=None, master_branch:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._watchers = watchers
        self._open_issues = open_issues
        self._updated_at = updated_at
        self._created_at = created_at
        self._pushed_at = pushed_at
        self._disabled = disabled
        self._has_pages = has_pages
        self._open_issues_count = open_issues_count
        self._default_branch = default_branch
        self._size = size
        self._watchers_count = watchers_count
        self._stargazers_count = stargazers_count
        self._forks_count = forks_count
        self._language = language
        self._homepage = homepage
        self._svn_url = svn_url
        self._hooks_url = hooks_url
        self._mirror_url = mirror_url
        self._clone_url = clone_url
        self._trees_url = trees_url
        self._teams_url = teams_url
        self._tags_url = tags_url
        self._subscription_url = subscription_url
        self._subscribers_url = subscribers_url
        self._statuses_url = statuses_url
        self._stargazers_url = stargazers_url
        self._ssh_url = ssh_url
        self._releases_url = releases_url
        self._pulls_url = pulls_url
        self._notifications_url = notifications_url
        self._milestones_url = milestones_url
        self._merges_url = merges_url
        self._languages_url = languages_url
        self._labels_url = labels_url
        self._keys_url = keys_url
        self._issues_url = issues_url
        self._issue_events_url = issue_events_url
        self._issue_comment_url = issue_comment_url
        self._git_url = git_url
        self._git_tags_url = git_tags_url
        self._git_refs_url = git_refs_url
        self._git_commits_url = git_commits_url
        self._forks_url = forks_url
        self._events_url = events_url
        self._downloads_url = downloads_url
        self._deployments_url = deployments_url
        self._contributors_url = contributors_url
        self._contents_url = contents_url
        self._compare_url = compare_url
        self._commits_url = commits_url
        self._comments_url = comments_url
        self._collaborators_url = collaborators_url
        self._branches_url = branches_url
        self._blobs_url = blobs_url
        self._assignees_url = assignees_url
        self._archive_url = archive_url
        self._url = url
        self._fork = fork
        self._description = description
        self._html_url = html_url
        self._owner = owner
        self._forks = forks
        self._license = license
        self._full_name = full_name
        self._name = name
        self._node_id = node_id
        self._id = id
        self._permissions = permissions
        self._private = private
        self._is_template = is_template
        self._topics = topics
        self._has_issues = has_issues
        self._has_projects = has_projects
        self._has_wiki = has_wiki
        self._has_downloads = has_downloads
        self._archived = archived
        self._visibility = visibility
        self._allow_rebase_merge = allow_rebase_merge
        self._template_repository = template_repository
        self._temp_clone_token = temp_clone_token
        self._allow_squash_merge = allow_squash_merge
        self._allow_auto_merge = allow_auto_merge
        self._delete_branch_on_merge = delete_branch_on_merge
        self._allow_merge_commit = allow_merge_commit
        self._allow_forking = allow_forking
        self._subscribers_count = subscribers_count
        self._network_count = network_count
        self._master_branch = master_branch
        return
        
    

    
    def _getwatchers(self):
        return self._watchers
        
    watchers = property(_getwatchers)

    def _getopen_issues(self):
        return self._open_issues
        
    open_issues = property(_getopen_issues)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getpushed_at(self):
        return self._pushed_at and datetime.datetime.fromisoformat(self._pushed_at[0:-1])
        
    pushed_at = property(_getpushed_at)

    def _getdisabled(self):
        return self._disabled
        
    disabled = property(_getdisabled, doc="""Returns whether or not this repository disabled. """)

    def _gethas_pages(self):
        return self._has_pages
        
    has_pages = property(_gethas_pages)

    def _getopen_issues_count(self):
        return self._open_issues_count
        
    open_issues_count = property(_getopen_issues_count)

    def _getdefault_branch(self):
        return self._default_branch
        
    default_branch = property(_getdefault_branch, doc="""The default branch of the repository. """)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _getwatchers_count(self):
        return self._watchers_count
        
    watchers_count = property(_getwatchers_count)

    def _getstargazers_count(self):
        return self._stargazers_count
        
    stargazers_count = property(_getstargazers_count)

    def _getforks_count(self):
        return self._forks_count
        
    forks_count = property(_getforks_count)

    def _getlanguage(self):
        return self._language
        
    language = property(_getlanguage)

    def _gethomepage(self):
        return self._homepage
        
    homepage = property(_gethomepage)

    def _getsvn_url(self):
        return self._svn_url
        
    svn_url = property(_getsvn_url)

    def _gethooks_url(self):
        return self._hooks_url
        
    hooks_url = property(_gethooks_url)

    def _getmirror_url(self):
        return self._mirror_url
        
    mirror_url = property(_getmirror_url)

    def _getclone_url(self):
        return self._clone_url
        
    clone_url = property(_getclone_url)

    def _gettrees_url(self):
        return self._trees_url
        
    trees_url = property(_gettrees_url)

    def _getteams_url(self):
        return self._teams_url
        
    teams_url = property(_getteams_url)

    def _gettags_url(self):
        return self._tags_url
        
    tags_url = property(_gettags_url)

    def _getsubscription_url(self):
        return self._subscription_url
        
    subscription_url = property(_getsubscription_url)

    def _getsubscribers_url(self):
        return self._subscribers_url
        
    subscribers_url = property(_getsubscribers_url)

    def _getstatuses_url(self):
        return self._statuses_url
        
    statuses_url = property(_getstatuses_url)

    def _getstargazers_url(self):
        return self._stargazers_url
        
    stargazers_url = property(_getstargazers_url)

    def _getssh_url(self):
        return self._ssh_url
        
    ssh_url = property(_getssh_url)

    def _getreleases_url(self):
        return self._releases_url
        
    releases_url = property(_getreleases_url)

    def _getpulls_url(self):
        return self._pulls_url
        
    pulls_url = property(_getpulls_url)

    def _getnotifications_url(self):
        return self._notifications_url
        
    notifications_url = property(_getnotifications_url)

    def _getmilestones_url(self):
        return self._milestones_url
        
    milestones_url = property(_getmilestones_url)

    def _getmerges_url(self):
        return self._merges_url
        
    merges_url = property(_getmerges_url)

    def _getlanguages_url(self):
        return self._languages_url
        
    languages_url = property(_getlanguages_url)

    def _getlabels_url(self):
        return self._labels_url
        
    labels_url = property(_getlabels_url)

    def _getkeys_url(self):
        return self._keys_url
        
    keys_url = property(_getkeys_url)

    def _getissues_url(self):
        return self._issues_url
        
    issues_url = property(_getissues_url)

    def _getissue_events_url(self):
        return self._issue_events_url
        
    issue_events_url = property(_getissue_events_url)

    def _getissue_comment_url(self):
        return self._issue_comment_url
        
    issue_comment_url = property(_getissue_comment_url)

    def _getgit_url(self):
        return self._git_url
        
    git_url = property(_getgit_url)

    def _getgit_tags_url(self):
        return self._git_tags_url
        
    git_tags_url = property(_getgit_tags_url)

    def _getgit_refs_url(self):
        return self._git_refs_url
        
    git_refs_url = property(_getgit_refs_url)

    def _getgit_commits_url(self):
        return self._git_commits_url
        
    git_commits_url = property(_getgit_commits_url)

    def _getforks_url(self):
        return self._forks_url
        
    forks_url = property(_getforks_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getdownloads_url(self):
        return self._downloads_url
        
    downloads_url = property(_getdownloads_url)

    def _getdeployments_url(self):
        return self._deployments_url
        
    deployments_url = property(_getdeployments_url)

    def _getcontributors_url(self):
        return self._contributors_url
        
    contributors_url = property(_getcontributors_url)

    def _getcontents_url(self):
        return self._contents_url
        
    contents_url = property(_getcontents_url)

    def _getcompare_url(self):
        return self._compare_url
        
    compare_url = property(_getcompare_url)

    def _getcommits_url(self):
        return self._commits_url
        
    commits_url = property(_getcommits_url)

    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _getcollaborators_url(self):
        return self._collaborators_url
        
    collaborators_url = property(_getcollaborators_url)

    def _getbranches_url(self):
        return self._branches_url
        
    branches_url = property(_getbranches_url)

    def _getblobs_url(self):
        return self._blobs_url
        
    blobs_url = property(_getblobs_url)

    def _getassignees_url(self):
        return self._assignees_url
        
    assignees_url = property(_getassignees_url)

    def _getarchive_url(self):
        return self._archive_url
        
    archive_url = property(_getarchive_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getfork(self):
        return self._fork
        
    fork = property(_getfork)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getowner(self):
        return self._owner and NullableSimpleUser(**self._owner)
        
    owner = property(_getowner)

    def _getforks(self):
        return self._forks
        
    forks = property(_getforks)

    def _getlicense(self):
        return self._license and NullableLicenseSimple(**self._license)
        
    license = property(_getlicense)

    def _getfull_name(self):
        return self._full_name
        
    full_name = property(_getfull_name)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the repository. """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the repository """)

    def _getpermissions(self):
        return self._permissions and Teamrepository_permissions(**self._permissions)
        
    permissions = property(_getpermissions)

    def _getprivate(self):
        return self._private
        
    private = property(_getprivate, doc="""Whether the repository is private or public. """)

    def _getis_template(self):
        return self._is_template
        
    is_template = property(_getis_template, doc="""Whether this repository acts as a template that can be used to generate new repositories. """)

    def _gettopics(self):
        return self._topics and [ entry for entry in self._topics ]
        
    topics = property(_gettopics)

    def _gethas_issues(self):
        return self._has_issues
        
    has_issues = property(_gethas_issues, doc="""Whether issues are enabled. """)

    def _gethas_projects(self):
        return self._has_projects
        
    has_projects = property(_gethas_projects, doc="""Whether projects are enabled. """)

    def _gethas_wiki(self):
        return self._has_wiki
        
    has_wiki = property(_gethas_wiki, doc="""Whether the wiki is enabled. """)

    def _gethas_downloads(self):
        return self._has_downloads
        
    has_downloads = property(_gethas_downloads, doc="""Whether downloads are enabled. """)

    def _getarchived(self):
        return self._archived
        
    archived = property(_getarchived, doc="""Whether the repository is archived. """)

    def _getvisibility(self):
        return self._visibility
        
    visibility = property(_getvisibility, doc="""The repository visibility: public, private, or internal. """)

    def _getallow_rebase_merge(self):
        return self._allow_rebase_merge
        
    allow_rebase_merge = property(_getallow_rebase_merge, doc="""Whether to allow rebase merges for pull requests. """)

    def _gettemplate_repository(self):
        return self._template_repository and NullableRepository(**self._template_repository)
        
    template_repository = property(_gettemplate_repository)

    def _gettemp_clone_token(self):
        return self._temp_clone_token
        
    temp_clone_token = property(_gettemp_clone_token)

    def _getallow_squash_merge(self):
        return self._allow_squash_merge
        
    allow_squash_merge = property(_getallow_squash_merge, doc="""Whether to allow squash merges for pull requests. """)

    def _getallow_auto_merge(self):
        return self._allow_auto_merge
        
    allow_auto_merge = property(_getallow_auto_merge, doc="""Whether to allow Auto-merge to be used on pull requests. """)

    def _getdelete_branch_on_merge(self):
        return self._delete_branch_on_merge
        
    delete_branch_on_merge = property(_getdelete_branch_on_merge, doc="""Whether to delete head branches when pull requests are merged """)

    def _getallow_merge_commit(self):
        return self._allow_merge_commit
        
    allow_merge_commit = property(_getallow_merge_commit, doc="""Whether to allow merge commits for pull requests. """)

    def _getallow_forking(self):
        return self._allow_forking
        
    allow_forking = property(_getallow_forking, doc="""Whether to allow forking this repo """)

    def _getsubscribers_count(self):
        return self._subscribers_count
        
    subscribers_count = property(_getsubscribers_count)

    def _getnetwork_count(self):
        return self._network_count
        
    network_count = property(_getnetwork_count)

    def _getmaster_branch(self):
        return self._master_branch
        
    master_branch = property(_getmaster_branch)


    
##
##
##
class ProjectCard(ResponseBase):
    """Project cards represent a scope of work. """
    def __init__(self, project_url:str, column_url:str, updated_at:datetime, created_at:datetime, creator:dict, note:str, node_id:str, id:int, url:str, archived:bool=None, column_name:str=None, project_id:str=None, content_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._project_url = project_url
        self._column_url = column_url
        self._updated_at = updated_at
        self._created_at = created_at
        self._creator = creator
        self._note = note
        self._node_id = node_id
        self._id = id
        self._url = url
        self._archived = archived
        self._column_name = column_name
        self._project_id = project_id
        self._content_url = content_url
        return
        
    

    
    def _getproject_url(self):
        return self._project_url
        
    project_url = property(_getproject_url)

    def _getcolumn_url(self):
        return self._column_url
        
    column_url = property(_getcolumn_url)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getcreator(self):
        return self._creator and NullableSimpleUser(**self._creator)
        
    creator = property(_getcreator)

    def _getnote(self):
        return self._note
        
    note = property(_getnote)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""The project card's ID """)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getarchived(self):
        return self._archived
        
    archived = property(_getarchived, doc="""Whether or not the card is archived """)

    def _getcolumn_name(self):
        return self._column_name
        
    column_name = property(_getcolumn_name)

    def _getproject_id(self):
        return self._project_id
        
    project_id = property(_getproject_id)

    def _getcontent_url(self):
        return self._content_url
        
    content_url = property(_getcontent_url)


    
##
##
##
class ProjectColumn(ResponseBase):
    """Project columns contain cards of work. """
    def __init__(self, updated_at:datetime, created_at:datetime, name:str, node_id:str, id:int, cards_url:str, project_url:str, url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._updated_at = updated_at
        self._created_at = created_at
        self._name = name
        self._node_id = node_id
        self._id = id
        self._cards_url = cards_url
        self._project_url = project_url
        self._url = url
        return
        
    

    
    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""Name of the project column """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""The unique identifier of the project column """)

    def _getcards_url(self):
        return self._cards_url
        
    cards_url = property(_getcards_url)

    def _getproject_url(self):
        return self._project_url
        
    project_url = property(_getproject_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class ProjectCollaboratorPermission(ResponseBase):
    """Project Collaborator Permission """
    def __init__(self, user:dict, permission:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._user = user
        self._permission = permission
        return
        
    

    
    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _getpermission(self):
        return self._permission
        
    permission = property(_getpermission)


    
##
##
##
class RateLimit(ResponseBase):
    def __init__(self, used:int, reset:int, remaining:int, limit:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._used = used
        self._reset = reset
        self._remaining = remaining
        self._limit = limit
        return
        
    

    
    def _getused(self):
        return self._used
        
    used = property(_getused)

    def _getreset(self):
        return self._reset
        
    reset = property(_getreset)

    def _getremaining(self):
        return self._remaining
        
    remaining = property(_getremaining)

    def _getlimit(self):
        return self._limit
        
    limit = property(_getlimit)


    
##
##
##
class Ratelimitoverview_resources(ResponseBase):
    def __init__(self, search:dict, core:dict, graphql:dict=None, source_import:dict=None, integration_manifest:dict=None, code_scanning_upload:dict=None, actions_runner_registration:dict=None, scim:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._search = search
        self._core = core
        self._graphql = graphql
        self._source_import = source_import
        self._integration_manifest = integration_manifest
        self._code_scanning_upload = code_scanning_upload
        self._actions_runner_registration = actions_runner_registration
        self._scim = scim
        return
        
    

    
    def _getsearch(self):
        return self._search and RateLimit(**self._search)
        
    search = property(_getsearch)

    def _getcore(self):
        return self._core and RateLimit(**self._core)
        
    core = property(_getcore)

    def _getgraphql(self):
        return self._graphql and RateLimit(**self._graphql)
        
    graphql = property(_getgraphql)

    def _getsource_import(self):
        return self._source_import and RateLimit(**self._source_import)
        
    source_import = property(_getsource_import)

    def _getintegration_manifest(self):
        return self._integration_manifest and RateLimit(**self._integration_manifest)
        
    integration_manifest = property(_getintegration_manifest)

    def _getcode_scanning_upload(self):
        return self._code_scanning_upload and RateLimit(**self._code_scanning_upload)
        
    code_scanning_upload = property(_getcode_scanning_upload)

    def _getactions_runner_registration(self):
        return self._actions_runner_registration and RateLimit(**self._actions_runner_registration)
        
    actions_runner_registration = property(_getactions_runner_registration)

    def _getscim(self):
        return self._scim and RateLimit(**self._scim)
        
    scim = property(_getscim)


    
##
##
##
class RateLimitOverview(ResponseBase):
    """Rate Limit Overview """
    def __init__(self, rate:dict, resources:dict, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._rate = rate
        self._resources = resources
        return
        
    

    
    def _getrate(self):
        return self._rate and RateLimit(**self._rate)
        
    rate = property(_getrate)

    def _getresources(self):
        return self._resources and Ratelimitoverview_resources(**self._resources)
        
    resources = property(_getresources)


    
##
##
##
class CodeOfConductSimple(ResponseBase):
    """Code of Conduct Simple """
    def __init__(self, html_url:str, name:str, key:str, url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._html_url = html_url
        self._name = name
        self._key = key
        self._url = url
        return
        
    

    
    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getkey(self):
        return self._key
        
    key = property(_getkey)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class Fullrepository_permissions(ResponseBase):
    def __init__(self, pull:bool, push:bool, admin:bool, maintain:bool=None, triage:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._pull = pull
        self._push = push
        self._admin = admin
        self._maintain = maintain
        self._triage = triage
        return
        
    

    
    def _getpull(self):
        return self._pull
        
    pull = property(_getpull)

    def _getpush(self):
        return self._push
        
    push = property(_getpush)

    def _getadmin(self):
        return self._admin
        
    admin = property(_getadmin)

    def _getmaintain(self):
        return self._maintain
        
    maintain = property(_getmaintain)

    def _gettriage(self):
        return self._triage
        
    triage = property(_gettriage)


    
##
##
##
class Fullrepository_security_and_analysis_advanced_security(ResponseBase):
    def __init__(self, status:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._status = status
        return
        
    

    
    def _getstatus(self):
        return self._status
        
    status = property(_getstatus)


    
##
##
##
class Fullrepository_security_and_analysis_secret_scanning(ResponseBase):
    def __init__(self, status:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._status = status
        return
        
    

    
    def _getstatus(self):
        return self._status
        
    status = property(_getstatus)


    
##
##
##
class Fullrepository_security_and_analysis(ResponseBase):
    def __init__(self, advanced_security:dict=None, secret_scanning:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._advanced_security = advanced_security
        self._secret_scanning = secret_scanning
        return
        
    

    
    def _getadvanced_security(self):
        return self._advanced_security and Fullrepository_security_and_analysis_advanced_security(**self._advanced_security)
        
    advanced_security = property(_getadvanced_security)

    def _getsecret_scanning(self):
        return self._secret_scanning and Fullrepository_security_and_analysis_secret_scanning(**self._secret_scanning)
        
    secret_scanning = property(_getsecret_scanning)


    
##
##
##
class FullRepository(ResponseBase):
    """Full Repository """
    def __init__(self, watchers:int, open_issues:int, forks:int, license:dict, network_count:int, subscribers_count:int, updated_at:datetime, created_at:datetime, pushed_at:datetime, disabled:bool, archived:bool, has_downloads:bool, has_pages:bool, has_wiki:bool, has_projects:bool, has_issues:bool, open_issues_count:int, default_branch:str, size:int, watchers_count:int, stargazers_count:int, forks_count:int, language:str, homepage:str, svn_url:str, hooks_url:str, mirror_url:str, clone_url:str, trees_url:str, teams_url:str, tags_url:str, subscription_url:str, subscribers_url:str, statuses_url:str, stargazers_url:str, ssh_url:str, releases_url:str, pulls_url:str, notifications_url:str, milestones_url:str, merges_url:str, languages_url:str, labels_url:str, keys_url:str, issues_url:str, issue_events_url:str, issue_comment_url:str, git_url:str, git_tags_url:str, git_refs_url:str, git_commits_url:str, forks_url:str, events_url:str, downloads_url:str, deployments_url:str, contributors_url:str, contents_url:str, compare_url:str, commits_url:str, comments_url:str, collaborators_url:str, branches_url:str, blobs_url:str, assignees_url:str, archive_url:str, url:str, fork:bool, description:str, html_url:str, private:bool, owner:dict, full_name:str, name:str, node_id:str, id:int, is_template:bool=None, topics:list=[], visibility:str=None, permissions:dict=None, allow_rebase_merge:bool=None, template_repository:dict=None, temp_clone_token:str=None, allow_squash_merge:bool=None, allow_auto_merge:bool=None, delete_branch_on_merge:bool=None, allow_merge_commit:bool=None, allow_forking:bool=None, organization:dict=None, parent:dict=None, source:dict=None, master_branch:str=None, anonymous_access_enabled:bool=True, code_of_conduct:dict=None, security_and_analysis:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._watchers = watchers
        self._open_issues = open_issues
        self._forks = forks
        self._license = license
        self._network_count = network_count
        self._subscribers_count = subscribers_count
        self._updated_at = updated_at
        self._created_at = created_at
        self._pushed_at = pushed_at
        self._disabled = disabled
        self._archived = archived
        self._has_downloads = has_downloads
        self._has_pages = has_pages
        self._has_wiki = has_wiki
        self._has_projects = has_projects
        self._has_issues = has_issues
        self._open_issues_count = open_issues_count
        self._default_branch = default_branch
        self._size = size
        self._watchers_count = watchers_count
        self._stargazers_count = stargazers_count
        self._forks_count = forks_count
        self._language = language
        self._homepage = homepage
        self._svn_url = svn_url
        self._hooks_url = hooks_url
        self._mirror_url = mirror_url
        self._clone_url = clone_url
        self._trees_url = trees_url
        self._teams_url = teams_url
        self._tags_url = tags_url
        self._subscription_url = subscription_url
        self._subscribers_url = subscribers_url
        self._statuses_url = statuses_url
        self._stargazers_url = stargazers_url
        self._ssh_url = ssh_url
        self._releases_url = releases_url
        self._pulls_url = pulls_url
        self._notifications_url = notifications_url
        self._milestones_url = milestones_url
        self._merges_url = merges_url
        self._languages_url = languages_url
        self._labels_url = labels_url
        self._keys_url = keys_url
        self._issues_url = issues_url
        self._issue_events_url = issue_events_url
        self._issue_comment_url = issue_comment_url
        self._git_url = git_url
        self._git_tags_url = git_tags_url
        self._git_refs_url = git_refs_url
        self._git_commits_url = git_commits_url
        self._forks_url = forks_url
        self._events_url = events_url
        self._downloads_url = downloads_url
        self._deployments_url = deployments_url
        self._contributors_url = contributors_url
        self._contents_url = contents_url
        self._compare_url = compare_url
        self._commits_url = commits_url
        self._comments_url = comments_url
        self._collaborators_url = collaborators_url
        self._branches_url = branches_url
        self._blobs_url = blobs_url
        self._assignees_url = assignees_url
        self._archive_url = archive_url
        self._url = url
        self._fork = fork
        self._description = description
        self._html_url = html_url
        self._private = private
        self._owner = owner
        self._full_name = full_name
        self._name = name
        self._node_id = node_id
        self._id = id
        self._is_template = is_template
        self._topics = topics
        self._visibility = visibility
        self._permissions = permissions
        self._allow_rebase_merge = allow_rebase_merge
        self._template_repository = template_repository
        self._temp_clone_token = temp_clone_token
        self._allow_squash_merge = allow_squash_merge
        self._allow_auto_merge = allow_auto_merge
        self._delete_branch_on_merge = delete_branch_on_merge
        self._allow_merge_commit = allow_merge_commit
        self._allow_forking = allow_forking
        self._organization = organization
        self._parent = parent
        self._source = source
        self._master_branch = master_branch
        self._anonymous_access_enabled = anonymous_access_enabled
        self._code_of_conduct = code_of_conduct
        self._security_and_analysis = security_and_analysis
        return
        
    

    
    def _getwatchers(self):
        return self._watchers
        
    watchers = property(_getwatchers)

    def _getopen_issues(self):
        return self._open_issues
        
    open_issues = property(_getopen_issues)

    def _getforks(self):
        return self._forks
        
    forks = property(_getforks)

    def _getlicense(self):
        return self._license and NullableLicenseSimple(**self._license)
        
    license = property(_getlicense)

    def _getnetwork_count(self):
        return self._network_count
        
    network_count = property(_getnetwork_count)

    def _getsubscribers_count(self):
        return self._subscribers_count
        
    subscribers_count = property(_getsubscribers_count)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getpushed_at(self):
        return self._pushed_at and datetime.datetime.fromisoformat(self._pushed_at[0:-1])
        
    pushed_at = property(_getpushed_at)

    def _getdisabled(self):
        return self._disabled
        
    disabled = property(_getdisabled, doc="""Returns whether or not this repository disabled. """)

    def _getarchived(self):
        return self._archived
        
    archived = property(_getarchived)

    def _gethas_downloads(self):
        return self._has_downloads
        
    has_downloads = property(_gethas_downloads)

    def _gethas_pages(self):
        return self._has_pages
        
    has_pages = property(_gethas_pages)

    def _gethas_wiki(self):
        return self._has_wiki
        
    has_wiki = property(_gethas_wiki)

    def _gethas_projects(self):
        return self._has_projects
        
    has_projects = property(_gethas_projects)

    def _gethas_issues(self):
        return self._has_issues
        
    has_issues = property(_gethas_issues)

    def _getopen_issues_count(self):
        return self._open_issues_count
        
    open_issues_count = property(_getopen_issues_count)

    def _getdefault_branch(self):
        return self._default_branch
        
    default_branch = property(_getdefault_branch)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _getwatchers_count(self):
        return self._watchers_count
        
    watchers_count = property(_getwatchers_count)

    def _getstargazers_count(self):
        return self._stargazers_count
        
    stargazers_count = property(_getstargazers_count)

    def _getforks_count(self):
        return self._forks_count
        
    forks_count = property(_getforks_count)

    def _getlanguage(self):
        return self._language
        
    language = property(_getlanguage)

    def _gethomepage(self):
        return self._homepage
        
    homepage = property(_gethomepage)

    def _getsvn_url(self):
        return self._svn_url
        
    svn_url = property(_getsvn_url)

    def _gethooks_url(self):
        return self._hooks_url
        
    hooks_url = property(_gethooks_url)

    def _getmirror_url(self):
        return self._mirror_url
        
    mirror_url = property(_getmirror_url)

    def _getclone_url(self):
        return self._clone_url
        
    clone_url = property(_getclone_url)

    def _gettrees_url(self):
        return self._trees_url
        
    trees_url = property(_gettrees_url)

    def _getteams_url(self):
        return self._teams_url
        
    teams_url = property(_getteams_url)

    def _gettags_url(self):
        return self._tags_url
        
    tags_url = property(_gettags_url)

    def _getsubscription_url(self):
        return self._subscription_url
        
    subscription_url = property(_getsubscription_url)

    def _getsubscribers_url(self):
        return self._subscribers_url
        
    subscribers_url = property(_getsubscribers_url)

    def _getstatuses_url(self):
        return self._statuses_url
        
    statuses_url = property(_getstatuses_url)

    def _getstargazers_url(self):
        return self._stargazers_url
        
    stargazers_url = property(_getstargazers_url)

    def _getssh_url(self):
        return self._ssh_url
        
    ssh_url = property(_getssh_url)

    def _getreleases_url(self):
        return self._releases_url
        
    releases_url = property(_getreleases_url)

    def _getpulls_url(self):
        return self._pulls_url
        
    pulls_url = property(_getpulls_url)

    def _getnotifications_url(self):
        return self._notifications_url
        
    notifications_url = property(_getnotifications_url)

    def _getmilestones_url(self):
        return self._milestones_url
        
    milestones_url = property(_getmilestones_url)

    def _getmerges_url(self):
        return self._merges_url
        
    merges_url = property(_getmerges_url)

    def _getlanguages_url(self):
        return self._languages_url
        
    languages_url = property(_getlanguages_url)

    def _getlabels_url(self):
        return self._labels_url
        
    labels_url = property(_getlabels_url)

    def _getkeys_url(self):
        return self._keys_url
        
    keys_url = property(_getkeys_url)

    def _getissues_url(self):
        return self._issues_url
        
    issues_url = property(_getissues_url)

    def _getissue_events_url(self):
        return self._issue_events_url
        
    issue_events_url = property(_getissue_events_url)

    def _getissue_comment_url(self):
        return self._issue_comment_url
        
    issue_comment_url = property(_getissue_comment_url)

    def _getgit_url(self):
        return self._git_url
        
    git_url = property(_getgit_url)

    def _getgit_tags_url(self):
        return self._git_tags_url
        
    git_tags_url = property(_getgit_tags_url)

    def _getgit_refs_url(self):
        return self._git_refs_url
        
    git_refs_url = property(_getgit_refs_url)

    def _getgit_commits_url(self):
        return self._git_commits_url
        
    git_commits_url = property(_getgit_commits_url)

    def _getforks_url(self):
        return self._forks_url
        
    forks_url = property(_getforks_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getdownloads_url(self):
        return self._downloads_url
        
    downloads_url = property(_getdownloads_url)

    def _getdeployments_url(self):
        return self._deployments_url
        
    deployments_url = property(_getdeployments_url)

    def _getcontributors_url(self):
        return self._contributors_url
        
    contributors_url = property(_getcontributors_url)

    def _getcontents_url(self):
        return self._contents_url
        
    contents_url = property(_getcontents_url)

    def _getcompare_url(self):
        return self._compare_url
        
    compare_url = property(_getcompare_url)

    def _getcommits_url(self):
        return self._commits_url
        
    commits_url = property(_getcommits_url)

    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _getcollaborators_url(self):
        return self._collaborators_url
        
    collaborators_url = property(_getcollaborators_url)

    def _getbranches_url(self):
        return self._branches_url
        
    branches_url = property(_getbranches_url)

    def _getblobs_url(self):
        return self._blobs_url
        
    blobs_url = property(_getblobs_url)

    def _getassignees_url(self):
        return self._assignees_url
        
    assignees_url = property(_getassignees_url)

    def _getarchive_url(self):
        return self._archive_url
        
    archive_url = property(_getarchive_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getfork(self):
        return self._fork
        
    fork = property(_getfork)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getprivate(self):
        return self._private
        
    private = property(_getprivate)

    def _getowner(self):
        return self._owner and SimpleUser(**self._owner)
        
    owner = property(_getowner)

    def _getfull_name(self):
        return self._full_name
        
    full_name = property(_getfull_name)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getis_template(self):
        return self._is_template
        
    is_template = property(_getis_template)

    def _gettopics(self):
        return self._topics and [ entry for entry in self._topics ]
        
    topics = property(_gettopics)

    def _getvisibility(self):
        return self._visibility
        
    visibility = property(_getvisibility, doc="""The repository visibility: public, private, or internal. """)

    def _getpermissions(self):
        return self._permissions and Fullrepository_permissions(**self._permissions)
        
    permissions = property(_getpermissions)

    def _getallow_rebase_merge(self):
        return self._allow_rebase_merge
        
    allow_rebase_merge = property(_getallow_rebase_merge)

    def _gettemplate_repository(self):
        return self._template_repository and NullableRepository(**self._template_repository)
        
    template_repository = property(_gettemplate_repository)

    def _gettemp_clone_token(self):
        return self._temp_clone_token
        
    temp_clone_token = property(_gettemp_clone_token)

    def _getallow_squash_merge(self):
        return self._allow_squash_merge
        
    allow_squash_merge = property(_getallow_squash_merge)

    def _getallow_auto_merge(self):
        return self._allow_auto_merge
        
    allow_auto_merge = property(_getallow_auto_merge)

    def _getdelete_branch_on_merge(self):
        return self._delete_branch_on_merge
        
    delete_branch_on_merge = property(_getdelete_branch_on_merge)

    def _getallow_merge_commit(self):
        return self._allow_merge_commit
        
    allow_merge_commit = property(_getallow_merge_commit)

    def _getallow_forking(self):
        return self._allow_forking
        
    allow_forking = property(_getallow_forking)

    def _getorganization(self):
        return self._organization and NullableSimpleUser(**self._organization)
        
    organization = property(_getorganization)

    def _getparent(self):
        return self._parent and Repository(**self._parent)
        
    parent = property(_getparent)

    def _getsource(self):
        return self._source and Repository(**self._source)
        
    source = property(_getsource)

    def _getmaster_branch(self):
        return self._master_branch
        
    master_branch = property(_getmaster_branch)

    def _getanonymous_access_enabled(self):
        return self._anonymous_access_enabled
        
    anonymous_access_enabled = property(_getanonymous_access_enabled, doc="""Whether anonymous git access is allowed. """)

    def _getcode_of_conduct(self):
        return self._code_of_conduct and CodeOfConductSimple(**self._code_of_conduct)
        
    code_of_conduct = property(_getcode_of_conduct)

    def _getsecurity_and_analysis(self):
        return self._security_and_analysis and Fullrepository_security_and_analysis(**self._security_and_analysis)
        
    security_and_analysis = property(_getsecurity_and_analysis)


    
##
##
##
class Artifact(ResponseBase):
    """An artifact """
    def __init__(self, updated_at:datetime, expires_at:datetime, created_at:datetime, expired:bool, archive_download_url:str, url:str, size_in_bytes:int, name:str, node_id:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._updated_at = updated_at
        self._expires_at = expires_at
        self._created_at = created_at
        self._expired = expired
        self._archive_download_url = archive_download_url
        self._url = url
        self._size_in_bytes = size_in_bytes
        self._name = name
        self._node_id = node_id
        self._id = id
        return
        
    

    
    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getexpires_at(self):
        return self._expires_at and datetime.datetime.fromisoformat(self._expires_at[0:-1])
        
    expires_at = property(_getexpires_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getexpired(self):
        return self._expired
        
    expired = property(_getexpired, doc="""Whether or not the artifact has expired. """)

    def _getarchive_download_url(self):
        return self._archive_download_url
        
    archive_download_url = property(_getarchive_download_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsize_in_bytes(self):
        return self._size_in_bytes
        
    size_in_bytes = property(_getsize_in_bytes, doc="""The size in bytes of the artifact. """)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the artifact. """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class Job_steps(ResponseBase):
    def __init__(self, number:int, name:str, conclusion:str, status:str, started_at:datetime=None, completed_at:datetime=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._number = number
        self._name = name
        self._conclusion = conclusion
        self._status = status
        self._started_at = started_at
        self._completed_at = completed_at
        return
        
    

    
    def _getnumber(self):
        return self._number
        
    number = property(_getnumber)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the job. """)

    def _getconclusion(self):
        return self._conclusion
        
    conclusion = property(_getconclusion, doc="""The outcome of the job. """)

    def _getstatus(self):
        return self._status
        
    status = property(_getstatus, doc="""The phase of the lifecycle that the job is currently in. """)

    def _getstarted_at(self):
        return self._started_at and datetime.datetime.fromisoformat(self._started_at[0:-1])
        
    started_at = property(_getstarted_at, doc="""The time that the step started, in ISO 8601 format. """)

    def _getcompleted_at(self):
        return self._completed_at and datetime.datetime.fromisoformat(self._completed_at[0:-1])
        
    completed_at = property(_getcompleted_at, doc="""The time that the job finished, in ISO 8601 format. """)


    
##
##
##
class Job(ResponseBase):
    """Information of a job execution in a workflow run """
    def __init__(self, runner_group_name:str, runner_group_id:int, runner_name:str, runner_id:int, labels:list, check_run_url:str, name:str, completed_at:datetime, started_at:datetime, conclusion:str, status:str, html_url:str, url:str, head_sha:str, node_id:str, run_url:str, run_id:int, id:int, run_attempt:int=None, steps:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._runner_group_name = runner_group_name
        self._runner_group_id = runner_group_id
        self._runner_name = runner_name
        self._runner_id = runner_id
        self._labels = labels
        self._check_run_url = check_run_url
        self._name = name
        self._completed_at = completed_at
        self._started_at = started_at
        self._conclusion = conclusion
        self._status = status
        self._html_url = html_url
        self._url = url
        self._head_sha = head_sha
        self._node_id = node_id
        self._run_url = run_url
        self._run_id = run_id
        self._id = id
        self._run_attempt = run_attempt
        self._steps = steps
        return
        
    

    
    def _getrunner_group_name(self):
        return self._runner_group_name
        
    runner_group_name = property(_getrunner_group_name, doc="""The name of the runner group to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.) """)

    def _getrunner_group_id(self):
        return self._runner_group_id
        
    runner_group_id = property(_getrunner_group_id, doc="""The ID of the runner group to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.) """)

    def _getrunner_name(self):
        return self._runner_name
        
    runner_name = property(_getrunner_name, doc="""The name of the runner to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.) """)

    def _getrunner_id(self):
        return self._runner_id
        
    runner_id = property(_getrunner_id, doc="""The ID of the runner to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.) """)

    def _getlabels(self):
        return self._labels and [ entry for entry in self._labels ]
        
    labels = property(_getlabels, doc="""Labels for the workflow job. Specified by the "runs_on" attribute in the action's workflow file. """)

    def _getcheck_run_url(self):
        return self._check_run_url
        
    check_run_url = property(_getcheck_run_url)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the job. """)

    def _getcompleted_at(self):
        return self._completed_at and datetime.datetime.fromisoformat(self._completed_at[0:-1])
        
    completed_at = property(_getcompleted_at, doc="""The time that the job finished, in ISO 8601 format. """)

    def _getstarted_at(self):
        return self._started_at and datetime.datetime.fromisoformat(self._started_at[0:-1])
        
    started_at = property(_getstarted_at, doc="""The time that the job started, in ISO 8601 format. """)

    def _getconclusion(self):
        return self._conclusion
        
    conclusion = property(_getconclusion, doc="""The outcome of the job. """)

    def _getstatus(self):
        return self._status
        
    status = property(_getstatus, doc="""The phase of the lifecycle that the job is currently in. """)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gethead_sha(self):
        return self._head_sha
        
    head_sha = property(_gethead_sha, doc="""The SHA of the commit that is being run. """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getrun_url(self):
        return self._run_url
        
    run_url = property(_getrun_url)

    def _getrun_id(self):
        return self._run_id
        
    run_id = property(_getrun_id, doc="""The id of the associated workflow run. """)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""The id of the job. """)

    def _getrun_attempt(self):
        return self._run_attempt
        
    run_attempt = property(_getrun_attempt, doc="""Attempt number of the associated workflow run, 1 for first attempt and higher if the workflow was re-run. """)

    def _getsteps(self):
        return self._steps and [ entry and Job_steps(**entry) for entry in self._steps ]
        
    steps = property(_getsteps, doc="""Steps in this job. """)


    
##
##
##
class ActionsRepositoryPermissions(ResponseBase):
    def __init__(self, enabled:bool, allowed_actions:str=None, selected_actions_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        self._allowed_actions = allowed_actions
        self._selected_actions_url = selected_actions_url
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)

    def _getallowed_actions(self):
        return self._allowed_actions
        
    allowed_actions = property(_getallowed_actions)

    def _getselected_actions_url(self):
        return self._selected_actions_url
        
    selected_actions_url = property(_getselected_actions_url)


    
##
##
##
class Pullrequestminimal_head_repo(ResponseBase):
    def __init__(self, name:str, url:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._name = name
        self._url = url
        self._id = id
        return
        
    

    
    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class Pullrequestminimal_head(ResponseBase):
    def __init__(self, repo:dict, sha:str, ref:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._repo = repo
        self._sha = sha
        self._ref = ref
        return
        
    

    
    def _getrepo(self):
        return self._repo and Pullrequestminimal_head_repo(**self._repo)
        
    repo = property(_getrepo)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getref(self):
        return self._ref
        
    ref = property(_getref)


    
##
##
##
class Pullrequestminimal_base_repo(ResponseBase):
    def __init__(self, name:str, url:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._name = name
        self._url = url
        self._id = id
        return
        
    

    
    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class Pullrequestminimal_base(ResponseBase):
    def __init__(self, repo:dict, sha:str, ref:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._repo = repo
        self._sha = sha
        self._ref = ref
        return
        
    

    
    def _getrepo(self):
        return self._repo and Pullrequestminimal_base_repo(**self._repo)
        
    repo = property(_getrepo)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getref(self):
        return self._ref
        
    ref = property(_getref)


    
##
##
##
class PullRequestMinimal(ResponseBase):
    def __init__(self, base:dict, head:dict, url:str, number:int, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._base = base
        self._head = head
        self._url = url
        self._number = number
        self._id = id
        return
        
    

    
    def _getbase(self):
        return self._base and Pullrequestminimal_base(**self._base)
        
    base = property(_getbase)

    def _gethead(self):
        return self._head and Pullrequestminimal_head(**self._head)
        
    head = property(_gethead)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnumber(self):
        return self._number
        
    number = property(_getnumber)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class Nullablesimplecommit_author(ResponseBase):
    def __init__(self, email:str, name:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._email = email
        self._name = name
        return
        
    

    
    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _getname(self):
        return self._name
        
    name = property(_getname)


    
##
##
##
class Nullablesimplecommit_committer(ResponseBase):
    def __init__(self, email:str, name:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._email = email
        self._name = name
        return
        
    

    
    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _getname(self):
        return self._name
        
    name = property(_getname)


    
##
##
##
class NullableSimpleCommit(ResponseBase):
    """Simple Commit """
    def __init__(self, committer:dict, author:dict, timestamp:datetime, message:str, tree_id:str, id:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._committer = committer
        self._author = author
        self._timestamp = timestamp
        self._message = message
        self._tree_id = tree_id
        self._id = id
        return
        
    

    
    def _getcommitter(self):
        return self._committer and Nullablesimplecommit_committer(**self._committer)
        
    committer = property(_getcommitter)

    def _getauthor(self):
        return self._author and Nullablesimplecommit_author(**self._author)
        
    author = property(_getauthor)

    def _gettimestamp(self):
        return self._timestamp and datetime.datetime.fromisoformat(self._timestamp[0:-1])
        
    timestamp = property(_gettimestamp)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _gettree_id(self):
        return self._tree_id
        
    tree_id = property(_gettree_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class WorkflowRun(ResponseBase):
    """An invocation of a workflow """
    def __init__(self, head_repository:dict, repository:dict, head_commit:dict, workflow_url:str, rerun_url:str, cancel_url:str, artifacts_url:str, check_suite_url:str, logs_url:str, jobs_url:str, updated_at:datetime, created_at:datetime, pull_requests:list, html_url:str, url:str, workflow_id:int, conclusion:str, status:str, event:str, run_number:int, head_sha:str, head_branch:str, node_id:str, id:int, name:str=None, check_suite_id:int=None, check_suite_node_id:str=None, run_attempt:int=None, run_started_at:datetime=None, previous_attempt_url:str=None, head_repository_id:int=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._head_repository = head_repository
        self._repository = repository
        self._head_commit = head_commit
        self._workflow_url = workflow_url
        self._rerun_url = rerun_url
        self._cancel_url = cancel_url
        self._artifacts_url = artifacts_url
        self._check_suite_url = check_suite_url
        self._logs_url = logs_url
        self._jobs_url = jobs_url
        self._updated_at = updated_at
        self._created_at = created_at
        self._pull_requests = pull_requests
        self._html_url = html_url
        self._url = url
        self._workflow_id = workflow_id
        self._conclusion = conclusion
        self._status = status
        self._event = event
        self._run_number = run_number
        self._head_sha = head_sha
        self._head_branch = head_branch
        self._node_id = node_id
        self._id = id
        self._name = name
        self._check_suite_id = check_suite_id
        self._check_suite_node_id = check_suite_node_id
        self._run_attempt = run_attempt
        self._run_started_at = run_started_at
        self._previous_attempt_url = previous_attempt_url
        self._head_repository_id = head_repository_id
        return
        
    

    
    def _gethead_repository(self):
        return self._head_repository and MinimalRepository(**self._head_repository)
        
    head_repository = property(_gethead_repository)

    def _getrepository(self):
        return self._repository and MinimalRepository(**self._repository)
        
    repository = property(_getrepository)

    def _gethead_commit(self):
        return self._head_commit and NullableSimpleCommit(**self._head_commit)
        
    head_commit = property(_gethead_commit)

    def _getworkflow_url(self):
        return self._workflow_url
        
    workflow_url = property(_getworkflow_url, doc="""The URL to the workflow. """)

    def _getrerun_url(self):
        return self._rerun_url
        
    rerun_url = property(_getrerun_url, doc="""The URL to rerun the workflow run. """)

    def _getcancel_url(self):
        return self._cancel_url
        
    cancel_url = property(_getcancel_url, doc="""The URL to cancel the workflow run. """)

    def _getartifacts_url(self):
        return self._artifacts_url
        
    artifacts_url = property(_getartifacts_url, doc="""The URL to the artifacts for the workflow run. """)

    def _getcheck_suite_url(self):
        return self._check_suite_url
        
    check_suite_url = property(_getcheck_suite_url, doc="""The URL to the associated check suite. """)

    def _getlogs_url(self):
        return self._logs_url
        
    logs_url = property(_getlogs_url, doc="""The URL to download the logs for the workflow run. """)

    def _getjobs_url(self):
        return self._jobs_url
        
    jobs_url = property(_getjobs_url, doc="""The URL to the jobs for the workflow run. """)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getpull_requests(self):
        return self._pull_requests and [ entry and PullRequestMinimal(**entry) for entry in self._pull_requests ]
        
    pull_requests = property(_getpull_requests)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl, doc="""The URL to the workflow run. """)

    def _getworkflow_id(self):
        return self._workflow_id
        
    workflow_id = property(_getworkflow_id, doc="""The ID of the parent workflow. """)

    def _getconclusion(self):
        return self._conclusion
        
    conclusion = property(_getconclusion)

    def _getstatus(self):
        return self._status
        
    status = property(_getstatus)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getrun_number(self):
        return self._run_number
        
    run_number = property(_getrun_number, doc="""The auto incrementing run number for the workflow run. """)

    def _gethead_sha(self):
        return self._head_sha
        
    head_sha = property(_gethead_sha, doc="""The SHA of the head commit that points to the version of the worflow being run. """)

    def _gethead_branch(self):
        return self._head_branch
        
    head_branch = property(_gethead_branch)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""The ID of the workflow run. """)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the workflow run. """)

    def _getcheck_suite_id(self):
        return self._check_suite_id
        
    check_suite_id = property(_getcheck_suite_id, doc="""The ID of the associated check suite. """)

    def _getcheck_suite_node_id(self):
        return self._check_suite_node_id
        
    check_suite_node_id = property(_getcheck_suite_node_id, doc="""The node ID of the associated check suite. """)

    def _getrun_attempt(self):
        return self._run_attempt
        
    run_attempt = property(_getrun_attempt, doc="""Attempt number of the run, 1 for first attempt and higher if the workflow was re-run. """)

    def _getrun_started_at(self):
        return self._run_started_at and datetime.datetime.fromisoformat(self._run_started_at[0:-1])
        
    run_started_at = property(_getrun_started_at, doc="""The start time of the latest run. Resets on re-run. """)

    def _getprevious_attempt_url(self):
        return self._previous_attempt_url
        
    previous_attempt_url = property(_getprevious_attempt_url, doc="""The URL to the previous attempted run of this workflow, if one exists. """)

    def _gethead_repository_id(self):
        return self._head_repository_id
        
    head_repository_id = property(_gethead_repository_id)


    
##
##
##
class Environmentapprovals_environments(ResponseBase):
    def __init__(self, id:int=None, node_id:str=None, name:str=None, url:str=None, html_url:str=None, created_at:datetime=None, updated_at:datetime=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._node_id = node_id
        self._name = name
        self._url = url
        self._html_url = html_url
        self._created_at = created_at
        self._updated_at = updated_at
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""The id of the environment. """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the environment. """)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at, doc="""The time that the environment was created, in ISO 8601 format. """)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at, doc="""The time that the environment was last updated, in ISO 8601 format. """)


    
##
##
##
class EnvironmentApprovals(ResponseBase):
    """An entry in the reviews log for environment deployments """
    def __init__(self, comment:str, user:dict, state:str, environments:list, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._comment = comment
        self._user = user
        self._state = state
        self._environments = environments
        return
        
    

    
    def _getcomment(self):
        return self._comment
        
    comment = property(_getcomment, doc="""The comment submitted with the deployment review """)

    def _getuser(self):
        return self._user and SimpleUser(**self._user)
        
    user = property(_getuser)

    def _getstate(self):
        return self._state
        
    state = property(_getstate, doc="""Whether deployment to the environment(s) was approved or rejected """)

    def _getenvironments(self):
        return self._environments and [ entry and Environmentapprovals_environments(**entry) for entry in self._environments ]
        
    environments = property(_getenvironments, doc="""The list of environments that were approved or rejected """)


    
##
##
##
class Pendingdeployment_environment(ResponseBase):
    def __init__(self, id:int=None, node_id:str=None, name:str=None, url:str=None, html_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._node_id = node_id
        self._name = name
        self._url = url
        self._html_url = html_url
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""The id of the environment. """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the environment. """)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)


    
##
##
##
class Pendingdeployment_reviewers(ResponseBase):
    def __init__(self, type:str=None, reviewer=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._type = type
        self._reviewer = reviewer
        return
        
    

    
    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getreviewer(self):
        return self._reviewer
        
    reviewer = property(_getreviewer)


    
##
##
##
class PendingDeployment(ResponseBase):
    """Details of a deployment that is waiting for protection rules to pass """
    def __init__(self, reviewers:list, current_user_can_approve:bool, wait_timer_started_at:datetime, wait_timer:int, environment:dict, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._reviewers = reviewers
        self._current_user_can_approve = current_user_can_approve
        self._wait_timer_started_at = wait_timer_started_at
        self._wait_timer = wait_timer
        self._environment = environment
        return
        
    

    
    def _getreviewers(self):
        return self._reviewers and [ entry and Pendingdeployment_reviewers(**entry) for entry in self._reviewers ]
        
    reviewers = property(_getreviewers, doc="""The people or teams that may approve jobs that reference the environment. You can list up to six users or teams as reviewers. The reviewers must have at least read access to the repository. Only one of the required reviewers needs to approve the job for it to proceed. """)

    def _getcurrent_user_can_approve(self):
        return self._current_user_can_approve
        
    current_user_can_approve = property(_getcurrent_user_can_approve, doc="""Whether the currently authenticated user can approve the deployment """)

    def _getwait_timer_started_at(self):
        return self._wait_timer_started_at and datetime.datetime.fromisoformat(self._wait_timer_started_at[0:-1])
        
    wait_timer_started_at = property(_getwait_timer_started_at, doc="""The time that the wait timer began. """)

    def _getwait_timer(self):
        return self._wait_timer
        
    wait_timer = property(_getwait_timer, doc="""The set duration of the wait timer """)

    def _getenvironment(self):
        return self._environment and Pendingdeployment_environment(**self._environment)
        
    environment = property(_getenvironment)


    
##
##
##
class Deployment(ResponseBase):
    """A request for a specific ref(branch,sha,tag) to be deployed """
    def __init__(self, repository_url:str, statuses_url:str, updated_at:datetime, created_at:datetime, creator:dict, description:str, environment:str, payload, task:str, ref:str, sha:str, node_id:str, id:int, url:str, original_environment:str=None, transient_environment:bool=None, production_environment:bool=None, performed_via_github_app:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._repository_url = repository_url
        self._statuses_url = statuses_url
        self._updated_at = updated_at
        self._created_at = created_at
        self._creator = creator
        self._description = description
        self._environment = environment
        self._payload = payload
        self._task = task
        self._ref = ref
        self._sha = sha
        self._node_id = node_id
        self._id = id
        self._url = url
        self._original_environment = original_environment
        self._transient_environment = transient_environment
        self._production_environment = production_environment
        self._performed_via_github_app = performed_via_github_app
        return
        
    

    
    def _getrepository_url(self):
        return self._repository_url
        
    repository_url = property(_getrepository_url)

    def _getstatuses_url(self):
        return self._statuses_url
        
    statuses_url = property(_getstatuses_url)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getcreator(self):
        return self._creator and NullableSimpleUser(**self._creator)
        
    creator = property(_getcreator)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getenvironment(self):
        return self._environment
        
    environment = property(_getenvironment, doc="""Name for the target deployment environment. """)

    def _getpayload(self):
        return self._payload
        
    payload = property(_getpayload)

    def _gettask(self):
        return self._task
        
    task = property(_gettask, doc="""Parameter to specify a task to execute """)

    def _getref(self):
        return self._ref
        
    ref = property(_getref, doc="""The ref to deploy. This can be a branch, tag, or sha. """)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the deployment """)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getoriginal_environment(self):
        return self._original_environment
        
    original_environment = property(_getoriginal_environment)

    def _gettransient_environment(self):
        return self._transient_environment
        
    transient_environment = property(_gettransient_environment, doc="""Specifies if the given environment is will no longer exist at some point in the future. Default: false. """)

    def _getproduction_environment(self):
        return self._production_environment
        
    production_environment = property(_getproduction_environment, doc="""Specifies if the given environment is one that end-users directly interact with. Default: false. """)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)


    
##
##
##
class ActionsSecret(ResponseBase):
    """Set secrets for GitHub Actions. """
    def __init__(self, updated_at:datetime, created_at:datetime, name:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._updated_at = updated_at
        self._created_at = created_at
        self._name = name
        return
        
    

    
    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the secret. """)


    
##
##
##
class Workflow(ResponseBase):
    """A GitHub Actions workflow """
    def __init__(self, badge_url:str, html_url:str, url:str, updated_at:datetime, created_at:datetime, state:str, path:str, name:str, node_id:str, id:int, deleted_at:datetime=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._badge_url = badge_url
        self._html_url = html_url
        self._url = url
        self._updated_at = updated_at
        self._created_at = created_at
        self._state = state
        self._path = path
        self._name = name
        self._node_id = node_id
        self._id = id
        self._deleted_at = deleted_at
        return
        
    

    
    def _getbadge_url(self):
        return self._badge_url
        
    badge_url = property(_getbadge_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)

    def _getpath(self):
        return self._path
        
    path = property(_getpath)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getdeleted_at(self):
        return self._deleted_at and datetime.datetime.fromisoformat(self._deleted_at[0:-1])
        
    deleted_at = property(_getdeleted_at)


    
##
##
##
class AutolinkReference(ResponseBase):
    """An autolink reference. """
    def __init__(self, url_template:str, key_prefix:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url_template = url_template
        self._key_prefix = key_prefix
        self._id = id
        return
        
    

    
    def _geturl_template(self):
        return self._url_template
        
    url_template = property(_geturl_template, doc="""A template for the target URL that is generated if a key was found. """)

    def _getkey_prefix(self):
        return self._key_prefix
        
    key_prefix = property(_getkey_prefix, doc="""The prefix of a key that is linkified. """)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class ProtectedBranchRequiredStatusCheck(ResponseBase):
    """Protected Branch Required Status Check """
    def __init__(self, contexts:list, url:str=None, enforcement_level:str=None, contexts_url:str=None, strict:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._contexts = contexts
        self._url = url
        self._enforcement_level = enforcement_level
        self._contexts_url = contexts_url
        self._strict = strict
        return
        
    

    
    def _getcontexts(self):
        return self._contexts and [ entry for entry in self._contexts ]
        
    contexts = property(_getcontexts)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getenforcement_level(self):
        return self._enforcement_level
        
    enforcement_level = property(_getenforcement_level)

    def _getcontexts_url(self):
        return self._contexts_url
        
    contexts_url = property(_getcontexts_url)

    def _getstrict(self):
        return self._strict
        
    strict = property(_getstrict)


    
##
##
##
class ProtectedBranchAdminEnforced(ResponseBase):
    """Protected Branch Admin Enforced """
    def __init__(self, enabled:bool, url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        self._url = url
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class Protectedbranchpullrequestreview_dismissal_restrictions(ResponseBase):
    def __init__(self, users:list=[], teams:list=[], url:str=None, users_url:str=None, teams_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._users = users
        self._teams = teams
        self._url = url
        self._users_url = users_url
        self._teams_url = teams_url
        return
        
    

    
    def _getusers(self):
        return self._users and [ entry and SimpleUser(**entry) for entry in self._users ]
        
    users = property(_getusers, doc="""The list of users with review dismissal access. """)

    def _getteams(self):
        return self._teams and [ entry and Team(**entry) for entry in self._teams ]
        
    teams = property(_getteams, doc="""The list of teams with review dismissal access. """)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getusers_url(self):
        return self._users_url
        
    users_url = property(_getusers_url)

    def _getteams_url(self):
        return self._teams_url
        
    teams_url = property(_getteams_url)


    
##
##
##
class ProtectedBranchPullRequestReview(ResponseBase):
    """Protected Branch Pull Request Review """
    def __init__(self, require_code_owner_reviews:bool, dismiss_stale_reviews:bool, url:str=None, dismissal_restrictions:dict=None, required_approving_review_count:int=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._require_code_owner_reviews = require_code_owner_reviews
        self._dismiss_stale_reviews = dismiss_stale_reviews
        self._url = url
        self._dismissal_restrictions = dismissal_restrictions
        self._required_approving_review_count = required_approving_review_count
        return
        
    

    
    def _getrequire_code_owner_reviews(self):
        return self._require_code_owner_reviews
        
    require_code_owner_reviews = property(_getrequire_code_owner_reviews)

    def _getdismiss_stale_reviews(self):
        return self._dismiss_stale_reviews
        
    dismiss_stale_reviews = property(_getdismiss_stale_reviews)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getdismissal_restrictions(self):
        return self._dismissal_restrictions and Protectedbranchpullrequestreview_dismissal_restrictions(**self._dismissal_restrictions)
        
    dismissal_restrictions = property(_getdismissal_restrictions)

    def _getrequired_approving_review_count(self):
        return self._required_approving_review_count
        
    required_approving_review_count = property(_getrequired_approving_review_count)


    
##
##
##
class Branchrestrictionpolicy_users(ResponseBase):
    def __init__(self, login:str=None, id:int=None, node_id:str=None, avatar_url:str=None, gravatar_id:str=None, url:str=None, html_url:str=None, followers_url:str=None, following_url:str=None, gists_url:str=None, starred_url:str=None, subscriptions_url:str=None, organizations_url:str=None, repos_url:str=None, events_url:str=None, received_events_url:str=None, type:str=None, site_admin:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._login = login
        self._id = id
        self._node_id = node_id
        self._avatar_url = avatar_url
        self._gravatar_id = gravatar_id
        self._url = url
        self._html_url = html_url
        self._followers_url = followers_url
        self._following_url = following_url
        self._gists_url = gists_url
        self._starred_url = starred_url
        self._subscriptions_url = subscriptions_url
        self._organizations_url = organizations_url
        self._repos_url = repos_url
        self._events_url = events_url
        self._received_events_url = received_events_url
        self._type = type
        self._site_admin = site_admin
        return
        
    

    
    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)

    def _getgravatar_id(self):
        return self._gravatar_id
        
    gravatar_id = property(_getgravatar_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getfollowers_url(self):
        return self._followers_url
        
    followers_url = property(_getfollowers_url)

    def _getfollowing_url(self):
        return self._following_url
        
    following_url = property(_getfollowing_url)

    def _getgists_url(self):
        return self._gists_url
        
    gists_url = property(_getgists_url)

    def _getstarred_url(self):
        return self._starred_url
        
    starred_url = property(_getstarred_url)

    def _getsubscriptions_url(self):
        return self._subscriptions_url
        
    subscriptions_url = property(_getsubscriptions_url)

    def _getorganizations_url(self):
        return self._organizations_url
        
    organizations_url = property(_getorganizations_url)

    def _getrepos_url(self):
        return self._repos_url
        
    repos_url = property(_getrepos_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getreceived_events_url(self):
        return self._received_events_url
        
    received_events_url = property(_getreceived_events_url)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getsite_admin(self):
        return self._site_admin
        
    site_admin = property(_getsite_admin)


    
##
##
##
class Branchrestrictionpolicy_teams(ResponseBase):
    def __init__(self, id:int=None, node_id:str=None, url:str=None, html_url:str=None, name:str=None, slug:str=None, description:str=None, privacy:str=None, permission:str=None, members_url:str=None, repositories_url:str=None, parent:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._node_id = node_id
        self._url = url
        self._html_url = html_url
        self._name = name
        self._slug = slug
        self._description = description
        self._privacy = privacy
        self._permission = permission
        self._members_url = members_url
        self._repositories_url = repositories_url
        self._parent = parent
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getslug(self):
        return self._slug
        
    slug = property(_getslug)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getprivacy(self):
        return self._privacy
        
    privacy = property(_getprivacy)

    def _getpermission(self):
        return self._permission
        
    permission = property(_getpermission)

    def _getmembers_url(self):
        return self._members_url
        
    members_url = property(_getmembers_url)

    def _getrepositories_url(self):
        return self._repositories_url
        
    repositories_url = property(_getrepositories_url)

    def _getparent(self):
        return self._parent
        
    parent = property(_getparent)


    
##
##
##
class Branchrestrictionpolicy_apps_owner(ResponseBase):
    def __init__(self, login:str=None, id:int=None, node_id:str=None, url:str=None, repos_url:str=None, events_url:str=None, hooks_url:str=None, issues_url:str=None, members_url:str=None, public_members_url:str=None, avatar_url:str=None, description:str=None, gravatar_id:str=None, html_url:str=None, followers_url:str=None, following_url:str=None, gists_url:str=None, starred_url:str=None, subscriptions_url:str=None, organizations_url:str=None, received_events_url:str=None, type:str=None, site_admin:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._login = login
        self._id = id
        self._node_id = node_id
        self._url = url
        self._repos_url = repos_url
        self._events_url = events_url
        self._hooks_url = hooks_url
        self._issues_url = issues_url
        self._members_url = members_url
        self._public_members_url = public_members_url
        self._avatar_url = avatar_url
        self._description = description
        self._gravatar_id = gravatar_id
        self._html_url = html_url
        self._followers_url = followers_url
        self._following_url = following_url
        self._gists_url = gists_url
        self._starred_url = starred_url
        self._subscriptions_url = subscriptions_url
        self._organizations_url = organizations_url
        self._received_events_url = received_events_url
        self._type = type
        self._site_admin = site_admin
        return
        
    

    
    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getrepos_url(self):
        return self._repos_url
        
    repos_url = property(_getrepos_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _gethooks_url(self):
        return self._hooks_url
        
    hooks_url = property(_gethooks_url)

    def _getissues_url(self):
        return self._issues_url
        
    issues_url = property(_getissues_url)

    def _getmembers_url(self):
        return self._members_url
        
    members_url = property(_getmembers_url)

    def _getpublic_members_url(self):
        return self._public_members_url
        
    public_members_url = property(_getpublic_members_url)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getgravatar_id(self):
        return self._gravatar_id
        
    gravatar_id = property(_getgravatar_id)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getfollowers_url(self):
        return self._followers_url
        
    followers_url = property(_getfollowers_url)

    def _getfollowing_url(self):
        return self._following_url
        
    following_url = property(_getfollowing_url)

    def _getgists_url(self):
        return self._gists_url
        
    gists_url = property(_getgists_url)

    def _getstarred_url(self):
        return self._starred_url
        
    starred_url = property(_getstarred_url)

    def _getsubscriptions_url(self):
        return self._subscriptions_url
        
    subscriptions_url = property(_getsubscriptions_url)

    def _getorganizations_url(self):
        return self._organizations_url
        
    organizations_url = property(_getorganizations_url)

    def _getreceived_events_url(self):
        return self._received_events_url
        
    received_events_url = property(_getreceived_events_url)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getsite_admin(self):
        return self._site_admin
        
    site_admin = property(_getsite_admin)


    
##
##
##
class Branchrestrictionpolicy_apps_permissions(ResponseBase):
    def __init__(self, metadata:str=None, contents:str=None, issues:str=None, single_file:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._metadata = metadata
        self._contents = contents
        self._issues = issues
        self._single_file = single_file
        return
        
    

    
    def _getmetadata(self):
        return self._metadata
        
    metadata = property(_getmetadata)

    def _getcontents(self):
        return self._contents
        
    contents = property(_getcontents)

    def _getissues(self):
        return self._issues
        
    issues = property(_getissues)

    def _getsingle_file(self):
        return self._single_file
        
    single_file = property(_getsingle_file)


    
##
##
##
class Branchrestrictionpolicy_apps(ResponseBase):
    def __init__(self, id:int=None, slug:str=None, node_id:str=None, owner:dict=None, name:str=None, description:str=None, external_url:str=None, html_url:str=None, created_at:str=None, updated_at:str=None, permissions:dict=None, events:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._slug = slug
        self._node_id = node_id
        self._owner = owner
        self._name = name
        self._description = description
        self._external_url = external_url
        self._html_url = html_url
        self._created_at = created_at
        self._updated_at = updated_at
        self._permissions = permissions
        self._events = events
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getslug(self):
        return self._slug
        
    slug = property(_getslug)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getowner(self):
        return self._owner and Branchrestrictionpolicy_apps_owner(**self._owner)
        
    owner = property(_getowner)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getexternal_url(self):
        return self._external_url
        
    external_url = property(_getexternal_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getupdated_at(self):
        return self._updated_at
        
    updated_at = property(_getupdated_at)

    def _getpermissions(self):
        return self._permissions and Branchrestrictionpolicy_apps_permissions(**self._permissions)
        
    permissions = property(_getpermissions)

    def _getevents(self):
        return self._events and [ entry for entry in self._events ]
        
    events = property(_getevents)


    
##
##
##
class BranchRestrictionPolicy(ResponseBase):
    """Branch Restriction Policy """
    def __init__(self, apps:list, teams:list, users:list, apps_url:str, teams_url:str, users_url:str, url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._apps = apps
        self._teams = teams
        self._users = users
        self._apps_url = apps_url
        self._teams_url = teams_url
        self._users_url = users_url
        self._url = url
        return
        
    

    
    def _getapps(self):
        return self._apps and [ entry and Branchrestrictionpolicy_apps(**entry) for entry in self._apps ]
        
    apps = property(_getapps)

    def _getteams(self):
        return self._teams and [ entry and Branchrestrictionpolicy_teams(**entry) for entry in self._teams ]
        
    teams = property(_getteams)

    def _getusers(self):
        return self._users and [ entry and Branchrestrictionpolicy_users(**entry) for entry in self._users ]
        
    users = property(_getusers)

    def _getapps_url(self):
        return self._apps_url
        
    apps_url = property(_getapps_url)

    def _getteams_url(self):
        return self._teams_url
        
    teams_url = property(_getteams_url)

    def _getusers_url(self):
        return self._users_url
        
    users_url = property(_getusers_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class Branchprotection_required_linear_history(ResponseBase):
    def __init__(self, enabled:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)


    
##
##
##
class Branchprotection_allow_force_pushes(ResponseBase):
    def __init__(self, enabled:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)


    
##
##
##
class Branchprotection_allow_deletions(ResponseBase):
    def __init__(self, enabled:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)


    
##
##
##
class Branchprotection_required_conversation_resolution(ResponseBase):
    def __init__(self, enabled:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)


    
##
##
##
class Branchprotection_required_signatures(ResponseBase):
    def __init__(self, enabled:bool, url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        self._url = url
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class BranchProtection(ResponseBase):
    """Branch Protection """
    def __init__(self, url:str=None, enabled:bool=None, required_status_checks:dict=None, enforce_admins:dict=None, required_pull_request_reviews:dict=None, restrictions:dict=None, required_linear_history:dict=None, allow_force_pushes:dict=None, allow_deletions:dict=None, required_conversation_resolution:dict=None, name:str=None, protection_url:str=None, required_signatures:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._enabled = enabled
        self._required_status_checks = required_status_checks
        self._enforce_admins = enforce_admins
        self._required_pull_request_reviews = required_pull_request_reviews
        self._restrictions = restrictions
        self._required_linear_history = required_linear_history
        self._allow_force_pushes = allow_force_pushes
        self._allow_deletions = allow_deletions
        self._required_conversation_resolution = required_conversation_resolution
        self._name = name
        self._protection_url = protection_url
        self._required_signatures = required_signatures
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)

    def _getrequired_status_checks(self):
        return self._required_status_checks and ProtectedBranchRequiredStatusCheck(**self._required_status_checks)
        
    required_status_checks = property(_getrequired_status_checks)

    def _getenforce_admins(self):
        return self._enforce_admins and ProtectedBranchAdminEnforced(**self._enforce_admins)
        
    enforce_admins = property(_getenforce_admins)

    def _getrequired_pull_request_reviews(self):
        return self._required_pull_request_reviews and ProtectedBranchPullRequestReview(**self._required_pull_request_reviews)
        
    required_pull_request_reviews = property(_getrequired_pull_request_reviews)

    def _getrestrictions(self):
        return self._restrictions and BranchRestrictionPolicy(**self._restrictions)
        
    restrictions = property(_getrestrictions)

    def _getrequired_linear_history(self):
        return self._required_linear_history and Branchprotection_required_linear_history(**self._required_linear_history)
        
    required_linear_history = property(_getrequired_linear_history)

    def _getallow_force_pushes(self):
        return self._allow_force_pushes and Branchprotection_allow_force_pushes(**self._allow_force_pushes)
        
    allow_force_pushes = property(_getallow_force_pushes)

    def _getallow_deletions(self):
        return self._allow_deletions and Branchprotection_allow_deletions(**self._allow_deletions)
        
    allow_deletions = property(_getallow_deletions)

    def _getrequired_conversation_resolution(self):
        return self._required_conversation_resolution and Branchprotection_required_conversation_resolution(**self._required_conversation_resolution)
        
    required_conversation_resolution = property(_getrequired_conversation_resolution)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getprotection_url(self):
        return self._protection_url
        
    protection_url = property(_getprotection_url)

    def _getrequired_signatures(self):
        return self._required_signatures and Branchprotection_required_signatures(**self._required_signatures)
        
    required_signatures = property(_getrequired_signatures)


    
##
##
##
class Shortbranch_commit(ResponseBase):
    def __init__(self, url:str, sha:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._sha = sha
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)


    
##
##
##
class ShortBranch(ResponseBase):
    """Short Branch """
    def __init__(self, protected:bool, commit:dict, name:str, protection:dict=None, protection_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._protected = protected
        self._commit = commit
        self._name = name
        self._protection = protection
        self._protection_url = protection_url
        return
        
    

    
    def _getprotected(self):
        return self._protected
        
    protected = property(_getprotected)

    def _getcommit(self):
        return self._commit and Shortbranch_commit(**self._commit)
        
    commit = property(_getcommit)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getprotection(self):
        return self._protection and BranchProtection(**self._protection)
        
    protection = property(_getprotection)

    def _getprotection_url(self):
        return self._protection_url
        
    protection_url = property(_getprotection_url)


    
##
##
##
class NullableGitUser(ResponseBase):
    """Metaproperties for Git author/committer information. """
    def __init__(self, name:str=None, email:str=None, date:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._name = name
        self._email = email
        self._date = date
        return
        
    

    
    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _getdate(self):
        return self._date
        
    date = property(_getdate)


    
##
##
##
class Verification(ResponseBase):
    def __init__(self, signature:str, payload:str, reason:str, verified:bool, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._signature = signature
        self._payload = payload
        self._reason = reason
        self._verified = verified
        return
        
    

    
    def _getsignature(self):
        return self._signature
        
    signature = property(_getsignature)

    def _getpayload(self):
        return self._payload
        
    payload = property(_getpayload)

    def _getreason(self):
        return self._reason
        
    reason = property(_getreason)

    def _getverified(self):
        return self._verified
        
    verified = property(_getverified)


    
##
##
##
class DiffEntry(ResponseBase):
    """Diff Entry """
    def __init__(self, contents_url:str, raw_url:str, blob_url:str, changes:int, deletions:int, additions:int, status:str, filename:str, sha:str, patch:str=None, previous_filename:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._contents_url = contents_url
        self._raw_url = raw_url
        self._blob_url = blob_url
        self._changes = changes
        self._deletions = deletions
        self._additions = additions
        self._status = status
        self._filename = filename
        self._sha = sha
        self._patch = patch
        self._previous_filename = previous_filename
        return
        
    

    
    def _getcontents_url(self):
        return self._contents_url
        
    contents_url = property(_getcontents_url)

    def _getraw_url(self):
        return self._raw_url
        
    raw_url = property(_getraw_url)

    def _getblob_url(self):
        return self._blob_url
        
    blob_url = property(_getblob_url)

    def _getchanges(self):
        return self._changes
        
    changes = property(_getchanges)

    def _getdeletions(self):
        return self._deletions
        
    deletions = property(_getdeletions)

    def _getadditions(self):
        return self._additions
        
    additions = property(_getadditions)

    def _getstatus(self):
        return self._status
        
    status = property(_getstatus)

    def _getfilename(self):
        return self._filename
        
    filename = property(_getfilename)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getpatch(self):
        return self._patch
        
    patch = property(_getpatch)

    def _getprevious_filename(self):
        return self._previous_filename
        
    previous_filename = property(_getprevious_filename)


    
##
##
##
class Commit_commit_tree(ResponseBase):
    def __init__(self, url:str, sha:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._sha = sha
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)


    
##
##
##
class Commit_commit(ResponseBase):
    def __init__(self, tree:dict, comment_count:int, message:str, committer:dict, author:dict, url:str, verification:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._tree = tree
        self._comment_count = comment_count
        self._message = message
        self._committer = committer
        self._author = author
        self._url = url
        self._verification = verification
        return
        
    

    
    def _gettree(self):
        return self._tree and Commit_commit_tree(**self._tree)
        
    tree = property(_gettree)

    def _getcomment_count(self):
        return self._comment_count
        
    comment_count = property(_getcomment_count)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getcommitter(self):
        return self._committer and NullableGitUser(**self._committer)
        
    committer = property(_getcommitter)

    def _getauthor(self):
        return self._author and NullableGitUser(**self._author)
        
    author = property(_getauthor)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getverification(self):
        return self._verification and Verification(**self._verification)
        
    verification = property(_getverification)


    
##
##
##
class Commit_parents(ResponseBase):
    def __init__(self, url:str, sha:str, html_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._sha = sha
        self._html_url = html_url
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)


    
##
##
##
class Commit_stats(ResponseBase):
    def __init__(self, additions:int=None, deletions:int=None, total:int=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._additions = additions
        self._deletions = deletions
        self._total = total
        return
        
    

    
    def _getadditions(self):
        return self._additions
        
    additions = property(_getadditions)

    def _getdeletions(self):
        return self._deletions
        
    deletions = property(_getdeletions)

    def _gettotal(self):
        return self._total
        
    total = property(_gettotal)


    
##
##
##
class Commit(ResponseBase):
    """Commit """
    def __init__(self, parents:list, committer:dict, author:dict, commit:dict, comments_url:str, html_url:str, node_id:str, sha:str, url:str, stats:dict=None, files:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._parents = parents
        self._committer = committer
        self._author = author
        self._commit = commit
        self._comments_url = comments_url
        self._html_url = html_url
        self._node_id = node_id
        self._sha = sha
        self._url = url
        self._stats = stats
        self._files = files
        return
        
    

    
    def _getparents(self):
        return self._parents and [ entry and Commit_parents(**entry) for entry in self._parents ]
        
    parents = property(_getparents)

    def _getcommitter(self):
        return self._committer and NullableSimpleUser(**self._committer)
        
    committer = property(_getcommitter)

    def _getauthor(self):
        return self._author and NullableSimpleUser(**self._author)
        
    author = property(_getauthor)

    def _getcommit(self):
        return self._commit and Commit_commit(**self._commit)
        
    commit = property(_getcommit)

    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getstats(self):
        return self._stats and Commit_stats(**self._stats)
        
    stats = property(_getstats)

    def _getfiles(self):
        return self._files and [ entry and DiffEntry(**entry) for entry in self._files ]
        
    files = property(_getfiles)


    
##
##
##
class Branchwithprotection__links(ResponseBase):
    def __init__(self, Self:str, html:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._Self = Self
        self._html = html
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['Self'] = entry.pop('self')
        return entry
    

    
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

    def _gethtml(self):
        return self._html
        
    html = property(_gethtml)


    
    ##
    ##
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

##
##
##
class BranchWithProtection(ResponseBase):
    """Branch With Protection """
    def __init__(self, protection_url:str, protection:dict, protected:bool, _links:dict, commit:dict, name:str, pattern:str=None, required_approving_review_count:int=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._protection_url = protection_url
        self._protection = protection
        self._protected = protected
        self.__links = _links
        self._commit = commit
        self._name = name
        self._pattern = pattern
        self._required_approving_review_count = required_approving_review_count
        return
        
    

    
    def _getprotection_url(self):
        return self._protection_url
        
    protection_url = property(_getprotection_url)

    def _getprotection(self):
        return self._protection and BranchProtection(**self._protection)
        
    protection = property(_getprotection)

    def _getprotected(self):
        return self._protected
        
    protected = property(_getprotected)

    def _get_links(self):
        return self.__links and Branchwithprotection__links(**Branchwithprotection__links.patchEntry(self.__links))
        
    _links = property(_get_links)

    def _getcommit(self):
        return self._commit and Commit(**self._commit)
        
    commit = property(_getcommit)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getpattern(self):
        return self._pattern
        
    pattern = property(_getpattern)

    def _getrequired_approving_review_count(self):
        return self._required_approving_review_count
        
    required_approving_review_count = property(_getrequired_approving_review_count)


    
##
##
##
class StatusCheckPolicy(ResponseBase):
    """Status Check Policy """
    def __init__(self, contexts_url:str, contexts:list, strict:bool, url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._contexts_url = contexts_url
        self._contexts = contexts
        self._strict = strict
        self._url = url
        return
        
    

    
    def _getcontexts_url(self):
        return self._contexts_url
        
    contexts_url = property(_getcontexts_url)

    def _getcontexts(self):
        return self._contexts and [ entry for entry in self._contexts ]
        
    contexts = property(_getcontexts)

    def _getstrict(self):
        return self._strict
        
    strict = property(_getstrict)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class Protectedbranch_required_pull_request_reviews_dismissal_restrictions(ResponseBase):
    def __init__(self, teams:list, users:list, teams_url:str, users_url:str, url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._teams = teams
        self._users = users
        self._teams_url = teams_url
        self._users_url = users_url
        self._url = url
        return
        
    

    
    def _getteams(self):
        return self._teams and [ entry and Team(**entry) for entry in self._teams ]
        
    teams = property(_getteams)

    def _getusers(self):
        return self._users and [ entry and SimpleUser(**entry) for entry in self._users ]
        
    users = property(_getusers)

    def _getteams_url(self):
        return self._teams_url
        
    teams_url = property(_getteams_url)

    def _getusers_url(self):
        return self._users_url
        
    users_url = property(_getusers_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class Protectedbranch_required_pull_request_reviews(ResponseBase):
    def __init__(self, url:str, dismiss_stale_reviews:bool=None, require_code_owner_reviews:bool=None, required_approving_review_count:int=None, dismissal_restrictions:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._dismiss_stale_reviews = dismiss_stale_reviews
        self._require_code_owner_reviews = require_code_owner_reviews
        self._required_approving_review_count = required_approving_review_count
        self._dismissal_restrictions = dismissal_restrictions
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getdismiss_stale_reviews(self):
        return self._dismiss_stale_reviews
        
    dismiss_stale_reviews = property(_getdismiss_stale_reviews)

    def _getrequire_code_owner_reviews(self):
        return self._require_code_owner_reviews
        
    require_code_owner_reviews = property(_getrequire_code_owner_reviews)

    def _getrequired_approving_review_count(self):
        return self._required_approving_review_count
        
    required_approving_review_count = property(_getrequired_approving_review_count)

    def _getdismissal_restrictions(self):
        return self._dismissal_restrictions and Protectedbranch_required_pull_request_reviews_dismissal_restrictions(**self._dismissal_restrictions)
        
    dismissal_restrictions = property(_getdismissal_restrictions)


    
##
##
##
class Protectedbranch_required_signatures(ResponseBase):
    def __init__(self, enabled:bool, url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        self._url = url
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class Protectedbranch_enforce_admins(ResponseBase):
    def __init__(self, enabled:bool, url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        self._url = url
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class Protectedbranch_required_linear_history(ResponseBase):
    def __init__(self, enabled:bool, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)


    
##
##
##
class Protectedbranch_allow_force_pushes(ResponseBase):
    def __init__(self, enabled:bool, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)


    
##
##
##
class Protectedbranch_allow_deletions(ResponseBase):
    def __init__(self, enabled:bool, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)


    
##
##
##
class Protectedbranch_required_conversation_resolution(ResponseBase):
    def __init__(self, enabled:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)


    
##
##
##
class ProtectedBranch(ResponseBase):
    """Branch protections protect branches """
    def __init__(self, url:str, required_status_checks:dict=None, required_pull_request_reviews:dict=None, required_signatures:dict=None, enforce_admins:dict=None, required_linear_history:dict=None, allow_force_pushes:dict=None, allow_deletions:dict=None, restrictions:dict=None, required_conversation_resolution:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._required_status_checks = required_status_checks
        self._required_pull_request_reviews = required_pull_request_reviews
        self._required_signatures = required_signatures
        self._enforce_admins = enforce_admins
        self._required_linear_history = required_linear_history
        self._allow_force_pushes = allow_force_pushes
        self._allow_deletions = allow_deletions
        self._restrictions = restrictions
        self._required_conversation_resolution = required_conversation_resolution
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getrequired_status_checks(self):
        return self._required_status_checks and StatusCheckPolicy(**self._required_status_checks)
        
    required_status_checks = property(_getrequired_status_checks)

    def _getrequired_pull_request_reviews(self):
        return self._required_pull_request_reviews and Protectedbranch_required_pull_request_reviews(**self._required_pull_request_reviews)
        
    required_pull_request_reviews = property(_getrequired_pull_request_reviews)

    def _getrequired_signatures(self):
        return self._required_signatures and Protectedbranch_required_signatures(**self._required_signatures)
        
    required_signatures = property(_getrequired_signatures)

    def _getenforce_admins(self):
        return self._enforce_admins and Protectedbranch_enforce_admins(**self._enforce_admins)
        
    enforce_admins = property(_getenforce_admins)

    def _getrequired_linear_history(self):
        return self._required_linear_history and Protectedbranch_required_linear_history(**self._required_linear_history)
        
    required_linear_history = property(_getrequired_linear_history)

    def _getallow_force_pushes(self):
        return self._allow_force_pushes and Protectedbranch_allow_force_pushes(**self._allow_force_pushes)
        
    allow_force_pushes = property(_getallow_force_pushes)

    def _getallow_deletions(self):
        return self._allow_deletions and Protectedbranch_allow_deletions(**self._allow_deletions)
        
    allow_deletions = property(_getallow_deletions)

    def _getrestrictions(self):
        return self._restrictions and BranchRestrictionPolicy(**self._restrictions)
        
    restrictions = property(_getrestrictions)

    def _getrequired_conversation_resolution(self):
        return self._required_conversation_resolution and Protectedbranch_required_conversation_resolution(**self._required_conversation_resolution)
        
    required_conversation_resolution = property(_getrequired_conversation_resolution)


    
##
##
##
class DeploymentSimple(ResponseBase):
    """A deployment created as the result of an Actions check run from a workflow that references an environment """
    def __init__(self, repository_url:str, statuses_url:str, updated_at:datetime, created_at:datetime, description:str, environment:str, task:str, node_id:str, id:int, url:str, original_environment:str=None, transient_environment:bool=None, production_environment:bool=None, performed_via_github_app:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._repository_url = repository_url
        self._statuses_url = statuses_url
        self._updated_at = updated_at
        self._created_at = created_at
        self._description = description
        self._environment = environment
        self._task = task
        self._node_id = node_id
        self._id = id
        self._url = url
        self._original_environment = original_environment
        self._transient_environment = transient_environment
        self._production_environment = production_environment
        self._performed_via_github_app = performed_via_github_app
        return
        
    

    
    def _getrepository_url(self):
        return self._repository_url
        
    repository_url = property(_getrepository_url)

    def _getstatuses_url(self):
        return self._statuses_url
        
    statuses_url = property(_getstatuses_url)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getenvironment(self):
        return self._environment
        
    environment = property(_getenvironment, doc="""Name for the target deployment environment. """)

    def _gettask(self):
        return self._task
        
    task = property(_gettask, doc="""Parameter to specify a task to execute """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the deployment """)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getoriginal_environment(self):
        return self._original_environment
        
    original_environment = property(_getoriginal_environment)

    def _gettransient_environment(self):
        return self._transient_environment
        
    transient_environment = property(_gettransient_environment, doc="""Specifies if the given environment is will no longer exist at some point in the future. Default: false. """)

    def _getproduction_environment(self):
        return self._production_environment
        
    production_environment = property(_getproduction_environment, doc="""Specifies if the given environment is one that end-users directly interact with. Default: false. """)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)


    
##
##
##
class Checkrun_output(ResponseBase):
    def __init__(self, annotations_url:str, annotations_count:int, text:str, summary:str, title:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._annotations_url = annotations_url
        self._annotations_count = annotations_count
        self._text = text
        self._summary = summary
        self._title = title
        return
        
    

    
    def _getannotations_url(self):
        return self._annotations_url
        
    annotations_url = property(_getannotations_url)

    def _getannotations_count(self):
        return self._annotations_count
        
    annotations_count = property(_getannotations_count)

    def _gettext(self):
        return self._text
        
    text = property(_gettext)

    def _getsummary(self):
        return self._summary
        
    summary = property(_getsummary)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle)


    
##
##
##
class Checkrun_check_suite(ResponseBase):
    def __init__(self, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class Checkrun(ResponseBase):
    """A check performed on the code of a given code change """
    def __init__(self, pull_requests:list, app:dict, check_suite:dict, name:str, output:dict, completed_at:datetime, started_at:datetime, conclusion:str, status:str, details_url:str, html_url:str, url:str, external_id:str, node_id:str, head_sha:str, id:int, deployment:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._pull_requests = pull_requests
        self._app = app
        self._check_suite = check_suite
        self._name = name
        self._output = output
        self._completed_at = completed_at
        self._started_at = started_at
        self._conclusion = conclusion
        self._status = status
        self._details_url = details_url
        self._html_url = html_url
        self._url = url
        self._external_id = external_id
        self._node_id = node_id
        self._head_sha = head_sha
        self._id = id
        self._deployment = deployment
        return
        
    

    
    def _getpull_requests(self):
        return self._pull_requests and [ entry and PullRequestMinimal(**entry) for entry in self._pull_requests ]
        
    pull_requests = property(_getpull_requests)

    def _getapp(self):
        return self._app and NullableIntegration(**self._app)
        
    app = property(_getapp)

    def _getcheck_suite(self):
        return self._check_suite and Checkrun_check_suite(**self._check_suite)
        
    check_suite = property(_getcheck_suite)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the check. """)

    def _getoutput(self):
        return self._output and Checkrun_output(**self._output)
        
    output = property(_getoutput)

    def _getcompleted_at(self):
        return self._completed_at and datetime.datetime.fromisoformat(self._completed_at[0:-1])
        
    completed_at = property(_getcompleted_at)

    def _getstarted_at(self):
        return self._started_at and datetime.datetime.fromisoformat(self._started_at[0:-1])
        
    started_at = property(_getstarted_at)

    def _getconclusion(self):
        return self._conclusion
        
    conclusion = property(_getconclusion)

    def _getstatus(self):
        return self._status
        
    status = property(_getstatus, doc="""The phase of the lifecycle that the check is currently in. """)

    def _getdetails_url(self):
        return self._details_url
        
    details_url = property(_getdetails_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getexternal_id(self):
        return self._external_id
        
    external_id = property(_getexternal_id)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _gethead_sha(self):
        return self._head_sha
        
    head_sha = property(_gethead_sha, doc="""The SHA of the commit that is being checked. """)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""The id of the check. """)

    def _getdeployment(self):
        return self._deployment and DeploymentSimple(**self._deployment)
        
    deployment = property(_getdeployment)


    
##
##
##
class CheckAnnotation(ResponseBase):
    """Check Annotation """
    def __init__(self, blob_href:str, raw_details:str, message:str, title:str, annotation_level:str, end_column:int, start_column:int, end_line:int, start_line:int, path:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._blob_href = blob_href
        self._raw_details = raw_details
        self._message = message
        self._title = title
        self._annotation_level = annotation_level
        self._end_column = end_column
        self._start_column = start_column
        self._end_line = end_line
        self._start_line = start_line
        self._path = path
        return
        
    

    
    def _getblob_href(self):
        return self._blob_href
        
    blob_href = property(_getblob_href)

    def _getraw_details(self):
        return self._raw_details
        
    raw_details = property(_getraw_details)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle)

    def _getannotation_level(self):
        return self._annotation_level
        
    annotation_level = property(_getannotation_level)

    def _getend_column(self):
        return self._end_column
        
    end_column = property(_getend_column)

    def _getstart_column(self):
        return self._start_column
        
    start_column = property(_getstart_column)

    def _getend_line(self):
        return self._end_line
        
    end_line = property(_getend_line)

    def _getstart_line(self):
        return self._start_line
        
    start_line = property(_getstart_line)

    def _getpath(self):
        return self._path
        
    path = property(_getpath)


    
##
##
##
class Simplecommit_author(ResponseBase):
    def __init__(self, email:str, name:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._email = email
        self._name = name
        return
        
    

    
    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _getname(self):
        return self._name
        
    name = property(_getname)


    
##
##
##
class Simplecommit_committer(ResponseBase):
    def __init__(self, email:str, name:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._email = email
        self._name = name
        return
        
    

    
    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _getname(self):
        return self._name
        
    name = property(_getname)


    
##
##
##
class SimpleCommit(ResponseBase):
    """Simple Commit """
    def __init__(self, committer:dict, author:dict, timestamp:datetime, message:str, tree_id:str, id:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._committer = committer
        self._author = author
        self._timestamp = timestamp
        self._message = message
        self._tree_id = tree_id
        self._id = id
        return
        
    

    
    def _getcommitter(self):
        return self._committer and Simplecommit_committer(**self._committer)
        
    committer = property(_getcommitter)

    def _getauthor(self):
        return self._author and Simplecommit_author(**self._author)
        
    author = property(_getauthor)

    def _gettimestamp(self):
        return self._timestamp and datetime.datetime.fromisoformat(self._timestamp[0:-1])
        
    timestamp = property(_gettimestamp)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _gettree_id(self):
        return self._tree_id
        
    tree_id = property(_gettree_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class Checksuite(ResponseBase):
    """A suite of checks performed on the code of a given code change """
    def __init__(self, check_runs_url:str, latest_check_runs_count:int, head_commit:dict, updated_at:datetime, created_at:datetime, repository:dict, app:dict, pull_requests:list, after:str, before:str, url:str, conclusion:str, status:str, head_sha:str, head_branch:str, node_id:str, id:int, rerequestable:bool=None, runs_rerequestable:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._check_runs_url = check_runs_url
        self._latest_check_runs_count = latest_check_runs_count
        self._head_commit = head_commit
        self._updated_at = updated_at
        self._created_at = created_at
        self._repository = repository
        self._app = app
        self._pull_requests = pull_requests
        self._after = after
        self._before = before
        self._url = url
        self._conclusion = conclusion
        self._status = status
        self._head_sha = head_sha
        self._head_branch = head_branch
        self._node_id = node_id
        self._id = id
        self._rerequestable = rerequestable
        self._runs_rerequestable = runs_rerequestable
        return
        
    

    
    def _getcheck_runs_url(self):
        return self._check_runs_url
        
    check_runs_url = property(_getcheck_runs_url)

    def _getlatest_check_runs_count(self):
        return self._latest_check_runs_count
        
    latest_check_runs_count = property(_getlatest_check_runs_count)

    def _gethead_commit(self):
        return self._head_commit and SimpleCommit(**self._head_commit)
        
    head_commit = property(_gethead_commit)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getrepository(self):
        return self._repository and MinimalRepository(**self._repository)
        
    repository = property(_getrepository)

    def _getapp(self):
        return self._app and NullableIntegration(**self._app)
        
    app = property(_getapp)

    def _getpull_requests(self):
        return self._pull_requests and [ entry and PullRequestMinimal(**entry) for entry in self._pull_requests ]
        
    pull_requests = property(_getpull_requests)

    def _getafter(self):
        return self._after
        
    after = property(_getafter)

    def _getbefore(self):
        return self._before
        
    before = property(_getbefore)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getconclusion(self):
        return self._conclusion
        
    conclusion = property(_getconclusion)

    def _getstatus(self):
        return self._status
        
    status = property(_getstatus)

    def _gethead_sha(self):
        return self._head_sha
        
    head_sha = property(_gethead_sha, doc="""The SHA of the head commit that is being checked. """)

    def _gethead_branch(self):
        return self._head_branch
        
    head_branch = property(_gethead_branch)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getrerequestable(self):
        return self._rerequestable
        
    rerequestable = property(_getrerequestable)

    def _getruns_rerequestable(self):
        return self._runs_rerequestable
        
    runs_rerequestable = property(_getruns_rerequestable)


    
##
##
##
class Checksuitepreference_preferences_auto_trigger_checks(ResponseBase):
    def __init__(self, setting:bool, app_id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._setting = setting
        self._app_id = app_id
        return
        
    

    
    def _getsetting(self):
        return self._setting
        
    setting = property(_getsetting)

    def _getapp_id(self):
        return self._app_id
        
    app_id = property(_getapp_id)


    
##
##
##
class Checksuitepreference_preferences(ResponseBase):
    def __init__(self, auto_trigger_checks:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._auto_trigger_checks = auto_trigger_checks
        return
        
    

    
    def _getauto_trigger_checks(self):
        return self._auto_trigger_checks and [ entry and Checksuitepreference_preferences_auto_trigger_checks(**entry) for entry in self._auto_trigger_checks ]
        
    auto_trigger_checks = property(_getauto_trigger_checks)


    
##
##
##
class CheckSuitePreference(ResponseBase):
    """Check suite configuration preferences for a repository. """
    def __init__(self, repository:dict, preferences:dict, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._repository = repository
        self._preferences = preferences
        return
        
    

    
    def _getrepository(self):
        return self._repository and MinimalRepository(**self._repository)
        
    repository = property(_getrepository)

    def _getpreferences(self):
        return self._preferences and Checksuitepreference_preferences(**self._preferences)
        
    preferences = property(_getpreferences)


    
##
##
##
class CodeScanningAlertRuleSummary(ResponseBase):
    def __init__(self, id:str=None, name:str=None, severity:str=None, description:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._name = name
        self._severity = severity
        self._description = description
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""A unique identifier for the rule used to detect the alert. """)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the rule used to detect the alert. """)

    def _getseverity(self):
        return self._severity
        
    severity = property(_getseverity, doc="""The severity of the alert. """)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription, doc="""A short description of the rule used to detect the alert. """)


    
##
##
##
class CodeScanningAnalysisTool(ResponseBase):
    def __init__(self, name:str=None, version:str=None, guid:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._name = name
        self._version = version
        self._guid = guid
        return
        
    

    
    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getversion(self):
        return self._version
        
    version = property(_getversion)

    def _getguid(self):
        return self._guid
        
    guid = property(_getguid)


    
##
##
##
class CodeScanningAlertLocation(ResponseBase):
    """Describe a region within a file for the alert. """
    def __init__(self, path:str=None, start_line:int=None, end_line:int=None, start_column:int=None, end_column:int=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._path = path
        self._start_line = start_line
        self._end_line = end_line
        self._start_column = start_column
        self._end_column = end_column
        return
        
    

    
    def _getpath(self):
        return self._path
        
    path = property(_getpath)

    def _getstart_line(self):
        return self._start_line
        
    start_line = property(_getstart_line)

    def _getend_line(self):
        return self._end_line
        
    end_line = property(_getend_line)

    def _getstart_column(self):
        return self._start_column
        
    start_column = property(_getstart_column)

    def _getend_column(self):
        return self._end_column
        
    end_column = property(_getend_column)


    
##
##
##
class Codescanningalertinstance_message(ResponseBase):
    def __init__(self, text:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._text = text
        return
        
    

    
    def _gettext(self):
        return self._text
        
    text = property(_gettext)


    
##
##
##
class CodeScanningAlertInstance(ResponseBase):
    def __init__(self, ref:str=None, analysis_key:str=None, environment:str=None, category:str=None, state:str=None, commit_sha:str=None, message:dict=None, location:dict=None, html_url:str=None, classifications:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._ref = ref
        self._analysis_key = analysis_key
        self._environment = environment
        self._category = category
        self._state = state
        self._commit_sha = commit_sha
        self._message = message
        self._location = location
        self._html_url = html_url
        self._classifications = classifications
        return
        
    

    
    def _getref(self):
        return self._ref
        
    ref = property(_getref)

    def _getanalysis_key(self):
        return self._analysis_key
        
    analysis_key = property(_getanalysis_key)

    def _getenvironment(self):
        return self._environment
        
    environment = property(_getenvironment)

    def _getcategory(self):
        return self._category
        
    category = property(_getcategory)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)

    def _getcommit_sha(self):
        return self._commit_sha
        
    commit_sha = property(_getcommit_sha)

    def _getmessage(self):
        return self._message and Codescanningalertinstance_message(**self._message)
        
    message = property(_getmessage)

    def _getlocation(self):
        return self._location and CodeScanningAlertLocation(**self._location)
        
    location = property(_getlocation)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getclassifications(self):
        return self._classifications and [ entry for entry in self._classifications ]
        
    classifications = property(_getclassifications, doc="""Classifications that have been applied to the file that triggered the alert.
For example identifying it as documentation, or a generated file. """)


    
##
##
##
class CodeScanningAlertItems(ResponseBase):
    def __init__(self, most_recent_instance:dict, tool:dict, rule:dict, dismissed_reason:str, dismissed_at:datetime, dismissed_by:dict, state:str, instances_url:str, html_url:str, url:str, created_at:datetime, number:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._most_recent_instance = most_recent_instance
        self._tool = tool
        self._rule = rule
        self._dismissed_reason = dismissed_reason
        self._dismissed_at = dismissed_at
        self._dismissed_by = dismissed_by
        self._state = state
        self._instances_url = instances_url
        self._html_url = html_url
        self._url = url
        self._created_at = created_at
        self._number = number
        return
        
    

    
    def _getmost_recent_instance(self):
        return self._most_recent_instance and CodeScanningAlertInstance(**self._most_recent_instance)
        
    most_recent_instance = property(_getmost_recent_instance)

    def _gettool(self):
        return self._tool and CodeScanningAnalysisTool(**self._tool)
        
    tool = property(_gettool)

    def _getrule(self):
        return self._rule and CodeScanningAlertRuleSummary(**self._rule)
        
    rule = property(_getrule)

    def _getdismissed_reason(self):
        return self._dismissed_reason
        
    dismissed_reason = property(_getdismissed_reason)

    def _getdismissed_at(self):
        return self._dismissed_at and datetime.datetime.fromisoformat(self._dismissed_at[0:-1])
        
    dismissed_at = property(_getdismissed_at)

    def _getdismissed_by(self):
        return self._dismissed_by and NullableSimpleUser(**self._dismissed_by)
        
    dismissed_by = property(_getdismissed_by)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)

    def _getinstances_url(self):
        return self._instances_url
        
    instances_url = property(_getinstances_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getnumber(self):
        return self._number
        
    number = property(_getnumber)


    
##
##
##
class CodeScanningAlertRule(ResponseBase):
    def __init__(self, id:str=None, name:str=None, severity:str=None, security_severity_level:str=None, description:str=None, full_description:str=None, tags:list=[], help:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._name = name
        self._severity = severity
        self._security_severity_level = security_severity_level
        self._description = description
        self._full_description = full_description
        self._tags = tags
        self._help = help
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""A unique identifier for the rule used to detect the alert. """)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the rule used to detect the alert. """)

    def _getseverity(self):
        return self._severity
        
    severity = property(_getseverity, doc="""The severity of the alert. """)

    def _getsecurity_severity_level(self):
        return self._security_severity_level
        
    security_severity_level = property(_getsecurity_severity_level, doc="""The security severity of the alert. """)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription, doc="""A short description of the rule used to detect the alert. """)

    def _getfull_description(self):
        return self._full_description
        
    full_description = property(_getfull_description, doc="""description of the rule used to detect the alert. """)

    def _gettags(self):
        return self._tags and [ entry for entry in self._tags ]
        
    tags = property(_gettags, doc="""A set of tags applicable for the rule. """)

    def _gethelp(self):
        return self._help
        
    help = property(_gethelp, doc="""Detailed documentation for the rule as GitHub Flavored Markdown. """)


    
##
##
##
class CodeScanningAlert(ResponseBase):
    def __init__(self, most_recent_instance:dict, tool:dict, rule:dict, dismissed_reason:str, dismissed_at:datetime, dismissed_by:dict, state:str, instances_url:str, html_url:str, url:str, created_at:datetime, number:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._most_recent_instance = most_recent_instance
        self._tool = tool
        self._rule = rule
        self._dismissed_reason = dismissed_reason
        self._dismissed_at = dismissed_at
        self._dismissed_by = dismissed_by
        self._state = state
        self._instances_url = instances_url
        self._html_url = html_url
        self._url = url
        self._created_at = created_at
        self._number = number
        return
        
    

    
    def _getmost_recent_instance(self):
        return self._most_recent_instance and CodeScanningAlertInstance(**self._most_recent_instance)
        
    most_recent_instance = property(_getmost_recent_instance)

    def _gettool(self):
        return self._tool and CodeScanningAnalysisTool(**self._tool)
        
    tool = property(_gettool)

    def _getrule(self):
        return self._rule and CodeScanningAlertRule(**self._rule)
        
    rule = property(_getrule)

    def _getdismissed_reason(self):
        return self._dismissed_reason
        
    dismissed_reason = property(_getdismissed_reason)

    def _getdismissed_at(self):
        return self._dismissed_at and datetime.datetime.fromisoformat(self._dismissed_at[0:-1])
        
    dismissed_at = property(_getdismissed_at)

    def _getdismissed_by(self):
        return self._dismissed_by and NullableSimpleUser(**self._dismissed_by)
        
    dismissed_by = property(_getdismissed_by)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)

    def _getinstances_url(self):
        return self._instances_url
        
    instances_url = property(_getinstances_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getnumber(self):
        return self._number
        
    number = property(_getnumber)


    
##
##
##
class CodeScanningAnalysis(ResponseBase):
    def __init__(self, warning:str, deletable:bool, tool:dict, sarif_id:str, url:str, id:int, rules_count:int, results_count:int, created_at:datetime, error:str, environment:str, analysis_key:str, commit_sha:str, ref:str, category:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._warning = warning
        self._deletable = deletable
        self._tool = tool
        self._sarif_id = sarif_id
        self._url = url
        self._id = id
        self._rules_count = rules_count
        self._results_count = results_count
        self._created_at = created_at
        self._error = error
        self._environment = environment
        self._analysis_key = analysis_key
        self._commit_sha = commit_sha
        self._ref = ref
        self._category = category
        return
        
    

    
    def _getwarning(self):
        return self._warning
        
    warning = property(_getwarning, doc="""Warning generated when processing the analysis """)

    def _getdeletable(self):
        return self._deletable
        
    deletable = property(_getdeletable)

    def _gettool(self):
        return self._tool and CodeScanningAnalysisTool(**self._tool)
        
    tool = property(_gettool)

    def _getsarif_id(self):
        return self._sarif_id
        
    sarif_id = property(_getsarif_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier for this analysis. """)

    def _getrules_count(self):
        return self._rules_count
        
    rules_count = property(_getrules_count, doc="""The total number of rules used in the analysis. """)

    def _getresults_count(self):
        return self._results_count
        
    results_count = property(_getresults_count, doc="""The total number of results in the analysis. """)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _geterror(self):
        return self._error
        
    error = property(_geterror)

    def _getenvironment(self):
        return self._environment
        
    environment = property(_getenvironment)

    def _getanalysis_key(self):
        return self._analysis_key
        
    analysis_key = property(_getanalysis_key)

    def _getcommit_sha(self):
        return self._commit_sha
        
    commit_sha = property(_getcommit_sha)

    def _getref(self):
        return self._ref
        
    ref = property(_getref)

    def _getcategory(self):
        return self._category
        
    category = property(_getcategory)


    
##
##
##
class CodeScanningAnalysisDeletion(ResponseBase):
    """Successful deletion of a code scanning analysis """
    def __init__(self, confirm_delete_url:str, next_analysis_url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._confirm_delete_url = confirm_delete_url
        self._next_analysis_url = next_analysis_url
        return
        
    

    
    def _getconfirm_delete_url(self):
        return self._confirm_delete_url
        
    confirm_delete_url = property(_getconfirm_delete_url, doc="""Next deletable analysis in chain, with last analysis deletion confirmation """)

    def _getnext_analysis_url(self):
        return self._next_analysis_url
        
    next_analysis_url = property(_getnext_analysis_url, doc="""Next deletable analysis in chain, without last analysis deletion confirmation """)


    
##
##
##
class CodeScanningSarifsReceipt(ResponseBase):
    def __init__(self, id:str=None, url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._url = url
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _geturl(self):
        return self._url
        
    url = property(_geturl, doc="""The REST API URL for checking the status of the upload. """)


    
##
##
##
class CodeScanningSarifsStatus(ResponseBase):
    def __init__(self, processing_status:str=None, analyses_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._processing_status = processing_status
        self._analyses_url = analyses_url
        return
        
    

    
    def _getprocessing_status(self):
        return self._processing_status
        
    processing_status = property(_getprocessing_status, doc="""`pending` files have not yet been processed, while `complete` means all results in the SARIF have been stored. """)

    def _getanalyses_url(self):
        return self._analyses_url
        
    analyses_url = property(_getanalyses_url, doc="""The REST API URL for getting the analyses associated with the upload. """)


    
##
##
##
class Collaborator_permissions(ResponseBase):
    def __init__(self, admin:bool, push:bool, pull:bool, triage:bool=None, maintain:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._admin = admin
        self._push = push
        self._pull = pull
        self._triage = triage
        self._maintain = maintain
        return
        
    

    
    def _getadmin(self):
        return self._admin
        
    admin = property(_getadmin)

    def _getpush(self):
        return self._push
        
    push = property(_getpush)

    def _getpull(self):
        return self._pull
        
    pull = property(_getpull)

    def _gettriage(self):
        return self._triage
        
    triage = property(_gettriage)

    def _getmaintain(self):
        return self._maintain
        
    maintain = property(_getmaintain)


    
##
##
##
class Collaborator(ResponseBase):
    """Collaborator """
    def __init__(self, site_admin:bool, type:str, received_events_url:str, events_url:str, repos_url:str, organizations_url:str, subscriptions_url:str, starred_url:str, gists_url:str, following_url:str, followers_url:str, html_url:str, url:str, gravatar_id:str, avatar_url:str, node_id:str, id:int, login:str, email:str=None, name:str=None, permissions:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._site_admin = site_admin
        self._type = type
        self._received_events_url = received_events_url
        self._events_url = events_url
        self._repos_url = repos_url
        self._organizations_url = organizations_url
        self._subscriptions_url = subscriptions_url
        self._starred_url = starred_url
        self._gists_url = gists_url
        self._following_url = following_url
        self._followers_url = followers_url
        self._html_url = html_url
        self._url = url
        self._gravatar_id = gravatar_id
        self._avatar_url = avatar_url
        self._node_id = node_id
        self._id = id
        self._login = login
        self._email = email
        self._name = name
        self._permissions = permissions
        return
        
    

    
    def _getsite_admin(self):
        return self._site_admin
        
    site_admin = property(_getsite_admin)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getreceived_events_url(self):
        return self._received_events_url
        
    received_events_url = property(_getreceived_events_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getrepos_url(self):
        return self._repos_url
        
    repos_url = property(_getrepos_url)

    def _getorganizations_url(self):
        return self._organizations_url
        
    organizations_url = property(_getorganizations_url)

    def _getsubscriptions_url(self):
        return self._subscriptions_url
        
    subscriptions_url = property(_getsubscriptions_url)

    def _getstarred_url(self):
        return self._starred_url
        
    starred_url = property(_getstarred_url)

    def _getgists_url(self):
        return self._gists_url
        
    gists_url = property(_getgists_url)

    def _getfollowing_url(self):
        return self._following_url
        
    following_url = property(_getfollowing_url)

    def _getfollowers_url(self):
        return self._followers_url
        
    followers_url = property(_getfollowers_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getgravatar_id(self):
        return self._gravatar_id
        
    gravatar_id = property(_getgravatar_id)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)

    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getpermissions(self):
        return self._permissions and Collaborator_permissions(**self._permissions)
        
    permissions = property(_getpermissions)


    
##
##
##
class RepositoryInvitation(ResponseBase):
    """Repository invitations let you manage who you collaborate with. """
    def __init__(self, node_id:str, html_url:str, url:str, created_at:datetime, permissions:str, inviter:dict, invitee:dict, repository:dict, id:int, expired:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._node_id = node_id
        self._html_url = html_url
        self._url = url
        self._created_at = created_at
        self._permissions = permissions
        self._inviter = inviter
        self._invitee = invitee
        self._repository = repository
        self._id = id
        self._expired = expired
        return
        
    

    
    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl, doc="""URL for the repository invitation """)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getpermissions(self):
        return self._permissions
        
    permissions = property(_getpermissions, doc="""The permission associated with the invitation. """)

    def _getinviter(self):
        return self._inviter and NullableSimpleUser(**self._inviter)
        
    inviter = property(_getinviter)

    def _getinvitee(self):
        return self._invitee and NullableSimpleUser(**self._invitee)
        
    invitee = property(_getinvitee)

    def _getrepository(self):
        return self._repository and MinimalRepository(**self._repository)
        
    repository = property(_getrepository)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the repository invitation. """)

    def _getexpired(self):
        return self._expired
        
    expired = property(_getexpired, doc="""Whether or not the invitation has expired """)


    
##
##
##
class Nullablecollaborator_permissions(ResponseBase):
    def __init__(self, admin:bool, push:bool, pull:bool, triage:bool=None, maintain:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._admin = admin
        self._push = push
        self._pull = pull
        self._triage = triage
        self._maintain = maintain
        return
        
    

    
    def _getadmin(self):
        return self._admin
        
    admin = property(_getadmin)

    def _getpush(self):
        return self._push
        
    push = property(_getpush)

    def _getpull(self):
        return self._pull
        
    pull = property(_getpull)

    def _gettriage(self):
        return self._triage
        
    triage = property(_gettriage)

    def _getmaintain(self):
        return self._maintain
        
    maintain = property(_getmaintain)


    
##
##
##
class NullableCollaborator(ResponseBase):
    """Collaborator """
    def __init__(self, site_admin:bool, type:str, received_events_url:str, events_url:str, repos_url:str, organizations_url:str, subscriptions_url:str, starred_url:str, gists_url:str, following_url:str, followers_url:str, html_url:str, url:str, gravatar_id:str, avatar_url:str, node_id:str, id:int, login:str, email:str=None, name:str=None, permissions:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._site_admin = site_admin
        self._type = type
        self._received_events_url = received_events_url
        self._events_url = events_url
        self._repos_url = repos_url
        self._organizations_url = organizations_url
        self._subscriptions_url = subscriptions_url
        self._starred_url = starred_url
        self._gists_url = gists_url
        self._following_url = following_url
        self._followers_url = followers_url
        self._html_url = html_url
        self._url = url
        self._gravatar_id = gravatar_id
        self._avatar_url = avatar_url
        self._node_id = node_id
        self._id = id
        self._login = login
        self._email = email
        self._name = name
        self._permissions = permissions
        return
        
    

    
    def _getsite_admin(self):
        return self._site_admin
        
    site_admin = property(_getsite_admin)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getreceived_events_url(self):
        return self._received_events_url
        
    received_events_url = property(_getreceived_events_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getrepos_url(self):
        return self._repos_url
        
    repos_url = property(_getrepos_url)

    def _getorganizations_url(self):
        return self._organizations_url
        
    organizations_url = property(_getorganizations_url)

    def _getsubscriptions_url(self):
        return self._subscriptions_url
        
    subscriptions_url = property(_getsubscriptions_url)

    def _getstarred_url(self):
        return self._starred_url
        
    starred_url = property(_getstarred_url)

    def _getgists_url(self):
        return self._gists_url
        
    gists_url = property(_getgists_url)

    def _getfollowing_url(self):
        return self._following_url
        
    following_url = property(_getfollowing_url)

    def _getfollowers_url(self):
        return self._followers_url
        
    followers_url = property(_getfollowers_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getgravatar_id(self):
        return self._gravatar_id
        
    gravatar_id = property(_getgravatar_id)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)

    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getpermissions(self):
        return self._permissions and Nullablecollaborator_permissions(**self._permissions)
        
    permissions = property(_getpermissions)


    
##
##
##
class RepositoryCollaboratorPermission(ResponseBase):
    """Repository Collaborator Permission """
    def __init__(self, user:dict, permission:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._user = user
        self._permission = permission
        return
        
    

    
    def _getuser(self):
        return self._user and NullableCollaborator(**self._user)
        
    user = property(_getuser)

    def _getpermission(self):
        return self._permission
        
    permission = property(_getpermission)


    
##
##
##
class CommitComment(ResponseBase):
    """Commit Comment """
    def __init__(self, author_association:str, updated_at:datetime, created_at:datetime, user:dict, commit_id:str, line:int, position:int, path:str, body:str, node_id:str, id:int, url:str, html_url:str, reactions:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._author_association = author_association
        self._updated_at = updated_at
        self._created_at = created_at
        self._user = user
        self._commit_id = commit_id
        self._line = line
        self._position = position
        self._path = path
        self._body = body
        self._node_id = node_id
        self._id = id
        self._url = url
        self._html_url = html_url
        self._reactions = reactions
        return
        
    

    
    def _getauthor_association(self):
        return self._author_association
        
    author_association = property(_getauthor_association)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getline(self):
        return self._line
        
    line = property(_getline)

    def _getposition(self):
        return self._position
        
    position = property(_getposition)

    def _getpath(self):
        return self._path
        
    path = property(_getpath)

    def _getbody(self):
        return self._body
        
    body = property(_getbody)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getreactions(self):
        return self._reactions and ReactionRollup(**ReactionRollup.patchEntry(self._reactions))
        
    reactions = property(_getreactions)


    
##
##
##
class Branchshort_commit(ResponseBase):
    def __init__(self, url:str, sha:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._sha = sha
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)


    
##
##
##
class BranchShort(ResponseBase):
    """Branch Short """
    def __init__(self, protected:bool, commit:dict, name:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._protected = protected
        self._commit = commit
        self._name = name
        return
        
    

    
    def _getprotected(self):
        return self._protected
        
    protected = property(_getprotected)

    def _getcommit(self):
        return self._commit and Branchshort_commit(**self._commit)
        
    commit = property(_getcommit)

    def _getname(self):
        return self._name
        
    name = property(_getname)


    
##
##
##
class Link(ResponseBase):
    """Hypermedia Link """
    def __init__(self, href:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._href = href
        return
        
    

    
    def _gethref(self):
        return self._href
        
    href = property(_gethref)


    
##
##
##
class Auto_merge(ResponseBase):
    """The status of auto merging a pull request. """
    def __init__(self, commit_message:str, commit_title:str, merge_method:str, enabled_by:dict, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._commit_message = commit_message
        self._commit_title = commit_title
        self._merge_method = merge_method
        self._enabled_by = enabled_by
        return
        
    

    
    def _getcommit_message(self):
        return self._commit_message
        
    commit_message = property(_getcommit_message, doc="""Commit message for the merge commit. """)

    def _getcommit_title(self):
        return self._commit_title
        
    commit_title = property(_getcommit_title, doc="""Title for the merge commit message. """)

    def _getmerge_method(self):
        return self._merge_method
        
    merge_method = property(_getmerge_method, doc="""The merge method to use. """)

    def _getenabled_by(self):
        return self._enabled_by and SimpleUser(**self._enabled_by)
        
    enabled_by = property(_getenabled_by)


    
##
##
##
class Pullrequestsimple_labels(ResponseBase):
    def __init__(self, default:bool, color:str, description:str, name:str, url:str, node_id:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._default = default
        self._color = color
        self._description = description
        self._name = name
        self._url = url
        self._node_id = node_id
        self._id = id
        return
        
    

    
    def _getdefault(self):
        return self._default
        
    default = property(_getdefault)

    def _getcolor(self):
        return self._color
        
    color = property(_getcolor)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class Pullrequestsimple_head(ResponseBase):
    def __init__(self, user:dict, sha:str, repo:dict, ref:str, label:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._user = user
        self._sha = sha
        self._repo = repo
        self._ref = ref
        self._label = label
        return
        
    

    
    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getrepo(self):
        return self._repo and Repository(**self._repo)
        
    repo = property(_getrepo)

    def _getref(self):
        return self._ref
        
    ref = property(_getref)

    def _getlabel(self):
        return self._label
        
    label = property(_getlabel)


    
##
##
##
class Pullrequestsimple_base(ResponseBase):
    def __init__(self, user:dict, sha:str, repo:dict, ref:str, label:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._user = user
        self._sha = sha
        self._repo = repo
        self._ref = ref
        self._label = label
        return
        
    

    
    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getrepo(self):
        return self._repo and Repository(**self._repo)
        
    repo = property(_getrepo)

    def _getref(self):
        return self._ref
        
    ref = property(_getref)

    def _getlabel(self):
        return self._label
        
    label = property(_getlabel)


    
##
##
##
class Pullrequestsimple__links(ResponseBase):
    def __init__(self, Self:dict, review_comment:dict, review_comments:dict, issue:dict, html:dict, statuses:dict, commits:dict, comments:dict, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._Self = Self
        self._review_comment = review_comment
        self._review_comments = review_comments
        self._issue = issue
        self._html = html
        self._statuses = statuses
        self._commits = commits
        self._comments = comments
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['Self'] = entry.pop('self')
        return entry
    

    
    def _getSelf(self):
        return self._Self and Link(**self._Self)
        
    Self = property(_getSelf)

    def _getreview_comment(self):
        return self._review_comment and Link(**self._review_comment)
        
    review_comment = property(_getreview_comment)

    def _getreview_comments(self):
        return self._review_comments and Link(**self._review_comments)
        
    review_comments = property(_getreview_comments)

    def _getissue(self):
        return self._issue and Link(**self._issue)
        
    issue = property(_getissue)

    def _gethtml(self):
        return self._html and Link(**self._html)
        
    html = property(_gethtml)

    def _getstatuses(self):
        return self._statuses and Link(**self._statuses)
        
    statuses = property(_getstatuses)

    def _getcommits(self):
        return self._commits and Link(**self._commits)
        
    commits = property(_getcommits)

    def _getcomments(self):
        return self._comments and Link(**self._comments)
        
    comments = property(_getcomments)


    
    ##
    ##
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

##
##
##
class PullRequestSimple(ResponseBase):
    """Pull Request Simple """
    def __init__(self, auto_merge:dict, author_association:str, _links:dict, base:dict, head:dict, assignee:dict, merge_commit_sha:str, merged_at:datetime, closed_at:datetime, updated_at:datetime, created_at:datetime, milestone:dict, labels:list, body:str, user:dict, title:str, locked:bool, state:str, number:int, statuses_url:str, comments_url:str, review_comment_url:str, review_comments_url:str, commits_url:str, issue_url:str, patch_url:str, diff_url:str, html_url:str, node_id:str, id:int, url:str, active_lock_reason:str=None, assignees:list=[], requested_reviewers:list=[], requested_teams:list=[], draft:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._auto_merge = auto_merge
        self._author_association = author_association
        self.__links = _links
        self._base = base
        self._head = head
        self._assignee = assignee
        self._merge_commit_sha = merge_commit_sha
        self._merged_at = merged_at
        self._closed_at = closed_at
        self._updated_at = updated_at
        self._created_at = created_at
        self._milestone = milestone
        self._labels = labels
        self._body = body
        self._user = user
        self._title = title
        self._locked = locked
        self._state = state
        self._number = number
        self._statuses_url = statuses_url
        self._comments_url = comments_url
        self._review_comment_url = review_comment_url
        self._review_comments_url = review_comments_url
        self._commits_url = commits_url
        self._issue_url = issue_url
        self._patch_url = patch_url
        self._diff_url = diff_url
        self._html_url = html_url
        self._node_id = node_id
        self._id = id
        self._url = url
        self._active_lock_reason = active_lock_reason
        self._assignees = assignees
        self._requested_reviewers = requested_reviewers
        self._requested_teams = requested_teams
        self._draft = draft
        return
        
    

    
    def _getauto_merge(self):
        return self._auto_merge and Auto_merge(**self._auto_merge)
        
    auto_merge = property(_getauto_merge)

    def _getauthor_association(self):
        return self._author_association
        
    author_association = property(_getauthor_association)

    def _get_links(self):
        return self.__links and Pullrequestsimple__links(**Pullrequestsimple__links.patchEntry(self.__links))
        
    _links = property(_get_links)

    def _getbase(self):
        return self._base and Pullrequestsimple_base(**self._base)
        
    base = property(_getbase)

    def _gethead(self):
        return self._head and Pullrequestsimple_head(**self._head)
        
    head = property(_gethead)

    def _getassignee(self):
        return self._assignee and NullableSimpleUser(**self._assignee)
        
    assignee = property(_getassignee)

    def _getmerge_commit_sha(self):
        return self._merge_commit_sha
        
    merge_commit_sha = property(_getmerge_commit_sha)

    def _getmerged_at(self):
        return self._merged_at and datetime.datetime.fromisoformat(self._merged_at[0:-1])
        
    merged_at = property(_getmerged_at)

    def _getclosed_at(self):
        return self._closed_at and datetime.datetime.fromisoformat(self._closed_at[0:-1])
        
    closed_at = property(_getclosed_at)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getmilestone(self):
        return self._milestone and NullableMilestone(**self._milestone)
        
    milestone = property(_getmilestone)

    def _getlabels(self):
        return self._labels and [ entry and Pullrequestsimple_labels(**entry) for entry in self._labels ]
        
    labels = property(_getlabels)

    def _getbody(self):
        return self._body
        
    body = property(_getbody)

    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle)

    def _getlocked(self):
        return self._locked
        
    locked = property(_getlocked)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)

    def _getnumber(self):
        return self._number
        
    number = property(_getnumber)

    def _getstatuses_url(self):
        return self._statuses_url
        
    statuses_url = property(_getstatuses_url)

    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _getreview_comment_url(self):
        return self._review_comment_url
        
    review_comment_url = property(_getreview_comment_url)

    def _getreview_comments_url(self):
        return self._review_comments_url
        
    review_comments_url = property(_getreview_comments_url)

    def _getcommits_url(self):
        return self._commits_url
        
    commits_url = property(_getcommits_url)

    def _getissue_url(self):
        return self._issue_url
        
    issue_url = property(_getissue_url)

    def _getpatch_url(self):
        return self._patch_url
        
    patch_url = property(_getpatch_url)

    def _getdiff_url(self):
        return self._diff_url
        
    diff_url = property(_getdiff_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getactive_lock_reason(self):
        return self._active_lock_reason
        
    active_lock_reason = property(_getactive_lock_reason)

    def _getassignees(self):
        return self._assignees and [ entry and SimpleUser(**entry) for entry in self._assignees ]
        
    assignees = property(_getassignees)

    def _getrequested_reviewers(self):
        return self._requested_reviewers and [ entry and SimpleUser(**entry) for entry in self._requested_reviewers ]
        
    requested_reviewers = property(_getrequested_reviewers)

    def _getrequested_teams(self):
        return self._requested_teams and [ entry and Team(**entry) for entry in self._requested_teams ]
        
    requested_teams = property(_getrequested_teams)

    def _getdraft(self):
        return self._draft
        
    draft = property(_getdraft, doc="""Indicates whether or not the pull request is a draft. """)


    
##
##
##
class SimpleCommitStatus(ResponseBase):
    def __init__(self, updated_at:datetime, created_at:datetime, url:str, avatar_url:str, target_url:str, context:str, state:str, node_id:str, id:int, description:str, required:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._updated_at = updated_at
        self._created_at = created_at
        self._url = url
        self._avatar_url = avatar_url
        self._target_url = target_url
        self._context = context
        self._state = state
        self._node_id = node_id
        self._id = id
        self._description = description
        self._required = required
        return
        
    

    
    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)

    def _gettarget_url(self):
        return self._target_url
        
    target_url = property(_gettarget_url)

    def _getcontext(self):
        return self._context
        
    context = property(_getcontext)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getrequired(self):
        return self._required
        
    required = property(_getrequired)


    
##
##
##
class CombinedCommitStatus(ResponseBase):
    """Combined Commit Status """
    def __init__(self, url:str, commit_url:str, repository:dict, total_count:int, sha:str, statuses:list, state:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._commit_url = commit_url
        self._repository = repository
        self._total_count = total_count
        self._sha = sha
        self._statuses = statuses
        self._state = state
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url)

    def _getrepository(self):
        return self._repository and MinimalRepository(**self._repository)
        
    repository = property(_getrepository)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getstatuses(self):
        return self._statuses and [ entry and SimpleCommitStatus(**entry) for entry in self._statuses ]
        
    statuses = property(_getstatuses)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)


    
##
##
##
class Status(ResponseBase):
    """The status of a commit. """
    def __init__(self, creator:dict, updated_at:str, created_at:str, context:str, target_url:str, description:str, state:str, node_id:str, id:int, avatar_url:str, url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._creator = creator
        self._updated_at = updated_at
        self._created_at = created_at
        self._context = context
        self._target_url = target_url
        self._description = description
        self._state = state
        self._node_id = node_id
        self._id = id
        self._avatar_url = avatar_url
        self._url = url
        return
        
    

    
    def _getcreator(self):
        return self._creator and NullableSimpleUser(**self._creator)
        
    creator = property(_getcreator)

    def _getupdated_at(self):
        return self._updated_at
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getcontext(self):
        return self._context
        
    context = property(_getcontext)

    def _gettarget_url(self):
        return self._target_url
        
    target_url = property(_gettarget_url)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class CommitComparison(ResponseBase):
    """Commit Comparison """
    def __init__(self, commits:list, total_commits:int, behind_by:int, ahead_by:int, status:str, merge_base_commit:dict, base_commit:dict, patch_url:str, diff_url:str, permalink_url:str, html_url:str, url:str, files:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._commits = commits
        self._total_commits = total_commits
        self._behind_by = behind_by
        self._ahead_by = ahead_by
        self._status = status
        self._merge_base_commit = merge_base_commit
        self._base_commit = base_commit
        self._patch_url = patch_url
        self._diff_url = diff_url
        self._permalink_url = permalink_url
        self._html_url = html_url
        self._url = url
        self._files = files
        return
        
    

    
    def _getcommits(self):
        return self._commits and [ entry and Commit(**entry) for entry in self._commits ]
        
    commits = property(_getcommits)

    def _gettotal_commits(self):
        return self._total_commits
        
    total_commits = property(_gettotal_commits)

    def _getbehind_by(self):
        return self._behind_by
        
    behind_by = property(_getbehind_by)

    def _getahead_by(self):
        return self._ahead_by
        
    ahead_by = property(_getahead_by)

    def _getstatus(self):
        return self._status
        
    status = property(_getstatus)

    def _getmerge_base_commit(self):
        return self._merge_base_commit and Commit(**self._merge_base_commit)
        
    merge_base_commit = property(_getmerge_base_commit)

    def _getbase_commit(self):
        return self._base_commit and Commit(**self._base_commit)
        
    base_commit = property(_getbase_commit)

    def _getpatch_url(self):
        return self._patch_url
        
    patch_url = property(_getpatch_url)

    def _getdiff_url(self):
        return self._diff_url
        
    diff_url = property(_getdiff_url)

    def _getpermalink_url(self):
        return self._permalink_url
        
    permalink_url = property(_getpermalink_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getfiles(self):
        return self._files and [ entry and DiffEntry(**entry) for entry in self._files ]
        
    files = property(_getfiles)


    
##
##
##
class Contentreferenceattachment(ResponseBase):
    """Content Reference attachments allow you to provide context around URLs posted in comments """
    def __init__(self, body:str, title:str, id:int, node_id:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._body = body
        self._title = title
        self._id = id
        self._node_id = node_id
        return
        
    

    
    def _getbody(self):
        return self._body
        
    body = property(_getbody, doc="""The body of the attachment """)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle, doc="""The title of the attachment """)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""The ID of the attachment """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id, doc="""The node_id of the content attachment """)


    
##
##
##
class Contenttree_entries__links(ResponseBase):
    def __init__(self, Self:str, html:str, git:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._Self = Self
        self._html = html
        self._git = git
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['Self'] = entry.pop('self')
        return entry
    

    
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

    def _gethtml(self):
        return self._html
        
    html = property(_gethtml)

    def _getgit(self):
        return self._git
        
    git = property(_getgit)


    
    ##
    ##
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

##
##
##
class Contenttree_entries(ResponseBase):
    def __init__(self, _links:dict, download_url:str, html_url:str, git_url:str, url:str, sha:str, path:str, name:str, size:int, type:str, content:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self.__links = _links
        self._download_url = download_url
        self._html_url = html_url
        self._git_url = git_url
        self._url = url
        self._sha = sha
        self._path = path
        self._name = name
        self._size = size
        self._type = type
        self._content = content
        return
        
    

    
    def _get_links(self):
        return self.__links and Contenttree_entries__links(**Contenttree_entries__links.patchEntry(self.__links))
        
    _links = property(_get_links)

    def _getdownload_url(self):
        return self._download_url
        
    download_url = property(_getdownload_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getgit_url(self):
        return self._git_url
        
    git_url = property(_getgit_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getpath(self):
        return self._path
        
    path = property(_getpath)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getcontent(self):
        return self._content
        
    content = property(_getcontent)


    
##
##
##
class Contenttree__links(ResponseBase):
    def __init__(self, Self:str, html:str, git:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._Self = Self
        self._html = html
        self._git = git
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['Self'] = entry.pop('self')
        return entry
    

    
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

    def _gethtml(self):
        return self._html
        
    html = property(_gethtml)

    def _getgit(self):
        return self._git
        
    git = property(_getgit)


    
    ##
    ##
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

##
##
##
class ContentTree(ResponseBase):
    """Content Tree """
    def __init__(self, _links:dict, download_url:str, html_url:str, git_url:str, url:str, sha:str, path:str, name:str, size:int, type:str, entries:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self.__links = _links
        self._download_url = download_url
        self._html_url = html_url
        self._git_url = git_url
        self._url = url
        self._sha = sha
        self._path = path
        self._name = name
        self._size = size
        self._type = type
        self._entries = entries
        return
        
    

    
    def _get_links(self):
        return self.__links and Contenttree__links(**Contenttree__links.patchEntry(self.__links))
        
    _links = property(_get_links)

    def _getdownload_url(self):
        return self._download_url
        
    download_url = property(_getdownload_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getgit_url(self):
        return self._git_url
        
    git_url = property(_getgit_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getpath(self):
        return self._path
        
    path = property(_getpath)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getentries(self):
        return self._entries and [ entry and Contenttree_entries(**entry) for entry in self._entries ]
        
    entries = property(_getentries)


    
##
##
##
class Contentdirectory__links(ResponseBase):
    def __init__(self, Self:str, html:str, git:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._Self = Self
        self._html = html
        self._git = git
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['Self'] = entry.pop('self')
        return entry
    

    
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

    def _gethtml(self):
        return self._html
        
    html = property(_gethtml)

    def _getgit(self):
        return self._git
        
    git = property(_getgit)


    
    ##
    ##
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

##
##
##
class Contentdirectory(ResponseBase):
    def __init__(self, _links:dict, download_url:str, html_url:str, git_url:str, url:str, sha:str, path:str, name:str, size:int, type:str, content:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self.__links = _links
        self._download_url = download_url
        self._html_url = html_url
        self._git_url = git_url
        self._url = url
        self._sha = sha
        self._path = path
        self._name = name
        self._size = size
        self._type = type
        self._content = content
        return
        
    

    
    def _get_links(self):
        return self.__links and Contentdirectory__links(**Contentdirectory__links.patchEntry(self.__links))
        
    _links = property(_get_links)

    def _getdownload_url(self):
        return self._download_url
        
    download_url = property(_getdownload_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getgit_url(self):
        return self._git_url
        
    git_url = property(_getgit_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getpath(self):
        return self._path
        
    path = property(_getpath)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getcontent(self):
        return self._content
        
    content = property(_getcontent)


    
##
##
##
class Contentfile__links(ResponseBase):
    def __init__(self, Self:str, html:str, git:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._Self = Self
        self._html = html
        self._git = git
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['Self'] = entry.pop('self')
        return entry
    

    
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

    def _gethtml(self):
        return self._html
        
    html = property(_gethtml)

    def _getgit(self):
        return self._git
        
    git = property(_getgit)


    
    ##
    ##
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

##
##
##
class ContentFile(ResponseBase):
    """Content File """
    def __init__(self, _links:dict, download_url:str, html_url:str, git_url:str, url:str, sha:str, content:str, path:str, name:str, size:int, encoding:str, type:str, target:str=None, submodule_git_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self.__links = _links
        self._download_url = download_url
        self._html_url = html_url
        self._git_url = git_url
        self._url = url
        self._sha = sha
        self._content = content
        self._path = path
        self._name = name
        self._size = size
        self._encoding = encoding
        self._type = type
        self._target = target
        self._submodule_git_url = submodule_git_url
        return
        
    

    
    def _get_links(self):
        return self.__links and Contentfile__links(**Contentfile__links.patchEntry(self.__links))
        
    _links = property(_get_links)

    def _getdownload_url(self):
        return self._download_url
        
    download_url = property(_getdownload_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getgit_url(self):
        return self._git_url
        
    git_url = property(_getgit_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getcontent(self):
        return self._content
        
    content = property(_getcontent)

    def _getpath(self):
        return self._path
        
    path = property(_getpath)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _getencoding(self):
        return self._encoding
        
    encoding = property(_getencoding)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _gettarget(self):
        return self._target
        
    target = property(_gettarget)

    def _getsubmodule_git_url(self):
        return self._submodule_git_url
        
    submodule_git_url = property(_getsubmodule_git_url)


    
##
##
##
class Symlinkcontent__links(ResponseBase):
    def __init__(self, Self:str, html:str, git:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._Self = Self
        self._html = html
        self._git = git
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['Self'] = entry.pop('self')
        return entry
    

    
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

    def _gethtml(self):
        return self._html
        
    html = property(_gethtml)

    def _getgit(self):
        return self._git
        
    git = property(_getgit)


    
    ##
    ##
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

##
##
##
class SymlinkContent(ResponseBase):
    """An object describing a symlink """
    def __init__(self, _links:dict, download_url:str, html_url:str, git_url:str, url:str, sha:str, path:str, name:str, size:int, target:str, type:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self.__links = _links
        self._download_url = download_url
        self._html_url = html_url
        self._git_url = git_url
        self._url = url
        self._sha = sha
        self._path = path
        self._name = name
        self._size = size
        self._target = target
        self._type = type
        return
        
    

    
    def _get_links(self):
        return self.__links and Symlinkcontent__links(**Symlinkcontent__links.patchEntry(self.__links))
        
    _links = property(_get_links)

    def _getdownload_url(self):
        return self._download_url
        
    download_url = property(_getdownload_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getgit_url(self):
        return self._git_url
        
    git_url = property(_getgit_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getpath(self):
        return self._path
        
    path = property(_getpath)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _gettarget(self):
        return self._target
        
    target = property(_gettarget)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)


    
##
##
##
class Contentsubmodule__links(ResponseBase):
    def __init__(self, Self:str, html:str, git:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._Self = Self
        self._html = html
        self._git = git
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['Self'] = entry.pop('self')
        return entry
    

    
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

    def _gethtml(self):
        return self._html
        
    html = property(_gethtml)

    def _getgit(self):
        return self._git
        
    git = property(_getgit)


    
    ##
    ##
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

##
##
##
class ContentSubmodule(ResponseBase):
    """An object describing a symlink """
    def __init__(self, _links:dict, download_url:str, html_url:str, git_url:str, url:str, sha:str, path:str, name:str, size:int, submodule_git_url:str, type:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self.__links = _links
        self._download_url = download_url
        self._html_url = html_url
        self._git_url = git_url
        self._url = url
        self._sha = sha
        self._path = path
        self._name = name
        self._size = size
        self._submodule_git_url = submodule_git_url
        self._type = type
        return
        
    

    
    def _get_links(self):
        return self.__links and Contentsubmodule__links(**Contentsubmodule__links.patchEntry(self.__links))
        
    _links = property(_get_links)

    def _getdownload_url(self):
        return self._download_url
        
    download_url = property(_getdownload_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getgit_url(self):
        return self._git_url
        
    git_url = property(_getgit_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getpath(self):
        return self._path
        
    path = property(_getpath)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _getsubmodule_git_url(self):
        return self._submodule_git_url
        
    submodule_git_url = property(_getsubmodule_git_url)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)


    
##
##
##
class Filecommit_content__links(ResponseBase):
    def __init__(self, Self:str=None, git:str=None, html:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._Self = Self
        self._git = git
        self._html = html
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['Self'] = entry.pop('self')
        return entry
    

    
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

    def _getgit(self):
        return self._git
        
    git = property(_getgit)

    def _gethtml(self):
        return self._html
        
    html = property(_gethtml)


    
    ##
    ##
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

##
##
##
class Filecommit_content(ResponseBase):
    def __init__(self, name:str=None, path:str=None, sha:str=None, size:int=None, url:str=None, html_url:str=None, git_url:str=None, download_url:str=None, type:str=None, _links:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._name = name
        self._path = path
        self._sha = sha
        self._size = size
        self._url = url
        self._html_url = html_url
        self._git_url = git_url
        self._download_url = download_url
        self._type = type
        self.__links = _links
        return
        
    

    
    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getpath(self):
        return self._path
        
    path = property(_getpath)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getgit_url(self):
        return self._git_url
        
    git_url = property(_getgit_url)

    def _getdownload_url(self):
        return self._download_url
        
    download_url = property(_getdownload_url)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _get_links(self):
        return self.__links and Filecommit_content__links(**Filecommit_content__links.patchEntry(self.__links))
        
    _links = property(_get_links)


    
##
##
##
class Filecommit_commit_author(ResponseBase):
    def __init__(self, date:str=None, name:str=None, email:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._date = date
        self._name = name
        self._email = email
        return
        
    

    
    def _getdate(self):
        return self._date
        
    date = property(_getdate)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getemail(self):
        return self._email
        
    email = property(_getemail)


    
##
##
##
class Filecommit_commit_committer(ResponseBase):
    def __init__(self, date:str=None, name:str=None, email:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._date = date
        self._name = name
        self._email = email
        return
        
    

    
    def _getdate(self):
        return self._date
        
    date = property(_getdate)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getemail(self):
        return self._email
        
    email = property(_getemail)


    
##
##
##
class Filecommit_commit_tree(ResponseBase):
    def __init__(self, url:str=None, sha:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._sha = sha
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)


    
##
##
##
class Filecommit_commit_parents(ResponseBase):
    def __init__(self, url:str=None, html_url:str=None, sha:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._html_url = html_url
        self._sha = sha
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)


    
##
##
##
class Filecommit_commit_verification(ResponseBase):
    def __init__(self, verified:bool=None, reason:str=None, signature:str=None, payload:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._verified = verified
        self._reason = reason
        self._signature = signature
        self._payload = payload
        return
        
    

    
    def _getverified(self):
        return self._verified
        
    verified = property(_getverified)

    def _getreason(self):
        return self._reason
        
    reason = property(_getreason)

    def _getsignature(self):
        return self._signature
        
    signature = property(_getsignature)

    def _getpayload(self):
        return self._payload
        
    payload = property(_getpayload)


    
##
##
##
class Filecommit_commit(ResponseBase):
    def __init__(self, sha:str=None, node_id:str=None, url:str=None, html_url:str=None, author:dict=None, committer:dict=None, message:str=None, tree:dict=None, parents:list=[], verification:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._sha = sha
        self._node_id = node_id
        self._url = url
        self._html_url = html_url
        self._author = author
        self._committer = committer
        self._message = message
        self._tree = tree
        self._parents = parents
        self._verification = verification
        return
        
    

    
    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getauthor(self):
        return self._author and Filecommit_commit_author(**self._author)
        
    author = property(_getauthor)

    def _getcommitter(self):
        return self._committer and Filecommit_commit_committer(**self._committer)
        
    committer = property(_getcommitter)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _gettree(self):
        return self._tree and Filecommit_commit_tree(**self._tree)
        
    tree = property(_gettree)

    def _getparents(self):
        return self._parents and [ entry and Filecommit_commit_parents(**entry) for entry in self._parents ]
        
    parents = property(_getparents)

    def _getverification(self):
        return self._verification and Filecommit_commit_verification(**self._verification)
        
    verification = property(_getverification)


    
##
##
##
class FileCommit(ResponseBase):
    """File Commit """
    def __init__(self, commit:dict, content:dict, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._commit = commit
        self._content = content
        return
        
    

    
    def _getcommit(self):
        return self._commit and Filecommit_commit(**self._commit)
        
    commit = property(_getcommit)

    def _getcontent(self):
        return self._content and Filecommit_content(**self._content)
        
    content = property(_getcontent)


    
##
##
##
class Contributor(ResponseBase):
    """Contributor """
    def __init__(self, contributions:int, type:str, login:str=None, id:int=None, node_id:str=None, avatar_url:str=None, gravatar_id:str=None, url:str=None, html_url:str=None, followers_url:str=None, following_url:str=None, gists_url:str=None, starred_url:str=None, subscriptions_url:str=None, organizations_url:str=None, repos_url:str=None, events_url:str=None, received_events_url:str=None, site_admin:bool=None, email:str=None, name:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._contributions = contributions
        self._type = type
        self._login = login
        self._id = id
        self._node_id = node_id
        self._avatar_url = avatar_url
        self._gravatar_id = gravatar_id
        self._url = url
        self._html_url = html_url
        self._followers_url = followers_url
        self._following_url = following_url
        self._gists_url = gists_url
        self._starred_url = starred_url
        self._subscriptions_url = subscriptions_url
        self._organizations_url = organizations_url
        self._repos_url = repos_url
        self._events_url = events_url
        self._received_events_url = received_events_url
        self._site_admin = site_admin
        self._email = email
        self._name = name
        return
        
    

    
    def _getcontributions(self):
        return self._contributions
        
    contributions = property(_getcontributions)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)

    def _getgravatar_id(self):
        return self._gravatar_id
        
    gravatar_id = property(_getgravatar_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getfollowers_url(self):
        return self._followers_url
        
    followers_url = property(_getfollowers_url)

    def _getfollowing_url(self):
        return self._following_url
        
    following_url = property(_getfollowing_url)

    def _getgists_url(self):
        return self._gists_url
        
    gists_url = property(_getgists_url)

    def _getstarred_url(self):
        return self._starred_url
        
    starred_url = property(_getstarred_url)

    def _getsubscriptions_url(self):
        return self._subscriptions_url
        
    subscriptions_url = property(_getsubscriptions_url)

    def _getorganizations_url(self):
        return self._organizations_url
        
    organizations_url = property(_getorganizations_url)

    def _getrepos_url(self):
        return self._repos_url
        
    repos_url = property(_getrepos_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getreceived_events_url(self):
        return self._received_events_url
        
    received_events_url = property(_getreceived_events_url)

    def _getsite_admin(self):
        return self._site_admin
        
    site_admin = property(_getsite_admin)

    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _getname(self):
        return self._name
        
    name = property(_getname)


    
##
##
##
class DeploymentStatus(ResponseBase):
    """The status of a deployment. """
    def __init__(self, repository_url:str, deployment_url:str, updated_at:datetime, created_at:datetime, creator:dict, state:str, node_id:str, id:int, url:str, description:str='""', environment:str='""', target_url:str='""', environment_url:str='""', log_url:str='""', performed_via_github_app:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._repository_url = repository_url
        self._deployment_url = deployment_url
        self._updated_at = updated_at
        self._created_at = created_at
        self._creator = creator
        self._state = state
        self._node_id = node_id
        self._id = id
        self._url = url
        self._description = description
        self._environment = environment
        self._target_url = target_url
        self._environment_url = environment_url
        self._log_url = log_url
        self._performed_via_github_app = performed_via_github_app
        return
        
    

    
    def _getrepository_url(self):
        return self._repository_url
        
    repository_url = property(_getrepository_url)

    def _getdeployment_url(self):
        return self._deployment_url
        
    deployment_url = property(_getdeployment_url)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getcreator(self):
        return self._creator and NullableSimpleUser(**self._creator)
        
    creator = property(_getcreator)

    def _getstate(self):
        return self._state
        
    state = property(_getstate, doc="""The state of the status. """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription, doc="""A short description of the status. """)

    def _getenvironment(self):
        return self._environment
        
    environment = property(_getenvironment, doc="""The environment of the deployment that the status is for. """)

    def _gettarget_url(self):
        return self._target_url
        
    target_url = property(_gettarget_url, doc="""Deprecated: the URL to associate with this status. """)

    def _getenvironment_url(self):
        return self._environment_url
        
    environment_url = property(_getenvironment_url, doc="""The URL for accessing your environment. """)

    def _getlog_url(self):
        return self._log_url
        
    log_url = property(_getlog_url, doc="""The URL to associate with this status. """)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)


    
##
##
##
class Deployment_branch_policy(ResponseBase):
    """The type of deployment branch policy for this environment. To allow all branches to deploy, set to `null`. """
    def __init__(self, custom_branch_policies:bool, protected_branches:bool, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._custom_branch_policies = custom_branch_policies
        self._protected_branches = protected_branches
        return
        
    

    
    def _getcustom_branch_policies(self):
        return self._custom_branch_policies
        
    custom_branch_policies = property(_getcustom_branch_policies, doc="""Whether only branches that match the specified name patterns can deploy to this environment.  If `custom_branch_policies` is `true`, `protected_branches` must be `false`; if `custom_branch_policies` is `false`, `protected_branches` must be `true`. """)

    def _getprotected_branches(self):
        return self._protected_branches
        
    protected_branches = property(_getprotected_branches, doc="""Whether only branches with branch protection rules can deploy to this environment. If `protected_branches` is `true`, `custom_branch_policies` must be `false`; if `protected_branches` is `false`, `custom_branch_policies` must be `true`. """)


    
##
##
##
class Environment_protection_rules(ResponseBase):
    def __init__(self, type:str, node_id:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._type = type
        self._node_id = node_id
        self._id = id
        return
        
    

    
    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class Environment_protection_rules_reviewers(ResponseBase):
    def __init__(self, type:str=None, reviewer=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._type = type
        self._reviewer = reviewer
        return
        
    

    
    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getreviewer(self):
        return self._reviewer
        
    reviewer = property(_getreviewer)


    
##
##
##
class Environment(ResponseBase):
    """Details of a deployment environment """
    def __init__(self, updated_at:datetime, created_at:datetime, html_url:str, url:str, name:str, node_id:str, id:int, protection_rules:list=[], deployment_branch_policy:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._updated_at = updated_at
        self._created_at = created_at
        self._html_url = html_url
        self._url = url
        self._name = name
        self._node_id = node_id
        self._id = id
        self._protection_rules = protection_rules
        self._deployment_branch_policy = deployment_branch_policy
        return
        
    

    
    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at, doc="""The time that the environment was last updated, in ISO 8601 format. """)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at, doc="""The time that the environment was created, in ISO 8601 format. """)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the environment. """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""The id of the environment. """)

    def _getprotection_rules(self):
        return self._protection_rules and [ entry for entry in self._protection_rules ]
        
    protection_rules = property(_getprotection_rules)

    def _getdeployment_branch_policy(self):
        return self._deployment_branch_policy and Deployment_branch_policy(**self._deployment_branch_policy)
        
    deployment_branch_policy = property(_getdeployment_branch_policy)


    
##
##
##
class ShortBlob(ResponseBase):
    """Short Blob """
    def __init__(self, sha:str, url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._sha = sha
        self._url = url
        return
        
    

    
    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class Blob(ResponseBase):
    """Blob """
    def __init__(self, node_id:str, size:int, sha:str, url:str, encoding:str, content:str, highlighted_content:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._node_id = node_id
        self._size = size
        self._sha = sha
        self._url = url
        self._encoding = encoding
        self._content = content
        self._highlighted_content = highlighted_content
        return
        
    

    
    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getencoding(self):
        return self._encoding
        
    encoding = property(_getencoding)

    def _getcontent(self):
        return self._content
        
    content = property(_getcontent)

    def _gethighlighted_content(self):
        return self._highlighted_content
        
    highlighted_content = property(_gethighlighted_content)


    
##
##
##
class Gitcommit_author(ResponseBase):
    """Identifying information for the git-user """
    def __init__(self, name:str, email:str, date:datetime, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._name = name
        self._email = email
        self._date = date
        return
        
    

    
    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""Name of the git user """)

    def _getemail(self):
        return self._email
        
    email = property(_getemail, doc="""Git email address of the user """)

    def _getdate(self):
        return self._date and datetime.datetime.fromisoformat(self._date[0:-1])
        
    date = property(_getdate, doc="""Timestamp of the commit """)


    
##
##
##
class Gitcommit_committer(ResponseBase):
    """Identifying information for the git-user """
    def __init__(self, name:str, email:str, date:datetime, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._name = name
        self._email = email
        self._date = date
        return
        
    

    
    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""Name of the git user """)

    def _getemail(self):
        return self._email
        
    email = property(_getemail, doc="""Git email address of the user """)

    def _getdate(self):
        return self._date and datetime.datetime.fromisoformat(self._date[0:-1])
        
    date = property(_getdate, doc="""Timestamp of the commit """)


    
##
##
##
class Gitcommit_tree(ResponseBase):
    def __init__(self, url:str, sha:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._sha = sha
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha, doc="""SHA for the commit """)


    
##
##
##
class Gitcommit_parents(ResponseBase):
    def __init__(self, html_url:str, url:str, sha:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._html_url = html_url
        self._url = url
        self._sha = sha
        return
        
    

    
    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha, doc="""SHA for the commit """)


    
##
##
##
class Gitcommit_verification(ResponseBase):
    def __init__(self, payload:str, signature:str, reason:str, verified:bool, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._payload = payload
        self._signature = signature
        self._reason = reason
        self._verified = verified
        return
        
    

    
    def _getpayload(self):
        return self._payload
        
    payload = property(_getpayload)

    def _getsignature(self):
        return self._signature
        
    signature = property(_getsignature)

    def _getreason(self):
        return self._reason
        
    reason = property(_getreason)

    def _getverified(self):
        return self._verified
        
    verified = property(_getverified)


    
##
##
##
class GitCommit(ResponseBase):
    """Low-level Git commit operations within a repository """
    def __init__(self, html_url:str, verification:dict, parents:list, tree:dict, message:str, committer:dict, author:dict, url:str, node_id:str, sha:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._html_url = html_url
        self._verification = verification
        self._parents = parents
        self._tree = tree
        self._message = message
        self._committer = committer
        self._author = author
        self._url = url
        self._node_id = node_id
        self._sha = sha
        return
        
    

    
    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getverification(self):
        return self._verification and Gitcommit_verification(**self._verification)
        
    verification = property(_getverification)

    def _getparents(self):
        return self._parents and [ entry and Gitcommit_parents(**entry) for entry in self._parents ]
        
    parents = property(_getparents)

    def _gettree(self):
        return self._tree and Gitcommit_tree(**self._tree)
        
    tree = property(_gettree)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage, doc="""Message describing the purpose of the commit """)

    def _getcommitter(self):
        return self._committer and Gitcommit_committer(**self._committer)
        
    committer = property(_getcommitter, doc="""Identifying information for the git-user """)

    def _getauthor(self):
        return self._author and Gitcommit_author(**self._author)
        
    author = property(_getauthor, doc="""Identifying information for the git-user """)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha, doc="""SHA for the commit """)


    
##
##
##
class Gitreference_object(ResponseBase):
    def __init__(self, url:str, sha:str, type:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._sha = sha
        self._type = type
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha, doc="""SHA for the reference """)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)


    
##
##
##
class GitReference(ResponseBase):
    """Git references within a repository """
    def __init__(self, object:dict, url:str, node_id:str, ref:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._object = object
        self._url = url
        self._node_id = node_id
        self._ref = ref
        return
        
    

    
    def _getobject(self):
        return self._object and Gitreference_object(**self._object)
        
    object = property(_getobject)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getref(self):
        return self._ref
        
    ref = property(_getref)


    
##
##
##
class Gittag_tagger(ResponseBase):
    def __init__(self, name:str, email:str, date:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._name = name
        self._email = email
        self._date = date
        return
        
    

    
    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _getdate(self):
        return self._date
        
    date = property(_getdate)


    
##
##
##
class Gittag_object(ResponseBase):
    def __init__(self, url:str, type:str, sha:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._type = type
        self._sha = sha
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)


    
##
##
##
class GitTag(ResponseBase):
    """Metadata for a Git tag """
    def __init__(self, object:dict, tagger:dict, message:str, url:str, sha:str, tag:str, node_id:str, verification:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._object = object
        self._tagger = tagger
        self._message = message
        self._url = url
        self._sha = sha
        self._tag = tag
        self._node_id = node_id
        self._verification = verification
        return
        
    

    
    def _getobject(self):
        return self._object and Gittag_object(**self._object)
        
    object = property(_getobject)

    def _gettagger(self):
        return self._tagger and Gittag_tagger(**self._tagger)
        
    tagger = property(_gettagger)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage, doc="""Message describing the purpose of the tag """)

    def _geturl(self):
        return self._url
        
    url = property(_geturl, doc="""URL for the tag """)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _gettag(self):
        return self._tag
        
    tag = property(_gettag, doc="""Name of the tag """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getverification(self):
        return self._verification and Verification(**self._verification)
        
    verification = property(_getverification)


    
##
##
##
class Gittree_tree(ResponseBase):
    def __init__(self, path:str=None, mode:str=None, type:str=None, sha:str=None, size:int=None, url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._path = path
        self._mode = mode
        self._type = type
        self._sha = sha
        self._size = size
        self._url = url
        return
        
    

    
    def _getpath(self):
        return self._path
        
    path = property(_getpath)

    def _getmode(self):
        return self._mode
        
    mode = property(_getmode)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class GitTree(ResponseBase):
    """The hierarchy between files in a Git repository. """
    def __init__(self, tree:list, truncated:bool, url:str, sha:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._tree = tree
        self._truncated = truncated
        self._url = url
        self._sha = sha
        return
        
    

    
    def _gettree(self):
        return self._tree and [ entry and Gittree_tree(**entry) for entry in self._tree ]
        
    tree = property(_gettree, doc="""Objects specifying a tree structure """)

    def _gettruncated(self):
        return self._truncated
        
    truncated = property(_gettruncated)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)


    
##
##
##
class HookResponse(ResponseBase):
    def __init__(self, message:str, status:str, code:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._status = status
        self._code = code
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getstatus(self):
        return self._status
        
    status = property(_getstatus)

    def _getcode(self):
        return self._code
        
    code = property(_getcode)


    
##
##
##
class Webhook_config(ResponseBase):
    def __init__(self, email:str=None, password:str=None, room:str=None, subdomain:str=None, url:str=None, insecure_ssl=None, content_type:str=None, digest:str=None, secret:str=None, token:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._email = email
        self._password = password
        self._room = room
        self._subdomain = subdomain
        self._url = url
        self._insecure_ssl = insecure_ssl
        self._content_type = content_type
        self._digest = digest
        self._secret = secret
        self._token = token
        return
        
    

    
    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _getpassword(self):
        return self._password
        
    password = property(_getpassword)

    def _getroom(self):
        return self._room
        
    room = property(_getroom)

    def _getsubdomain(self):
        return self._subdomain
        
    subdomain = property(_getsubdomain)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getinsecure_ssl(self):
        return self._insecure_ssl
        
    insecure_ssl = property(_getinsecure_ssl)

    def _getcontent_type(self):
        return self._content_type
        
    content_type = property(_getcontent_type)

    def _getdigest(self):
        return self._digest
        
    digest = property(_getdigest)

    def _getsecret(self):
        return self._secret
        
    secret = property(_getsecret)

    def _gettoken(self):
        return self._token
        
    token = property(_gettoken)


    
##
##
##
class Webhook(ResponseBase):
    """Webhooks for repositories. """
    def __init__(self, last_response:dict, ping_url:str, test_url:str, url:str, created_at:datetime, updated_at:datetime, config:dict, events:list, active:bool, name:str, id:int, type:str, deliveries_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._last_response = last_response
        self._ping_url = ping_url
        self._test_url = test_url
        self._url = url
        self._created_at = created_at
        self._updated_at = updated_at
        self._config = config
        self._events = events
        self._active = active
        self._name = name
        self._id = id
        self._type = type
        self._deliveries_url = deliveries_url
        return
        
    

    
    def _getlast_response(self):
        return self._last_response and HookResponse(**self._last_response)
        
    last_response = property(_getlast_response)

    def _getping_url(self):
        return self._ping_url
        
    ping_url = property(_getping_url)

    def _gettest_url(self):
        return self._test_url
        
    test_url = property(_gettest_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getconfig(self):
        return self._config and Webhook_config(**self._config)
        
    config = property(_getconfig)

    def _getevents(self):
        return self._events and [ entry for entry in self._events ]
        
    events = property(_getevents, doc="""Determines what events the hook is triggered for. Default: ['push']. """)

    def _getactive(self):
        return self._active
        
    active = property(_getactive, doc="""Determines whether the hook is actually triggered on pushes. """)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of a valid service, use 'web' for a webhook. """)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the webhook. """)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getdeliveries_url(self):
        return self._deliveries_url
        
    deliveries_url = property(_getdeliveries_url)


    
##
##
##
class Nullableissue_labels(ResponseBase):
    def __init__(self, id:int=None, node_id:str=None, url:str=None, name:str=None, description:str=None, color:str=None, default:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._node_id = node_id
        self._url = url
        self._name = name
        self._description = description
        self._color = color
        self._default = default
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getcolor(self):
        return self._color
        
    color = property(_getcolor)

    def _getdefault(self):
        return self._default
        
    default = property(_getdefault)


    
##
##
##
class Nullableissue_pull_request(ResponseBase):
    def __init__(self, url:str, patch_url:str, html_url:str, diff_url:str, merged_at:datetime=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._patch_url = patch_url
        self._html_url = html_url
        self._diff_url = diff_url
        self._merged_at = merged_at
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getpatch_url(self):
        return self._patch_url
        
    patch_url = property(_getpatch_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getdiff_url(self):
        return self._diff_url
        
    diff_url = property(_getdiff_url)

    def _getmerged_at(self):
        return self._merged_at and datetime.datetime.fromisoformat(self._merged_at[0:-1])
        
    merged_at = property(_getmerged_at)


    
##
##
##
class NullableIssue(ResponseBase):
    """Issues are a great way to keep track of tasks, enhancements, and bugs for your projects. """
    def __init__(self, author_association:str, updated_at:datetime, created_at:datetime, closed_at:datetime, comments:int, locked:bool, milestone:dict, assignee:dict, labels:list, user:dict, title:str, state:str, number:int, html_url:str, events_url:str, comments_url:str, labels_url:str, repository_url:str, url:str, node_id:str, id:int, body:str=None, assignees:list=[], active_lock_reason:str=None, pull_request:dict=None, draft:bool=None, closed_by:dict=None, body_html:str=None, body_text:str=None, timeline_url:str=None, repository:dict=None, performed_via_github_app:dict=None, reactions:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._author_association = author_association
        self._updated_at = updated_at
        self._created_at = created_at
        self._closed_at = closed_at
        self._comments = comments
        self._locked = locked
        self._milestone = milestone
        self._assignee = assignee
        self._labels = labels
        self._user = user
        self._title = title
        self._state = state
        self._number = number
        self._html_url = html_url
        self._events_url = events_url
        self._comments_url = comments_url
        self._labels_url = labels_url
        self._repository_url = repository_url
        self._url = url
        self._node_id = node_id
        self._id = id
        self._body = body
        self._assignees = assignees
        self._active_lock_reason = active_lock_reason
        self._pull_request = pull_request
        self._draft = draft
        self._closed_by = closed_by
        self._body_html = body_html
        self._body_text = body_text
        self._timeline_url = timeline_url
        self._repository = repository
        self._performed_via_github_app = performed_via_github_app
        self._reactions = reactions
        return
        
    

    
    def _getauthor_association(self):
        return self._author_association
        
    author_association = property(_getauthor_association)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getclosed_at(self):
        return self._closed_at and datetime.datetime.fromisoformat(self._closed_at[0:-1])
        
    closed_at = property(_getclosed_at)

    def _getcomments(self):
        return self._comments
        
    comments = property(_getcomments)

    def _getlocked(self):
        return self._locked
        
    locked = property(_getlocked)

    def _getmilestone(self):
        return self._milestone and NullableMilestone(**self._milestone)
        
    milestone = property(_getmilestone)

    def _getassignee(self):
        return self._assignee and NullableSimpleUser(**self._assignee)
        
    assignee = property(_getassignee)

    def _getlabels(self):
        return self._labels and [ entry for entry in self._labels ]
        
    labels = property(_getlabels, doc="""Labels to associate with this issue; pass one or more label names to replace the set of labels on this issue; send an empty array to clear all labels from the issue; note that the labels are silently dropped for users without push access to the repository """)

    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle, doc="""Title of the issue """)

    def _getstate(self):
        return self._state
        
    state = property(_getstate, doc="""State of the issue; either 'open' or 'closed' """)

    def _getnumber(self):
        return self._number
        
    number = property(_getnumber, doc="""Number uniquely identifying the issue within its repository """)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _getlabels_url(self):
        return self._labels_url
        
    labels_url = property(_getlabels_url)

    def _getrepository_url(self):
        return self._repository_url
        
    repository_url = property(_getrepository_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl, doc="""URL for the issue """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getbody(self):
        return self._body
        
    body = property(_getbody, doc="""Contents of the issue """)

    def _getassignees(self):
        return self._assignees and [ entry and SimpleUser(**entry) for entry in self._assignees ]
        
    assignees = property(_getassignees)

    def _getactive_lock_reason(self):
        return self._active_lock_reason
        
    active_lock_reason = property(_getactive_lock_reason)

    def _getpull_request(self):
        return self._pull_request and Nullableissue_pull_request(**self._pull_request)
        
    pull_request = property(_getpull_request)

    def _getdraft(self):
        return self._draft
        
    draft = property(_getdraft)

    def _getclosed_by(self):
        return self._closed_by and NullableSimpleUser(**self._closed_by)
        
    closed_by = property(_getclosed_by)

    def _getbody_html(self):
        return self._body_html
        
    body_html = property(_getbody_html)

    def _getbody_text(self):
        return self._body_text
        
    body_text = property(_getbody_text)

    def _gettimeline_url(self):
        return self._timeline_url
        
    timeline_url = property(_gettimeline_url)

    def _getrepository(self):
        return self._repository and Repository(**self._repository)
        
    repository = property(_getrepository)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getreactions(self):
        return self._reactions and ReactionRollup(**ReactionRollup.patchEntry(self._reactions))
        
    reactions = property(_getreactions)


    
##
##
##
class IssueEventLabel(ResponseBase):
    """Issue Event Label """
    def __init__(self, color:str, name:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._color = color
        self._name = name
        return
        
    

    
    def _getcolor(self):
        return self._color
        
    color = property(_getcolor)

    def _getname(self):
        return self._name
        
    name = property(_getname)


    
##
##
##
class IssueEventDismissedReview(ResponseBase):
    def __init__(self, dismissal_message:str, review_id:int, state:str, dismissal_commit_id:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._dismissal_message = dismissal_message
        self._review_id = review_id
        self._state = state
        self._dismissal_commit_id = dismissal_commit_id
        return
        
    

    
    def _getdismissal_message(self):
        return self._dismissal_message
        
    dismissal_message = property(_getdismissal_message)

    def _getreview_id(self):
        return self._review_id
        
    review_id = property(_getreview_id)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)

    def _getdismissal_commit_id(self):
        return self._dismissal_commit_id
        
    dismissal_commit_id = property(_getdismissal_commit_id)


    
##
##
##
class IssueEventMilestone(ResponseBase):
    """Issue Event Milestone """
    def __init__(self, title:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._title = title
        return
        
    

    
    def _gettitle(self):
        return self._title
        
    title = property(_gettitle)


    
##
##
##
class IssueEventProjectCard(ResponseBase):
    """Issue Event Project Card """
    def __init__(self, column_name:str, project_id:int, project_url:str, id:int, url:str, previous_column_name:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._column_name = column_name
        self._project_id = project_id
        self._project_url = project_url
        self._id = id
        self._url = url
        self._previous_column_name = previous_column_name
        return
        
    

    
    def _getcolumn_name(self):
        return self._column_name
        
    column_name = property(_getcolumn_name)

    def _getproject_id(self):
        return self._project_id
        
    project_id = property(_getproject_id)

    def _getproject_url(self):
        return self._project_url
        
    project_url = property(_getproject_url)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getprevious_column_name(self):
        return self._previous_column_name
        
    previous_column_name = property(_getprevious_column_name)


    
##
##
##
class IssueEventRename(ResponseBase):
    """Issue Event Rename """
    def __init__(self, to:str, From:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._to = to
        self._From = From
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['From'] = entry.pop('from')
        return entry
    

    
    def _getto(self):
        return self._to
        
    to = property(_getto)

    def _getFrom(self):
        return self._From
        
    From = property(_getFrom)


    
    ##
    ##
    def _getFrom(self):
        return self._From
        
    From = property(_getFrom)

##
##
##
class IssueEvent(ResponseBase):
    """Issue Event """
    def __init__(self, created_at:datetime, commit_url:str, commit_id:str, event:str, actor:dict, url:str, node_id:str, id:int, issue:dict=None, label:dict=None, assignee:dict=None, assigner:dict=None, review_requester:dict=None, requested_reviewer:dict=None, requested_team:dict=None, dismissed_review:dict=None, milestone:dict=None, project_card:dict=None, rename:dict=None, author_association:str=None, lock_reason:str=None, performed_via_github_app:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._created_at = created_at
        self._commit_url = commit_url
        self._commit_id = commit_id
        self._event = event
        self._actor = actor
        self._url = url
        self._node_id = node_id
        self._id = id
        self._issue = issue
        self._label = label
        self._assignee = assignee
        self._assigner = assigner
        self._review_requester = review_requester
        self._requested_reviewer = requested_reviewer
        self._requested_team = requested_team
        self._dismissed_review = dismissed_review
        self._milestone = milestone
        self._project_card = project_card
        self._rename = rename
        self._author_association = author_association
        self._lock_reason = lock_reason
        self._performed_via_github_app = performed_via_github_app
        return
        
    

    
    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getactor(self):
        return self._actor and NullableSimpleUser(**self._actor)
        
    actor = property(_getactor)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getissue(self):
        return self._issue and NullableIssue(**self._issue)
        
    issue = property(_getissue)

    def _getlabel(self):
        return self._label and IssueEventLabel(**self._label)
        
    label = property(_getlabel)

    def _getassignee(self):
        return self._assignee and NullableSimpleUser(**self._assignee)
        
    assignee = property(_getassignee)

    def _getassigner(self):
        return self._assigner and NullableSimpleUser(**self._assigner)
        
    assigner = property(_getassigner)

    def _getreview_requester(self):
        return self._review_requester and NullableSimpleUser(**self._review_requester)
        
    review_requester = property(_getreview_requester)

    def _getrequested_reviewer(self):
        return self._requested_reviewer and NullableSimpleUser(**self._requested_reviewer)
        
    requested_reviewer = property(_getrequested_reviewer)

    def _getrequested_team(self):
        return self._requested_team and Team(**self._requested_team)
        
    requested_team = property(_getrequested_team)

    def _getdismissed_review(self):
        return self._dismissed_review and IssueEventDismissedReview(**self._dismissed_review)
        
    dismissed_review = property(_getdismissed_review)

    def _getmilestone(self):
        return self._milestone and IssueEventMilestone(**self._milestone)
        
    milestone = property(_getmilestone)

    def _getproject_card(self):
        return self._project_card and IssueEventProjectCard(**self._project_card)
        
    project_card = property(_getproject_card)

    def _getrename(self):
        return self._rename and IssueEventRename(**IssueEventRename.patchEntry(self._rename))
        
    rename = property(_getrename)

    def _getauthor_association(self):
        return self._author_association
        
    author_association = property(_getauthor_association)

    def _getlock_reason(self):
        return self._lock_reason
        
    lock_reason = property(_getlock_reason)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)


    
##
##
##
class Labeledissueevent_label(ResponseBase):
    def __init__(self, color:str, name:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._color = color
        self._name = name
        return
        
    

    
    def _getcolor(self):
        return self._color
        
    color = property(_getcolor)

    def _getname(self):
        return self._name
        
    name = property(_getname)


    
##
##
##
class LabeledIssueEvent(ResponseBase):
    """Labeled Issue Event """
    def __init__(self, label:dict, performed_via_github_app:dict, created_at:str, commit_url:str, commit_id:str, event:str, actor:dict, url:str, node_id:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._label = label
        self._performed_via_github_app = performed_via_github_app
        self._created_at = created_at
        self._commit_url = commit_url
        self._commit_id = commit_id
        self._event = event
        self._actor = actor
        self._url = url
        self._node_id = node_id
        self._id = id
        return
        
    

    
    def _getlabel(self):
        return self._label and Labeledissueevent_label(**self._label)
        
    label = property(_getlabel)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getactor(self):
        return self._actor and SimpleUser(**self._actor)
        
    actor = property(_getactor)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class Unlabeledissueevent_label(ResponseBase):
    def __init__(self, color:str, name:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._color = color
        self._name = name
        return
        
    

    
    def _getcolor(self):
        return self._color
        
    color = property(_getcolor)

    def _getname(self):
        return self._name
        
    name = property(_getname)


    
##
##
##
class UnlabeledIssueEvent(ResponseBase):
    """Unlabeled Issue Event """
    def __init__(self, label:dict, performed_via_github_app:dict, created_at:str, commit_url:str, commit_id:str, event:str, actor:dict, url:str, node_id:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._label = label
        self._performed_via_github_app = performed_via_github_app
        self._created_at = created_at
        self._commit_url = commit_url
        self._commit_id = commit_id
        self._event = event
        self._actor = actor
        self._url = url
        self._node_id = node_id
        self._id = id
        return
        
    

    
    def _getlabel(self):
        return self._label and Unlabeledissueevent_label(**self._label)
        
    label = property(_getlabel)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getactor(self):
        return self._actor and SimpleUser(**self._actor)
        
    actor = property(_getactor)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class AssignedIssueEvent(ResponseBase):
    """Assigned Issue Event """
    def __init__(self, assigner:dict, assignee:dict, performed_via_github_app:dict, created_at:str, commit_url:str, commit_id:str, event:str, actor:dict, url:str, node_id:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._assigner = assigner
        self._assignee = assignee
        self._performed_via_github_app = performed_via_github_app
        self._created_at = created_at
        self._commit_url = commit_url
        self._commit_id = commit_id
        self._event = event
        self._actor = actor
        self._url = url
        self._node_id = node_id
        self._id = id
        return
        
    

    
    def _getassigner(self):
        return self._assigner and SimpleUser(**self._assigner)
        
    assigner = property(_getassigner)

    def _getassignee(self):
        return self._assignee and SimpleUser(**self._assignee)
        
    assignee = property(_getassignee)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and Integration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getactor(self):
        return self._actor and SimpleUser(**self._actor)
        
    actor = property(_getactor)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class UnassignedIssueEvent(ResponseBase):
    """Unassigned Issue Event """
    def __init__(self, assigner:dict, assignee:dict, performed_via_github_app:dict, created_at:str, commit_url:str, commit_id:str, event:str, actor:dict, url:str, node_id:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._assigner = assigner
        self._assignee = assignee
        self._performed_via_github_app = performed_via_github_app
        self._created_at = created_at
        self._commit_url = commit_url
        self._commit_id = commit_id
        self._event = event
        self._actor = actor
        self._url = url
        self._node_id = node_id
        self._id = id
        return
        
    

    
    def _getassigner(self):
        return self._assigner and SimpleUser(**self._assigner)
        
    assigner = property(_getassigner)

    def _getassignee(self):
        return self._assignee and SimpleUser(**self._assignee)
        
    assignee = property(_getassignee)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getactor(self):
        return self._actor and SimpleUser(**self._actor)
        
    actor = property(_getactor)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class Milestonedissueevent_milestone(ResponseBase):
    def __init__(self, title:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._title = title
        return
        
    

    
    def _gettitle(self):
        return self._title
        
    title = property(_gettitle)


    
##
##
##
class MilestonedIssueEvent(ResponseBase):
    """Milestoned Issue Event """
    def __init__(self, milestone:dict, performed_via_github_app:dict, created_at:str, commit_url:str, commit_id:str, event:str, actor:dict, url:str, node_id:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._milestone = milestone
        self._performed_via_github_app = performed_via_github_app
        self._created_at = created_at
        self._commit_url = commit_url
        self._commit_id = commit_id
        self._event = event
        self._actor = actor
        self._url = url
        self._node_id = node_id
        self._id = id
        return
        
    

    
    def _getmilestone(self):
        return self._milestone and Milestonedissueevent_milestone(**self._milestone)
        
    milestone = property(_getmilestone)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getactor(self):
        return self._actor and SimpleUser(**self._actor)
        
    actor = property(_getactor)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class Demilestonedissueevent_milestone(ResponseBase):
    def __init__(self, title:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._title = title
        return
        
    

    
    def _gettitle(self):
        return self._title
        
    title = property(_gettitle)


    
##
##
##
class DemilestonedIssueEvent(ResponseBase):
    """Demilestoned Issue Event """
    def __init__(self, milestone:dict, performed_via_github_app:dict, created_at:str, commit_url:str, commit_id:str, event:str, actor:dict, url:str, node_id:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._milestone = milestone
        self._performed_via_github_app = performed_via_github_app
        self._created_at = created_at
        self._commit_url = commit_url
        self._commit_id = commit_id
        self._event = event
        self._actor = actor
        self._url = url
        self._node_id = node_id
        self._id = id
        return
        
    

    
    def _getmilestone(self):
        return self._milestone and Demilestonedissueevent_milestone(**self._milestone)
        
    milestone = property(_getmilestone)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getactor(self):
        return self._actor and SimpleUser(**self._actor)
        
    actor = property(_getactor)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class Renamedissueevent_rename(ResponseBase):
    def __init__(self, to:str, From:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._to = to
        self._From = From
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['From'] = entry.pop('from')
        return entry
    

    
    def _getto(self):
        return self._to
        
    to = property(_getto)

    def _getFrom(self):
        return self._From
        
    From = property(_getFrom)


    
    ##
    ##
    def _getFrom(self):
        return self._From
        
    From = property(_getFrom)

##
##
##
class RenamedIssueEvent(ResponseBase):
    """Renamed Issue Event """
    def __init__(self, rename:dict, performed_via_github_app:dict, created_at:str, commit_url:str, commit_id:str, event:str, actor:dict, url:str, node_id:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._rename = rename
        self._performed_via_github_app = performed_via_github_app
        self._created_at = created_at
        self._commit_url = commit_url
        self._commit_id = commit_id
        self._event = event
        self._actor = actor
        self._url = url
        self._node_id = node_id
        self._id = id
        return
        
    

    
    def _getrename(self):
        return self._rename and Renamedissueevent_rename(**Renamedissueevent_rename.patchEntry(self._rename))
        
    rename = property(_getrename)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getactor(self):
        return self._actor and SimpleUser(**self._actor)
        
    actor = property(_getactor)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class ReviewRequestedIssueEvent(ResponseBase):
    """Review Requested Issue Event """
    def __init__(self, review_requester:dict, performed_via_github_app:dict, created_at:str, commit_url:str, commit_id:str, event:str, actor:dict, url:str, node_id:str, id:int, requested_team:dict=None, requested_reviewer:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._review_requester = review_requester
        self._performed_via_github_app = performed_via_github_app
        self._created_at = created_at
        self._commit_url = commit_url
        self._commit_id = commit_id
        self._event = event
        self._actor = actor
        self._url = url
        self._node_id = node_id
        self._id = id
        self._requested_team = requested_team
        self._requested_reviewer = requested_reviewer
        return
        
    

    
    def _getreview_requester(self):
        return self._review_requester and SimpleUser(**self._review_requester)
        
    review_requester = property(_getreview_requester)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getactor(self):
        return self._actor and SimpleUser(**self._actor)
        
    actor = property(_getactor)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getrequested_team(self):
        return self._requested_team and Team(**self._requested_team)
        
    requested_team = property(_getrequested_team)

    def _getrequested_reviewer(self):
        return self._requested_reviewer and SimpleUser(**self._requested_reviewer)
        
    requested_reviewer = property(_getrequested_reviewer)


    
##
##
##
class ReviewRequestRemovedIssueEvent(ResponseBase):
    """Review Request Removed Issue Event """
    def __init__(self, review_requester:dict, performed_via_github_app:dict, created_at:str, commit_url:str, commit_id:str, event:str, actor:dict, url:str, node_id:str, id:int, requested_team:dict=None, requested_reviewer:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._review_requester = review_requester
        self._performed_via_github_app = performed_via_github_app
        self._created_at = created_at
        self._commit_url = commit_url
        self._commit_id = commit_id
        self._event = event
        self._actor = actor
        self._url = url
        self._node_id = node_id
        self._id = id
        self._requested_team = requested_team
        self._requested_reviewer = requested_reviewer
        return
        
    

    
    def _getreview_requester(self):
        return self._review_requester and SimpleUser(**self._review_requester)
        
    review_requester = property(_getreview_requester)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getactor(self):
        return self._actor and SimpleUser(**self._actor)
        
    actor = property(_getactor)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getrequested_team(self):
        return self._requested_team and Team(**self._requested_team)
        
    requested_team = property(_getrequested_team)

    def _getrequested_reviewer(self):
        return self._requested_reviewer and SimpleUser(**self._requested_reviewer)
        
    requested_reviewer = property(_getrequested_reviewer)


    
##
##
##
class Reviewdismissedissueevent_dismissed_review(ResponseBase):
    def __init__(self, dismissal_message:str, review_id:int, state:str, dismissal_commit_id:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._dismissal_message = dismissal_message
        self._review_id = review_id
        self._state = state
        self._dismissal_commit_id = dismissal_commit_id
        return
        
    

    
    def _getdismissal_message(self):
        return self._dismissal_message
        
    dismissal_message = property(_getdismissal_message)

    def _getreview_id(self):
        return self._review_id
        
    review_id = property(_getreview_id)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)

    def _getdismissal_commit_id(self):
        return self._dismissal_commit_id
        
    dismissal_commit_id = property(_getdismissal_commit_id)


    
##
##
##
class ReviewDismissedIssueEvent(ResponseBase):
    """Review Dismissed Issue Event """
    def __init__(self, dismissed_review:dict, performed_via_github_app:dict, created_at:str, commit_url:str, commit_id:str, event:str, actor:dict, url:str, node_id:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._dismissed_review = dismissed_review
        self._performed_via_github_app = performed_via_github_app
        self._created_at = created_at
        self._commit_url = commit_url
        self._commit_id = commit_id
        self._event = event
        self._actor = actor
        self._url = url
        self._node_id = node_id
        self._id = id
        return
        
    

    
    def _getdismissed_review(self):
        return self._dismissed_review and Reviewdismissedissueevent_dismissed_review(**self._dismissed_review)
        
    dismissed_review = property(_getdismissed_review)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getactor(self):
        return self._actor and SimpleUser(**self._actor)
        
    actor = property(_getactor)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class LockedIssueEvent(ResponseBase):
    """Locked Issue Event """
    def __init__(self, lock_reason:str, performed_via_github_app:dict, created_at:str, commit_url:str, commit_id:str, event:str, actor:dict, url:str, node_id:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._lock_reason = lock_reason
        self._performed_via_github_app = performed_via_github_app
        self._created_at = created_at
        self._commit_url = commit_url
        self._commit_id = commit_id
        self._event = event
        self._actor = actor
        self._url = url
        self._node_id = node_id
        self._id = id
        return
        
    

    
    def _getlock_reason(self):
        return self._lock_reason
        
    lock_reason = property(_getlock_reason)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getactor(self):
        return self._actor and SimpleUser(**self._actor)
        
    actor = property(_getactor)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class Addedtoprojectissueevent_project_card(ResponseBase):
    def __init__(self, column_name:str, project_url:str, project_id:int, url:str, id:int, previous_column_name:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._column_name = column_name
        self._project_url = project_url
        self._project_id = project_id
        self._url = url
        self._id = id
        self._previous_column_name = previous_column_name
        return
        
    

    
    def _getcolumn_name(self):
        return self._column_name
        
    column_name = property(_getcolumn_name)

    def _getproject_url(self):
        return self._project_url
        
    project_url = property(_getproject_url)

    def _getproject_id(self):
        return self._project_id
        
    project_id = property(_getproject_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getprevious_column_name(self):
        return self._previous_column_name
        
    previous_column_name = property(_getprevious_column_name)


    
##
##
##
class AddedToProjectIssueEvent(ResponseBase):
    """Added to Project Issue Event """
    def __init__(self, performed_via_github_app:dict, created_at:str, commit_url:str, commit_id:str, event:str, actor:dict, url:str, node_id:str, id:int, project_card:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._performed_via_github_app = performed_via_github_app
        self._created_at = created_at
        self._commit_url = commit_url
        self._commit_id = commit_id
        self._event = event
        self._actor = actor
        self._url = url
        self._node_id = node_id
        self._id = id
        self._project_card = project_card
        return
        
    

    
    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getactor(self):
        return self._actor and SimpleUser(**self._actor)
        
    actor = property(_getactor)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getproject_card(self):
        return self._project_card and Addedtoprojectissueevent_project_card(**self._project_card)
        
    project_card = property(_getproject_card)


    
##
##
##
class Movedcolumninprojectissueevent_project_card(ResponseBase):
    def __init__(self, column_name:str, project_url:str, project_id:int, url:str, id:int, previous_column_name:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._column_name = column_name
        self._project_url = project_url
        self._project_id = project_id
        self._url = url
        self._id = id
        self._previous_column_name = previous_column_name
        return
        
    

    
    def _getcolumn_name(self):
        return self._column_name
        
    column_name = property(_getcolumn_name)

    def _getproject_url(self):
        return self._project_url
        
    project_url = property(_getproject_url)

    def _getproject_id(self):
        return self._project_id
        
    project_id = property(_getproject_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getprevious_column_name(self):
        return self._previous_column_name
        
    previous_column_name = property(_getprevious_column_name)


    
##
##
##
class MovedColumnInProjectIssueEvent(ResponseBase):
    """Moved Column in Project Issue Event """
    def __init__(self, performed_via_github_app:dict, created_at:str, commit_url:str, commit_id:str, event:str, actor:dict, url:str, node_id:str, id:int, project_card:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._performed_via_github_app = performed_via_github_app
        self._created_at = created_at
        self._commit_url = commit_url
        self._commit_id = commit_id
        self._event = event
        self._actor = actor
        self._url = url
        self._node_id = node_id
        self._id = id
        self._project_card = project_card
        return
        
    

    
    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getactor(self):
        return self._actor and SimpleUser(**self._actor)
        
    actor = property(_getactor)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getproject_card(self):
        return self._project_card and Movedcolumninprojectissueevent_project_card(**self._project_card)
        
    project_card = property(_getproject_card)


    
##
##
##
class Removedfromprojectissueevent_project_card(ResponseBase):
    def __init__(self, column_name:str, project_url:str, project_id:int, url:str, id:int, previous_column_name:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._column_name = column_name
        self._project_url = project_url
        self._project_id = project_id
        self._url = url
        self._id = id
        self._previous_column_name = previous_column_name
        return
        
    

    
    def _getcolumn_name(self):
        return self._column_name
        
    column_name = property(_getcolumn_name)

    def _getproject_url(self):
        return self._project_url
        
    project_url = property(_getproject_url)

    def _getproject_id(self):
        return self._project_id
        
    project_id = property(_getproject_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getprevious_column_name(self):
        return self._previous_column_name
        
    previous_column_name = property(_getprevious_column_name)


    
##
##
##
class RemovedFromProjectIssueEvent(ResponseBase):
    """Removed from Project Issue Event """
    def __init__(self, performed_via_github_app:dict, created_at:str, commit_url:str, commit_id:str, event:str, actor:dict, url:str, node_id:str, id:int, project_card:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._performed_via_github_app = performed_via_github_app
        self._created_at = created_at
        self._commit_url = commit_url
        self._commit_id = commit_id
        self._event = event
        self._actor = actor
        self._url = url
        self._node_id = node_id
        self._id = id
        self._project_card = project_card
        return
        
    

    
    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getactor(self):
        return self._actor and SimpleUser(**self._actor)
        
    actor = property(_getactor)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getproject_card(self):
        return self._project_card and Removedfromprojectissueevent_project_card(**self._project_card)
        
    project_card = property(_getproject_card)


    
##
##
##
class Convertednotetoissueissueevent_project_card(ResponseBase):
    def __init__(self, column_name:str, project_url:str, project_id:int, url:str, id:int, previous_column_name:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._column_name = column_name
        self._project_url = project_url
        self._project_id = project_id
        self._url = url
        self._id = id
        self._previous_column_name = previous_column_name
        return
        
    

    
    def _getcolumn_name(self):
        return self._column_name
        
    column_name = property(_getcolumn_name)

    def _getproject_url(self):
        return self._project_url
        
    project_url = property(_getproject_url)

    def _getproject_id(self):
        return self._project_id
        
    project_id = property(_getproject_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getprevious_column_name(self):
        return self._previous_column_name
        
    previous_column_name = property(_getprevious_column_name)


    
##
##
##
class ConvertedNoteToIssueIssueEvent(ResponseBase):
    """Converted Note to Issue Issue Event """
    def __init__(self, performed_via_github_app:dict, created_at:str, commit_url:str, commit_id:str, event:str, actor:dict, url:str, node_id:str, id:int, project_card:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._performed_via_github_app = performed_via_github_app
        self._created_at = created_at
        self._commit_url = commit_url
        self._commit_id = commit_id
        self._event = event
        self._actor = actor
        self._url = url
        self._node_id = node_id
        self._id = id
        self._project_card = project_card
        return
        
    

    
    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and Integration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getactor(self):
        return self._actor and SimpleUser(**self._actor)
        
    actor = property(_getactor)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getproject_card(self):
        return self._project_card and Convertednotetoissueissueevent_project_card(**self._project_card)
        
    project_card = property(_getproject_card)


    
##
##
##
class Label(ResponseBase):
    """Color-coded labels help you categorize and filter your issues (just like labels in Gmail). """
    def __init__(self, default:bool, color:str, description:str, name:str, url:str, node_id:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._default = default
        self._color = color
        self._description = description
        self._name = name
        self._url = url
        self._node_id = node_id
        self._id = id
        return
        
    

    
    def _getdefault(self):
        return self._default
        
    default = property(_getdefault)

    def _getcolor(self):
        return self._color
        
    color = property(_getcolor, doc="""6-character hex code, without the leading #, identifying the color """)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the label. """)

    def _geturl(self):
        return self._url
        
    url = property(_geturl, doc="""URL for the label """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class TimelineCommentEvent(ResponseBase):
    """Timeline Comment Event """
    def __init__(self, author_association:str, issue_url:str, updated_at:datetime, created_at:datetime, user:dict, html_url:str, url:str, node_id:str, id:int, actor:dict, event:str, body:str=None, body_text:str=None, body_html:str=None, performed_via_github_app:dict=None, reactions:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._author_association = author_association
        self._issue_url = issue_url
        self._updated_at = updated_at
        self._created_at = created_at
        self._user = user
        self._html_url = html_url
        self._url = url
        self._node_id = node_id
        self._id = id
        self._actor = actor
        self._event = event
        self._body = body
        self._body_text = body_text
        self._body_html = body_html
        self._performed_via_github_app = performed_via_github_app
        self._reactions = reactions
        return
        
    

    
    def _getauthor_association(self):
        return self._author_association
        
    author_association = property(_getauthor_association)

    def _getissue_url(self):
        return self._issue_url
        
    issue_url = property(_getissue_url)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getuser(self):
        return self._user and SimpleUser(**self._user)
        
    user = property(_getuser)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl, doc="""URL for the issue comment """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the issue comment """)

    def _getactor(self):
        return self._actor and SimpleUser(**self._actor)
        
    actor = property(_getactor)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getbody(self):
        return self._body
        
    body = property(_getbody, doc="""Contents of the issue comment """)

    def _getbody_text(self):
        return self._body_text
        
    body_text = property(_getbody_text)

    def _getbody_html(self):
        return self._body_html
        
    body_html = property(_getbody_html)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getreactions(self):
        return self._reactions and ReactionRollup(**ReactionRollup.patchEntry(self._reactions))
        
    reactions = property(_getreactions)


    
##
##
##
class Timelinecrossreferencedevent_source(ResponseBase):
    def __init__(self, type:str=None, issue:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._type = type
        self._issue = issue
        return
        
    

    
    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getissue(self):
        return self._issue and Issue(**self._issue)
        
    issue = property(_getissue)


    
##
##
##
class TimelineCrossReferencedEvent(ResponseBase):
    """Timeline Cross Referenced Event """
    def __init__(self, source:dict, updated_at:datetime, created_at:datetime, event:str, actor:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._source = source
        self._updated_at = updated_at
        self._created_at = created_at
        self._event = event
        self._actor = actor
        return
        
    

    
    def _getsource(self):
        return self._source and Timelinecrossreferencedevent_source(**self._source)
        
    source = property(_getsource)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getactor(self):
        return self._actor and SimpleUser(**self._actor)
        
    actor = property(_getactor)


    
##
##
##
class Timelinecommittedevent_author(ResponseBase):
    """Identifying information for the git-user """
    def __init__(self, name:str, email:str, date:datetime, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._name = name
        self._email = email
        self._date = date
        return
        
    

    
    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""Name of the git user """)

    def _getemail(self):
        return self._email
        
    email = property(_getemail, doc="""Git email address of the user """)

    def _getdate(self):
        return self._date and datetime.datetime.fromisoformat(self._date[0:-1])
        
    date = property(_getdate, doc="""Timestamp of the commit """)


    
##
##
##
class Timelinecommittedevent_committer(ResponseBase):
    """Identifying information for the git-user """
    def __init__(self, name:str, email:str, date:datetime, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._name = name
        self._email = email
        self._date = date
        return
        
    

    
    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""Name of the git user """)

    def _getemail(self):
        return self._email
        
    email = property(_getemail, doc="""Git email address of the user """)

    def _getdate(self):
        return self._date and datetime.datetime.fromisoformat(self._date[0:-1])
        
    date = property(_getdate, doc="""Timestamp of the commit """)


    
##
##
##
class Timelinecommittedevent_tree(ResponseBase):
    def __init__(self, url:str, sha:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._sha = sha
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha, doc="""SHA for the commit """)


    
##
##
##
class Timelinecommittedevent_parents(ResponseBase):
    def __init__(self, html_url:str, url:str, sha:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._html_url = html_url
        self._url = url
        self._sha = sha
        return
        
    

    
    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha, doc="""SHA for the commit """)


    
##
##
##
class Timelinecommittedevent_verification(ResponseBase):
    def __init__(self, payload:str, signature:str, reason:str, verified:bool, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._payload = payload
        self._signature = signature
        self._reason = reason
        self._verified = verified
        return
        
    

    
    def _getpayload(self):
        return self._payload
        
    payload = property(_getpayload)

    def _getsignature(self):
        return self._signature
        
    signature = property(_getsignature)

    def _getreason(self):
        return self._reason
        
    reason = property(_getreason)

    def _getverified(self):
        return self._verified
        
    verified = property(_getverified)


    
##
##
##
class TimelineCommittedEvent(ResponseBase):
    """Timeline Committed Event """
    def __init__(self, html_url:str, verification:dict, parents:list, tree:dict, message:str, committer:dict, author:dict, url:str, node_id:str, sha:str, event:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._html_url = html_url
        self._verification = verification
        self._parents = parents
        self._tree = tree
        self._message = message
        self._committer = committer
        self._author = author
        self._url = url
        self._node_id = node_id
        self._sha = sha
        self._event = event
        return
        
    

    
    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getverification(self):
        return self._verification and Timelinecommittedevent_verification(**self._verification)
        
    verification = property(_getverification)

    def _getparents(self):
        return self._parents and [ entry and Timelinecommittedevent_parents(**entry) for entry in self._parents ]
        
    parents = property(_getparents)

    def _gettree(self):
        return self._tree and Timelinecommittedevent_tree(**self._tree)
        
    tree = property(_gettree)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage, doc="""Message describing the purpose of the commit """)

    def _getcommitter(self):
        return self._committer and Timelinecommittedevent_committer(**self._committer)
        
    committer = property(_getcommitter, doc="""Identifying information for the git-user """)

    def _getauthor(self):
        return self._author and Timelinecommittedevent_author(**self._author)
        
    author = property(_getauthor, doc="""Identifying information for the git-user """)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha, doc="""SHA for the commit """)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)


    
##
##
##
class Timelinereviewedevent__links_html(ResponseBase):
    def __init__(self, href:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._href = href
        return
        
    

    
    def _gethref(self):
        return self._href
        
    href = property(_gethref)


    
##
##
##
class Timelinereviewedevent__links_pull_request(ResponseBase):
    def __init__(self, href:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._href = href
        return
        
    

    
    def _gethref(self):
        return self._href
        
    href = property(_gethref)


    
##
##
##
class Timelinereviewedevent__links(ResponseBase):
    def __init__(self, pull_request:dict, html:dict, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._pull_request = pull_request
        self._html = html
        return
        
    

    
    def _getpull_request(self):
        return self._pull_request and Timelinereviewedevent__links_pull_request(**self._pull_request)
        
    pull_request = property(_getpull_request)

    def _gethtml(self):
        return self._html and Timelinereviewedevent__links_html(**self._html)
        
    html = property(_gethtml)


    
##
##
##
class TimelineReviewedEvent(ResponseBase):
    """Timeline Reviewed Event """
    def __init__(self, author_association:str, commit_id:str, _links:dict, pull_request_url:str, html_url:str, state:str, body:str, user:dict, node_id:str, id:int, event:str, submitted_at:datetime=None, body_html:str=None, body_text:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._author_association = author_association
        self._commit_id = commit_id
        self.__links = _links
        self._pull_request_url = pull_request_url
        self._html_url = html_url
        self._state = state
        self._body = body
        self._user = user
        self._node_id = node_id
        self._id = id
        self._event = event
        self._submitted_at = submitted_at
        self._body_html = body_html
        self._body_text = body_text
        return
        
    

    
    def _getauthor_association(self):
        return self._author_association
        
    author_association = property(_getauthor_association)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id, doc="""A commit SHA for the review. """)

    def _get_links(self):
        return self.__links and Timelinereviewedevent__links(**self.__links)
        
    _links = property(_get_links)

    def _getpull_request_url(self):
        return self._pull_request_url
        
    pull_request_url = property(_getpull_request_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)

    def _getbody(self):
        return self._body
        
    body = property(_getbody, doc="""The text of the review. """)

    def _getuser(self):
        return self._user and SimpleUser(**self._user)
        
    user = property(_getuser)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the review """)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getsubmitted_at(self):
        return self._submitted_at and datetime.datetime.fromisoformat(self._submitted_at[0:-1])
        
    submitted_at = property(_getsubmitted_at)

    def _getbody_html(self):
        return self._body_html
        
    body_html = property(_getbody_html)

    def _getbody_text(self):
        return self._body_text
        
    body_text = property(_getbody_text)


    
##
##
##
class Pullrequestreviewcomment__links_self(ResponseBase):
    def __init__(self, href:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._href = href
        return
        
    

    
    def _gethref(self):
        return self._href
        
    href = property(_gethref)


    
##
##
##
class Pullrequestreviewcomment__links_html(ResponseBase):
    def __init__(self, href:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._href = href
        return
        
    

    
    def _gethref(self):
        return self._href
        
    href = property(_gethref)


    
##
##
##
class Pullrequestreviewcomment__links_pull_request(ResponseBase):
    def __init__(self, href:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._href = href
        return
        
    

    
    def _gethref(self):
        return self._href
        
    href = property(_gethref)


    
##
##
##
class Pullrequestreviewcomment__links(ResponseBase):
    def __init__(self, pull_request:dict, html:dict, Self:dict, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._pull_request = pull_request
        self._html = html
        self._Self = Self
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['Self'] = entry.pop('self')
        return entry
    

    
    def _getpull_request(self):
        return self._pull_request and Pullrequestreviewcomment__links_pull_request(**self._pull_request)
        
    pull_request = property(_getpull_request)

    def _gethtml(self):
        return self._html and Pullrequestreviewcomment__links_html(**self._html)
        
    html = property(_gethtml)

    def _getSelf(self):
        return self._Self and Pullrequestreviewcomment__links_self(**self._Self)
        
    Self = property(_getSelf)


    
    ##
    ##
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

##
##
##
class PullRequestReviewComment(ResponseBase):
    """Pull Request Review Comments are comments on a portion of the Pull Request's diff. """
    def __init__(self, _links:dict, author_association:str, pull_request_url:str, html_url:str, updated_at:datetime, created_at:datetime, body:str, user:dict, original_commit_id:str, commit_id:str, original_position:int, position:int, path:str, diff_hunk:str, node_id:str, id:int, pull_request_review_id:int, url:str, in_reply_to_id:int=None, start_line:int=None, original_start_line:int=None, start_side:str='RIGHT', line:int=None, original_line:int=None, side:str='RIGHT', reactions:dict=None, body_html:str=None, body_text:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self.__links = _links
        self._author_association = author_association
        self._pull_request_url = pull_request_url
        self._html_url = html_url
        self._updated_at = updated_at
        self._created_at = created_at
        self._body = body
        self._user = user
        self._original_commit_id = original_commit_id
        self._commit_id = commit_id
        self._original_position = original_position
        self._position = position
        self._path = path
        self._diff_hunk = diff_hunk
        self._node_id = node_id
        self._id = id
        self._pull_request_review_id = pull_request_review_id
        self._url = url
        self._in_reply_to_id = in_reply_to_id
        self._start_line = start_line
        self._original_start_line = original_start_line
        self._start_side = start_side
        self._line = line
        self._original_line = original_line
        self._side = side
        self._reactions = reactions
        self._body_html = body_html
        self._body_text = body_text
        return
        
    

    
    def _get_links(self):
        return self.__links and Pullrequestreviewcomment__links(**Pullrequestreviewcomment__links.patchEntry(self.__links))
        
    _links = property(_get_links)

    def _getauthor_association(self):
        return self._author_association
        
    author_association = property(_getauthor_association)

    def _getpull_request_url(self):
        return self._pull_request_url
        
    pull_request_url = property(_getpull_request_url, doc="""URL for the pull request that the review comment belongs to. """)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url, doc="""HTML URL for the pull request review comment. """)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getbody(self):
        return self._body
        
    body = property(_getbody, doc="""The text of the comment. """)

    def _getuser(self):
        return self._user and SimpleUser(**self._user)
        
    user = property(_getuser)

    def _getoriginal_commit_id(self):
        return self._original_commit_id
        
    original_commit_id = property(_getoriginal_commit_id, doc="""The SHA of the original commit to which the comment applies. """)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id, doc="""The SHA of the commit to which the comment applies. """)

    def _getoriginal_position(self):
        return self._original_position
        
    original_position = property(_getoriginal_position, doc="""The index of the original line in the diff to which the comment applies. """)

    def _getposition(self):
        return self._position
        
    position = property(_getposition, doc="""The line index in the diff to which the comment applies. """)

    def _getpath(self):
        return self._path
        
    path = property(_getpath, doc="""The relative path of the file to which the comment applies. """)

    def _getdiff_hunk(self):
        return self._diff_hunk
        
    diff_hunk = property(_getdiff_hunk, doc="""The diff of the line that the comment refers to. """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id, doc="""The node ID of the pull request review comment. """)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""The ID of the pull request review comment. """)

    def _getpull_request_review_id(self):
        return self._pull_request_review_id
        
    pull_request_review_id = property(_getpull_request_review_id, doc="""The ID of the pull request review to which the comment belongs. """)

    def _geturl(self):
        return self._url
        
    url = property(_geturl, doc="""URL for the pull request review comment """)

    def _getin_reply_to_id(self):
        return self._in_reply_to_id
        
    in_reply_to_id = property(_getin_reply_to_id, doc="""The comment ID to reply to. """)

    def _getstart_line(self):
        return self._start_line
        
    start_line = property(_getstart_line, doc="""The first line of the range for a multi-line comment. """)

    def _getoriginal_start_line(self):
        return self._original_start_line
        
    original_start_line = property(_getoriginal_start_line, doc="""The first line of the range for a multi-line comment. """)

    def _getstart_side(self):
        return self._start_side
        
    start_side = property(_getstart_side, doc="""The side of the first line of the range for a multi-line comment. """)

    def _getline(self):
        return self._line
        
    line = property(_getline, doc="""The line of the blob to which the comment applies. The last line of the range for a multi-line comment """)

    def _getoriginal_line(self):
        return self._original_line
        
    original_line = property(_getoriginal_line, doc="""The line of the blob to which the comment applies. The last line of the range for a multi-line comment """)

    def _getside(self):
        return self._side
        
    side = property(_getside, doc="""The side of the diff to which the comment applies. The side of the last line of the range for a multi-line comment """)

    def _getreactions(self):
        return self._reactions and ReactionRollup(**ReactionRollup.patchEntry(self._reactions))
        
    reactions = property(_getreactions)

    def _getbody_html(self):
        return self._body_html
        
    body_html = property(_getbody_html)

    def _getbody_text(self):
        return self._body_text
        
    body_text = property(_getbody_text)


    
##
##
##
class TimelineLineCommentedEvent(ResponseBase):
    """Timeline Line Commented Event """
    def __init__(self, event:str=None, node_id:str=None, comments:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._event = event
        self._node_id = node_id
        self._comments = comments
        return
        
    

    
    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getcomments(self):
        return self._comments and [ entry and PullRequestReviewComment(**entry) for entry in self._comments ]
        
    comments = property(_getcomments)


    
##
##
##
class TimelineCommitCommentedEvent(ResponseBase):
    """Timeline Commit Commented Event """
    def __init__(self, event:str=None, node_id:str=None, commit_id:str=None, comments:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._event = event
        self._node_id = node_id
        self._commit_id = commit_id
        self._comments = comments
        return
        
    

    
    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getcomments(self):
        return self._comments and [ entry and CommitComment(**entry) for entry in self._comments ]
        
    comments = property(_getcomments)


    
##
##
##
class TimelineAssignedIssueEvent(ResponseBase):
    """Timeline Assigned Issue Event """
    def __init__(self, assignee:dict, performed_via_github_app:dict, created_at:str, commit_url:str, commit_id:str, event:str, actor:dict, url:str, node_id:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._assignee = assignee
        self._performed_via_github_app = performed_via_github_app
        self._created_at = created_at
        self._commit_url = commit_url
        self._commit_id = commit_id
        self._event = event
        self._actor = actor
        self._url = url
        self._node_id = node_id
        self._id = id
        return
        
    

    
    def _getassignee(self):
        return self._assignee and SimpleUser(**self._assignee)
        
    assignee = property(_getassignee)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getactor(self):
        return self._actor and SimpleUser(**self._actor)
        
    actor = property(_getactor)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class TimelineUnassignedIssueEvent(ResponseBase):
    """Timeline Unassigned Issue Event """
    def __init__(self, assignee:dict, performed_via_github_app:dict, created_at:str, commit_url:str, commit_id:str, event:str, actor:dict, url:str, node_id:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._assignee = assignee
        self._performed_via_github_app = performed_via_github_app
        self._created_at = created_at
        self._commit_url = commit_url
        self._commit_id = commit_id
        self._event = event
        self._actor = actor
        self._url = url
        self._node_id = node_id
        self._id = id
        return
        
    

    
    def _getassignee(self):
        return self._assignee and SimpleUser(**self._assignee)
        
    assignee = property(_getassignee)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getevent(self):
        return self._event
        
    event = property(_getevent)

    def _getactor(self):
        return self._actor and SimpleUser(**self._actor)
        
    actor = property(_getactor)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class DeployKey(ResponseBase):
    """An SSH key granting access to a single repository. """
    def __init__(self, read_only:bool, created_at:str, verified:bool, title:str, url:str, key:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._read_only = read_only
        self._created_at = created_at
        self._verified = verified
        self._title = title
        self._url = url
        self._key = key
        self._id = id
        return
        
    

    
    def _getread_only(self):
        return self._read_only
        
    read_only = property(_getread_only)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getverified(self):
        return self._verified
        
    verified = property(_getverified)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getkey(self):
        return self._key
        
    key = property(_getkey)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class Licensecontent__links(ResponseBase):
    def __init__(self, Self:str, html:str, git:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._Self = Self
        self._html = html
        self._git = git
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['Self'] = entry.pop('self')
        return entry
    

    
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

    def _gethtml(self):
        return self._html
        
    html = property(_gethtml)

    def _getgit(self):
        return self._git
        
    git = property(_getgit)


    
    ##
    ##
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

##
##
##
class LicenseContent(ResponseBase):
    """License Content """
    def __init__(self, license:dict, _links:dict, encoding:str, content:str, type:str, download_url:str, git_url:str, html_url:str, url:str, size:int, sha:str, path:str, name:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._license = license
        self.__links = _links
        self._encoding = encoding
        self._content = content
        self._type = type
        self._download_url = download_url
        self._git_url = git_url
        self._html_url = html_url
        self._url = url
        self._size = size
        self._sha = sha
        self._path = path
        self._name = name
        return
        
    

    
    def _getlicense(self):
        return self._license and NullableLicenseSimple(**self._license)
        
    license = property(_getlicense)

    def _get_links(self):
        return self.__links and Licensecontent__links(**Licensecontent__links.patchEntry(self.__links))
        
    _links = property(_get_links)

    def _getencoding(self):
        return self._encoding
        
    encoding = property(_getencoding)

    def _getcontent(self):
        return self._content
        
    content = property(_getcontent)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getdownload_url(self):
        return self._download_url
        
    download_url = property(_getdownload_url)

    def _getgit_url(self):
        return self._git_url
        
    git_url = property(_getgit_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getpath(self):
        return self._path
        
    path = property(_getpath)

    def _getname(self):
        return self._name
        
    name = property(_getname)


    
##
##
##
class MergedUpstream(ResponseBase):
    """Results of a successful merge upstream request """
    def __init__(self, message:str=None, merge_type:str=None, base_branch:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._merge_type = merge_type
        self._base_branch = base_branch
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getmerge_type(self):
        return self._merge_type
        
    merge_type = property(_getmerge_type)

    def _getbase_branch(self):
        return self._base_branch
        
    base_branch = property(_getbase_branch)


    
##
##
##
class Milestone(ResponseBase):
    """A collection of related issues and pull requests. """
    def __init__(self, due_on:datetime, closed_at:datetime, updated_at:datetime, created_at:datetime, closed_issues:int, open_issues:int, creator:dict, description:str, title:str, number:int, node_id:str, id:int, labels_url:str, html_url:str, url:str, state:str='open', **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._due_on = due_on
        self._closed_at = closed_at
        self._updated_at = updated_at
        self._created_at = created_at
        self._closed_issues = closed_issues
        self._open_issues = open_issues
        self._creator = creator
        self._description = description
        self._title = title
        self._number = number
        self._node_id = node_id
        self._id = id
        self._labels_url = labels_url
        self._html_url = html_url
        self._url = url
        self._state = state
        return
        
    

    
    def _getdue_on(self):
        return self._due_on and datetime.datetime.fromisoformat(self._due_on[0:-1])
        
    due_on = property(_getdue_on)

    def _getclosed_at(self):
        return self._closed_at and datetime.datetime.fromisoformat(self._closed_at[0:-1])
        
    closed_at = property(_getclosed_at)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getclosed_issues(self):
        return self._closed_issues
        
    closed_issues = property(_getclosed_issues)

    def _getopen_issues(self):
        return self._open_issues
        
    open_issues = property(_getopen_issues)

    def _getcreator(self):
        return self._creator and NullableSimpleUser(**self._creator)
        
    creator = property(_getcreator)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle, doc="""The title of the milestone. """)

    def _getnumber(self):
        return self._number
        
    number = property(_getnumber, doc="""The number of the milestone. """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getlabels_url(self):
        return self._labels_url
        
    labels_url = property(_getlabels_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getstate(self):
        return self._state
        
    state = property(_getstate, doc="""The state of the milestone. """)


    
##
##
##
class PagesSourceHash(ResponseBase):
    def __init__(self, path:str, branch:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._path = path
        self._branch = branch
        return
        
    

    
    def _getpath(self):
        return self._path
        
    path = property(_getpath)

    def _getbranch(self):
        return self._branch
        
    branch = property(_getbranch)


    
##
##
##
class PagesHttpsCertificate(ResponseBase):
    def __init__(self, domains:list, description:str, state:str, expires_at:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._domains = domains
        self._description = description
        self._state = state
        self._expires_at = expires_at
        return
        
    

    
    def _getdomains(self):
        return self._domains and [ entry for entry in self._domains ]
        
    domains = property(_getdomains, doc="""Array of the domain set and its alternate name (if it is configured) """)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)

    def _getexpires_at(self):
        return self._expires_at
        
    expires_at = property(_getexpires_at)


    
##
##
##
class GithubPages(ResponseBase):
    """The configuration for GitHub Pages for a repository. """
    def __init__(self, public:bool, cname:str, status:str, url:str, protected_domain_state:str=None, pending_domain_unverified_at:datetime=None, custom_404:bool=False, html_url:str=None, source:dict=None, https_certificate:dict=None, https_enforced:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._public = public
        self._cname = cname
        self._status = status
        self._url = url
        self._protected_domain_state = protected_domain_state
        self._pending_domain_unverified_at = pending_domain_unverified_at
        self._custom_404 = custom_404
        self._html_url = html_url
        self._source = source
        self._https_certificate = https_certificate
        self._https_enforced = https_enforced
        return
        
    

    
    def _getpublic(self):
        return self._public
        
    public = property(_getpublic, doc="""Whether the GitHub Pages site is publicly visible. If set to `true`, the site is accessible to anyone on the internet. If set to `false`, the site will only be accessible to users who have at least `read` access to the repository that published the site. """)

    def _getcname(self):
        return self._cname
        
    cname = property(_getcname, doc="""The Pages site's custom domain """)

    def _getstatus(self):
        return self._status
        
    status = property(_getstatus, doc="""The status of the most recent build of the Page. """)

    def _geturl(self):
        return self._url
        
    url = property(_geturl, doc="""The API address for accessing this Page resource. """)

    def _getprotected_domain_state(self):
        return self._protected_domain_state
        
    protected_domain_state = property(_getprotected_domain_state, doc="""The state if the domain is verified """)

    def _getpending_domain_unverified_at(self):
        return self._pending_domain_unverified_at and datetime.datetime.fromisoformat(self._pending_domain_unverified_at[0:-1])
        
    pending_domain_unverified_at = property(_getpending_domain_unverified_at, doc="""The timestamp when a pending domain becomes unverified. """)

    def _getcustom_404(self):
        return self._custom_404
        
    custom_404 = property(_getcustom_404, doc="""Whether the Page has a custom 404 page. """)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url, doc="""The web address the Page can be accessed from. """)

    def _getsource(self):
        return self._source and PagesSourceHash(**self._source)
        
    source = property(_getsource)

    def _gethttps_certificate(self):
        return self._https_certificate and PagesHttpsCertificate(**self._https_certificate)
        
    https_certificate = property(_gethttps_certificate)

    def _gethttps_enforced(self):
        return self._https_enforced
        
    https_enforced = property(_gethttps_enforced, doc="""Whether https is enabled on the domain """)


    
##
##
##
class Pagebuild_error(ResponseBase):
    def __init__(self, message:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)


    
##
##
##
class PageBuild(ResponseBase):
    """Page Build """
    def __init__(self, updated_at:datetime, created_at:datetime, duration:int, commit:str, pusher:dict, error:dict, status:str, url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._updated_at = updated_at
        self._created_at = created_at
        self._duration = duration
        self._commit = commit
        self._pusher = pusher
        self._error = error
        self._status = status
        self._url = url
        return
        
    

    
    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getduration(self):
        return self._duration
        
    duration = property(_getduration)

    def _getcommit(self):
        return self._commit
        
    commit = property(_getcommit)

    def _getpusher(self):
        return self._pusher and NullableSimpleUser(**self._pusher)
        
    pusher = property(_getpusher)

    def _geterror(self):
        return self._error and Pagebuild_error(**self._error)
        
    error = property(_geterror)

    def _getstatus(self):
        return self._status
        
    status = property(_getstatus)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class PageBuildStatus(ResponseBase):
    """Page Build Status """
    def __init__(self, status:str, url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._status = status
        self._url = url
        return
        
    

    
    def _getstatus(self):
        return self._status
        
    status = property(_getstatus)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class RepositoryPreReceiveHook(ResponseBase):
    def __init__(self, id:int=None, name:str=None, enforcement:str=None, configuration_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._name = name
        self._enforcement = enforcement
        self._configuration_url = configuration_url
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getenforcement(self):
        return self._enforcement
        
    enforcement = property(_getenforcement)

    def _getconfiguration_url(self):
        return self._configuration_url
        
    configuration_url = property(_getconfiguration_url)


    
##
##
##
class TeamSimple(ResponseBase):
    """Groups of organization members that gives permissions on specified repositories. """
    def __init__(self, slug:str, repositories_url:str, html_url:str, permission:str, description:str, name:str, members_url:str, url:str, node_id:str, id:int, privacy:str=None, ldap_dn:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._slug = slug
        self._repositories_url = repositories_url
        self._html_url = html_url
        self._permission = permission
        self._description = description
        self._name = name
        self._members_url = members_url
        self._url = url
        self._node_id = node_id
        self._id = id
        self._privacy = privacy
        self._ldap_dn = ldap_dn
        return
        
    

    
    def _getslug(self):
        return self._slug
        
    slug = property(_getslug)

    def _getrepositories_url(self):
        return self._repositories_url
        
    repositories_url = property(_getrepositories_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getpermission(self):
        return self._permission
        
    permission = property(_getpermission, doc="""Permission that the team will have for its repositories """)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription, doc="""Description of the team """)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""Name of the team """)

    def _getmembers_url(self):
        return self._members_url
        
    members_url = property(_getmembers_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl, doc="""URL for the team """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the team """)

    def _getprivacy(self):
        return self._privacy
        
    privacy = property(_getprivacy, doc="""The level of privacy this team should have """)

    def _getldap_dn(self):
        return self._ldap_dn
        
    ldap_dn = property(_getldap_dn, doc="""Distinguished Name (DN) that team maps to within LDAP environment """)


    
##
##
##
class Pullrequest_labels(ResponseBase):
    def __init__(self, default:bool, color:str, description:str, name:str, url:str, node_id:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._default = default
        self._color = color
        self._description = description
        self._name = name
        self._url = url
        self._node_id = node_id
        self._id = id
        return
        
    

    
    def _getdefault(self):
        return self._default
        
    default = property(_getdefault)

    def _getcolor(self):
        return self._color
        
    color = property(_getcolor)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class Pullrequest_head_repo_owner(ResponseBase):
    def __init__(self, url:str, type:str, subscriptions_url:str, starred_url:str, site_admin:bool, repos_url:str, received_events_url:str, organizations_url:str, login:str, node_id:str, id:int, html_url:str, gravatar_id:str, gists_url:str, following_url:str, followers_url:str, events_url:str, avatar_url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._type = type
        self._subscriptions_url = subscriptions_url
        self._starred_url = starred_url
        self._site_admin = site_admin
        self._repos_url = repos_url
        self._received_events_url = received_events_url
        self._organizations_url = organizations_url
        self._login = login
        self._node_id = node_id
        self._id = id
        self._html_url = html_url
        self._gravatar_id = gravatar_id
        self._gists_url = gists_url
        self._following_url = following_url
        self._followers_url = followers_url
        self._events_url = events_url
        self._avatar_url = avatar_url
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getsubscriptions_url(self):
        return self._subscriptions_url
        
    subscriptions_url = property(_getsubscriptions_url)

    def _getstarred_url(self):
        return self._starred_url
        
    starred_url = property(_getstarred_url)

    def _getsite_admin(self):
        return self._site_admin
        
    site_admin = property(_getsite_admin)

    def _getrepos_url(self):
        return self._repos_url
        
    repos_url = property(_getrepos_url)

    def _getreceived_events_url(self):
        return self._received_events_url
        
    received_events_url = property(_getreceived_events_url)

    def _getorganizations_url(self):
        return self._organizations_url
        
    organizations_url = property(_getorganizations_url)

    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getgravatar_id(self):
        return self._gravatar_id
        
    gravatar_id = property(_getgravatar_id)

    def _getgists_url(self):
        return self._gists_url
        
    gists_url = property(_getgists_url)

    def _getfollowing_url(self):
        return self._following_url
        
    following_url = property(_getfollowing_url)

    def _getfollowers_url(self):
        return self._followers_url
        
    followers_url = property(_getfollowers_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)


    
##
##
##
class Pullrequest_head_repo_permissions(ResponseBase):
    def __init__(self, pull:bool, push:bool, admin:bool, maintain:bool=None, triage:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._pull = pull
        self._push = push
        self._admin = admin
        self._maintain = maintain
        self._triage = triage
        return
        
    

    
    def _getpull(self):
        return self._pull
        
    pull = property(_getpull)

    def _getpush(self):
        return self._push
        
    push = property(_getpush)

    def _getadmin(self):
        return self._admin
        
    admin = property(_getadmin)

    def _getmaintain(self):
        return self._maintain
        
    maintain = property(_getmaintain)

    def _gettriage(self):
        return self._triage
        
    triage = property(_gettriage)


    
##
##
##
class Pullrequest_head_repo_license(ResponseBase):
    def __init__(self, node_id:str, spdx_id:str, url:str, name:str, key:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._node_id = node_id
        self._spdx_id = spdx_id
        self._url = url
        self._name = name
        self._key = key
        return
        
    

    
    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getspdx_id(self):
        return self._spdx_id
        
    spdx_id = property(_getspdx_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getkey(self):
        return self._key
        
    key = property(_getkey)


    
##
##
##
class Pullrequest_head_repo(ResponseBase):
    def __init__(self, updated_at:datetime, created_at:datetime, watchers_count:int, watchers:int, svn_url:str, stargazers_count:int, ssh_url:str, size:int, pushed_at:datetime, license:dict, open_issues_count:int, open_issues:int, mirror_url:str, disabled:bool, archived:bool, language:str, homepage:str, has_pages:bool, has_wiki:bool, has_projects:bool, has_issues:bool, has_downloads:bool, git_url:str, forks_count:int, forks:int, default_branch:str, clone_url:str, url:str, trees_url:str, teams_url:str, tags_url:str, subscription_url:str, subscribers_url:str, statuses_url:str, stargazers_url:str, releases_url:str, pulls_url:str, private:bool, owner:dict, notifications_url:str, name:str, milestones_url:str, merges_url:str, languages_url:str, labels_url:str, keys_url:str, issues_url:str, issue_events_url:str, issue_comment_url:str, node_id:str, id:int, html_url:str, hooks_url:str, git_tags_url:str, git_refs_url:str, git_commits_url:str, full_name:str, forks_url:str, fork:bool, events_url:str, downloads_url:str, description:str, deployments_url:str, contributors_url:str, contents_url:str, compare_url:str, commits_url:str, comments_url:str, collaborators_url:str, branches_url:str, blobs_url:str, assignees_url:str, archive_url:str, master_branch:str=None, visibility:str=None, permissions:dict=None, temp_clone_token:str=None, allow_merge_commit:bool=None, allow_squash_merge:bool=None, allow_rebase_merge:bool=None, topics:list=[], allow_forking:bool=None, is_template:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._updated_at = updated_at
        self._created_at = created_at
        self._watchers_count = watchers_count
        self._watchers = watchers
        self._svn_url = svn_url
        self._stargazers_count = stargazers_count
        self._ssh_url = ssh_url
        self._size = size
        self._pushed_at = pushed_at
        self._license = license
        self._open_issues_count = open_issues_count
        self._open_issues = open_issues
        self._mirror_url = mirror_url
        self._disabled = disabled
        self._archived = archived
        self._language = language
        self._homepage = homepage
        self._has_pages = has_pages
        self._has_wiki = has_wiki
        self._has_projects = has_projects
        self._has_issues = has_issues
        self._has_downloads = has_downloads
        self._git_url = git_url
        self._forks_count = forks_count
        self._forks = forks
        self._default_branch = default_branch
        self._clone_url = clone_url
        self._url = url
        self._trees_url = trees_url
        self._teams_url = teams_url
        self._tags_url = tags_url
        self._subscription_url = subscription_url
        self._subscribers_url = subscribers_url
        self._statuses_url = statuses_url
        self._stargazers_url = stargazers_url
        self._releases_url = releases_url
        self._pulls_url = pulls_url
        self._private = private
        self._owner = owner
        self._notifications_url = notifications_url
        self._name = name
        self._milestones_url = milestones_url
        self._merges_url = merges_url
        self._languages_url = languages_url
        self._labels_url = labels_url
        self._keys_url = keys_url
        self._issues_url = issues_url
        self._issue_events_url = issue_events_url
        self._issue_comment_url = issue_comment_url
        self._node_id = node_id
        self._id = id
        self._html_url = html_url
        self._hooks_url = hooks_url
        self._git_tags_url = git_tags_url
        self._git_refs_url = git_refs_url
        self._git_commits_url = git_commits_url
        self._full_name = full_name
        self._forks_url = forks_url
        self._fork = fork
        self._events_url = events_url
        self._downloads_url = downloads_url
        self._description = description
        self._deployments_url = deployments_url
        self._contributors_url = contributors_url
        self._contents_url = contents_url
        self._compare_url = compare_url
        self._commits_url = commits_url
        self._comments_url = comments_url
        self._collaborators_url = collaborators_url
        self._branches_url = branches_url
        self._blobs_url = blobs_url
        self._assignees_url = assignees_url
        self._archive_url = archive_url
        self._master_branch = master_branch
        self._visibility = visibility
        self._permissions = permissions
        self._temp_clone_token = temp_clone_token
        self._allow_merge_commit = allow_merge_commit
        self._allow_squash_merge = allow_squash_merge
        self._allow_rebase_merge = allow_rebase_merge
        self._topics = topics
        self._allow_forking = allow_forking
        self._is_template = is_template
        return
        
    

    
    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getwatchers_count(self):
        return self._watchers_count
        
    watchers_count = property(_getwatchers_count)

    def _getwatchers(self):
        return self._watchers
        
    watchers = property(_getwatchers)

    def _getsvn_url(self):
        return self._svn_url
        
    svn_url = property(_getsvn_url)

    def _getstargazers_count(self):
        return self._stargazers_count
        
    stargazers_count = property(_getstargazers_count)

    def _getssh_url(self):
        return self._ssh_url
        
    ssh_url = property(_getssh_url)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _getpushed_at(self):
        return self._pushed_at and datetime.datetime.fromisoformat(self._pushed_at[0:-1])
        
    pushed_at = property(_getpushed_at)

    def _getlicense(self):
        return self._license and Pullrequest_head_repo_license(**self._license)
        
    license = property(_getlicense)

    def _getopen_issues_count(self):
        return self._open_issues_count
        
    open_issues_count = property(_getopen_issues_count)

    def _getopen_issues(self):
        return self._open_issues
        
    open_issues = property(_getopen_issues)

    def _getmirror_url(self):
        return self._mirror_url
        
    mirror_url = property(_getmirror_url)

    def _getdisabled(self):
        return self._disabled
        
    disabled = property(_getdisabled)

    def _getarchived(self):
        return self._archived
        
    archived = property(_getarchived)

    def _getlanguage(self):
        return self._language
        
    language = property(_getlanguage)

    def _gethomepage(self):
        return self._homepage
        
    homepage = property(_gethomepage)

    def _gethas_pages(self):
        return self._has_pages
        
    has_pages = property(_gethas_pages)

    def _gethas_wiki(self):
        return self._has_wiki
        
    has_wiki = property(_gethas_wiki)

    def _gethas_projects(self):
        return self._has_projects
        
    has_projects = property(_gethas_projects)

    def _gethas_issues(self):
        return self._has_issues
        
    has_issues = property(_gethas_issues)

    def _gethas_downloads(self):
        return self._has_downloads
        
    has_downloads = property(_gethas_downloads)

    def _getgit_url(self):
        return self._git_url
        
    git_url = property(_getgit_url)

    def _getforks_count(self):
        return self._forks_count
        
    forks_count = property(_getforks_count)

    def _getforks(self):
        return self._forks
        
    forks = property(_getforks)

    def _getdefault_branch(self):
        return self._default_branch
        
    default_branch = property(_getdefault_branch)

    def _getclone_url(self):
        return self._clone_url
        
    clone_url = property(_getclone_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gettrees_url(self):
        return self._trees_url
        
    trees_url = property(_gettrees_url)

    def _getteams_url(self):
        return self._teams_url
        
    teams_url = property(_getteams_url)

    def _gettags_url(self):
        return self._tags_url
        
    tags_url = property(_gettags_url)

    def _getsubscription_url(self):
        return self._subscription_url
        
    subscription_url = property(_getsubscription_url)

    def _getsubscribers_url(self):
        return self._subscribers_url
        
    subscribers_url = property(_getsubscribers_url)

    def _getstatuses_url(self):
        return self._statuses_url
        
    statuses_url = property(_getstatuses_url)

    def _getstargazers_url(self):
        return self._stargazers_url
        
    stargazers_url = property(_getstargazers_url)

    def _getreleases_url(self):
        return self._releases_url
        
    releases_url = property(_getreleases_url)

    def _getpulls_url(self):
        return self._pulls_url
        
    pulls_url = property(_getpulls_url)

    def _getprivate(self):
        return self._private
        
    private = property(_getprivate)

    def _getowner(self):
        return self._owner and Pullrequest_head_repo_owner(**self._owner)
        
    owner = property(_getowner)

    def _getnotifications_url(self):
        return self._notifications_url
        
    notifications_url = property(_getnotifications_url)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getmilestones_url(self):
        return self._milestones_url
        
    milestones_url = property(_getmilestones_url)

    def _getmerges_url(self):
        return self._merges_url
        
    merges_url = property(_getmerges_url)

    def _getlanguages_url(self):
        return self._languages_url
        
    languages_url = property(_getlanguages_url)

    def _getlabels_url(self):
        return self._labels_url
        
    labels_url = property(_getlabels_url)

    def _getkeys_url(self):
        return self._keys_url
        
    keys_url = property(_getkeys_url)

    def _getissues_url(self):
        return self._issues_url
        
    issues_url = property(_getissues_url)

    def _getissue_events_url(self):
        return self._issue_events_url
        
    issue_events_url = property(_getissue_events_url)

    def _getissue_comment_url(self):
        return self._issue_comment_url
        
    issue_comment_url = property(_getissue_comment_url)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _gethooks_url(self):
        return self._hooks_url
        
    hooks_url = property(_gethooks_url)

    def _getgit_tags_url(self):
        return self._git_tags_url
        
    git_tags_url = property(_getgit_tags_url)

    def _getgit_refs_url(self):
        return self._git_refs_url
        
    git_refs_url = property(_getgit_refs_url)

    def _getgit_commits_url(self):
        return self._git_commits_url
        
    git_commits_url = property(_getgit_commits_url)

    def _getfull_name(self):
        return self._full_name
        
    full_name = property(_getfull_name)

    def _getforks_url(self):
        return self._forks_url
        
    forks_url = property(_getforks_url)

    def _getfork(self):
        return self._fork
        
    fork = property(_getfork)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getdownloads_url(self):
        return self._downloads_url
        
    downloads_url = property(_getdownloads_url)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getdeployments_url(self):
        return self._deployments_url
        
    deployments_url = property(_getdeployments_url)

    def _getcontributors_url(self):
        return self._contributors_url
        
    contributors_url = property(_getcontributors_url)

    def _getcontents_url(self):
        return self._contents_url
        
    contents_url = property(_getcontents_url)

    def _getcompare_url(self):
        return self._compare_url
        
    compare_url = property(_getcompare_url)

    def _getcommits_url(self):
        return self._commits_url
        
    commits_url = property(_getcommits_url)

    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _getcollaborators_url(self):
        return self._collaborators_url
        
    collaborators_url = property(_getcollaborators_url)

    def _getbranches_url(self):
        return self._branches_url
        
    branches_url = property(_getbranches_url)

    def _getblobs_url(self):
        return self._blobs_url
        
    blobs_url = property(_getblobs_url)

    def _getassignees_url(self):
        return self._assignees_url
        
    assignees_url = property(_getassignees_url)

    def _getarchive_url(self):
        return self._archive_url
        
    archive_url = property(_getarchive_url)

    def _getmaster_branch(self):
        return self._master_branch
        
    master_branch = property(_getmaster_branch)

    def _getvisibility(self):
        return self._visibility
        
    visibility = property(_getvisibility, doc="""The repository visibility: public, private, or internal. """)

    def _getpermissions(self):
        return self._permissions and Pullrequest_head_repo_permissions(**self._permissions)
        
    permissions = property(_getpermissions)

    def _gettemp_clone_token(self):
        return self._temp_clone_token
        
    temp_clone_token = property(_gettemp_clone_token)

    def _getallow_merge_commit(self):
        return self._allow_merge_commit
        
    allow_merge_commit = property(_getallow_merge_commit)

    def _getallow_squash_merge(self):
        return self._allow_squash_merge
        
    allow_squash_merge = property(_getallow_squash_merge)

    def _getallow_rebase_merge(self):
        return self._allow_rebase_merge
        
    allow_rebase_merge = property(_getallow_rebase_merge)

    def _gettopics(self):
        return self._topics and [ entry for entry in self._topics ]
        
    topics = property(_gettopics)

    def _getallow_forking(self):
        return self._allow_forking
        
    allow_forking = property(_getallow_forking)

    def _getis_template(self):
        return self._is_template
        
    is_template = property(_getis_template)


    
##
##
##
class Pullrequest_head_user(ResponseBase):
    def __init__(self, url:str, type:str, subscriptions_url:str, starred_url:str, site_admin:bool, repos_url:str, received_events_url:str, organizations_url:str, login:str, node_id:str, id:int, html_url:str, gravatar_id:str, gists_url:str, following_url:str, followers_url:str, events_url:str, avatar_url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._type = type
        self._subscriptions_url = subscriptions_url
        self._starred_url = starred_url
        self._site_admin = site_admin
        self._repos_url = repos_url
        self._received_events_url = received_events_url
        self._organizations_url = organizations_url
        self._login = login
        self._node_id = node_id
        self._id = id
        self._html_url = html_url
        self._gravatar_id = gravatar_id
        self._gists_url = gists_url
        self._following_url = following_url
        self._followers_url = followers_url
        self._events_url = events_url
        self._avatar_url = avatar_url
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getsubscriptions_url(self):
        return self._subscriptions_url
        
    subscriptions_url = property(_getsubscriptions_url)

    def _getstarred_url(self):
        return self._starred_url
        
    starred_url = property(_getstarred_url)

    def _getsite_admin(self):
        return self._site_admin
        
    site_admin = property(_getsite_admin)

    def _getrepos_url(self):
        return self._repos_url
        
    repos_url = property(_getrepos_url)

    def _getreceived_events_url(self):
        return self._received_events_url
        
    received_events_url = property(_getreceived_events_url)

    def _getorganizations_url(self):
        return self._organizations_url
        
    organizations_url = property(_getorganizations_url)

    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getgravatar_id(self):
        return self._gravatar_id
        
    gravatar_id = property(_getgravatar_id)

    def _getgists_url(self):
        return self._gists_url
        
    gists_url = property(_getgists_url)

    def _getfollowing_url(self):
        return self._following_url
        
    following_url = property(_getfollowing_url)

    def _getfollowers_url(self):
        return self._followers_url
        
    followers_url = property(_getfollowers_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)


    
##
##
##
class Pullrequest_head(ResponseBase):
    def __init__(self, user:dict, sha:str, repo:dict, ref:str, label:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._user = user
        self._sha = sha
        self._repo = repo
        self._ref = ref
        self._label = label
        return
        
    

    
    def _getuser(self):
        return self._user and Pullrequest_head_user(**self._user)
        
    user = property(_getuser)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getrepo(self):
        return self._repo and Pullrequest_head_repo(**self._repo)
        
    repo = property(_getrepo)

    def _getref(self):
        return self._ref
        
    ref = property(_getref)

    def _getlabel(self):
        return self._label
        
    label = property(_getlabel)


    
##
##
##
class Pullrequest_base_repo_owner(ResponseBase):
    def __init__(self, url:str, type:str, subscriptions_url:str, starred_url:str, site_admin:bool, repos_url:str, received_events_url:str, organizations_url:str, login:str, node_id:str, id:int, html_url:str, gravatar_id:str, gists_url:str, following_url:str, followers_url:str, events_url:str, avatar_url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._type = type
        self._subscriptions_url = subscriptions_url
        self._starred_url = starred_url
        self._site_admin = site_admin
        self._repos_url = repos_url
        self._received_events_url = received_events_url
        self._organizations_url = organizations_url
        self._login = login
        self._node_id = node_id
        self._id = id
        self._html_url = html_url
        self._gravatar_id = gravatar_id
        self._gists_url = gists_url
        self._following_url = following_url
        self._followers_url = followers_url
        self._events_url = events_url
        self._avatar_url = avatar_url
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getsubscriptions_url(self):
        return self._subscriptions_url
        
    subscriptions_url = property(_getsubscriptions_url)

    def _getstarred_url(self):
        return self._starred_url
        
    starred_url = property(_getstarred_url)

    def _getsite_admin(self):
        return self._site_admin
        
    site_admin = property(_getsite_admin)

    def _getrepos_url(self):
        return self._repos_url
        
    repos_url = property(_getrepos_url)

    def _getreceived_events_url(self):
        return self._received_events_url
        
    received_events_url = property(_getreceived_events_url)

    def _getorganizations_url(self):
        return self._organizations_url
        
    organizations_url = property(_getorganizations_url)

    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getgravatar_id(self):
        return self._gravatar_id
        
    gravatar_id = property(_getgravatar_id)

    def _getgists_url(self):
        return self._gists_url
        
    gists_url = property(_getgists_url)

    def _getfollowing_url(self):
        return self._following_url
        
    following_url = property(_getfollowing_url)

    def _getfollowers_url(self):
        return self._followers_url
        
    followers_url = property(_getfollowers_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)


    
##
##
##
class Pullrequest_base_repo_permissions(ResponseBase):
    def __init__(self, pull:bool, push:bool, admin:bool, maintain:bool=None, triage:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._pull = pull
        self._push = push
        self._admin = admin
        self._maintain = maintain
        self._triage = triage
        return
        
    

    
    def _getpull(self):
        return self._pull
        
    pull = property(_getpull)

    def _getpush(self):
        return self._push
        
    push = property(_getpush)

    def _getadmin(self):
        return self._admin
        
    admin = property(_getadmin)

    def _getmaintain(self):
        return self._maintain
        
    maintain = property(_getmaintain)

    def _gettriage(self):
        return self._triage
        
    triage = property(_gettriage)


    
##
##
##
class Pullrequest_base_repo(ResponseBase):
    def __init__(self, updated_at:datetime, created_at:datetime, watchers_count:int, watchers:int, svn_url:str, stargazers_count:int, ssh_url:str, size:int, pushed_at:datetime, license:dict, open_issues_count:int, open_issues:int, mirror_url:str, disabled:bool, archived:bool, language:str, homepage:str, has_pages:bool, has_wiki:bool, has_projects:bool, has_issues:bool, has_downloads:bool, git_url:str, forks_count:int, forks:int, default_branch:str, clone_url:str, url:str, trees_url:str, teams_url:str, tags_url:str, subscription_url:str, subscribers_url:str, statuses_url:str, stargazers_url:str, releases_url:str, pulls_url:str, private:bool, owner:dict, notifications_url:str, name:str, milestones_url:str, merges_url:str, languages_url:str, labels_url:str, keys_url:str, issues_url:str, issue_events_url:str, issue_comment_url:str, node_id:str, id:int, html_url:str, hooks_url:str, git_tags_url:str, git_refs_url:str, git_commits_url:str, full_name:str, forks_url:str, fork:bool, events_url:str, downloads_url:str, description:str, deployments_url:str, contributors_url:str, contents_url:str, compare_url:str, commits_url:str, comments_url:str, collaborators_url:str, branches_url:str, blobs_url:str, assignees_url:str, archive_url:str, is_template:bool=None, master_branch:str=None, visibility:str=None, permissions:dict=None, temp_clone_token:str=None, allow_merge_commit:bool=None, allow_squash_merge:bool=None, allow_rebase_merge:bool=None, topics:list=[], allow_forking:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._updated_at = updated_at
        self._created_at = created_at
        self._watchers_count = watchers_count
        self._watchers = watchers
        self._svn_url = svn_url
        self._stargazers_count = stargazers_count
        self._ssh_url = ssh_url
        self._size = size
        self._pushed_at = pushed_at
        self._license = license
        self._open_issues_count = open_issues_count
        self._open_issues = open_issues
        self._mirror_url = mirror_url
        self._disabled = disabled
        self._archived = archived
        self._language = language
        self._homepage = homepage
        self._has_pages = has_pages
        self._has_wiki = has_wiki
        self._has_projects = has_projects
        self._has_issues = has_issues
        self._has_downloads = has_downloads
        self._git_url = git_url
        self._forks_count = forks_count
        self._forks = forks
        self._default_branch = default_branch
        self._clone_url = clone_url
        self._url = url
        self._trees_url = trees_url
        self._teams_url = teams_url
        self._tags_url = tags_url
        self._subscription_url = subscription_url
        self._subscribers_url = subscribers_url
        self._statuses_url = statuses_url
        self._stargazers_url = stargazers_url
        self._releases_url = releases_url
        self._pulls_url = pulls_url
        self._private = private
        self._owner = owner
        self._notifications_url = notifications_url
        self._name = name
        self._milestones_url = milestones_url
        self._merges_url = merges_url
        self._languages_url = languages_url
        self._labels_url = labels_url
        self._keys_url = keys_url
        self._issues_url = issues_url
        self._issue_events_url = issue_events_url
        self._issue_comment_url = issue_comment_url
        self._node_id = node_id
        self._id = id
        self._html_url = html_url
        self._hooks_url = hooks_url
        self._git_tags_url = git_tags_url
        self._git_refs_url = git_refs_url
        self._git_commits_url = git_commits_url
        self._full_name = full_name
        self._forks_url = forks_url
        self._fork = fork
        self._events_url = events_url
        self._downloads_url = downloads_url
        self._description = description
        self._deployments_url = deployments_url
        self._contributors_url = contributors_url
        self._contents_url = contents_url
        self._compare_url = compare_url
        self._commits_url = commits_url
        self._comments_url = comments_url
        self._collaborators_url = collaborators_url
        self._branches_url = branches_url
        self._blobs_url = blobs_url
        self._assignees_url = assignees_url
        self._archive_url = archive_url
        self._is_template = is_template
        self._master_branch = master_branch
        self._visibility = visibility
        self._permissions = permissions
        self._temp_clone_token = temp_clone_token
        self._allow_merge_commit = allow_merge_commit
        self._allow_squash_merge = allow_squash_merge
        self._allow_rebase_merge = allow_rebase_merge
        self._topics = topics
        self._allow_forking = allow_forking
        return
        
    

    
    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getwatchers_count(self):
        return self._watchers_count
        
    watchers_count = property(_getwatchers_count)

    def _getwatchers(self):
        return self._watchers
        
    watchers = property(_getwatchers)

    def _getsvn_url(self):
        return self._svn_url
        
    svn_url = property(_getsvn_url)

    def _getstargazers_count(self):
        return self._stargazers_count
        
    stargazers_count = property(_getstargazers_count)

    def _getssh_url(self):
        return self._ssh_url
        
    ssh_url = property(_getssh_url)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _getpushed_at(self):
        return self._pushed_at and datetime.datetime.fromisoformat(self._pushed_at[0:-1])
        
    pushed_at = property(_getpushed_at)

    def _getlicense(self):
        return self._license and NullableLicenseSimple(**self._license)
        
    license = property(_getlicense)

    def _getopen_issues_count(self):
        return self._open_issues_count
        
    open_issues_count = property(_getopen_issues_count)

    def _getopen_issues(self):
        return self._open_issues
        
    open_issues = property(_getopen_issues)

    def _getmirror_url(self):
        return self._mirror_url
        
    mirror_url = property(_getmirror_url)

    def _getdisabled(self):
        return self._disabled
        
    disabled = property(_getdisabled)

    def _getarchived(self):
        return self._archived
        
    archived = property(_getarchived)

    def _getlanguage(self):
        return self._language
        
    language = property(_getlanguage)

    def _gethomepage(self):
        return self._homepage
        
    homepage = property(_gethomepage)

    def _gethas_pages(self):
        return self._has_pages
        
    has_pages = property(_gethas_pages)

    def _gethas_wiki(self):
        return self._has_wiki
        
    has_wiki = property(_gethas_wiki)

    def _gethas_projects(self):
        return self._has_projects
        
    has_projects = property(_gethas_projects)

    def _gethas_issues(self):
        return self._has_issues
        
    has_issues = property(_gethas_issues)

    def _gethas_downloads(self):
        return self._has_downloads
        
    has_downloads = property(_gethas_downloads)

    def _getgit_url(self):
        return self._git_url
        
    git_url = property(_getgit_url)

    def _getforks_count(self):
        return self._forks_count
        
    forks_count = property(_getforks_count)

    def _getforks(self):
        return self._forks
        
    forks = property(_getforks)

    def _getdefault_branch(self):
        return self._default_branch
        
    default_branch = property(_getdefault_branch)

    def _getclone_url(self):
        return self._clone_url
        
    clone_url = property(_getclone_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gettrees_url(self):
        return self._trees_url
        
    trees_url = property(_gettrees_url)

    def _getteams_url(self):
        return self._teams_url
        
    teams_url = property(_getteams_url)

    def _gettags_url(self):
        return self._tags_url
        
    tags_url = property(_gettags_url)

    def _getsubscription_url(self):
        return self._subscription_url
        
    subscription_url = property(_getsubscription_url)

    def _getsubscribers_url(self):
        return self._subscribers_url
        
    subscribers_url = property(_getsubscribers_url)

    def _getstatuses_url(self):
        return self._statuses_url
        
    statuses_url = property(_getstatuses_url)

    def _getstargazers_url(self):
        return self._stargazers_url
        
    stargazers_url = property(_getstargazers_url)

    def _getreleases_url(self):
        return self._releases_url
        
    releases_url = property(_getreleases_url)

    def _getpulls_url(self):
        return self._pulls_url
        
    pulls_url = property(_getpulls_url)

    def _getprivate(self):
        return self._private
        
    private = property(_getprivate)

    def _getowner(self):
        return self._owner and Pullrequest_base_repo_owner(**self._owner)
        
    owner = property(_getowner)

    def _getnotifications_url(self):
        return self._notifications_url
        
    notifications_url = property(_getnotifications_url)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getmilestones_url(self):
        return self._milestones_url
        
    milestones_url = property(_getmilestones_url)

    def _getmerges_url(self):
        return self._merges_url
        
    merges_url = property(_getmerges_url)

    def _getlanguages_url(self):
        return self._languages_url
        
    languages_url = property(_getlanguages_url)

    def _getlabels_url(self):
        return self._labels_url
        
    labels_url = property(_getlabels_url)

    def _getkeys_url(self):
        return self._keys_url
        
    keys_url = property(_getkeys_url)

    def _getissues_url(self):
        return self._issues_url
        
    issues_url = property(_getissues_url)

    def _getissue_events_url(self):
        return self._issue_events_url
        
    issue_events_url = property(_getissue_events_url)

    def _getissue_comment_url(self):
        return self._issue_comment_url
        
    issue_comment_url = property(_getissue_comment_url)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _gethooks_url(self):
        return self._hooks_url
        
    hooks_url = property(_gethooks_url)

    def _getgit_tags_url(self):
        return self._git_tags_url
        
    git_tags_url = property(_getgit_tags_url)

    def _getgit_refs_url(self):
        return self._git_refs_url
        
    git_refs_url = property(_getgit_refs_url)

    def _getgit_commits_url(self):
        return self._git_commits_url
        
    git_commits_url = property(_getgit_commits_url)

    def _getfull_name(self):
        return self._full_name
        
    full_name = property(_getfull_name)

    def _getforks_url(self):
        return self._forks_url
        
    forks_url = property(_getforks_url)

    def _getfork(self):
        return self._fork
        
    fork = property(_getfork)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getdownloads_url(self):
        return self._downloads_url
        
    downloads_url = property(_getdownloads_url)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getdeployments_url(self):
        return self._deployments_url
        
    deployments_url = property(_getdeployments_url)

    def _getcontributors_url(self):
        return self._contributors_url
        
    contributors_url = property(_getcontributors_url)

    def _getcontents_url(self):
        return self._contents_url
        
    contents_url = property(_getcontents_url)

    def _getcompare_url(self):
        return self._compare_url
        
    compare_url = property(_getcompare_url)

    def _getcommits_url(self):
        return self._commits_url
        
    commits_url = property(_getcommits_url)

    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _getcollaborators_url(self):
        return self._collaborators_url
        
    collaborators_url = property(_getcollaborators_url)

    def _getbranches_url(self):
        return self._branches_url
        
    branches_url = property(_getbranches_url)

    def _getblobs_url(self):
        return self._blobs_url
        
    blobs_url = property(_getblobs_url)

    def _getassignees_url(self):
        return self._assignees_url
        
    assignees_url = property(_getassignees_url)

    def _getarchive_url(self):
        return self._archive_url
        
    archive_url = property(_getarchive_url)

    def _getis_template(self):
        return self._is_template
        
    is_template = property(_getis_template)

    def _getmaster_branch(self):
        return self._master_branch
        
    master_branch = property(_getmaster_branch)

    def _getvisibility(self):
        return self._visibility
        
    visibility = property(_getvisibility, doc="""The repository visibility: public, private, or internal. """)

    def _getpermissions(self):
        return self._permissions and Pullrequest_base_repo_permissions(**self._permissions)
        
    permissions = property(_getpermissions)

    def _gettemp_clone_token(self):
        return self._temp_clone_token
        
    temp_clone_token = property(_gettemp_clone_token)

    def _getallow_merge_commit(self):
        return self._allow_merge_commit
        
    allow_merge_commit = property(_getallow_merge_commit)

    def _getallow_squash_merge(self):
        return self._allow_squash_merge
        
    allow_squash_merge = property(_getallow_squash_merge)

    def _getallow_rebase_merge(self):
        return self._allow_rebase_merge
        
    allow_rebase_merge = property(_getallow_rebase_merge)

    def _gettopics(self):
        return self._topics and [ entry for entry in self._topics ]
        
    topics = property(_gettopics)

    def _getallow_forking(self):
        return self._allow_forking
        
    allow_forking = property(_getallow_forking)


    
##
##
##
class Pullrequest_base_user(ResponseBase):
    def __init__(self, url:str, type:str, subscriptions_url:str, starred_url:str, site_admin:bool, repos_url:str, received_events_url:str, organizations_url:str, login:str, node_id:str, id:int, html_url:str, gravatar_id:str, gists_url:str, following_url:str, followers_url:str, events_url:str, avatar_url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._type = type
        self._subscriptions_url = subscriptions_url
        self._starred_url = starred_url
        self._site_admin = site_admin
        self._repos_url = repos_url
        self._received_events_url = received_events_url
        self._organizations_url = organizations_url
        self._login = login
        self._node_id = node_id
        self._id = id
        self._html_url = html_url
        self._gravatar_id = gravatar_id
        self._gists_url = gists_url
        self._following_url = following_url
        self._followers_url = followers_url
        self._events_url = events_url
        self._avatar_url = avatar_url
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getsubscriptions_url(self):
        return self._subscriptions_url
        
    subscriptions_url = property(_getsubscriptions_url)

    def _getstarred_url(self):
        return self._starred_url
        
    starred_url = property(_getstarred_url)

    def _getsite_admin(self):
        return self._site_admin
        
    site_admin = property(_getsite_admin)

    def _getrepos_url(self):
        return self._repos_url
        
    repos_url = property(_getrepos_url)

    def _getreceived_events_url(self):
        return self._received_events_url
        
    received_events_url = property(_getreceived_events_url)

    def _getorganizations_url(self):
        return self._organizations_url
        
    organizations_url = property(_getorganizations_url)

    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getgravatar_id(self):
        return self._gravatar_id
        
    gravatar_id = property(_getgravatar_id)

    def _getgists_url(self):
        return self._gists_url
        
    gists_url = property(_getgists_url)

    def _getfollowing_url(self):
        return self._following_url
        
    following_url = property(_getfollowing_url)

    def _getfollowers_url(self):
        return self._followers_url
        
    followers_url = property(_getfollowers_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)


    
##
##
##
class Pullrequest_base(ResponseBase):
    def __init__(self, user:dict, sha:str, repo:dict, ref:str, label:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._user = user
        self._sha = sha
        self._repo = repo
        self._ref = ref
        self._label = label
        return
        
    

    
    def _getuser(self):
        return self._user and Pullrequest_base_user(**self._user)
        
    user = property(_getuser)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getrepo(self):
        return self._repo and Pullrequest_base_repo(**self._repo)
        
    repo = property(_getrepo)

    def _getref(self):
        return self._ref
        
    ref = property(_getref)

    def _getlabel(self):
        return self._label
        
    label = property(_getlabel)


    
##
##
##
class Pullrequest__links(ResponseBase):
    def __init__(self, Self:dict, review_comment:dict, review_comments:dict, issue:dict, html:dict, statuses:dict, commits:dict, comments:dict, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._Self = Self
        self._review_comment = review_comment
        self._review_comments = review_comments
        self._issue = issue
        self._html = html
        self._statuses = statuses
        self._commits = commits
        self._comments = comments
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['Self'] = entry.pop('self')
        return entry
    

    
    def _getSelf(self):
        return self._Self and Link(**self._Self)
        
    Self = property(_getSelf)

    def _getreview_comment(self):
        return self._review_comment and Link(**self._review_comment)
        
    review_comment = property(_getreview_comment)

    def _getreview_comments(self):
        return self._review_comments and Link(**self._review_comments)
        
    review_comments = property(_getreview_comments)

    def _getissue(self):
        return self._issue and Link(**self._issue)
        
    issue = property(_getissue)

    def _gethtml(self):
        return self._html and Link(**self._html)
        
    html = property(_gethtml)

    def _getstatuses(self):
        return self._statuses and Link(**self._statuses)
        
    statuses = property(_getstatuses)

    def _getcommits(self):
        return self._commits and Link(**self._commits)
        
    commits = property(_getcommits)

    def _getcomments(self):
        return self._comments and Link(**self._comments)
        
    comments = property(_getcomments)


    
    ##
    ##
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

##
##
##
class PullRequest(ResponseBase):
    """Pull requests let you tell others about changes you've pushed to a repository on GitHub. Once a pull request is sent, interested parties can review the set of changes, discuss potential modifications, and even push follow-up commits if necessary. """
    def __init__(self, changed_files:int, deletions:int, additions:int, commits:int, maintainer_can_modify:bool, review_comments:int, comments:int, merged_by:dict, mergeable_state:str, mergeable:bool, merged:bool, auto_merge:dict, author_association:str, _links:dict, base:dict, head:dict, assignee:dict, merge_commit_sha:str, merged_at:datetime, closed_at:datetime, updated_at:datetime, created_at:datetime, milestone:dict, labels:list, body:str, user:dict, title:str, locked:bool, state:str, number:int, statuses_url:str, comments_url:str, review_comment_url:str, review_comments_url:str, commits_url:str, issue_url:str, patch_url:str, diff_url:str, html_url:str, node_id:str, id:int, url:str, active_lock_reason:str=None, assignees:list=[], requested_reviewers:list=[], requested_teams:list=[], draft:bool=None, rebaseable:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._changed_files = changed_files
        self._deletions = deletions
        self._additions = additions
        self._commits = commits
        self._maintainer_can_modify = maintainer_can_modify
        self._review_comments = review_comments
        self._comments = comments
        self._merged_by = merged_by
        self._mergeable_state = mergeable_state
        self._mergeable = mergeable
        self._merged = merged
        self._auto_merge = auto_merge
        self._author_association = author_association
        self.__links = _links
        self._base = base
        self._head = head
        self._assignee = assignee
        self._merge_commit_sha = merge_commit_sha
        self._merged_at = merged_at
        self._closed_at = closed_at
        self._updated_at = updated_at
        self._created_at = created_at
        self._milestone = milestone
        self._labels = labels
        self._body = body
        self._user = user
        self._title = title
        self._locked = locked
        self._state = state
        self._number = number
        self._statuses_url = statuses_url
        self._comments_url = comments_url
        self._review_comment_url = review_comment_url
        self._review_comments_url = review_comments_url
        self._commits_url = commits_url
        self._issue_url = issue_url
        self._patch_url = patch_url
        self._diff_url = diff_url
        self._html_url = html_url
        self._node_id = node_id
        self._id = id
        self._url = url
        self._active_lock_reason = active_lock_reason
        self._assignees = assignees
        self._requested_reviewers = requested_reviewers
        self._requested_teams = requested_teams
        self._draft = draft
        self._rebaseable = rebaseable
        return
        
    

    
    def _getchanged_files(self):
        return self._changed_files
        
    changed_files = property(_getchanged_files)

    def _getdeletions(self):
        return self._deletions
        
    deletions = property(_getdeletions)

    def _getadditions(self):
        return self._additions
        
    additions = property(_getadditions)

    def _getcommits(self):
        return self._commits
        
    commits = property(_getcommits)

    def _getmaintainer_can_modify(self):
        return self._maintainer_can_modify
        
    maintainer_can_modify = property(_getmaintainer_can_modify, doc="""Indicates whether maintainers can modify the pull request. """)

    def _getreview_comments(self):
        return self._review_comments
        
    review_comments = property(_getreview_comments)

    def _getcomments(self):
        return self._comments
        
    comments = property(_getcomments)

    def _getmerged_by(self):
        return self._merged_by and NullableSimpleUser(**self._merged_by)
        
    merged_by = property(_getmerged_by)

    def _getmergeable_state(self):
        return self._mergeable_state
        
    mergeable_state = property(_getmergeable_state)

    def _getmergeable(self):
        return self._mergeable
        
    mergeable = property(_getmergeable)

    def _getmerged(self):
        return self._merged
        
    merged = property(_getmerged)

    def _getauto_merge(self):
        return self._auto_merge and Auto_merge(**self._auto_merge)
        
    auto_merge = property(_getauto_merge)

    def _getauthor_association(self):
        return self._author_association
        
    author_association = property(_getauthor_association)

    def _get_links(self):
        return self.__links and Pullrequest__links(**Pullrequest__links.patchEntry(self.__links))
        
    _links = property(_get_links)

    def _getbase(self):
        return self._base and Pullrequest_base(**self._base)
        
    base = property(_getbase)

    def _gethead(self):
        return self._head and Pullrequest_head(**self._head)
        
    head = property(_gethead)

    def _getassignee(self):
        return self._assignee and NullableSimpleUser(**self._assignee)
        
    assignee = property(_getassignee)

    def _getmerge_commit_sha(self):
        return self._merge_commit_sha
        
    merge_commit_sha = property(_getmerge_commit_sha)

    def _getmerged_at(self):
        return self._merged_at and datetime.datetime.fromisoformat(self._merged_at[0:-1])
        
    merged_at = property(_getmerged_at)

    def _getclosed_at(self):
        return self._closed_at and datetime.datetime.fromisoformat(self._closed_at[0:-1])
        
    closed_at = property(_getclosed_at)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getmilestone(self):
        return self._milestone and NullableMilestone(**self._milestone)
        
    milestone = property(_getmilestone)

    def _getlabels(self):
        return self._labels and [ entry and Pullrequest_labels(**entry) for entry in self._labels ]
        
    labels = property(_getlabels)

    def _getbody(self):
        return self._body
        
    body = property(_getbody)

    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle, doc="""The title of the pull request. """)

    def _getlocked(self):
        return self._locked
        
    locked = property(_getlocked)

    def _getstate(self):
        return self._state
        
    state = property(_getstate, doc="""State of this Pull Request. Either `open` or `closed`. """)

    def _getnumber(self):
        return self._number
        
    number = property(_getnumber, doc="""Number uniquely identifying the pull request within its repository. """)

    def _getstatuses_url(self):
        return self._statuses_url
        
    statuses_url = property(_getstatuses_url)

    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _getreview_comment_url(self):
        return self._review_comment_url
        
    review_comment_url = property(_getreview_comment_url)

    def _getreview_comments_url(self):
        return self._review_comments_url
        
    review_comments_url = property(_getreview_comments_url)

    def _getcommits_url(self):
        return self._commits_url
        
    commits_url = property(_getcommits_url)

    def _getissue_url(self):
        return self._issue_url
        
    issue_url = property(_getissue_url)

    def _getpatch_url(self):
        return self._patch_url
        
    patch_url = property(_getpatch_url)

    def _getdiff_url(self):
        return self._diff_url
        
    diff_url = property(_getdiff_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getactive_lock_reason(self):
        return self._active_lock_reason
        
    active_lock_reason = property(_getactive_lock_reason)

    def _getassignees(self):
        return self._assignees and [ entry and SimpleUser(**entry) for entry in self._assignees ]
        
    assignees = property(_getassignees)

    def _getrequested_reviewers(self):
        return self._requested_reviewers and [ entry and SimpleUser(**entry) for entry in self._requested_reviewers ]
        
    requested_reviewers = property(_getrequested_reviewers)

    def _getrequested_teams(self):
        return self._requested_teams and [ entry and TeamSimple(**entry) for entry in self._requested_teams ]
        
    requested_teams = property(_getrequested_teams)

    def _getdraft(self):
        return self._draft
        
    draft = property(_getdraft, doc="""Indicates whether or not the pull request is a draft. """)

    def _getrebaseable(self):
        return self._rebaseable
        
    rebaseable = property(_getrebaseable)


    
##
##
##
class PullRequestMergeResult(ResponseBase):
    """Pull Request Merge Result """
    def __init__(self, message:str, merged:bool, sha:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._merged = merged
        self._sha = sha
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getmerged(self):
        return self._merged
        
    merged = property(_getmerged)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)


    
##
##
##
class PullRequestReviewRequest(ResponseBase):
    """Pull Request Review Request """
    def __init__(self, teams:list, users:list, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._teams = teams
        self._users = users
        return
        
    

    
    def _getteams(self):
        return self._teams and [ entry and Team(**entry) for entry in self._teams ]
        
    teams = property(_getteams)

    def _getusers(self):
        return self._users and [ entry and SimpleUser(**entry) for entry in self._users ]
        
    users = property(_getusers)


    
##
##
##
class Pullrequestreview__links_html(ResponseBase):
    def __init__(self, href:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._href = href
        return
        
    

    
    def _gethref(self):
        return self._href
        
    href = property(_gethref)


    
##
##
##
class Pullrequestreview__links_pull_request(ResponseBase):
    def __init__(self, href:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._href = href
        return
        
    

    
    def _gethref(self):
        return self._href
        
    href = property(_gethref)


    
##
##
##
class Pullrequestreview__links(ResponseBase):
    def __init__(self, pull_request:dict, html:dict, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._pull_request = pull_request
        self._html = html
        return
        
    

    
    def _getpull_request(self):
        return self._pull_request and Pullrequestreview__links_pull_request(**self._pull_request)
        
    pull_request = property(_getpull_request)

    def _gethtml(self):
        return self._html and Pullrequestreview__links_html(**self._html)
        
    html = property(_gethtml)


    
##
##
##
class PullRequestReview(ResponseBase):
    """Pull Request Reviews are reviews on pull requests. """
    def __init__(self, author_association:str, commit_id:str, _links:dict, pull_request_url:str, html_url:str, state:str, body:str, user:dict, node_id:str, id:int, submitted_at:datetime=None, body_html:str=None, body_text:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._author_association = author_association
        self._commit_id = commit_id
        self.__links = _links
        self._pull_request_url = pull_request_url
        self._html_url = html_url
        self._state = state
        self._body = body
        self._user = user
        self._node_id = node_id
        self._id = id
        self._submitted_at = submitted_at
        self._body_html = body_html
        self._body_text = body_text
        return
        
    

    
    def _getauthor_association(self):
        return self._author_association
        
    author_association = property(_getauthor_association)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id, doc="""A commit SHA for the review. """)

    def _get_links(self):
        return self.__links and Pullrequestreview__links(**self.__links)
        
    _links = property(_get_links)

    def _getpull_request_url(self):
        return self._pull_request_url
        
    pull_request_url = property(_getpull_request_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)

    def _getbody(self):
        return self._body
        
    body = property(_getbody, doc="""The text of the review. """)

    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""Unique identifier of the review """)

    def _getsubmitted_at(self):
        return self._submitted_at and datetime.datetime.fromisoformat(self._submitted_at[0:-1])
        
    submitted_at = property(_getsubmitted_at)

    def _getbody_html(self):
        return self._body_html
        
    body_html = property(_getbody_html)

    def _getbody_text(self):
        return self._body_text
        
    body_text = property(_getbody_text)


    
##
##
##
class Legacyreviewcomment__links(ResponseBase):
    def __init__(self, pull_request:dict, html:dict, Self:dict, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._pull_request = pull_request
        self._html = html
        self._Self = Self
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['Self'] = entry.pop('self')
        return entry
    

    
    def _getpull_request(self):
        return self._pull_request and Link(**self._pull_request)
        
    pull_request = property(_getpull_request)

    def _gethtml(self):
        return self._html and Link(**self._html)
        
    html = property(_gethtml)

    def _getSelf(self):
        return self._Self and Link(**self._Self)
        
    Self = property(_getSelf)


    
    ##
    ##
    def _getSelf(self):
        return self._Self
        
    Self = property(_getSelf)

##
##
##
class LegacyReviewComment(ResponseBase):
    """Legacy Review Comment """
    def __init__(self, _links:dict, author_association:str, pull_request_url:str, html_url:str, updated_at:datetime, created_at:datetime, body:str, user:dict, original_commit_id:str, commit_id:str, original_position:int, position:int, path:str, diff_hunk:str, node_id:str, id:int, pull_request_review_id:int, url:str, in_reply_to_id:int=None, body_text:str=None, body_html:str=None, reactions:dict=None, side:str='RIGHT', start_side:str='RIGHT', line:int=None, original_line:int=None, start_line:int=None, original_start_line:int=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self.__links = _links
        self._author_association = author_association
        self._pull_request_url = pull_request_url
        self._html_url = html_url
        self._updated_at = updated_at
        self._created_at = created_at
        self._body = body
        self._user = user
        self._original_commit_id = original_commit_id
        self._commit_id = commit_id
        self._original_position = original_position
        self._position = position
        self._path = path
        self._diff_hunk = diff_hunk
        self._node_id = node_id
        self._id = id
        self._pull_request_review_id = pull_request_review_id
        self._url = url
        self._in_reply_to_id = in_reply_to_id
        self._body_text = body_text
        self._body_html = body_html
        self._reactions = reactions
        self._side = side
        self._start_side = start_side
        self._line = line
        self._original_line = original_line
        self._start_line = start_line
        self._original_start_line = original_start_line
        return
        
    

    
    def _get_links(self):
        return self.__links and Legacyreviewcomment__links(**Legacyreviewcomment__links.patchEntry(self.__links))
        
    _links = property(_get_links)

    def _getauthor_association(self):
        return self._author_association
        
    author_association = property(_getauthor_association)

    def _getpull_request_url(self):
        return self._pull_request_url
        
    pull_request_url = property(_getpull_request_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getbody(self):
        return self._body
        
    body = property(_getbody)

    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _getoriginal_commit_id(self):
        return self._original_commit_id
        
    original_commit_id = property(_getoriginal_commit_id)

    def _getcommit_id(self):
        return self._commit_id
        
    commit_id = property(_getcommit_id)

    def _getoriginal_position(self):
        return self._original_position
        
    original_position = property(_getoriginal_position)

    def _getposition(self):
        return self._position
        
    position = property(_getposition)

    def _getpath(self):
        return self._path
        
    path = property(_getpath)

    def _getdiff_hunk(self):
        return self._diff_hunk
        
    diff_hunk = property(_getdiff_hunk)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getpull_request_review_id(self):
        return self._pull_request_review_id
        
    pull_request_review_id = property(_getpull_request_review_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getin_reply_to_id(self):
        return self._in_reply_to_id
        
    in_reply_to_id = property(_getin_reply_to_id)

    def _getbody_text(self):
        return self._body_text
        
    body_text = property(_getbody_text)

    def _getbody_html(self):
        return self._body_html
        
    body_html = property(_getbody_html)

    def _getreactions(self):
        return self._reactions and ReactionRollup(**ReactionRollup.patchEntry(self._reactions))
        
    reactions = property(_getreactions)

    def _getside(self):
        return self._side
        
    side = property(_getside, doc="""The side of the first line of the range for a multi-line comment. """)

    def _getstart_side(self):
        return self._start_side
        
    start_side = property(_getstart_side, doc="""The side of the first line of the range for a multi-line comment. """)

    def _getline(self):
        return self._line
        
    line = property(_getline, doc="""The line of the blob to which the comment applies. The last line of the range for a multi-line comment """)

    def _getoriginal_line(self):
        return self._original_line
        
    original_line = property(_getoriginal_line, doc="""The original line of the blob to which the comment applies. The last line of the range for a multi-line comment """)

    def _getstart_line(self):
        return self._start_line
        
    start_line = property(_getstart_line, doc="""The first line of the range for a multi-line comment. """)

    def _getoriginal_start_line(self):
        return self._original_start_line
        
    original_start_line = property(_getoriginal_start_line, doc="""The original first line of the range for a multi-line comment. """)


    
##
##
##
class ReleaseAsset(ResponseBase):
    """Data related to a release. """
    def __init__(self, uploader:dict, updated_at:datetime, created_at:datetime, download_count:int, size:int, content_type:str, state:str, label:str, name:str, node_id:str, id:int, browser_download_url:str, url:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._uploader = uploader
        self._updated_at = updated_at
        self._created_at = created_at
        self._download_count = download_count
        self._size = size
        self._content_type = content_type
        self._state = state
        self._label = label
        self._name = name
        self._node_id = node_id
        self._id = id
        self._browser_download_url = browser_download_url
        self._url = url
        return
        
    

    
    def _getuploader(self):
        return self._uploader and NullableSimpleUser(**self._uploader)
        
    uploader = property(_getuploader)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getdownload_count(self):
        return self._download_count
        
    download_count = property(_getdownload_count)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _getcontent_type(self):
        return self._content_type
        
    content_type = property(_getcontent_type)

    def _getstate(self):
        return self._state
        
    state = property(_getstate, doc="""State of the release asset. """)

    def _getlabel(self):
        return self._label
        
    label = property(_getlabel)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The file name of the asset. """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getbrowser_download_url(self):
        return self._browser_download_url
        
    browser_download_url = property(_getbrowser_download_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class Release(ResponseBase):
    """A release. """
    def __init__(self, assets:list, author:dict, published_at:datetime, created_at:datetime, prerelease:bool, draft:bool, name:str, target_commitish:str, tag_name:str, node_id:str, id:int, zipball_url:str, tarball_url:str, upload_url:str, assets_url:str, html_url:str, url:str, body:str=None, body_html:str=None, body_text:str=None, mentions_count:int=None, reactions:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._assets = assets
        self._author = author
        self._published_at = published_at
        self._created_at = created_at
        self._prerelease = prerelease
        self._draft = draft
        self._name = name
        self._target_commitish = target_commitish
        self._tag_name = tag_name
        self._node_id = node_id
        self._id = id
        self._zipball_url = zipball_url
        self._tarball_url = tarball_url
        self._upload_url = upload_url
        self._assets_url = assets_url
        self._html_url = html_url
        self._url = url
        self._body = body
        self._body_html = body_html
        self._body_text = body_text
        self._mentions_count = mentions_count
        self._reactions = reactions
        return
        
    

    
    def _getassets(self):
        return self._assets and [ entry and ReleaseAsset(**entry) for entry in self._assets ]
        
    assets = property(_getassets)

    def _getauthor(self):
        return self._author and SimpleUser(**self._author)
        
    author = property(_getauthor)

    def _getpublished_at(self):
        return self._published_at and datetime.datetime.fromisoformat(self._published_at[0:-1])
        
    published_at = property(_getpublished_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getprerelease(self):
        return self._prerelease
        
    prerelease = property(_getprerelease, doc="""Whether to identify the release as a prerelease or a full release. """)

    def _getdraft(self):
        return self._draft
        
    draft = property(_getdraft, doc="""true to create a draft (unpublished) release, false to create a published one. """)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _gettarget_commitish(self):
        return self._target_commitish
        
    target_commitish = property(_gettarget_commitish, doc="""Specifies the commitish value that determines where the Git tag is created from. """)

    def _gettag_name(self):
        return self._tag_name
        
    tag_name = property(_gettag_name, doc="""The name of the tag. """)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getzipball_url(self):
        return self._zipball_url
        
    zipball_url = property(_getzipball_url)

    def _gettarball_url(self):
        return self._tarball_url
        
    tarball_url = property(_gettarball_url)

    def _getupload_url(self):
        return self._upload_url
        
    upload_url = property(_getupload_url)

    def _getassets_url(self):
        return self._assets_url
        
    assets_url = property(_getassets_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getbody(self):
        return self._body
        
    body = property(_getbody)

    def _getbody_html(self):
        return self._body_html
        
    body_html = property(_getbody_html)

    def _getbody_text(self):
        return self._body_text
        
    body_text = property(_getbody_text)

    def _getmentions_count(self):
        return self._mentions_count
        
    mentions_count = property(_getmentions_count)

    def _getreactions(self):
        return self._reactions and ReactionRollup(**ReactionRollup.patchEntry(self._reactions))
        
    reactions = property(_getreactions)


    
##
##
##
class GeneratedReleaseNotesContent(ResponseBase):
    """Generated name and body describing a release """
    def __init__(self, body:str, name:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._body = body
        self._name = name
        return
        
    

    
    def _getbody(self):
        return self._body
        
    body = property(_getbody, doc="""The generated body describing the contents of the release supporting markdown formatting """)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The generated name of the release """)


    
##
##
##
class SecretScanningAlert(ResponseBase):
    def __init__(self, number:int=None, created_at:datetime=None, url:str=None, html_url:str=None, locations_url:str=None, state:str=None, resolution:str=None, resolved_at:datetime=None, resolved_by:dict=None, secret_type:str=None, secret:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._number = number
        self._created_at = created_at
        self._url = url
        self._html_url = html_url
        self._locations_url = locations_url
        self._state = state
        self._resolution = resolution
        self._resolved_at = resolved_at
        self._resolved_by = resolved_by
        self._secret_type = secret_type
        self._secret = secret
        return
        
    

    
    def _getnumber(self):
        return self._number
        
    number = property(_getnumber)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getlocations_url(self):
        return self._locations_url
        
    locations_url = property(_getlocations_url, doc="""The REST API URL of the code locations for this alert. """)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)

    def _getresolution(self):
        return self._resolution
        
    resolution = property(_getresolution)

    def _getresolved_at(self):
        return self._resolved_at and datetime.datetime.fromisoformat(self._resolved_at[0:-1])
        
    resolved_at = property(_getresolved_at, doc="""The time that the alert was resolved in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. """)

    def _getresolved_by(self):
        return self._resolved_by and NullableSimpleUser(**self._resolved_by)
        
    resolved_by = property(_getresolved_by)

    def _getsecret_type(self):
        return self._secret_type
        
    secret_type = property(_getsecret_type, doc="""The type of secret that secret scanning detected. """)

    def _getsecret(self):
        return self._secret
        
    secret = property(_getsecret, doc="""The secret that was detected. """)


    
##
##
##
class SecretScanningLocationCommit(ResponseBase):
    """Represents a 'commit' secret scanning location type. This location type shows that a secret was detected inside a commit to a repository. """
    def __init__(self, commit_url:str, commit_sha:str, blob_url:str, blob_sha:str, end_column:int, start_column:int, end_line:int, start_line:int, path:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._commit_url = commit_url
        self._commit_sha = commit_sha
        self._blob_url = blob_url
        self._blob_sha = blob_sha
        self._end_column = end_column
        self._start_column = start_column
        self._end_line = end_line
        self._start_line = start_line
        self._path = path
        return
        
    

    
    def _getcommit_url(self):
        return self._commit_url
        
    commit_url = property(_getcommit_url, doc="""The API URL to get the associated commit resource """)

    def _getcommit_sha(self):
        return self._commit_sha
        
    commit_sha = property(_getcommit_sha, doc="""SHA-1 hash ID of the associated commit """)

    def _getblob_url(self):
        return self._blob_url
        
    blob_url = property(_getblob_url, doc="""The API URL to get the associated blob resource """)

    def _getblob_sha(self):
        return self._blob_sha
        
    blob_sha = property(_getblob_sha, doc="""SHA-1 hash ID of the associated blob """)

    def _getend_column(self):
        return self._end_column
        
    end_column = property(_getend_column, doc="""The column at which the secret ends within the end line when the file is interpreted as 8BIT ASCII """)

    def _getstart_column(self):
        return self._start_column
        
    start_column = property(_getstart_column, doc="""The column at which the secret starts within the start line when the file is interpreted as 8BIT ASCII """)

    def _getend_line(self):
        return self._end_line
        
    end_line = property(_getend_line, doc="""Line number at which the secret ends in the file """)

    def _getstart_line(self):
        return self._start_line
        
    start_line = property(_getstart_line, doc="""Line number at which the secret starts in the file """)

    def _getpath(self):
        return self._path
        
    path = property(_getpath, doc="""The file path in the repository """)


    
##
##
##
class SecretScanningLocation(ResponseBase):
    def __init__(self, details, type:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._details = details
        self._type = type
        return
        
    

    
    def _getdetails(self):
        return self._details
        
    details = property(_getdetails)

    def _gettype(self):
        return self._type
        
    type = property(_gettype, doc="""The location type. Because secrets may be found in different types of resources (ie. code, comments, issues), this field identifies the type of resource where the secret was found. """)


    
##
##
##
class Stargazer(ResponseBase):
    """Stargazer """
    def __init__(self, user:dict, starred_at:datetime, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._user = user
        self._starred_at = starred_at
        return
        
    

    
    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _getstarred_at(self):
        return self._starred_at and datetime.datetime.fromisoformat(self._starred_at[0:-1])
        
    starred_at = property(_getstarred_at)


    
##
##
##
class CommitActivity(ResponseBase):
    """Commit Activity """
    def __init__(self, week:int, total:int, days:list, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._week = week
        self._total = total
        self._days = days
        return
        
    

    
    def _getweek(self):
        return self._week
        
    week = property(_getweek)

    def _gettotal(self):
        return self._total
        
    total = property(_gettotal)

    def _getdays(self):
        return self._days and [ entry for entry in self._days ]
        
    days = property(_getdays)


    
##
##
##
class Contributoractivity_weeks(ResponseBase):
    def __init__(self, w:int=None, a:int=None, d:int=None, c:int=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._w = w
        self._a = a
        self._d = d
        self._c = c
        return
        
    

    
    def _getw(self):
        return self._w
        
    w = property(_getw)

    def _geta(self):
        return self._a
        
    a = property(_geta)

    def _getd(self):
        return self._d
        
    d = property(_getd)

    def _getc(self):
        return self._c
        
    c = property(_getc)


    
##
##
##
class ContributorActivity(ResponseBase):
    """Contributor Activity """
    def __init__(self, weeks:list, total:int, author:dict, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._weeks = weeks
        self._total = total
        self._author = author
        return
        
    

    
    def _getweeks(self):
        return self._weeks and [ entry and Contributoractivity_weeks(**entry) for entry in self._weeks ]
        
    weeks = property(_getweeks)

    def _gettotal(self):
        return self._total
        
    total = property(_gettotal)

    def _getauthor(self):
        return self._author and NullableSimpleUser(**self._author)
        
    author = property(_getauthor)


    
##
##
##
class ParticipationStats(ResponseBase):
    def __init__(self, owner:list, all:list, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._owner = owner
        self._all = all
        return
        
    

    
    def _getowner(self):
        return self._owner and [ entry for entry in self._owner ]
        
    owner = property(_getowner)

    def _getall(self):
        return self._all and [ entry for entry in self._all ]
        
    all = property(_getall)


    
##
##
##
class RepositorySubscription(ResponseBase):
    """Repository invitations let you manage who you collaborate with. """
    def __init__(self, repository_url:str, url:str, created_at:datetime, reason:str, ignored:bool, subscribed:bool, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._repository_url = repository_url
        self._url = url
        self._created_at = created_at
        self._reason = reason
        self._ignored = ignored
        self._subscribed = subscribed
        return
        
    

    
    def _getrepository_url(self):
        return self._repository_url
        
    repository_url = property(_getrepository_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getreason(self):
        return self._reason
        
    reason = property(_getreason)

    def _getignored(self):
        return self._ignored
        
    ignored = property(_getignored, doc="""Determines if all notifications should be blocked from this repository. """)

    def _getsubscribed(self):
        return self._subscribed
        
    subscribed = property(_getsubscribed, doc="""Determines if notifications should be received from this repository. """)


    
##
##
##
class Tag_commit(ResponseBase):
    def __init__(self, url:str, sha:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._sha = sha
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)


    
##
##
##
class Tag(ResponseBase):
    """Tag """
    def __init__(self, node_id:str, tarball_url:str, zipball_url:str, commit:dict, name:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._node_id = node_id
        self._tarball_url = tarball_url
        self._zipball_url = zipball_url
        self._commit = commit
        self._name = name
        return
        
    

    
    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _gettarball_url(self):
        return self._tarball_url
        
    tarball_url = property(_gettarball_url)

    def _getzipball_url(self):
        return self._zipball_url
        
    zipball_url = property(_getzipball_url)

    def _getcommit(self):
        return self._commit and Tag_commit(**self._commit)
        
    commit = property(_getcommit)

    def _getname(self):
        return self._name
        
    name = property(_getname)


    
##
##
##
class Topic(ResponseBase):
    """A topic aggregates entities that are related to a subject. """
    def __init__(self, names:list, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._names = names
        return
        
    

    
    def _getnames(self):
        return self._names and [ entry for entry in self._names ]
        
    names = property(_getnames)


    
##
##
##
class Searchresulttextmatches_matches(ResponseBase):
    def __init__(self, text:str=None, indices:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._text = text
        self._indices = indices
        return
        
    

    
    def _gettext(self):
        return self._text
        
    text = property(_gettext)

    def _getindices(self):
        return self._indices and [ entry for entry in self._indices ]
        
    indices = property(_getindices)


    
##
##
##
class Searchresulttextmatches(ResponseBase):
    def __init__(self, object_url:str=None, object_type:str=None, Property:str=None, fragment:str=None, matches:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._object_url = object_url
        self._object_type = object_type
        self._Property = Property
        self._fragment = fragment
        self._matches = matches
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['Property'] = entry.pop('property')
        return entry
    

    
    def _getobject_url(self):
        return self._object_url
        
    object_url = property(_getobject_url)

    def _getobject_type(self):
        return self._object_type
        
    object_type = property(_getobject_type)

    def _getProperty(self):
        return self._Property
        
    Property = property(_getProperty)

    def _getfragment(self):
        return self._fragment
        
    fragment = property(_getfragment)

    def _getmatches(self):
        return self._matches and [ entry and Searchresulttextmatches_matches(**entry) for entry in self._matches ]
        
    matches = property(_getmatches)


    
    ##
    ##
    def _getProperty(self):
        return self._Property
        
    Property = property(_getProperty)

##
##
##
class CodeSearchResultItem(ResponseBase):
    """Code Search Result Item """
    def __init__(self, score:int, repository:dict, html_url:str, git_url:str, url:str, sha:str, path:str, name:str, file_size:int=None, language:str=None, last_modified_at:datetime=None, line_numbers:list=[], text_matches:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._score = score
        self._repository = repository
        self._html_url = html_url
        self._git_url = git_url
        self._url = url
        self._sha = sha
        self._path = path
        self._name = name
        self._file_size = file_size
        self._language = language
        self._last_modified_at = last_modified_at
        self._line_numbers = line_numbers
        self._text_matches = text_matches
        return
        
    

    
    def _getscore(self):
        return self._score
        
    score = property(_getscore)

    def _getrepository(self):
        return self._repository and MinimalRepository(**self._repository)
        
    repository = property(_getrepository)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getgit_url(self):
        return self._git_url
        
    git_url = property(_getgit_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _getpath(self):
        return self._path
        
    path = property(_getpath)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getfile_size(self):
        return self._file_size
        
    file_size = property(_getfile_size)

    def _getlanguage(self):
        return self._language
        
    language = property(_getlanguage)

    def _getlast_modified_at(self):
        return self._last_modified_at and datetime.datetime.fromisoformat(self._last_modified_at[0:-1])
        
    last_modified_at = property(_getlast_modified_at)

    def _getline_numbers(self):
        return self._line_numbers and [ entry for entry in self._line_numbers ]
        
    line_numbers = property(_getline_numbers)

    def _gettext_matches(self):
        return self._text_matches and [ entry and Searchresulttextmatches(**Searchresulttextmatches.patchEntry(entry)) for entry in self._text_matches ]
        
    text_matches = property(_gettext_matches)


    
##
##
##
class Commitsearchresultitem_commit_author(ResponseBase):
    def __init__(self, date:datetime, email:str, name:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._date = date
        self._email = email
        self._name = name
        return
        
    

    
    def _getdate(self):
        return self._date and datetime.datetime.fromisoformat(self._date[0:-1])
        
    date = property(_getdate)

    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _getname(self):
        return self._name
        
    name = property(_getname)


    
##
##
##
class Commitsearchresultitem_commit_tree(ResponseBase):
    def __init__(self, url:str, sha:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._sha = sha
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)


    
##
##
##
class Commitsearchresultitem_commit(ResponseBase):
    def __init__(self, url:str, tree:dict, message:str, comment_count:int, committer:dict, author:dict, verification:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._tree = tree
        self._message = message
        self._comment_count = comment_count
        self._committer = committer
        self._author = author
        self._verification = verification
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gettree(self):
        return self._tree and Commitsearchresultitem_commit_tree(**self._tree)
        
    tree = property(_gettree)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getcomment_count(self):
        return self._comment_count
        
    comment_count = property(_getcomment_count)

    def _getcommitter(self):
        return self._committer and NullableGitUser(**self._committer)
        
    committer = property(_getcommitter)

    def _getauthor(self):
        return self._author and Commitsearchresultitem_commit_author(**self._author)
        
    author = property(_getauthor)

    def _getverification(self):
        return self._verification and Verification(**self._verification)
        
    verification = property(_getverification)


    
##
##
##
class Commitsearchresultitem_parents(ResponseBase):
    def __init__(self, url:str=None, html_url:str=None, sha:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._html_url = html_url
        self._sha = sha
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)


    
##
##
##
class CommitSearchResultItem(ResponseBase):
    """Commit Search Result Item """
    def __init__(self, node_id:str, score:int, repository:dict, parents:list, committer:dict, author:dict, commit:dict, comments_url:str, html_url:str, sha:str, url:str, text_matches:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._node_id = node_id
        self._score = score
        self._repository = repository
        self._parents = parents
        self._committer = committer
        self._author = author
        self._commit = commit
        self._comments_url = comments_url
        self._html_url = html_url
        self._sha = sha
        self._url = url
        self._text_matches = text_matches
        return
        
    

    
    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getscore(self):
        return self._score
        
    score = property(_getscore)

    def _getrepository(self):
        return self._repository and MinimalRepository(**self._repository)
        
    repository = property(_getrepository)

    def _getparents(self):
        return self._parents and [ entry and Commitsearchresultitem_parents(**entry) for entry in self._parents ]
        
    parents = property(_getparents)

    def _getcommitter(self):
        return self._committer and NullableGitUser(**self._committer)
        
    committer = property(_getcommitter)

    def _getauthor(self):
        return self._author and NullableSimpleUser(**self._author)
        
    author = property(_getauthor)

    def _getcommit(self):
        return self._commit and Commitsearchresultitem_commit(**self._commit)
        
    commit = property(_getcommit)

    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _gettext_matches(self):
        return self._text_matches and [ entry and Searchresulttextmatches(**Searchresulttextmatches.patchEntry(entry)) for entry in self._text_matches ]
        
    text_matches = property(_gettext_matches)


    
##
##
##
class Issuesearchresultitem_labels(ResponseBase):
    def __init__(self, id:int=None, node_id:str=None, url:str=None, name:str=None, color:str=None, default:bool=None, description:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._node_id = node_id
        self._url = url
        self._name = name
        self._color = color
        self._default = default
        self._description = description
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getcolor(self):
        return self._color
        
    color = property(_getcolor)

    def _getdefault(self):
        return self._default
        
    default = property(_getdefault)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)


    
##
##
##
class Issuesearchresultitem_pull_request(ResponseBase):
    def __init__(self, url:str, patch_url:str, html_url:str, diff_url:str, merged_at:datetime=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._patch_url = patch_url
        self._html_url = html_url
        self._diff_url = diff_url
        self._merged_at = merged_at
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getpatch_url(self):
        return self._patch_url
        
    patch_url = property(_getpatch_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getdiff_url(self):
        return self._diff_url
        
    diff_url = property(_getdiff_url)

    def _getmerged_at(self):
        return self._merged_at and datetime.datetime.fromisoformat(self._merged_at[0:-1])
        
    merged_at = property(_getmerged_at)


    
##
##
##
class IssueSearchResultItem(ResponseBase):
    """Issue Search Result Item """
    def __init__(self, author_association:str, score:int, closed_at:datetime, updated_at:datetime, created_at:datetime, comments:int, milestone:dict, assignee:dict, state:str, labels:list, user:dict, locked:bool, title:str, number:int, node_id:str, id:int, html_url:str, events_url:str, comments_url:str, labels_url:str, repository_url:str, url:str, active_lock_reason:str=None, assignees:list=[], text_matches:list=[], pull_request:dict=None, body:str=None, draft:bool=None, repository:dict=None, body_html:str=None, body_text:str=None, timeline_url:str=None, performed_via_github_app:dict=None, reactions:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._author_association = author_association
        self._score = score
        self._closed_at = closed_at
        self._updated_at = updated_at
        self._created_at = created_at
        self._comments = comments
        self._milestone = milestone
        self._assignee = assignee
        self._state = state
        self._labels = labels
        self._user = user
        self._locked = locked
        self._title = title
        self._number = number
        self._node_id = node_id
        self._id = id
        self._html_url = html_url
        self._events_url = events_url
        self._comments_url = comments_url
        self._labels_url = labels_url
        self._repository_url = repository_url
        self._url = url
        self._active_lock_reason = active_lock_reason
        self._assignees = assignees
        self._text_matches = text_matches
        self._pull_request = pull_request
        self._body = body
        self._draft = draft
        self._repository = repository
        self._body_html = body_html
        self._body_text = body_text
        self._timeline_url = timeline_url
        self._performed_via_github_app = performed_via_github_app
        self._reactions = reactions
        return
        
    

    
    def _getauthor_association(self):
        return self._author_association
        
    author_association = property(_getauthor_association)

    def _getscore(self):
        return self._score
        
    score = property(_getscore)

    def _getclosed_at(self):
        return self._closed_at and datetime.datetime.fromisoformat(self._closed_at[0:-1])
        
    closed_at = property(_getclosed_at)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getcomments(self):
        return self._comments
        
    comments = property(_getcomments)

    def _getmilestone(self):
        return self._milestone and NullableMilestone(**self._milestone)
        
    milestone = property(_getmilestone)

    def _getassignee(self):
        return self._assignee and NullableSimpleUser(**self._assignee)
        
    assignee = property(_getassignee)

    def _getstate(self):
        return self._state
        
    state = property(_getstate)

    def _getlabels(self):
        return self._labels and [ entry and Issuesearchresultitem_labels(**entry) for entry in self._labels ]
        
    labels = property(_getlabels)

    def _getuser(self):
        return self._user and NullableSimpleUser(**self._user)
        
    user = property(_getuser)

    def _getlocked(self):
        return self._locked
        
    locked = property(_getlocked)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle)

    def _getnumber(self):
        return self._number
        
    number = property(_getnumber)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _getlabels_url(self):
        return self._labels_url
        
    labels_url = property(_getlabels_url)

    def _getrepository_url(self):
        return self._repository_url
        
    repository_url = property(_getrepository_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getactive_lock_reason(self):
        return self._active_lock_reason
        
    active_lock_reason = property(_getactive_lock_reason)

    def _getassignees(self):
        return self._assignees and [ entry and SimpleUser(**entry) for entry in self._assignees ]
        
    assignees = property(_getassignees)

    def _gettext_matches(self):
        return self._text_matches and [ entry and Searchresulttextmatches(**Searchresulttextmatches.patchEntry(entry)) for entry in self._text_matches ]
        
    text_matches = property(_gettext_matches)

    def _getpull_request(self):
        return self._pull_request and Issuesearchresultitem_pull_request(**self._pull_request)
        
    pull_request = property(_getpull_request)

    def _getbody(self):
        return self._body
        
    body = property(_getbody)

    def _getdraft(self):
        return self._draft
        
    draft = property(_getdraft)

    def _getrepository(self):
        return self._repository and Repository(**self._repository)
        
    repository = property(_getrepository)

    def _getbody_html(self):
        return self._body_html
        
    body_html = property(_getbody_html)

    def _getbody_text(self):
        return self._body_text
        
    body_text = property(_getbody_text)

    def _gettimeline_url(self):
        return self._timeline_url
        
    timeline_url = property(_gettimeline_url)

    def _getperformed_via_github_app(self):
        return self._performed_via_github_app and NullableIntegration(**self._performed_via_github_app)
        
    performed_via_github_app = property(_getperformed_via_github_app)

    def _getreactions(self):
        return self._reactions and ReactionRollup(**ReactionRollup.patchEntry(self._reactions))
        
    reactions = property(_getreactions)


    
##
##
##
class LabelSearchResultItem(ResponseBase):
    """Label Search Result Item """
    def __init__(self, score:int, description:str, default:bool, color:str, name:str, url:str, node_id:str, id:int, text_matches:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._score = score
        self._description = description
        self._default = default
        self._color = color
        self._name = name
        self._url = url
        self._node_id = node_id
        self._id = id
        self._text_matches = text_matches
        return
        
    

    
    def _getscore(self):
        return self._score
        
    score = property(_getscore)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getdefault(self):
        return self._default
        
    default = property(_getdefault)

    def _getcolor(self):
        return self._color
        
    color = property(_getcolor)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _gettext_matches(self):
        return self._text_matches and [ entry and Searchresulttextmatches(**Searchresulttextmatches.patchEntry(entry)) for entry in self._text_matches ]
        
    text_matches = property(_gettext_matches)


    
##
##
##
class Reposearchresultitem_permissions(ResponseBase):
    def __init__(self, pull:bool, push:bool, admin:bool, maintain:bool=None, triage:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._pull = pull
        self._push = push
        self._admin = admin
        self._maintain = maintain
        self._triage = triage
        return
        
    

    
    def _getpull(self):
        return self._pull
        
    pull = property(_getpull)

    def _getpush(self):
        return self._push
        
    push = property(_getpush)

    def _getadmin(self):
        return self._admin
        
    admin = property(_getadmin)

    def _getmaintain(self):
        return self._maintain
        
    maintain = property(_getmaintain)

    def _gettriage(self):
        return self._triage
        
    triage = property(_gettriage)


    
##
##
##
class RepoSearchResultItem(ResponseBase):
    """Repo Search Result Item """
    def __init__(self, license:dict, disabled:bool, archived:bool, has_downloads:bool, has_wiki:bool, has_pages:bool, has_projects:bool, has_issues:bool, mirror_url:str, watchers:int, open_issues:int, forks:int, svn_url:str, clone_url:str, ssh_url:str, git_url:str, deployments_url:str, releases_url:str, labels_url:str, notifications_url:str, milestones_url:str, pulls_url:str, issues_url:str, downloads_url:str, archive_url:str, merges_url:str, compare_url:str, contents_url:str, issue_comment_url:str, comments_url:str, git_commits_url:str, commits_url:str, subscription_url:str, subscribers_url:str, contributors_url:str, stargazers_url:str, languages_url:str, statuses_url:str, trees_url:str, git_refs_url:str, git_tags_url:str, blobs_url:str, tags_url:str, branches_url:str, assignees_url:str, events_url:str, issue_events_url:str, hooks_url:str, teams_url:str, collaborators_url:str, keys_url:str, forks_url:str, score:int, default_branch:str, open_issues_count:int, forks_count:int, language:str, watchers_count:int, stargazers_count:int, size:int, homepage:str, pushed_at:datetime, updated_at:datetime, created_at:datetime, url:str, fork:bool, description:str, html_url:str, private:bool, owner:dict, full_name:str, name:str, node_id:str, id:int, master_branch:str=None, topics:list=[], visibility:str=None, permissions:dict=None, text_matches:list=[], temp_clone_token:str=None, allow_merge_commit:bool=None, allow_squash_merge:bool=None, allow_rebase_merge:bool=None, allow_auto_merge:bool=None, delete_branch_on_merge:bool=None, allow_forking:bool=None, is_template:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._license = license
        self._disabled = disabled
        self._archived = archived
        self._has_downloads = has_downloads
        self._has_wiki = has_wiki
        self._has_pages = has_pages
        self._has_projects = has_projects
        self._has_issues = has_issues
        self._mirror_url = mirror_url
        self._watchers = watchers
        self._open_issues = open_issues
        self._forks = forks
        self._svn_url = svn_url
        self._clone_url = clone_url
        self._ssh_url = ssh_url
        self._git_url = git_url
        self._deployments_url = deployments_url
        self._releases_url = releases_url
        self._labels_url = labels_url
        self._notifications_url = notifications_url
        self._milestones_url = milestones_url
        self._pulls_url = pulls_url
        self._issues_url = issues_url
        self._downloads_url = downloads_url
        self._archive_url = archive_url
        self._merges_url = merges_url
        self._compare_url = compare_url
        self._contents_url = contents_url
        self._issue_comment_url = issue_comment_url
        self._comments_url = comments_url
        self._git_commits_url = git_commits_url
        self._commits_url = commits_url
        self._subscription_url = subscription_url
        self._subscribers_url = subscribers_url
        self._contributors_url = contributors_url
        self._stargazers_url = stargazers_url
        self._languages_url = languages_url
        self._statuses_url = statuses_url
        self._trees_url = trees_url
        self._git_refs_url = git_refs_url
        self._git_tags_url = git_tags_url
        self._blobs_url = blobs_url
        self._tags_url = tags_url
        self._branches_url = branches_url
        self._assignees_url = assignees_url
        self._events_url = events_url
        self._issue_events_url = issue_events_url
        self._hooks_url = hooks_url
        self._teams_url = teams_url
        self._collaborators_url = collaborators_url
        self._keys_url = keys_url
        self._forks_url = forks_url
        self._score = score
        self._default_branch = default_branch
        self._open_issues_count = open_issues_count
        self._forks_count = forks_count
        self._language = language
        self._watchers_count = watchers_count
        self._stargazers_count = stargazers_count
        self._size = size
        self._homepage = homepage
        self._pushed_at = pushed_at
        self._updated_at = updated_at
        self._created_at = created_at
        self._url = url
        self._fork = fork
        self._description = description
        self._html_url = html_url
        self._private = private
        self._owner = owner
        self._full_name = full_name
        self._name = name
        self._node_id = node_id
        self._id = id
        self._master_branch = master_branch
        self._topics = topics
        self._visibility = visibility
        self._permissions = permissions
        self._text_matches = text_matches
        self._temp_clone_token = temp_clone_token
        self._allow_merge_commit = allow_merge_commit
        self._allow_squash_merge = allow_squash_merge
        self._allow_rebase_merge = allow_rebase_merge
        self._allow_auto_merge = allow_auto_merge
        self._delete_branch_on_merge = delete_branch_on_merge
        self._allow_forking = allow_forking
        self._is_template = is_template
        return
        
    

    
    def _getlicense(self):
        return self._license and NullableLicenseSimple(**self._license)
        
    license = property(_getlicense)

    def _getdisabled(self):
        return self._disabled
        
    disabled = property(_getdisabled, doc="""Returns whether or not this repository disabled. """)

    def _getarchived(self):
        return self._archived
        
    archived = property(_getarchived)

    def _gethas_downloads(self):
        return self._has_downloads
        
    has_downloads = property(_gethas_downloads)

    def _gethas_wiki(self):
        return self._has_wiki
        
    has_wiki = property(_gethas_wiki)

    def _gethas_pages(self):
        return self._has_pages
        
    has_pages = property(_gethas_pages)

    def _gethas_projects(self):
        return self._has_projects
        
    has_projects = property(_gethas_projects)

    def _gethas_issues(self):
        return self._has_issues
        
    has_issues = property(_gethas_issues)

    def _getmirror_url(self):
        return self._mirror_url
        
    mirror_url = property(_getmirror_url)

    def _getwatchers(self):
        return self._watchers
        
    watchers = property(_getwatchers)

    def _getopen_issues(self):
        return self._open_issues
        
    open_issues = property(_getopen_issues)

    def _getforks(self):
        return self._forks
        
    forks = property(_getforks)

    def _getsvn_url(self):
        return self._svn_url
        
    svn_url = property(_getsvn_url)

    def _getclone_url(self):
        return self._clone_url
        
    clone_url = property(_getclone_url)

    def _getssh_url(self):
        return self._ssh_url
        
    ssh_url = property(_getssh_url)

    def _getgit_url(self):
        return self._git_url
        
    git_url = property(_getgit_url)

    def _getdeployments_url(self):
        return self._deployments_url
        
    deployments_url = property(_getdeployments_url)

    def _getreleases_url(self):
        return self._releases_url
        
    releases_url = property(_getreleases_url)

    def _getlabels_url(self):
        return self._labels_url
        
    labels_url = property(_getlabels_url)

    def _getnotifications_url(self):
        return self._notifications_url
        
    notifications_url = property(_getnotifications_url)

    def _getmilestones_url(self):
        return self._milestones_url
        
    milestones_url = property(_getmilestones_url)

    def _getpulls_url(self):
        return self._pulls_url
        
    pulls_url = property(_getpulls_url)

    def _getissues_url(self):
        return self._issues_url
        
    issues_url = property(_getissues_url)

    def _getdownloads_url(self):
        return self._downloads_url
        
    downloads_url = property(_getdownloads_url)

    def _getarchive_url(self):
        return self._archive_url
        
    archive_url = property(_getarchive_url)

    def _getmerges_url(self):
        return self._merges_url
        
    merges_url = property(_getmerges_url)

    def _getcompare_url(self):
        return self._compare_url
        
    compare_url = property(_getcompare_url)

    def _getcontents_url(self):
        return self._contents_url
        
    contents_url = property(_getcontents_url)

    def _getissue_comment_url(self):
        return self._issue_comment_url
        
    issue_comment_url = property(_getissue_comment_url)

    def _getcomments_url(self):
        return self._comments_url
        
    comments_url = property(_getcomments_url)

    def _getgit_commits_url(self):
        return self._git_commits_url
        
    git_commits_url = property(_getgit_commits_url)

    def _getcommits_url(self):
        return self._commits_url
        
    commits_url = property(_getcommits_url)

    def _getsubscription_url(self):
        return self._subscription_url
        
    subscription_url = property(_getsubscription_url)

    def _getsubscribers_url(self):
        return self._subscribers_url
        
    subscribers_url = property(_getsubscribers_url)

    def _getcontributors_url(self):
        return self._contributors_url
        
    contributors_url = property(_getcontributors_url)

    def _getstargazers_url(self):
        return self._stargazers_url
        
    stargazers_url = property(_getstargazers_url)

    def _getlanguages_url(self):
        return self._languages_url
        
    languages_url = property(_getlanguages_url)

    def _getstatuses_url(self):
        return self._statuses_url
        
    statuses_url = property(_getstatuses_url)

    def _gettrees_url(self):
        return self._trees_url
        
    trees_url = property(_gettrees_url)

    def _getgit_refs_url(self):
        return self._git_refs_url
        
    git_refs_url = property(_getgit_refs_url)

    def _getgit_tags_url(self):
        return self._git_tags_url
        
    git_tags_url = property(_getgit_tags_url)

    def _getblobs_url(self):
        return self._blobs_url
        
    blobs_url = property(_getblobs_url)

    def _gettags_url(self):
        return self._tags_url
        
    tags_url = property(_gettags_url)

    def _getbranches_url(self):
        return self._branches_url
        
    branches_url = property(_getbranches_url)

    def _getassignees_url(self):
        return self._assignees_url
        
    assignees_url = property(_getassignees_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getissue_events_url(self):
        return self._issue_events_url
        
    issue_events_url = property(_getissue_events_url)

    def _gethooks_url(self):
        return self._hooks_url
        
    hooks_url = property(_gethooks_url)

    def _getteams_url(self):
        return self._teams_url
        
    teams_url = property(_getteams_url)

    def _getcollaborators_url(self):
        return self._collaborators_url
        
    collaborators_url = property(_getcollaborators_url)

    def _getkeys_url(self):
        return self._keys_url
        
    keys_url = property(_getkeys_url)

    def _getforks_url(self):
        return self._forks_url
        
    forks_url = property(_getforks_url)

    def _getscore(self):
        return self._score
        
    score = property(_getscore)

    def _getdefault_branch(self):
        return self._default_branch
        
    default_branch = property(_getdefault_branch)

    def _getopen_issues_count(self):
        return self._open_issues_count
        
    open_issues_count = property(_getopen_issues_count)

    def _getforks_count(self):
        return self._forks_count
        
    forks_count = property(_getforks_count)

    def _getlanguage(self):
        return self._language
        
    language = property(_getlanguage)

    def _getwatchers_count(self):
        return self._watchers_count
        
    watchers_count = property(_getwatchers_count)

    def _getstargazers_count(self):
        return self._stargazers_count
        
    stargazers_count = property(_getstargazers_count)

    def _getsize(self):
        return self._size
        
    size = property(_getsize)

    def _gethomepage(self):
        return self._homepage
        
    homepage = property(_gethomepage)

    def _getpushed_at(self):
        return self._pushed_at and datetime.datetime.fromisoformat(self._pushed_at[0:-1])
        
    pushed_at = property(_getpushed_at)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getfork(self):
        return self._fork
        
    fork = property(_getfork)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _getprivate(self):
        return self._private
        
    private = property(_getprivate)

    def _getowner(self):
        return self._owner and NullableSimpleUser(**self._owner)
        
    owner = property(_getowner)

    def _getfull_name(self):
        return self._full_name
        
    full_name = property(_getfull_name)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getmaster_branch(self):
        return self._master_branch
        
    master_branch = property(_getmaster_branch)

    def _gettopics(self):
        return self._topics and [ entry for entry in self._topics ]
        
    topics = property(_gettopics)

    def _getvisibility(self):
        return self._visibility
        
    visibility = property(_getvisibility, doc="""The repository visibility: public, private, or internal. """)

    def _getpermissions(self):
        return self._permissions and Reposearchresultitem_permissions(**self._permissions)
        
    permissions = property(_getpermissions)

    def _gettext_matches(self):
        return self._text_matches and [ entry and Searchresulttextmatches(**Searchresulttextmatches.patchEntry(entry)) for entry in self._text_matches ]
        
    text_matches = property(_gettext_matches)

    def _gettemp_clone_token(self):
        return self._temp_clone_token
        
    temp_clone_token = property(_gettemp_clone_token)

    def _getallow_merge_commit(self):
        return self._allow_merge_commit
        
    allow_merge_commit = property(_getallow_merge_commit)

    def _getallow_squash_merge(self):
        return self._allow_squash_merge
        
    allow_squash_merge = property(_getallow_squash_merge)

    def _getallow_rebase_merge(self):
        return self._allow_rebase_merge
        
    allow_rebase_merge = property(_getallow_rebase_merge)

    def _getallow_auto_merge(self):
        return self._allow_auto_merge
        
    allow_auto_merge = property(_getallow_auto_merge)

    def _getdelete_branch_on_merge(self):
        return self._delete_branch_on_merge
        
    delete_branch_on_merge = property(_getdelete_branch_on_merge)

    def _getallow_forking(self):
        return self._allow_forking
        
    allow_forking = property(_getallow_forking)

    def _getis_template(self):
        return self._is_template
        
    is_template = property(_getis_template)


    
##
##
##
class Topicsearchresultitem_related_topic_relation(ResponseBase):
    def __init__(self, id:int=None, name:str=None, topic_id:int=None, relation_type:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._name = name
        self._topic_id = topic_id
        self._relation_type = relation_type
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _gettopic_id(self):
        return self._topic_id
        
    topic_id = property(_gettopic_id)

    def _getrelation_type(self):
        return self._relation_type
        
    relation_type = property(_getrelation_type)


    
##
##
##
class Topicsearchresultitem_related(ResponseBase):
    def __init__(self, topic_relation:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._topic_relation = topic_relation
        return
        
    

    
    def _gettopic_relation(self):
        return self._topic_relation and Topicsearchresultitem_related_topic_relation(**self._topic_relation)
        
    topic_relation = property(_gettopic_relation)


    
##
##
##
class Topicsearchresultitem_aliases_topic_relation(ResponseBase):
    def __init__(self, id:int=None, name:str=None, topic_id:int=None, relation_type:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._name = name
        self._topic_id = topic_id
        self._relation_type = relation_type
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _gettopic_id(self):
        return self._topic_id
        
    topic_id = property(_gettopic_id)

    def _getrelation_type(self):
        return self._relation_type
        
    relation_type = property(_getrelation_type)


    
##
##
##
class Topicsearchresultitem_aliases(ResponseBase):
    def __init__(self, topic_relation:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._topic_relation = topic_relation
        return
        
    

    
    def _gettopic_relation(self):
        return self._topic_relation and Topicsearchresultitem_aliases_topic_relation(**self._topic_relation)
        
    topic_relation = property(_gettopic_relation)


    
##
##
##
class TopicSearchResultItem(ResponseBase):
    """Topic Search Result Item """
    def __init__(self, score:int, curated:bool, featured:bool, updated_at:datetime, created_at:datetime, released:str, created_by:str, description:str, short_description:str, display_name:str, name:str, repository_count:int=None, logo_url:str=None, text_matches:list=[], related:list=[], aliases:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._score = score
        self._curated = curated
        self._featured = featured
        self._updated_at = updated_at
        self._created_at = created_at
        self._released = released
        self._created_by = created_by
        self._description = description
        self._short_description = short_description
        self._display_name = display_name
        self._name = name
        self._repository_count = repository_count
        self._logo_url = logo_url
        self._text_matches = text_matches
        self._related = related
        self._aliases = aliases
        return
        
    

    
    def _getscore(self):
        return self._score
        
    score = property(_getscore)

    def _getcurated(self):
        return self._curated
        
    curated = property(_getcurated)

    def _getfeatured(self):
        return self._featured
        
    featured = property(_getfeatured)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getreleased(self):
        return self._released
        
    released = property(_getreleased)

    def _getcreated_by(self):
        return self._created_by
        
    created_by = property(_getcreated_by)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getshort_description(self):
        return self._short_description
        
    short_description = property(_getshort_description)

    def _getdisplay_name(self):
        return self._display_name
        
    display_name = property(_getdisplay_name)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getrepository_count(self):
        return self._repository_count
        
    repository_count = property(_getrepository_count)

    def _getlogo_url(self):
        return self._logo_url
        
    logo_url = property(_getlogo_url)

    def _gettext_matches(self):
        return self._text_matches and [ entry and Searchresulttextmatches(**Searchresulttextmatches.patchEntry(entry)) for entry in self._text_matches ]
        
    text_matches = property(_gettext_matches)

    def _getrelated(self):
        return self._related and [ entry and Topicsearchresultitem_related(**entry) for entry in self._related ]
        
    related = property(_getrelated)

    def _getaliases(self):
        return self._aliases and [ entry and Topicsearchresultitem_aliases(**entry) for entry in self._aliases ]
        
    aliases = property(_getaliases)


    
##
##
##
class UserSearchResultItem(ResponseBase):
    """User Search Result Item """
    def __init__(self, site_admin:bool, events_url:str, starred_url:str, gists_url:str, following_url:str, score:int, type:str, received_events_url:str, repos_url:str, organizations_url:str, subscriptions_url:str, followers_url:str, html_url:str, url:str, gravatar_id:str, avatar_url:str, node_id:str, id:int, login:str, public_repos:int=None, public_gists:int=None, followers:int=None, following:int=None, created_at:datetime=None, updated_at:datetime=None, name:str=None, bio:str=None, email:str=None, location:str=None, hireable:bool=None, text_matches:list=[], blog:str=None, company:str=None, suspended_at:datetime=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._site_admin = site_admin
        self._events_url = events_url
        self._starred_url = starred_url
        self._gists_url = gists_url
        self._following_url = following_url
        self._score = score
        self._type = type
        self._received_events_url = received_events_url
        self._repos_url = repos_url
        self._organizations_url = organizations_url
        self._subscriptions_url = subscriptions_url
        self._followers_url = followers_url
        self._html_url = html_url
        self._url = url
        self._gravatar_id = gravatar_id
        self._avatar_url = avatar_url
        self._node_id = node_id
        self._id = id
        self._login = login
        self._public_repos = public_repos
        self._public_gists = public_gists
        self._followers = followers
        self._following = following
        self._created_at = created_at
        self._updated_at = updated_at
        self._name = name
        self._bio = bio
        self._email = email
        self._location = location
        self._hireable = hireable
        self._text_matches = text_matches
        self._blog = blog
        self._company = company
        self._suspended_at = suspended_at
        return
        
    

    
    def _getsite_admin(self):
        return self._site_admin
        
    site_admin = property(_getsite_admin)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getstarred_url(self):
        return self._starred_url
        
    starred_url = property(_getstarred_url)

    def _getgists_url(self):
        return self._gists_url
        
    gists_url = property(_getgists_url)

    def _getfollowing_url(self):
        return self._following_url
        
    following_url = property(_getfollowing_url)

    def _getscore(self):
        return self._score
        
    score = property(_getscore)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getreceived_events_url(self):
        return self._received_events_url
        
    received_events_url = property(_getreceived_events_url)

    def _getrepos_url(self):
        return self._repos_url
        
    repos_url = property(_getrepos_url)

    def _getorganizations_url(self):
        return self._organizations_url
        
    organizations_url = property(_getorganizations_url)

    def _getsubscriptions_url(self):
        return self._subscriptions_url
        
    subscriptions_url = property(_getsubscriptions_url)

    def _getfollowers_url(self):
        return self._followers_url
        
    followers_url = property(_getfollowers_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getgravatar_id(self):
        return self._gravatar_id
        
    gravatar_id = property(_getgravatar_id)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)

    def _getpublic_repos(self):
        return self._public_repos
        
    public_repos = property(_getpublic_repos)

    def _getpublic_gists(self):
        return self._public_gists
        
    public_gists = property(_getpublic_gists)

    def _getfollowers(self):
        return self._followers
        
    followers = property(_getfollowers)

    def _getfollowing(self):
        return self._following
        
    following = property(_getfollowing)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getbio(self):
        return self._bio
        
    bio = property(_getbio)

    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _getlocation(self):
        return self._location
        
    location = property(_getlocation)

    def _gethireable(self):
        return self._hireable
        
    hireable = property(_gethireable)

    def _gettext_matches(self):
        return self._text_matches and [ entry and Searchresulttextmatches(**Searchresulttextmatches.patchEntry(entry)) for entry in self._text_matches ]
        
    text_matches = property(_gettext_matches)

    def _getblog(self):
        return self._blog
        
    blog = property(_getblog)

    def _getcompany(self):
        return self._company
        
    company = property(_getcompany)

    def _getsuspended_at(self):
        return self._suspended_at and datetime.datetime.fromisoformat(self._suspended_at[0:-1])
        
    suspended_at = property(_getsuspended_at)


    
##
##
##
class Configurationstatus_progress(ResponseBase):
    def __init__(self, key:str, status:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._key = key
        self._status = status
        return
        
    

    
    def _getkey(self):
        return self._key
        
    key = property(_getkey)

    def _getstatus(self):
        return self._status
        
    status = property(_getstatus)


    
##
##
##
class ConfigurationStatus(ResponseBase):
    def __init__(self, status:str=None, progress:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._status = status
        self._progress = progress
        return
        
    

    
    def _getstatus(self):
        return self._status
        
    status = property(_getstatus)

    def _getprogress(self):
        return self._progress and [ entry and Configurationstatus_progress(**entry) for entry in self._progress ]
        
    progress = property(_getprogress)


    
##
##
##
class Maintenancestatus_connection_services(ResponseBase):
    def __init__(self, number:int, name:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._number = number
        self._name = name
        return
        
    

    
    def _getnumber(self):
        return self._number
        
    number = property(_getnumber)

    def _getname(self):
        return self._name
        
    name = property(_getname)


    
##
##
##
class MaintenanceStatus(ResponseBase):
    def __init__(self, status:str=None, scheduled_time:str=None, connection_services:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._status = status
        self._scheduled_time = scheduled_time
        self._connection_services = connection_services
        return
        
    

    
    def _getstatus(self):
        return self._status
        
    status = property(_getstatus)

    def _getscheduled_time(self):
        return self._scheduled_time
        
    scheduled_time = property(_getscheduled_time)

    def _getconnection_services(self):
        return self._connection_services and [ entry and Maintenancestatus_connection_services(**entry) for entry in self._connection_services ]
        
    connection_services = property(_getconnection_services)


    
##
##
##
class Enterprisesettings_enterprise_avatar(ResponseBase):
    def __init__(self, enabled:bool=None, uri:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        self._uri = uri
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)

    def _geturi(self):
        return self._uri
        
    uri = property(_geturi)


    
##
##
##
class Enterprisesettings_enterprise_customer(ResponseBase):
    def __init__(self, name:str=None, email:str=None, uuid:str=None, secret_key_data:str=None, public_key_data:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._name = name
        self._email = email
        self._uuid = uuid
        self._secret_key_data = secret_key_data
        self._public_key_data = public_key_data
        return
        
    

    
    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _getuuid(self):
        return self._uuid
        
    uuid = property(_getuuid)

    def _getsecret_key_data(self):
        return self._secret_key_data
        
    secret_key_data = property(_getsecret_key_data)

    def _getpublic_key_data(self):
        return self._public_key_data
        
    public_key_data = property(_getpublic_key_data)


    
##
##
##
class Enterprisesettings_enterprise_license(ResponseBase):
    def __init__(self, seats:int=None, evaluation:bool=None, perpetual:bool=None, unlimited_seating:bool=None, support_key:str=None, ssh_allowed:bool=None, cluster_support:bool=None, expire_at:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._seats = seats
        self._evaluation = evaluation
        self._perpetual = perpetual
        self._unlimited_seating = unlimited_seating
        self._support_key = support_key
        self._ssh_allowed = ssh_allowed
        self._cluster_support = cluster_support
        self._expire_at = expire_at
        return
        
    

    
    def _getseats(self):
        return self._seats
        
    seats = property(_getseats)

    def _getevaluation(self):
        return self._evaluation
        
    evaluation = property(_getevaluation)

    def _getperpetual(self):
        return self._perpetual
        
    perpetual = property(_getperpetual)

    def _getunlimited_seating(self):
        return self._unlimited_seating
        
    unlimited_seating = property(_getunlimited_seating)

    def _getsupport_key(self):
        return self._support_key
        
    support_key = property(_getsupport_key)

    def _getssh_allowed(self):
        return self._ssh_allowed
        
    ssh_allowed = property(_getssh_allowed)

    def _getcluster_support(self):
        return self._cluster_support
        
    cluster_support = property(_getcluster_support)

    def _getexpire_at(self):
        return self._expire_at
        
    expire_at = property(_getexpire_at)


    
##
##
##
class Enterprisesettings_enterprise_github_ssl(ResponseBase):
    def __init__(self, enabled:bool=None, cert:str=None, key:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        self._cert = cert
        self._key = key
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)

    def _getcert(self):
        return self._cert
        
    cert = property(_getcert)

    def _getkey(self):
        return self._key
        
    key = property(_getkey)


    
##
##
##
class Enterprisesettings_enterprise_ldap_reconciliation(ResponseBase):
    def __init__(self, user:str=None, org:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._user = user
        self._org = org
        return
        
    

    
    def _getuser(self):
        return self._user
        
    user = property(_getuser)

    def _getorg(self):
        return self._org
        
    org = property(_getorg)


    
##
##
##
class Enterprisesettings_enterprise_ldap_profile(ResponseBase):
    def __init__(self, uid:str=None, name:str=None, mail:str=None, key:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._uid = uid
        self._name = name
        self._mail = mail
        self._key = key
        return
        
    

    
    def _getuid(self):
        return self._uid
        
    uid = property(_getuid)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getmail(self):
        return self._mail
        
    mail = property(_getmail)

    def _getkey(self):
        return self._key
        
    key = property(_getkey)


    
##
##
##
class Enterprisesettings_enterprise_ldap(ResponseBase):
    def __init__(self, host:str=None, port:int=None, base:list=[], uid:str=None, bind_dn:str=None, password:str=None, method:str=None, search_strategy:str=None, user_groups:list=[], admin_group:str=None, virtual_attribute_enabled:bool=None, recursive_group_search:bool=None, posix_support:bool=None, user_sync_emails:bool=None, user_sync_keys:bool=None, user_sync_interval:int=None, team_sync_interval:int=None, sync_enabled:bool=None, reconciliation:dict=None, profile:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._host = host
        self._port = port
        self._base = base
        self._uid = uid
        self._bind_dn = bind_dn
        self._password = password
        self._method = method
        self._search_strategy = search_strategy
        self._user_groups = user_groups
        self._admin_group = admin_group
        self._virtual_attribute_enabled = virtual_attribute_enabled
        self._recursive_group_search = recursive_group_search
        self._posix_support = posix_support
        self._user_sync_emails = user_sync_emails
        self._user_sync_keys = user_sync_keys
        self._user_sync_interval = user_sync_interval
        self._team_sync_interval = team_sync_interval
        self._sync_enabled = sync_enabled
        self._reconciliation = reconciliation
        self._profile = profile
        return
        
    

    
    def _gethost(self):
        return self._host
        
    host = property(_gethost)

    def _getport(self):
        return self._port
        
    port = property(_getport)

    def _getbase(self):
        return self._base and [ entry for entry in self._base ]
        
    base = property(_getbase)

    def _getuid(self):
        return self._uid
        
    uid = property(_getuid)

    def _getbind_dn(self):
        return self._bind_dn
        
    bind_dn = property(_getbind_dn)

    def _getpassword(self):
        return self._password
        
    password = property(_getpassword)

    def _getmethod(self):
        return self._method
        
    method = property(_getmethod)

    def _getsearch_strategy(self):
        return self._search_strategy
        
    search_strategy = property(_getsearch_strategy)

    def _getuser_groups(self):
        return self._user_groups and [ entry for entry in self._user_groups ]
        
    user_groups = property(_getuser_groups)

    def _getadmin_group(self):
        return self._admin_group
        
    admin_group = property(_getadmin_group)

    def _getvirtual_attribute_enabled(self):
        return self._virtual_attribute_enabled
        
    virtual_attribute_enabled = property(_getvirtual_attribute_enabled)

    def _getrecursive_group_search(self):
        return self._recursive_group_search
        
    recursive_group_search = property(_getrecursive_group_search)

    def _getposix_support(self):
        return self._posix_support
        
    posix_support = property(_getposix_support)

    def _getuser_sync_emails(self):
        return self._user_sync_emails
        
    user_sync_emails = property(_getuser_sync_emails)

    def _getuser_sync_keys(self):
        return self._user_sync_keys
        
    user_sync_keys = property(_getuser_sync_keys)

    def _getuser_sync_interval(self):
        return self._user_sync_interval
        
    user_sync_interval = property(_getuser_sync_interval)

    def _getteam_sync_interval(self):
        return self._team_sync_interval
        
    team_sync_interval = property(_getteam_sync_interval)

    def _getsync_enabled(self):
        return self._sync_enabled
        
    sync_enabled = property(_getsync_enabled)

    def _getreconciliation(self):
        return self._reconciliation and Enterprisesettings_enterprise_ldap_reconciliation(**self._reconciliation)
        
    reconciliation = property(_getreconciliation)

    def _getprofile(self):
        return self._profile and Enterprisesettings_enterprise_ldap_profile(**self._profile)
        
    profile = property(_getprofile)


    
##
##
##
class Enterprisesettings_enterprise_cas(ResponseBase):
    def __init__(self, url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class Enterprisesettings_enterprise_saml(ResponseBase):
    def __init__(self, sso_url:str=None, certificate:str=None, certificate_path:str=None, issuer:str=None, idp_initiated_sso:bool=None, disable_admin_demote:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._sso_url = sso_url
        self._certificate = certificate
        self._certificate_path = certificate_path
        self._issuer = issuer
        self._idp_initiated_sso = idp_initiated_sso
        self._disable_admin_demote = disable_admin_demote
        return
        
    

    
    def _getsso_url(self):
        return self._sso_url
        
    sso_url = property(_getsso_url)

    def _getcertificate(self):
        return self._certificate
        
    certificate = property(_getcertificate)

    def _getcertificate_path(self):
        return self._certificate_path
        
    certificate_path = property(_getcertificate_path)

    def _getissuer(self):
        return self._issuer
        
    issuer = property(_getissuer)

    def _getidp_initiated_sso(self):
        return self._idp_initiated_sso
        
    idp_initiated_sso = property(_getidp_initiated_sso)

    def _getdisable_admin_demote(self):
        return self._disable_admin_demote
        
    disable_admin_demote = property(_getdisable_admin_demote)


    
##
##
##
class Enterprisesettings_enterprise_github_oauth(ResponseBase):
    def __init__(self, client_id:str=None, client_secret:str=None, organization_name:str=None, organization_team:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._client_id = client_id
        self._client_secret = client_secret
        self._organization_name = organization_name
        self._organization_team = organization_team
        return
        
    

    
    def _getclient_id(self):
        return self._client_id
        
    client_id = property(_getclient_id)

    def _getclient_secret(self):
        return self._client_secret
        
    client_secret = property(_getclient_secret)

    def _getorganization_name(self):
        return self._organization_name
        
    organization_name = property(_getorganization_name)

    def _getorganization_team(self):
        return self._organization_team
        
    organization_team = property(_getorganization_team)


    
##
##
##
class Enterprisesettings_enterprise_smtp(ResponseBase):
    def __init__(self, enabled:bool=None, address:str=None, authentication:str=None, port:str=None, domain:str=None, username:str=None, user_name:str=None, enable_starttls_auto:bool=None, password:str=None, discardtonoreplyaddress:bool=None, support_address:str=None, support_address_type:str=None, noreply_address:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        self._address = address
        self._authentication = authentication
        self._port = port
        self._domain = domain
        self._username = username
        self._user_name = user_name
        self._enable_starttls_auto = enable_starttls_auto
        self._password = password
        self._discardtonoreplyaddress = discardtonoreplyaddress
        self._support_address = support_address
        self._support_address_type = support_address_type
        self._noreply_address = noreply_address
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['discardtonoreplyaddress'] = entry.pop('discard-to-noreply-address')
        return entry
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)

    def _getaddress(self):
        return self._address
        
    address = property(_getaddress)

    def _getauthentication(self):
        return self._authentication
        
    authentication = property(_getauthentication)

    def _getport(self):
        return self._port
        
    port = property(_getport)

    def _getdomain(self):
        return self._domain
        
    domain = property(_getdomain)

    def _getusername(self):
        return self._username
        
    username = property(_getusername)

    def _getuser_name(self):
        return self._user_name
        
    user_name = property(_getuser_name)

    def _getenable_starttls_auto(self):
        return self._enable_starttls_auto
        
    enable_starttls_auto = property(_getenable_starttls_auto)

    def _getpassword(self):
        return self._password
        
    password = property(_getpassword)

    def _getdiscardtonoreplyaddress(self):
        return self._discardtonoreplyaddress
        
    discardtonoreplyaddress = property(_getdiscardtonoreplyaddress)

    def _getsupport_address(self):
        return self._support_address
        
    support_address = property(_getsupport_address)

    def _getsupport_address_type(self):
        return self._support_address_type
        
    support_address_type = property(_getsupport_address_type)

    def _getnoreply_address(self):
        return self._noreply_address
        
    noreply_address = property(_getnoreply_address)


    
    ##
    ##
    def _getdiscardtonoreplyaddress(self):
        return self._discardtonoreplyaddress
        
    discardtonoreplyaddress = property(_getdiscardtonoreplyaddress)

##
##
##
class Enterprisesettings_enterprise_ntp(ResponseBase):
    def __init__(self, primary_server:str=None, secondary_server:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._primary_server = primary_server
        self._secondary_server = secondary_server
        return
        
    

    
    def _getprimary_server(self):
        return self._primary_server
        
    primary_server = property(_getprimary_server)

    def _getsecondary_server(self):
        return self._secondary_server
        
    secondary_server = property(_getsecondary_server)


    
##
##
##
class Enterprisesettings_enterprise_snmp(ResponseBase):
    def __init__(self, enabled:bool=None, community:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        self._community = community
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)

    def _getcommunity(self):
        return self._community
        
    community = property(_getcommunity)


    
##
##
##
class Enterprisesettings_enterprise_syslog(ResponseBase):
    def __init__(self, enabled:bool=None, server:str=None, protocol_name:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        self._server = server
        self._protocol_name = protocol_name
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)

    def _getserver(self):
        return self._server
        
    server = property(_getserver)

    def _getprotocol_name(self):
        return self._protocol_name
        
    protocol_name = property(_getprotocol_name)


    
##
##
##
class Enterprisesettings_enterprise_pages(ResponseBase):
    def __init__(self, enabled:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)


    
##
##
##
class Enterprisesettings_enterprise_collectd(ResponseBase):
    def __init__(self, enabled:bool=None, server:str=None, port:int=None, encryption:str=None, username:str=None, password:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        self._server = server
        self._port = port
        self._encryption = encryption
        self._username = username
        self._password = password
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)

    def _getserver(self):
        return self._server
        
    server = property(_getserver)

    def _getport(self):
        return self._port
        
    port = property(_getport)

    def _getencryption(self):
        return self._encryption
        
    encryption = property(_getencryption)

    def _getusername(self):
        return self._username
        
    username = property(_getusername)

    def _getpassword(self):
        return self._password
        
    password = property(_getpassword)


    
##
##
##
class Enterprisesettings_enterprise_mapping(ResponseBase):
    def __init__(self, enabled:bool=None, tileserver:str=None, basemap:str=None, token:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enabled = enabled
        self._tileserver = tileserver
        self._basemap = basemap
        self._token = token
        return
        
    

    
    def _getenabled(self):
        return self._enabled
        
    enabled = property(_getenabled)

    def _gettileserver(self):
        return self._tileserver
        
    tileserver = property(_gettileserver)

    def _getbasemap(self):
        return self._basemap
        
    basemap = property(_getbasemap)

    def _gettoken(self):
        return self._token
        
    token = property(_gettoken)


    
##
##
##
class Enterprisesettings_enterprise(ResponseBase):
    def __init__(self, private_mode:bool=None, public_pages:bool=None, subdomain_isolation:bool=None, signup_enabled:bool=None, github_hostname:str=None, identicons_host:str=None, http_proxy:str=None, auth_mode:str=None, expire_sessions:bool=None, admin_password:str=None, configuration_id:int=None, configuration_run_count:int=None, avatar:dict=None, customer:dict=None, license:dict=None, github_ssl:dict=None, ldap:dict=None, cas:dict=None, saml:dict=None, github_oauth:dict=None, smtp:dict=None, ntp:dict=None, timezone:str=None, snmp:dict=None, syslog:dict=None, assets:str=None, pages:dict=None, collectd:dict=None, mapping:dict=None, load_balancer:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._private_mode = private_mode
        self._public_pages = public_pages
        self._subdomain_isolation = subdomain_isolation
        self._signup_enabled = signup_enabled
        self._github_hostname = github_hostname
        self._identicons_host = identicons_host
        self._http_proxy = http_proxy
        self._auth_mode = auth_mode
        self._expire_sessions = expire_sessions
        self._admin_password = admin_password
        self._configuration_id = configuration_id
        self._configuration_run_count = configuration_run_count
        self._avatar = avatar
        self._customer = customer
        self._license = license
        self._github_ssl = github_ssl
        self._ldap = ldap
        self._cas = cas
        self._saml = saml
        self._github_oauth = github_oauth
        self._smtp = smtp
        self._ntp = ntp
        self._timezone = timezone
        self._snmp = snmp
        self._syslog = syslog
        self._assets = assets
        self._pages = pages
        self._collectd = collectd
        self._mapping = mapping
        self._load_balancer = load_balancer
        return
        
    

    
    def _getprivate_mode(self):
        return self._private_mode
        
    private_mode = property(_getprivate_mode)

    def _getpublic_pages(self):
        return self._public_pages
        
    public_pages = property(_getpublic_pages)

    def _getsubdomain_isolation(self):
        return self._subdomain_isolation
        
    subdomain_isolation = property(_getsubdomain_isolation)

    def _getsignup_enabled(self):
        return self._signup_enabled
        
    signup_enabled = property(_getsignup_enabled)

    def _getgithub_hostname(self):
        return self._github_hostname
        
    github_hostname = property(_getgithub_hostname)

    def _getidenticons_host(self):
        return self._identicons_host
        
    identicons_host = property(_getidenticons_host)

    def _gethttp_proxy(self):
        return self._http_proxy
        
    http_proxy = property(_gethttp_proxy)

    def _getauth_mode(self):
        return self._auth_mode
        
    auth_mode = property(_getauth_mode)

    def _getexpire_sessions(self):
        return self._expire_sessions
        
    expire_sessions = property(_getexpire_sessions)

    def _getadmin_password(self):
        return self._admin_password
        
    admin_password = property(_getadmin_password)

    def _getconfiguration_id(self):
        return self._configuration_id
        
    configuration_id = property(_getconfiguration_id)

    def _getconfiguration_run_count(self):
        return self._configuration_run_count
        
    configuration_run_count = property(_getconfiguration_run_count)

    def _getavatar(self):
        return self._avatar and Enterprisesettings_enterprise_avatar(**self._avatar)
        
    avatar = property(_getavatar)

    def _getcustomer(self):
        return self._customer and Enterprisesettings_enterprise_customer(**self._customer)
        
    customer = property(_getcustomer)

    def _getlicense(self):
        return self._license and Enterprisesettings_enterprise_license(**self._license)
        
    license = property(_getlicense)

    def _getgithub_ssl(self):
        return self._github_ssl and Enterprisesettings_enterprise_github_ssl(**self._github_ssl)
        
    github_ssl = property(_getgithub_ssl)

    def _getldap(self):
        return self._ldap and Enterprisesettings_enterprise_ldap(**self._ldap)
        
    ldap = property(_getldap)

    def _getcas(self):
        return self._cas and Enterprisesettings_enterprise_cas(**self._cas)
        
    cas = property(_getcas)

    def _getsaml(self):
        return self._saml and Enterprisesettings_enterprise_saml(**self._saml)
        
    saml = property(_getsaml)

    def _getgithub_oauth(self):
        return self._github_oauth and Enterprisesettings_enterprise_github_oauth(**self._github_oauth)
        
    github_oauth = property(_getgithub_oauth)

    def _getsmtp(self):
        return self._smtp and Enterprisesettings_enterprise_smtp(**Enterprisesettings_enterprise_smtp.patchEntry(self._smtp))
        
    smtp = property(_getsmtp)

    def _getntp(self):
        return self._ntp and Enterprisesettings_enterprise_ntp(**self._ntp)
        
    ntp = property(_getntp)

    def _gettimezone(self):
        return self._timezone
        
    timezone = property(_gettimezone)

    def _getsnmp(self):
        return self._snmp and Enterprisesettings_enterprise_snmp(**self._snmp)
        
    snmp = property(_getsnmp)

    def _getsyslog(self):
        return self._syslog and Enterprisesettings_enterprise_syslog(**self._syslog)
        
    syslog = property(_getsyslog)

    def _getassets(self):
        return self._assets
        
    assets = property(_getassets)

    def _getpages(self):
        return self._pages and Enterprisesettings_enterprise_pages(**self._pages)
        
    pages = property(_getpages)

    def _getcollectd(self):
        return self._collectd and Enterprisesettings_enterprise_collectd(**self._collectd)
        
    collectd = property(_getcollectd)

    def _getmapping(self):
        return self._mapping and Enterprisesettings_enterprise_mapping(**self._mapping)
        
    mapping = property(_getmapping)

    def _getload_balancer(self):
        return self._load_balancer
        
    load_balancer = property(_getload_balancer)


    
##
##
##
class EnterpriseSettings(ResponseBase):
    def __init__(self, enterprise:dict=None, run_list:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._enterprise = enterprise
        self._run_list = run_list
        return
        
    

    
    def _getenterprise(self):
        return self._enterprise and Enterprisesettings_enterprise(**self._enterprise)
        
    enterprise = property(_getenterprise)

    def _getrun_list(self):
        return self._run_list and [ entry for entry in self._run_list ]
        
    run_list = property(_getrun_list)


    
##
##
##
class SshKey(ResponseBase):
    def __init__(self, key:str=None, prettyprint:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._key = key
        self._prettyprint = prettyprint
        return
        
    @classmethod
    def patchEntry(clazz, entry):
        entry['prettyprint'] = entry.pop('pretty-print')
        return entry
    

    
    def _getkey(self):
        return self._key
        
    key = property(_getkey)

    def _getprettyprint(self):
        return self._prettyprint
        
    prettyprint = property(_getprettyprint)


    
    ##
    ##
    def _getprettyprint(self):
        return self._prettyprint
        
    prettyprint = property(_getprettyprint)

##
##
##
class Privateuser_plan(ResponseBase):
    def __init__(self, private_repos:int, space:int, name:str, collaborators:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._private_repos = private_repos
        self._space = space
        self._name = name
        self._collaborators = collaborators
        return
        
    

    
    def _getprivate_repos(self):
        return self._private_repos
        
    private_repos = property(_getprivate_repos)

    def _getspace(self):
        return self._space
        
    space = property(_getspace)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getcollaborators(self):
        return self._collaborators
        
    collaborators = property(_getcollaborators)


    
##
##
##
class PrivateUser(ResponseBase):
    """Private User """
    def __init__(self, two_factor_authentication:bool, collaborators:int, disk_usage:int, owned_private_repos:int, total_private_repos:int, private_gists:int, updated_at:datetime, created_at:datetime, following:int, followers:int, public_gists:int, public_repos:int, bio:str, hireable:bool, email:str, location:str, blog:str, company:str, name:str, site_admin:bool, type:str, received_events_url:str, events_url:str, repos_url:str, organizations_url:str, subscriptions_url:str, starred_url:str, gists_url:str, following_url:str, followers_url:str, html_url:str, url:str, gravatar_id:str, avatar_url:str, node_id:str, id:int, login:str, twitter_username:str=None, plan:dict=None, suspended_at:datetime=None, business_plus:bool=None, ldap_dn:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._two_factor_authentication = two_factor_authentication
        self._collaborators = collaborators
        self._disk_usage = disk_usage
        self._owned_private_repos = owned_private_repos
        self._total_private_repos = total_private_repos
        self._private_gists = private_gists
        self._updated_at = updated_at
        self._created_at = created_at
        self._following = following
        self._followers = followers
        self._public_gists = public_gists
        self._public_repos = public_repos
        self._bio = bio
        self._hireable = hireable
        self._email = email
        self._location = location
        self._blog = blog
        self._company = company
        self._name = name
        self._site_admin = site_admin
        self._type = type
        self._received_events_url = received_events_url
        self._events_url = events_url
        self._repos_url = repos_url
        self._organizations_url = organizations_url
        self._subscriptions_url = subscriptions_url
        self._starred_url = starred_url
        self._gists_url = gists_url
        self._following_url = following_url
        self._followers_url = followers_url
        self._html_url = html_url
        self._url = url
        self._gravatar_id = gravatar_id
        self._avatar_url = avatar_url
        self._node_id = node_id
        self._id = id
        self._login = login
        self._twitter_username = twitter_username
        self._plan = plan
        self._suspended_at = suspended_at
        self._business_plus = business_plus
        self._ldap_dn = ldap_dn
        return
        
    

    
    def _gettwo_factor_authentication(self):
        return self._two_factor_authentication
        
    two_factor_authentication = property(_gettwo_factor_authentication)

    def _getcollaborators(self):
        return self._collaborators
        
    collaborators = property(_getcollaborators)

    def _getdisk_usage(self):
        return self._disk_usage
        
    disk_usage = property(_getdisk_usage)

    def _getowned_private_repos(self):
        return self._owned_private_repos
        
    owned_private_repos = property(_getowned_private_repos)

    def _gettotal_private_repos(self):
        return self._total_private_repos
        
    total_private_repos = property(_gettotal_private_repos)

    def _getprivate_gists(self):
        return self._private_gists
        
    private_gists = property(_getprivate_gists)

    def _getupdated_at(self):
        return self._updated_at and datetime.datetime.fromisoformat(self._updated_at[0:-1])
        
    updated_at = property(_getupdated_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getfollowing(self):
        return self._following
        
    following = property(_getfollowing)

    def _getfollowers(self):
        return self._followers
        
    followers = property(_getfollowers)

    def _getpublic_gists(self):
        return self._public_gists
        
    public_gists = property(_getpublic_gists)

    def _getpublic_repos(self):
        return self._public_repos
        
    public_repos = property(_getpublic_repos)

    def _getbio(self):
        return self._bio
        
    bio = property(_getbio)

    def _gethireable(self):
        return self._hireable
        
    hireable = property(_gethireable)

    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _getlocation(self):
        return self._location
        
    location = property(_getlocation)

    def _getblog(self):
        return self._blog
        
    blog = property(_getblog)

    def _getcompany(self):
        return self._company
        
    company = property(_getcompany)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getsite_admin(self):
        return self._site_admin
        
    site_admin = property(_getsite_admin)

    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getreceived_events_url(self):
        return self._received_events_url
        
    received_events_url = property(_getreceived_events_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getrepos_url(self):
        return self._repos_url
        
    repos_url = property(_getrepos_url)

    def _getorganizations_url(self):
        return self._organizations_url
        
    organizations_url = property(_getorganizations_url)

    def _getsubscriptions_url(self):
        return self._subscriptions_url
        
    subscriptions_url = property(_getsubscriptions_url)

    def _getstarred_url(self):
        return self._starred_url
        
    starred_url = property(_getstarred_url)

    def _getgists_url(self):
        return self._gists_url
        
    gists_url = property(_getgists_url)

    def _getfollowing_url(self):
        return self._following_url
        
    following_url = property(_getfollowing_url)

    def _getfollowers_url(self):
        return self._followers_url
        
    followers_url = property(_getfollowers_url)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getgravatar_id(self):
        return self._gravatar_id
        
    gravatar_id = property(_getgravatar_id)

    def _getavatar_url(self):
        return self._avatar_url
        
    avatar_url = property(_getavatar_url)

    def _getnode_id(self):
        return self._node_id
        
    node_id = property(_getnode_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getlogin(self):
        return self._login
        
    login = property(_getlogin)

    def _gettwitter_username(self):
        return self._twitter_username
        
    twitter_username = property(_gettwitter_username)

    def _getplan(self):
        return self._plan and Privateuser_plan(**self._plan)
        
    plan = property(_getplan)

    def _getsuspended_at(self):
        return self._suspended_at and datetime.datetime.fromisoformat(self._suspended_at[0:-1])
        
    suspended_at = property(_getsuspended_at)

    def _getbusiness_plus(self):
        return self._business_plus
        
    business_plus = property(_getbusiness_plus)

    def _getldap_dn(self):
        return self._ldap_dn
        
    ldap_dn = property(_getldap_dn)


    
##
##
##
class Email(ResponseBase):
    """Email """
    def __init__(self, visibility:str, verified:bool, primary:bool, email:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._visibility = visibility
        self._verified = verified
        self._primary = primary
        self._email = email
        return
        
    

    
    def _getvisibility(self):
        return self._visibility
        
    visibility = property(_getvisibility)

    def _getverified(self):
        return self._verified
        
    verified = property(_getverified)

    def _getprimary(self):
        return self._primary
        
    primary = property(_getprimary)

    def _getemail(self):
        return self._email
        
    email = property(_getemail)


    
##
##
##
class Gpgkey_emails(ResponseBase):
    def __init__(self, email:str=None, verified:bool=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._email = email
        self._verified = verified
        return
        
    

    
    def _getemail(self):
        return self._email
        
    email = property(_getemail)

    def _getverified(self):
        return self._verified
        
    verified = property(_getverified)


    
##
##
##
class Gpgkey_subkeys(ResponseBase):
    def __init__(self, id:int=None, primary_key_id:int=None, key_id:str=None, public_key:str=None, emails:list=[], subkeys:list=[], can_sign:bool=None, can_encrypt_comms:bool=None, can_encrypt_storage:bool=None, can_certify:bool=None, created_at:str=None, expires_at:str=None, raw_key:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._primary_key_id = primary_key_id
        self._key_id = key_id
        self._public_key = public_key
        self._emails = emails
        self._subkeys = subkeys
        self._can_sign = can_sign
        self._can_encrypt_comms = can_encrypt_comms
        self._can_encrypt_storage = can_encrypt_storage
        self._can_certify = can_certify
        self._created_at = created_at
        self._expires_at = expires_at
        self._raw_key = raw_key
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getprimary_key_id(self):
        return self._primary_key_id
        
    primary_key_id = property(_getprimary_key_id)

    def _getkey_id(self):
        return self._key_id
        
    key_id = property(_getkey_id)

    def _getpublic_key(self):
        return self._public_key
        
    public_key = property(_getpublic_key)

    def _getemails(self):
        return self._emails and [ entry for entry in self._emails ]
        
    emails = property(_getemails)

    def _getsubkeys(self):
        return self._subkeys and [ entry for entry in self._subkeys ]
        
    subkeys = property(_getsubkeys)

    def _getcan_sign(self):
        return self._can_sign
        
    can_sign = property(_getcan_sign)

    def _getcan_encrypt_comms(self):
        return self._can_encrypt_comms
        
    can_encrypt_comms = property(_getcan_encrypt_comms)

    def _getcan_encrypt_storage(self):
        return self._can_encrypt_storage
        
    can_encrypt_storage = property(_getcan_encrypt_storage)

    def _getcan_certify(self):
        return self._can_certify
        
    can_certify = property(_getcan_certify)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _getexpires_at(self):
        return self._expires_at
        
    expires_at = property(_getexpires_at)

    def _getraw_key(self):
        return self._raw_key
        
    raw_key = property(_getraw_key)


    
##
##
##
class GpgKey(ResponseBase):
    """A unique encryption key """
    def __init__(self, raw_key:str, expires_at:datetime, created_at:datetime, can_certify:bool, can_encrypt_storage:bool, can_encrypt_comms:bool, can_sign:bool, subkeys:list, emails:list, public_key:str, key_id:str, primary_key_id:int, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._raw_key = raw_key
        self._expires_at = expires_at
        self._created_at = created_at
        self._can_certify = can_certify
        self._can_encrypt_storage = can_encrypt_storage
        self._can_encrypt_comms = can_encrypt_comms
        self._can_sign = can_sign
        self._subkeys = subkeys
        self._emails = emails
        self._public_key = public_key
        self._key_id = key_id
        self._primary_key_id = primary_key_id
        self._id = id
        return
        
    

    
    def _getraw_key(self):
        return self._raw_key
        
    raw_key = property(_getraw_key)

    def _getexpires_at(self):
        return self._expires_at and datetime.datetime.fromisoformat(self._expires_at[0:-1])
        
    expires_at = property(_getexpires_at)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _getcan_certify(self):
        return self._can_certify
        
    can_certify = property(_getcan_certify)

    def _getcan_encrypt_storage(self):
        return self._can_encrypt_storage
        
    can_encrypt_storage = property(_getcan_encrypt_storage)

    def _getcan_encrypt_comms(self):
        return self._can_encrypt_comms
        
    can_encrypt_comms = property(_getcan_encrypt_comms)

    def _getcan_sign(self):
        return self._can_sign
        
    can_sign = property(_getcan_sign)

    def _getsubkeys(self):
        return self._subkeys and [ entry and Gpgkey_subkeys(**entry) for entry in self._subkeys ]
        
    subkeys = property(_getsubkeys)

    def _getemails(self):
        return self._emails and [ entry and Gpgkey_emails(**entry) for entry in self._emails ]
        
    emails = property(_getemails)

    def _getpublic_key(self):
        return self._public_key
        
    public_key = property(_getpublic_key)

    def _getkey_id(self):
        return self._key_id
        
    key_id = property(_getkey_id)

    def _getprimary_key_id(self):
        return self._primary_key_id
        
    primary_key_id = property(_getprimary_key_id)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class Key(ResponseBase):
    """Key """
    def __init__(self, read_only:bool, verified:bool, created_at:datetime, title:str, url:str, id:int, key:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._read_only = read_only
        self._verified = verified
        self._created_at = created_at
        self._title = title
        self._url = url
        self._id = id
        self._key = key
        return
        
    

    
    def _getread_only(self):
        return self._read_only
        
    read_only = property(_getread_only)

    def _getverified(self):
        return self._verified
        
    verified = property(_getverified)

    def _getcreated_at(self):
        return self._created_at and datetime.datetime.fromisoformat(self._created_at[0:-1])
        
    created_at = property(_getcreated_at)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getkey(self):
        return self._key
        
    key = property(_getkey)


    
##
##
##
class StarredRepository(ResponseBase):
    """Starred Repository """
    def __init__(self, repo:dict, starred_at:datetime, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._repo = repo
        self._starred_at = starred_at
        return
        
    

    
    def _getrepo(self):
        return self._repo and Repository(**self._repo)
        
    repo = property(_getrepo)

    def _getstarred_at(self):
        return self._starred_at and datetime.datetime.fromisoformat(self._starred_at[0:-1])
        
    starred_at = property(_getstarred_at)


    
##
##
##
class Hovercard_contexts(ResponseBase):
    def __init__(self, octicon:str, message:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._octicon = octicon
        self._message = message
        return
        
    

    
    def _getocticon(self):
        return self._octicon
        
    octicon = property(_getocticon)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)


    
##
##
##
class Hovercard(ResponseBase):
    """Hovercard """
    def __init__(self, contexts:list, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._contexts = contexts
        return
        
    

    
    def _getcontexts(self):
        return self._contexts and [ entry and Hovercard_contexts(**entry) for entry in self._contexts ]
        
    contexts = property(_getcontexts)


    
##
##
##
class KeySimple(ResponseBase):
    """Key Simple """
    def __init__(self, key:str, id:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._key = key
        self._id = id
        return
        
    

    
    def _getkey(self):
        return self._key
        
    key = property(_getkey)

    def _getid(self):
        return self._id
        
    id = property(_getid)


    
##
##
##
class Preview_header_missing(ResponseBase):
    def __init__(self, documentation_url:str, message:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._documentation_url = documentation_url
        self._message = message
        return
        
    

    
    def _getdocumentation_url(self):
        return self._documentation_url
        
    documentation_url = property(_getdocumentation_url)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)


    
##
##
##
class NotModified(ResponseBase):
    """Not modified """
    def __init__(self, **kwargs):
        ResponseBase.__init__(self, kwargs)
        return
        
    

    

    
##
##
##
class Service_unavailable(ResponseBase):
    def __init__(self, code:str=None, message:str=None, documentation_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._code = code
        self._message = message
        self._documentation_url = documentation_url
        return
        
    

    
    def _getcode(self):
        return self._code
        
    code = property(_getcode)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getdocumentation_url(self):
        return self._documentation_url
        
    documentation_url = property(_getdocumentation_url)


    def _ok(self):
        return False

    ok = property(_ok, doc='not ok')

##
##
##
class Forbidden_gist_block(ResponseBase):
    def __init__(self, reason:str=None, created_at:str=None, html_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._reason = reason
        self._created_at = created_at
        self._html_url = html_url
        return
        
    

    
    def _getreason(self):
        return self._reason
        
    reason = property(_getreason)

    def _getcreated_at(self):
        return self._created_at
        
    created_at = property(_getcreated_at)

    def _gethtml_url(self):
        return self._html_url
        
    html_url = property(_gethtml_url)


    
##
##
##
class Forbidden_gist(ResponseBase):
    def __init__(self, block:dict=None, message:str=None, documentation_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._block = block
        self._message = message
        self._documentation_url = documentation_url
        return
        
    

    
    def _getblock(self):
        return self._block and Forbidden_gist_block(**self._block)
        
    block = property(_getblock)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getdocumentation_url(self):
        return self._documentation_url
        
    documentation_url = property(_getdocumentation_url)


    
##
##
##
class Found(ResponseBase):
    """Found """
    def __init__(self, **kwargs):
        ResponseBase.__init__(self, kwargs)
        return
        
    

    

    
##
##
##
class NoContent(ResponseBase):
    """A header with no content is returned. """
    def __init__(self, **kwargs):
        ResponseBase.__init__(self, kwargs)
        return
        
    

    

    
##
##
##
class MetaRootSuccess(ResponseBase):
    def __init__(self, user_search_url:str, user_repositories_url:str, user_organizations_url:str, user_url:str, starred_gists_url:str, starred_url:str, current_user_repositories_url:str, repository_search_url:str, repository_url:str, rate_limit_url:str, public_gists_url:str, organization_teams_url:str, organization_repositories_url:str, organization_url:str, notifications_url:str, label_search_url:str, keys_url:str, issues_url:str, issue_search_url:str, hub_url:str, gists_url:str, following_url:str, followers_url:str, feeds_url:str, events_url:str, emojis_url:str, emails_url:str, commit_search_url:str, code_search_url:str, authorizations_url:str, current_user_authorizations_html_url:str, current_user_url:str, topic_search_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._user_search_url = user_search_url
        self._user_repositories_url = user_repositories_url
        self._user_organizations_url = user_organizations_url
        self._user_url = user_url
        self._starred_gists_url = starred_gists_url
        self._starred_url = starred_url
        self._current_user_repositories_url = current_user_repositories_url
        self._repository_search_url = repository_search_url
        self._repository_url = repository_url
        self._rate_limit_url = rate_limit_url
        self._public_gists_url = public_gists_url
        self._organization_teams_url = organization_teams_url
        self._organization_repositories_url = organization_repositories_url
        self._organization_url = organization_url
        self._notifications_url = notifications_url
        self._label_search_url = label_search_url
        self._keys_url = keys_url
        self._issues_url = issues_url
        self._issue_search_url = issue_search_url
        self._hub_url = hub_url
        self._gists_url = gists_url
        self._following_url = following_url
        self._followers_url = followers_url
        self._feeds_url = feeds_url
        self._events_url = events_url
        self._emojis_url = emojis_url
        self._emails_url = emails_url
        self._commit_search_url = commit_search_url
        self._code_search_url = code_search_url
        self._authorizations_url = authorizations_url
        self._current_user_authorizations_html_url = current_user_authorizations_html_url
        self._current_user_url = current_user_url
        self._topic_search_url = topic_search_url
        return
        
    

    
    def _getuser_search_url(self):
        return self._user_search_url
        
    user_search_url = property(_getuser_search_url)

    def _getuser_repositories_url(self):
        return self._user_repositories_url
        
    user_repositories_url = property(_getuser_repositories_url)

    def _getuser_organizations_url(self):
        return self._user_organizations_url
        
    user_organizations_url = property(_getuser_organizations_url)

    def _getuser_url(self):
        return self._user_url
        
    user_url = property(_getuser_url)

    def _getstarred_gists_url(self):
        return self._starred_gists_url
        
    starred_gists_url = property(_getstarred_gists_url)

    def _getstarred_url(self):
        return self._starred_url
        
    starred_url = property(_getstarred_url)

    def _getcurrent_user_repositories_url(self):
        return self._current_user_repositories_url
        
    current_user_repositories_url = property(_getcurrent_user_repositories_url)

    def _getrepository_search_url(self):
        return self._repository_search_url
        
    repository_search_url = property(_getrepository_search_url)

    def _getrepository_url(self):
        return self._repository_url
        
    repository_url = property(_getrepository_url)

    def _getrate_limit_url(self):
        return self._rate_limit_url
        
    rate_limit_url = property(_getrate_limit_url)

    def _getpublic_gists_url(self):
        return self._public_gists_url
        
    public_gists_url = property(_getpublic_gists_url)

    def _getorganization_teams_url(self):
        return self._organization_teams_url
        
    organization_teams_url = property(_getorganization_teams_url)

    def _getorganization_repositories_url(self):
        return self._organization_repositories_url
        
    organization_repositories_url = property(_getorganization_repositories_url)

    def _getorganization_url(self):
        return self._organization_url
        
    organization_url = property(_getorganization_url)

    def _getnotifications_url(self):
        return self._notifications_url
        
    notifications_url = property(_getnotifications_url)

    def _getlabel_search_url(self):
        return self._label_search_url
        
    label_search_url = property(_getlabel_search_url)

    def _getkeys_url(self):
        return self._keys_url
        
    keys_url = property(_getkeys_url)

    def _getissues_url(self):
        return self._issues_url
        
    issues_url = property(_getissues_url)

    def _getissue_search_url(self):
        return self._issue_search_url
        
    issue_search_url = property(_getissue_search_url)

    def _gethub_url(self):
        return self._hub_url
        
    hub_url = property(_gethub_url)

    def _getgists_url(self):
        return self._gists_url
        
    gists_url = property(_getgists_url)

    def _getfollowing_url(self):
        return self._following_url
        
    following_url = property(_getfollowing_url)

    def _getfollowers_url(self):
        return self._followers_url
        
    followers_url = property(_getfollowers_url)

    def _getfeeds_url(self):
        return self._feeds_url
        
    feeds_url = property(_getfeeds_url)

    def _getevents_url(self):
        return self._events_url
        
    events_url = property(_getevents_url)

    def _getemojis_url(self):
        return self._emojis_url
        
    emojis_url = property(_getemojis_url)

    def _getemails_url(self):
        return self._emails_url
        
    emails_url = property(_getemails_url)

    def _getcommit_search_url(self):
        return self._commit_search_url
        
    commit_search_url = property(_getcommit_search_url)

    def _getcode_search_url(self):
        return self._code_search_url
        
    code_search_url = property(_getcode_search_url)

    def _getauthorizations_url(self):
        return self._authorizations_url
        
    authorizations_url = property(_getauthorizations_url)

    def _getcurrent_user_authorizations_html_url(self):
        return self._current_user_authorizations_html_url
        
    current_user_authorizations_html_url = property(_getcurrent_user_authorizations_html_url)

    def _getcurrent_user_url(self):
        return self._current_user_url
        
    current_user_url = property(_getcurrent_user_url)

    def _gettopic_search_url(self):
        return self._topic_search_url
        
    topic_search_url = property(_gettopic_search_url)


    
##
##
##
class Enterpriseadmincreateglobalwebhook_config(ResponseBase):
    """Key/value pairs to provide settings for this webhook. """
    def __init__(self, url:str, content_type:str=None, secret:str=None, insecure_ssl:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._content_type = content_type
        self._secret = secret
        self._insecure_ssl = insecure_ssl
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl, doc="""The URL to which the payloads will be delivered. """)

    def _getcontent_type(self):
        return self._content_type
        
    content_type = property(_getcontent_type, doc="""The media type used to serialize the payloads. Supported values include `json` and `form`. The default is `form`. """)

    def _getsecret(self):
        return self._secret
        
    secret = property(_getsecret, doc="""If provided, the `secret` will be used as the `key` to generate the HMAC hex digest value in the [`X-Hub-Signature`](https://docs.github.com/enterprise-server@3.3/webhooks/event-payloads/#delivery-headers) header. """)

    def _getinsecure_ssl(self):
        return self._insecure_ssl
        
    insecure_ssl = property(_getinsecure_ssl, doc="""Determines whether the SSL certificate of the host for `url` will be verified when delivering payloads. Supported values include `0` (verification is performed) and `1` (verification is not performed). The default is `0`. **We strongly recommend not setting this to `1` as you are subject to man-in-the-middle and other attacks.** """)


    
##
##
##
class Enterpriseadminupdateglobalwebhook_config(ResponseBase):
    """Key/value pairs to provide settings for this webhook. """
    def __init__(self, url:str, content_type:str=None, secret:str=None, insecure_ssl:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._content_type = content_type
        self._secret = secret
        self._insecure_ssl = insecure_ssl
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl, doc="""The URL to which the payloads will be delivered. """)

    def _getcontent_type(self):
        return self._content_type
        
    content_type = property(_getcontent_type, doc="""The media type used to serialize the payloads. Supported values include `json` and `form`. The default is `form`. """)

    def _getsecret(self):
        return self._secret
        
    secret = property(_getsecret, doc="""If provided, the `secret` will be used as the `key` to generate the HMAC hex digest value in the [`X-Hub-Signature`](https://docs.github.com/enterprise-server@3.3/webhooks/event-payloads/#delivery-headers) header. """)

    def _getinsecure_ssl(self):
        return self._insecure_ssl
        
    insecure_ssl = property(_getinsecure_ssl, doc="""Determines whether the SSL certificate of the host for `url` will be verified when delivering payloads. Supported values include `0` (verification is performed) and `1` (verification is not performed). The default is `0`. **We strongly recommend not setting this to `1` as you are subject to man-in-the-middle and other attacks.** """)


    
##
##
##
class EnterpriseAdminSyncLdapMappingForTeamSuccess(ResponseBase):
    def __init__(self, status:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._status = status
        return
        
    

    
    def _getstatus(self):
        return self._status
        
    status = property(_getstatus)


    
##
##
##
class EnterpriseAdminSyncLdapMappingForUserSuccess(ResponseBase):
    def __init__(self, status:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._status = status
        return
        
    

    
    def _getstatus(self):
        return self._status
        
    status = property(_getstatus)


    
##
##
##
class EnterpriseAdminUpdateOrgName202(ResponseBase):
    def __init__(self, message:str=None, url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._url = url
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class Errors(ResponseBase):
    def __init__(self, code:str=None, message:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._code = code
        self._message = message
        return
        
    

    
    def _getcode(self):
        return self._code
        
    code = property(_getcode)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)


    
##
##
##
class EnterpriseAdminUpdatePreReceiveEnvironment422(ResponseBase):
    def __init__(self, message:str=None, errors:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._errors = errors
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _geterrors(self):
        return self._errors and [ entry and Errors(**entry) for entry in self._errors ]
        
    errors = property(_geterrors)


    
##
##
##
class EnterpriseAdminDeletePreReceiveEnvironment422(ResponseBase):
    def __init__(self, message:str=None, errors:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._errors = errors
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _geterrors(self):
        return self._errors and [ entry and Errors(**entry) for entry in self._errors ]
        
    errors = property(_geterrors)


    
##
##
##
class EnterpriseAdminStartPreReceiveEnvironmentDownload422(ResponseBase):
    def __init__(self, message:str=None, errors:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._errors = errors
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _geterrors(self):
        return self._errors and [ entry and Errors(**entry) for entry in self._errors ]
        
    errors = property(_geterrors)


    
##
##
##
class Enterpriseadmincreateprereceivehook_script_repository(ResponseBase):
    """The GitHub repository where the script is kept. """
    def __init__(self, **kwargs):
        ResponseBase.__init__(self, kwargs)
        return
        
    

    

    
##
##
##
class Enterpriseadmincreateprereceivehook_environment(ResponseBase):
    """The pre-receive environment where the script is executed. """
    def __init__(self, **kwargs):
        ResponseBase.__init__(self, kwargs)
        return
        
    

    

    
##
##
##
class Enterpriseadminupdateprereceivehook_script_repository(ResponseBase):
    """The GitHub repository where the script is kept. """
    def __init__(self, **kwargs):
        ResponseBase.__init__(self, kwargs)
        return
        
    

    

    
##
##
##
class Enterpriseadminupdateprereceivehook_environment(ResponseBase):
    """The pre-receive environment where the script is executed. """
    def __init__(self, **kwargs):
        ResponseBase.__init__(self, kwargs)
        return
        
    

    

    
##
##
##
class EnterpriseAdminUpdateUsernameForUser202(ResponseBase):
    def __init__(self, message:str=None, url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._url = url
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class EnterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterpriseSuccess(ResponseBase):
    def __init__(self, organizations:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._organizations = organizations
        self._total_count = total_count
        return
        
    

    
    def _getorganizations(self):
        return self._organizations and [ entry and OrganizationSimple(**entry) for entry in self._organizations ]
        
    organizations = property(_getorganizations)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class EnterpriseAdminListSelfHostedRunnerGroupsForEnterpriseSuccess(ResponseBase):
    def __init__(self, runner_groups:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._runner_groups = runner_groups
        self._total_count = total_count
        return
        
    

    
    def _getrunner_groups(self):
        return self._runner_groups and [ entry and RunnerGroupsEnterprise(**entry) for entry in self._runner_groups ]
        
    runner_groups = property(_getrunner_groups)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class EnterpriseAdminListOrgAccessToSelfHostedRunnerGroupInEnterpriseSuccess(ResponseBase):
    def __init__(self, organizations:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._organizations = organizations
        self._total_count = total_count
        return
        
    

    
    def _getorganizations(self):
        return self._organizations and [ entry and OrganizationSimple(**entry) for entry in self._organizations ]
        
    organizations = property(_getorganizations)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class EnterpriseAdminListSelfHostedRunnersInGroupForEnterpriseSuccess(ResponseBase):
    def __init__(self, runners:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._runners = runners
        self._total_count = total_count
        return
        
    

    
    def _getrunners(self):
        return self._runners and [ entry and SelfHostedRunners(**entry) for entry in self._runners ]
        
    runners = property(_getrunners)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class EnterpriseAdminListSelfHostedRunnersForEnterpriseSuccess(ResponseBase):
    def __init__(self, total_count:int=None, runners:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._total_count = total_count
        self._runners = runners
        return
        
    

    
    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)

    def _getrunners(self):
        return self._runners and [ entry and SelfHostedRunners(**entry) for entry in self._runners ]
        
    runners = property(_getrunners)


    
##
##
##
class GistsCheckIsStarredNotFound(ResponseBase):
    def __init__(self, **kwargs):
        ResponseBase.__init__(self, kwargs)
        return
        
    

    

    
##
##
##
class AppsListReposAccessibleToInstallationSuccess(ResponseBase):
    def __init__(self, repositories:list, total_count:int, repository_selection:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._repositories = repositories
        self._total_count = total_count
        self._repository_selection = repository_selection
        return
        
    

    
    def _getrepositories(self):
        return self._repositories and [ entry and Repository(**entry) for entry in self._repositories ]
        
    repositories = property(_getrepositories)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)

    def _getrepository_selection(self):
        return self._repository_selection
        
    repository_selection = property(_getrepository_selection)


    
##
##
##
class ActivityMarkNotificationsAsRead202(ResponseBase):
    def __init__(self, message:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)


    
##
##
##
class ActionsListSelectedRepositoriesEnabledGithubActionsOrganizationSuccess(ResponseBase):
    def __init__(self, repositories:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._repositories = repositories
        self._total_count = total_count
        return
        
    

    
    def _getrepositories(self):
        return self._repositories and [ entry and Repository(**entry) for entry in self._repositories ]
        
    repositories = property(_getrepositories)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class ActionsListSelfHostedRunnerGroupsForOrgSuccess(ResponseBase):
    def __init__(self, runner_groups:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._runner_groups = runner_groups
        self._total_count = total_count
        return
        
    

    
    def _getrunner_groups(self):
        return self._runner_groups and [ entry and RunnerGroupsOrg(**entry) for entry in self._runner_groups ]
        
    runner_groups = property(_getrunner_groups)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class ActionsListRepoAccessToSelfHostedRunnerGroupInOrgSuccess(ResponseBase):
    def __init__(self, repositories:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._repositories = repositories
        self._total_count = total_count
        return
        
    

    
    def _getrepositories(self):
        return self._repositories and [ entry and MinimalRepository(**entry) for entry in self._repositories ]
        
    repositories = property(_getrepositories)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class ActionsListSelfHostedRunnersInGroupForOrgSuccess(ResponseBase):
    def __init__(self, runners:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._runners = runners
        self._total_count = total_count
        return
        
    

    
    def _getrunners(self):
        return self._runners and [ entry and SelfHostedRunners(**entry) for entry in self._runners ]
        
    runners = property(_getrunners)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class ActionsListSelfHostedRunnersForOrgSuccess(ResponseBase):
    def __init__(self, runners:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._runners = runners
        self._total_count = total_count
        return
        
    

    
    def _getrunners(self):
        return self._runners and [ entry and SelfHostedRunners(**entry) for entry in self._runners ]
        
    runners = property(_getrunners)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class ActionsListOrgSecretsSuccess(ResponseBase):
    def __init__(self, secrets:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._secrets = secrets
        self._total_count = total_count
        return
        
    

    
    def _getsecrets(self):
        return self._secrets and [ entry and ActionsSecretForAnOrganization(**entry) for entry in self._secrets ]
        
    secrets = property(_getsecrets)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class ActionsListSelectedReposForOrgSecretSuccess(ResponseBase):
    def __init__(self, repositories:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._repositories = repositories
        self._total_count = total_count
        return
        
    

    
    def _getrepositories(self):
        return self._repositories and [ entry and MinimalRepository(**entry) for entry in self._repositories ]
        
    repositories = property(_getrepositories)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class Orgscreatewebhook_config(ResponseBase):
    """Key/value pairs to provide settings for this webhook. [These are defined below](https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#create-hook-config-params). """
    def __init__(self, url:str, content_type:str=None, secret:str=None, insecure_ssl=None, username:str=None, password:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._content_type = content_type
        self._secret = secret
        self._insecure_ssl = insecure_ssl
        self._username = username
        self._password = password
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getcontent_type(self):
        return self._content_type
        
    content_type = property(_getcontent_type)

    def _getsecret(self):
        return self._secret
        
    secret = property(_getsecret)

    def _getinsecure_ssl(self):
        return self._insecure_ssl
        
    insecure_ssl = property(_getinsecure_ssl)

    def _getusername(self):
        return self._username
        
    username = property(_getusername)

    def _getpassword(self):
        return self._password
        
    password = property(_getpassword)


    
##
##
##
class Orgsupdatewebhook_config(ResponseBase):
    """Key/value pairs to provide settings for this webhook. [These are defined below](https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#update-hook-config-params). """
    def __init__(self, url:str, content_type:str=None, secret:str=None, insecure_ssl=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._content_type = content_type
        self._secret = secret
        self._insecure_ssl = insecure_ssl
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getcontent_type(self):
        return self._content_type
        
    content_type = property(_getcontent_type)

    def _getsecret(self):
        return self._secret
        
    secret = property(_getsecret)

    def _getinsecure_ssl(self):
        return self._insecure_ssl
        
    insecure_ssl = property(_getinsecure_ssl)


    
##
##
##
class OrgsListAppInstallationsSuccess(ResponseBase):
    def __init__(self, installations:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._installations = installations
        self._total_count = total_count
        return
        
    

    
    def _getinstallations(self):
        return self._installations and [ entry and Installation(**entry) for entry in self._installations ]
        
    installations = property(_getinstallations)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class OrgsConvertMemberToOutsideCollaborator202(ResponseBase):
    def __init__(self, **kwargs):
        ResponseBase.__init__(self, kwargs)
        return
        
    

    

    
##
##
##
class OrgsRemoveOutsideCollaborator422(ResponseBase):
    def __init__(self, message:str=None, documentation_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._documentation_url = documentation_url
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getdocumentation_url(self):
        return self._documentation_url
        
    documentation_url = property(_getdocumentation_url)


    
##
##
##
class TeamsAddOrUpdateProjectPermissionsInOrgForbidden(ResponseBase):
    def __init__(self, message:str=None, documentation_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._documentation_url = documentation_url
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getdocumentation_url(self):
        return self._documentation_url
        
    documentation_url = property(_getdocumentation_url)


    
##
##
##
class ProjectsDeleteCardForbidden(ResponseBase):
    def __init__(self, message:str=None, documentation_url:str=None, errors:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._documentation_url = documentation_url
        self._errors = errors
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getdocumentation_url(self):
        return self._documentation_url
        
    documentation_url = property(_getdocumentation_url)

    def _geterrors(self):
        return self._errors and [ entry for entry in self._errors ]
        
    errors = property(_geterrors)


    
##
##
##
class ProjectsMoveCardSuccess(ResponseBase):
    def __init__(self, **kwargs):
        ResponseBase.__init__(self, kwargs)
        return
        
    

    

    
##
##
##
class ProjectsMoveCardForbidden(ResponseBase):
    def __init__(self, message:str=None, documentation_url:str=None, errors:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._documentation_url = documentation_url
        self._errors = errors
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getdocumentation_url(self):
        return self._documentation_url
        
    documentation_url = property(_getdocumentation_url)

    def _geterrors(self):
        return self._errors and [ entry and Errors(**entry) for entry in self._errors ]
        
    errors = property(_geterrors)


    
##
##
##
class ProjectsMoveCard503(ResponseBase):
    def __init__(self, code:str=None, message:str=None, documentation_url:str=None, errors:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._code = code
        self._message = message
        self._documentation_url = documentation_url
        self._errors = errors
        return
        
    

    
    def _getcode(self):
        return self._code
        
    code = property(_getcode)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getdocumentation_url(self):
        return self._documentation_url
        
    documentation_url = property(_getdocumentation_url)

    def _geterrors(self):
        return self._errors and [ entry and Errors(**entry) for entry in self._errors ]
        
    errors = property(_geterrors)


    
##
##
##
class ProjectsCreateCard503(ResponseBase):
    def __init__(self, code:str=None, message:str=None, documentation_url:str=None, errors:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._code = code
        self._message = message
        self._documentation_url = documentation_url
        self._errors = errors
        return
        
    

    
    def _getcode(self):
        return self._code
        
    code = property(_getcode)

    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getdocumentation_url(self):
        return self._documentation_url
        
    documentation_url = property(_getdocumentation_url)

    def _geterrors(self):
        return self._errors and [ entry and Errors(**entry) for entry in self._errors ]
        
    errors = property(_geterrors)


    
##
##
##
class ProjectsMoveColumnSuccess(ResponseBase):
    def __init__(self, **kwargs):
        ResponseBase.__init__(self, kwargs)
        return
        
    

    

    
##
##
##
class ProjectsUpdateForbidden(ResponseBase):
    def __init__(self, message:str=None, documentation_url:str=None, errors:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._documentation_url = documentation_url
        self._errors = errors
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getdocumentation_url(self):
        return self._documentation_url
        
    documentation_url = property(_getdocumentation_url)

    def _geterrors(self):
        return self._errors and [ entry for entry in self._errors ]
        
    errors = property(_geterrors)


    
##
##
##
class ProjectsDeleteForbidden(ResponseBase):
    def __init__(self, message:str=None, documentation_url:str=None, errors:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._documentation_url = documentation_url
        self._errors = errors
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getdocumentation_url(self):
        return self._documentation_url
        
    documentation_url = property(_getdocumentation_url)

    def _geterrors(self):
        return self._errors and [ entry for entry in self._errors ]
        
    errors = property(_geterrors)


    
##
##
##
class Reposupdate_security_and_analysis_advanced_security(ResponseBase):
    """Use the `status` property to enable or disable GitHub Advanced Security for this repository. For more information, see "[About GitHub Advanced Security](/github/getting-started-with-github/learning-about-github/about-github-advanced-security)." """
    def __init__(self, status:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._status = status
        return
        
    

    
    def _getstatus(self):
        return self._status
        
    status = property(_getstatus, doc="""Can be `enabled` or `disabled`. """)


    
##
##
##
class Reposupdate_security_and_analysis_secret_scanning(ResponseBase):
    """Use the `status` property to enable or disable secret scanning for this repository. For more information, see "[About secret scanning](/code-security/secret-security/about-secret-scanning)." """
    def __init__(self, status:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._status = status
        return
        
    

    
    def _getstatus(self):
        return self._status
        
    status = property(_getstatus, doc="""Can be `enabled` or `disabled`. """)


    
##
##
##
class Reposupdate_security_and_analysis(ResponseBase):
    """Specify which security and analysis features to enable or disable. For example, to enable GitHub Advanced Security, use this data in the body of the PATCH request: `{"security_and_analysis": {"advanced_security": {"status": "enabled"}}}`. If you have admin permissions for a private repository covered by an Advanced Security license, you can check which security and analysis features are currently enabled by using a `GET /repos/{owner}/{repo}` request. """
    def __init__(self, advanced_security:dict=None, secret_scanning:dict=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._advanced_security = advanced_security
        self._secret_scanning = secret_scanning
        return
        
    

    
    def _getadvanced_security(self):
        return self._advanced_security and Reposupdate_security_and_analysis_advanced_security(**self._advanced_security)
        
    advanced_security = property(_getadvanced_security, doc="""Use the `status` property to enable or disable GitHub Advanced Security for this repository. For more information, see "[About GitHub Advanced Security](/github/getting-started-with-github/learning-about-github/about-github-advanced-security)." """)

    def _getsecret_scanning(self):
        return self._secret_scanning and Reposupdate_security_and_analysis_secret_scanning(**self._secret_scanning)
        
    secret_scanning = property(_getsecret_scanning, doc="""Use the `status` property to enable or disable secret scanning for this repository. For more information, see "[About secret scanning](/code-security/secret-security/about-secret-scanning)." """)


    
##
##
##
class ReposDeleteForbidden(ResponseBase):
    def __init__(self, message:str=None, documentation_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._documentation_url = documentation_url
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getdocumentation_url(self):
        return self._documentation_url
        
    documentation_url = property(_getdocumentation_url)


    
##
##
##
class ActionsListArtifactsForRepoSuccess(ResponseBase):
    def __init__(self, artifacts:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._artifacts = artifacts
        self._total_count = total_count
        return
        
    

    
    def _getartifacts(self):
        return self._artifacts and [ entry and Artifact(**entry) for entry in self._artifacts ]
        
    artifacts = property(_getartifacts)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class ActionsListSelfHostedRunnersForRepoSuccess(ResponseBase):
    def __init__(self, runners:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._runners = runners
        self._total_count = total_count
        return
        
    

    
    def _getrunners(self):
        return self._runners and [ entry and SelfHostedRunners(**entry) for entry in self._runners ]
        
    runners = property(_getrunners)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class ActionsListWorkflowRunsForRepoSuccess(ResponseBase):
    def __init__(self, workflow_runs:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._workflow_runs = workflow_runs
        self._total_count = total_count
        return
        
    

    
    def _getworkflow_runs(self):
        return self._workflow_runs and [ entry and WorkflowRun(**entry) for entry in self._workflow_runs ]
        
    workflow_runs = property(_getworkflow_runs)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class ActionsListWorkflowRunArtifactsSuccess(ResponseBase):
    def __init__(self, artifacts:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._artifacts = artifacts
        self._total_count = total_count
        return
        
    

    
    def _getartifacts(self):
        return self._artifacts and [ entry and Artifact(**entry) for entry in self._artifacts ]
        
    artifacts = property(_getartifacts)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class ActionsListJobsForWorkflowRunAttemptSuccess(ResponseBase):
    def __init__(self, jobs:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._jobs = jobs
        self._total_count = total_count
        return
        
    

    
    def _getjobs(self):
        return self._jobs and [ entry and Job(**entry) for entry in self._jobs ]
        
    jobs = property(_getjobs)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class ActionsCancelWorkflowRun202(ResponseBase):
    def __init__(self, **kwargs):
        ResponseBase.__init__(self, kwargs)
        return
        
    

    

    
##
##
##
class ActionsListJobsForWorkflowRunSuccess(ResponseBase):
    def __init__(self, jobs:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._jobs = jobs
        self._total_count = total_count
        return
        
    

    
    def _getjobs(self):
        return self._jobs and [ entry and Job(**entry) for entry in self._jobs ]
        
    jobs = property(_getjobs)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class ActionsReRunWorkflowSuccess(ResponseBase):
    def __init__(self, **kwargs):
        ResponseBase.__init__(self, kwargs)
        return
        
    

    

    
##
##
##
class ActionsListRepoSecretsSuccess(ResponseBase):
    def __init__(self, secrets:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._secrets = secrets
        self._total_count = total_count
        return
        
    

    
    def _getsecrets(self):
        return self._secrets and [ entry and ActionsSecret(**entry) for entry in self._secrets ]
        
    secrets = property(_getsecrets)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class ActionsCreateOrUpdateRepoSecretSuccess(ResponseBase):
    def __init__(self, **kwargs):
        ResponseBase.__init__(self, kwargs)
        return
        
    

    

    
##
##
##
class ActionsListRepoWorkflowsSuccess(ResponseBase):
    def __init__(self, workflows:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._workflows = workflows
        self._total_count = total_count
        return
        
    

    
    def _getworkflows(self):
        return self._workflows and [ entry and Workflow(**entry) for entry in self._workflows ]
        
    workflows = property(_getworkflows)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class ActionsListWorkflowRunsSuccess(ResponseBase):
    def __init__(self, workflow_runs:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._workflow_runs = workflow_runs
        self._total_count = total_count
        return
        
    

    
    def _getworkflow_runs(self):
        return self._workflow_runs and [ entry and WorkflowRun(**entry) for entry in self._workflow_runs ]
        
    workflow_runs = property(_getworkflow_runs)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class Reposupdatebranchprotection_required_status_checks_checks(ResponseBase):
    def __init__(self, context:str, app_id:int=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._context = context
        self._app_id = app_id
        return
        
    

    
    def _getcontext(self):
        return self._context
        
    context = property(_getcontext, doc="""The name of the required check """)

    def _getapp_id(self):
        return self._app_id
        
    app_id = property(_getapp_id, doc="""The ID of the GitHub App that must provide this check. Omit this field to automatically select the GitHub App that has recently provided this check, or any app if it was not set by a GitHub App. Pass -1 to explicitly allow any app to set the status. """)


    
##
##
##
class Reposupdatebranchprotection_required_status_checks(ResponseBase):
    """Require status checks to pass before merging. Set to `null` to disable. """
    def __init__(self, contexts, strict:bool, checks:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._contexts = contexts
        self._strict = strict
        self._checks = checks
        return
        
    

    
    def _getcontexts(self):
        return self._contexts # deprecated
        
    contexts = property(_getcontexts, doc="""**Deprecated**: The list of status checks to require in order to merge into this branch. If any of these checks have recently been set by a particular GitHub App, they will be required to come from that app in future for the branch to merge. Use `checks` instead of `contexts` for more fine-grained control.
 """)

    def _getstrict(self):
        return self._strict
        
    strict = property(_getstrict, doc="""Require branches to be up to date before merging. """)

    def _getchecks(self):
        return self._checks and [ entry and Reposupdatebranchprotection_required_status_checks_checks(**entry) for entry in self._checks ]
        
    checks = property(_getchecks, doc="""The list of status checks to require in order to merge into this branch. """)


    
##
##
##
class Reposupdatebranchprotection_required_pull_request_reviews_dismissal_restrictions(ResponseBase):
    """Specify which users and teams can dismiss pull request reviews. Pass an empty `dismissal_restrictions` object to disable. User and team `dismissal_restrictions` are only available for organization-owned repositories. Omit this parameter for personal repositories. """
    def __init__(self, users:list=[], teams:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._users = users
        self._teams = teams
        return
        
    

    
    def _getusers(self):
        return self._users and [ entry for entry in self._users ]
        
    users = property(_getusers, doc="""The list of user `login`s with dismissal access """)

    def _getteams(self):
        return self._teams and [ entry for entry in self._teams ]
        
    teams = property(_getteams, doc="""The list of team `slug`s with dismissal access """)


    
##
##
##
class Reposupdatebranchprotection_required_pull_request_reviews(ResponseBase):
    """Require at least one approving review on a pull request, before merging. Set to `null` to disable. """
    def __init__(self, dismissal_restrictions:dict=None, dismiss_stale_reviews:bool=None, require_code_owner_reviews:bool=None, required_approving_review_count:int=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._dismissal_restrictions = dismissal_restrictions
        self._dismiss_stale_reviews = dismiss_stale_reviews
        self._require_code_owner_reviews = require_code_owner_reviews
        self._required_approving_review_count = required_approving_review_count
        return
        
    

    
    def _getdismissal_restrictions(self):
        return self._dismissal_restrictions and Reposupdatebranchprotection_required_pull_request_reviews_dismissal_restrictions(**self._dismissal_restrictions)
        
    dismissal_restrictions = property(_getdismissal_restrictions, doc="""Specify which users and teams can dismiss pull request reviews. Pass an empty `dismissal_restrictions` object to disable. User and team `dismissal_restrictions` are only available for organization-owned repositories. Omit this parameter for personal repositories. """)

    def _getdismiss_stale_reviews(self):
        return self._dismiss_stale_reviews
        
    dismiss_stale_reviews = property(_getdismiss_stale_reviews, doc="""Set to `true` if you want to automatically dismiss approving reviews when someone pushes a new commit. """)

    def _getrequire_code_owner_reviews(self):
        return self._require_code_owner_reviews
        
    require_code_owner_reviews = property(_getrequire_code_owner_reviews, doc="""Blocks merging pull requests until [code owners](https://help.github.com/articles/about-code-owners/) review them. """)

    def _getrequired_approving_review_count(self):
        return self._required_approving_review_count
        
    required_approving_review_count = property(_getrequired_approving_review_count, doc="""Specify the number of reviewers required to approve pull requests. Use a number between 1 and 6. """)


    
##
##
##
class Reposupdatebranchprotection_restrictions(ResponseBase):
    """Restrict who can push to the protected branch. User, app, and team `restrictions` are only available for organization-owned repositories. Set to `null` to disable. """
    def __init__(self, teams:list, users:list, apps:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._teams = teams
        self._users = users
        self._apps = apps
        return
        
    

    
    def _getteams(self):
        return self._teams and [ entry for entry in self._teams ]
        
    teams = property(_getteams, doc="""The list of team `slug`s with push access """)

    def _getusers(self):
        return self._users and [ entry for entry in self._users ]
        
    users = property(_getusers, doc="""The list of user `login`s with push access """)

    def _getapps(self):
        return self._apps and [ entry for entry in self._apps ]
        
    apps = property(_getapps, doc="""The list of app `slug`s with push access """)


    
##
##
##
class Reposupdatepullrequestreviewprotection_dismissal_restrictions(ResponseBase):
    """Specify which users and teams can dismiss pull request reviews. Pass an empty `dismissal_restrictions` object to disable. User and team `dismissal_restrictions` are only available for organization-owned repositories. Omit this parameter for personal repositories. """
    def __init__(self, users:list=[], teams:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._users = users
        self._teams = teams
        return
        
    

    
    def _getusers(self):
        return self._users and [ entry for entry in self._users ]
        
    users = property(_getusers, doc="""The list of user `login`s with dismissal access """)

    def _getteams(self):
        return self._teams and [ entry for entry in self._teams ]
        
    teams = property(_getteams, doc="""The list of team `slug`s with dismissal access """)


    
##
##
##
class Checkscreate_output_annotations(ResponseBase):
    def __init__(self, message:str, annotation_level:str, end_line:int, start_line:int, path:str, start_column:int=None, end_column:int=None, title:str=None, raw_details:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._annotation_level = annotation_level
        self._end_line = end_line
        self._start_line = start_line
        self._path = path
        self._start_column = start_column
        self._end_column = end_column
        self._title = title
        self._raw_details = raw_details
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage, doc="""A short description of the feedback for these lines of code. The maximum size is 64 KB. """)

    def _getannotation_level(self):
        return self._annotation_level
        
    annotation_level = property(_getannotation_level, doc="""The level of the annotation. Can be one of `notice`, `warning`, or `failure`. """)

    def _getend_line(self):
        return self._end_line
        
    end_line = property(_getend_line, doc="""The end line of the annotation. """)

    def _getstart_line(self):
        return self._start_line
        
    start_line = property(_getstart_line, doc="""The start line of the annotation. """)

    def _getpath(self):
        return self._path
        
    path = property(_getpath, doc="""The path of the file to add an annotation to. For example, `assets/css/main.css`. """)

    def _getstart_column(self):
        return self._start_column
        
    start_column = property(_getstart_column, doc="""The start column of the annotation. Annotations only support `start_column` and `end_column` on the same line. Omit this parameter if `start_line` and `end_line` have different values. """)

    def _getend_column(self):
        return self._end_column
        
    end_column = property(_getend_column, doc="""The end column of the annotation. Annotations only support `start_column` and `end_column` on the same line. Omit this parameter if `start_line` and `end_line` have different values. """)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle, doc="""The title that represents the annotation. The maximum size is 255 characters. """)

    def _getraw_details(self):
        return self._raw_details
        
    raw_details = property(_getraw_details, doc="""Details about this annotation. The maximum size is 64 KB. """)


    
##
##
##
class Checkscreate_output_images(ResponseBase):
    def __init__(self, image_url:str, alt:str, caption:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._image_url = image_url
        self._alt = alt
        self._caption = caption
        return
        
    

    
    def _getimage_url(self):
        return self._image_url
        
    image_url = property(_getimage_url, doc="""The full URL of the image. """)

    def _getalt(self):
        return self._alt
        
    alt = property(_getalt, doc="""The alternative text for the image. """)

    def _getcaption(self):
        return self._caption
        
    caption = property(_getcaption, doc="""A short image description. """)


    
##
##
##
class Checkscreate_output(ResponseBase):
    """Check runs can accept a variety of data in the `output` object, including a `title` and `summary` and can optionally provide descriptive details about the run. See the [`output` object](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#output-object) description. """
    def __init__(self, summary:str, title:str, text:str=None, annotations:list=[], images:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._summary = summary
        self._title = title
        self._text = text
        self._annotations = annotations
        self._images = images
        return
        
    

    
    def _getsummary(self):
        return self._summary
        
    summary = property(_getsummary, doc="""The summary of the check run. This parameter supports Markdown. """)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle, doc="""The title of the check run. """)

    def _gettext(self):
        return self._text
        
    text = property(_gettext, doc="""The details of the check run. This parameter supports Markdown. """)

    def _getannotations(self):
        return self._annotations and [ entry and Checkscreate_output_annotations(**entry) for entry in self._annotations ]
        
    annotations = property(_getannotations, doc="""Adds information from your analysis to specific lines of code. Annotations are visible on GitHub in the **Checks** and **Files changed** tab of the pull request. The Checks API limits the number of annotations to a maximum of 50 per API request. To create more than 50 annotations, you have to make multiple requests to the [Update a check run](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#update-a-check-run) endpoint. Each time you update the check run, annotations are appended to the list of annotations that already exist for the check run. For details about how you can view annotations on GitHub, see "[About status checks](https://help.github.com/articles/about-status-checks#checks)". See the [`annotations` object](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#annotations-object) description for details about how to use this parameter. """)

    def _getimages(self):
        return self._images and [ entry and Checkscreate_output_images(**entry) for entry in self._images ]
        
    images = property(_getimages, doc="""Adds images to the output displayed in the GitHub pull request UI. See the [`images` object](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#images-object) description for details. """)


    
##
##
##
class Checkscreate_actions(ResponseBase):
    def __init__(self, identifier:str, description:str, label:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._identifier = identifier
        self._description = description
        self._label = label
        return
        
    

    
    def _getidentifier(self):
        return self._identifier
        
    identifier = property(_getidentifier, doc="""A reference for the action on the integrator's system. The maximum size is 20 characters. """)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription, doc="""A short explanation of what this action would do. The maximum size is 40 characters. """)

    def _getlabel(self):
        return self._label
        
    label = property(_getlabel, doc="""The text to be displayed on a button in the web UI. The maximum size is 20 characters. """)


    
##
##
##
class Checksupdate_output_annotations(ResponseBase):
    def __init__(self, message:str, annotation_level:str, end_line:int, start_line:int, path:str, start_column:int=None, end_column:int=None, title:str=None, raw_details:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._annotation_level = annotation_level
        self._end_line = end_line
        self._start_line = start_line
        self._path = path
        self._start_column = start_column
        self._end_column = end_column
        self._title = title
        self._raw_details = raw_details
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage, doc="""A short description of the feedback for these lines of code. The maximum size is 64 KB. """)

    def _getannotation_level(self):
        return self._annotation_level
        
    annotation_level = property(_getannotation_level, doc="""The level of the annotation. Can be one of `notice`, `warning`, or `failure`. """)

    def _getend_line(self):
        return self._end_line
        
    end_line = property(_getend_line, doc="""The end line of the annotation. """)

    def _getstart_line(self):
        return self._start_line
        
    start_line = property(_getstart_line, doc="""The start line of the annotation. """)

    def _getpath(self):
        return self._path
        
    path = property(_getpath, doc="""The path of the file to add an annotation to. For example, `assets/css/main.css`. """)

    def _getstart_column(self):
        return self._start_column
        
    start_column = property(_getstart_column, doc="""The start column of the annotation. Annotations only support `start_column` and `end_column` on the same line. Omit this parameter if `start_line` and `end_line` have different values. """)

    def _getend_column(self):
        return self._end_column
        
    end_column = property(_getend_column, doc="""The end column of the annotation. Annotations only support `start_column` and `end_column` on the same line. Omit this parameter if `start_line` and `end_line` have different values. """)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle, doc="""The title that represents the annotation. The maximum size is 255 characters. """)

    def _getraw_details(self):
        return self._raw_details
        
    raw_details = property(_getraw_details, doc="""Details about this annotation. The maximum size is 64 KB. """)


    
##
##
##
class Checksupdate_output_images(ResponseBase):
    def __init__(self, image_url:str, alt:str, caption:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._image_url = image_url
        self._alt = alt
        self._caption = caption
        return
        
    

    
    def _getimage_url(self):
        return self._image_url
        
    image_url = property(_getimage_url, doc="""The full URL of the image. """)

    def _getalt(self):
        return self._alt
        
    alt = property(_getalt, doc="""The alternative text for the image. """)

    def _getcaption(self):
        return self._caption
        
    caption = property(_getcaption, doc="""A short image description. """)


    
##
##
##
class Checksupdate_output(ResponseBase):
    """Check runs can accept a variety of data in the `output` object, including a `title` and `summary` and can optionally provide descriptive details about the run. See the [`output` object](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#output-object-1) description. """
    def __init__(self, summary:str, title:str=None, text:str=None, annotations:list=[], images:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._summary = summary
        self._title = title
        self._text = text
        self._annotations = annotations
        self._images = images
        return
        
    

    
    def _getsummary(self):
        return self._summary
        
    summary = property(_getsummary, doc="""Can contain Markdown. """)

    def _gettitle(self):
        return self._title
        
    title = property(_gettitle, doc="""**Required**. """)

    def _gettext(self):
        return self._text
        
    text = property(_gettext, doc="""Can contain Markdown. """)

    def _getannotations(self):
        return self._annotations and [ entry and Checksupdate_output_annotations(**entry) for entry in self._annotations ]
        
    annotations = property(_getannotations, doc="""Adds information from your analysis to specific lines of code. Annotations are visible in GitHub's pull request UI. Annotations are visible in GitHub's pull request UI. The Checks API limits the number of annotations to a maximum of 50 per API request. To create more than 50 annotations, you have to make multiple requests to the [Update a check run](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#update-a-check-run) endpoint. Each time you update the check run, annotations are appended to the list of annotations that already exist for the check run. For details about annotations in the UI, see "[About status checks](https://help.github.com/articles/about-status-checks#checks)". See the [`annotations` object](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#annotations-object-1) description for details. """)

    def _getimages(self):
        return self._images and [ entry and Checksupdate_output_images(**entry) for entry in self._images ]
        
    images = property(_getimages, doc="""Adds images to the output displayed in the GitHub pull request UI. See the [`images` object](https://docs.github.com/enterprise-server@3.3/rest/reference/checks#annotations-object-1) description for details. """)


    
##
##
##
class Checksupdate_actions(ResponseBase):
    def __init__(self, identifier:str, description:str, label:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._identifier = identifier
        self._description = description
        self._label = label
        return
        
    

    
    def _getidentifier(self):
        return self._identifier
        
    identifier = property(_getidentifier, doc="""A reference for the action on the integrator's system. The maximum size is 20 characters. """)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription, doc="""A short explanation of what this action would do. The maximum size is 40 characters. """)

    def _getlabel(self):
        return self._label
        
    label = property(_getlabel, doc="""The text to be displayed on a button in the web UI. The maximum size is 20 characters. """)


    
##
##
##
class ChecksRerequestRunSuccess(ResponseBase):
    def __init__(self, **kwargs):
        ResponseBase.__init__(self, kwargs)
        return
        
    

    

    
##
##
##
class Checkssetsuitespreferences_auto_trigger_checks(ResponseBase):
    def __init__(self, app_id:int, setting:bool=True, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._app_id = app_id
        self._setting = setting
        return
        
    

    
    def _getapp_id(self):
        return self._app_id
        
    app_id = property(_getapp_id, doc="""The `id` of the GitHub App. """)

    def _getsetting(self):
        return self._setting
        
    setting = property(_getsetting, doc="""Set to `true` to enable automatic creation of CheckSuite events upon pushes to the repository, or `false` to disable them. """)


    
##
##
##
class ChecksListForSuiteSuccess(ResponseBase):
    def __init__(self, check_runs:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._check_runs = check_runs
        self._total_count = total_count
        return
        
    

    
    def _getcheck_runs(self):
        return self._check_runs and [ entry and Checkrun(**entry) for entry in self._check_runs ]
        
    check_runs = property(_getcheck_runs)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class ChecksRerequestSuiteSuccess(ResponseBase):
    def __init__(self, **kwargs):
        ResponseBase.__init__(self, kwargs)
        return
        
    

    

    
##
##
##
class ChecksListForRefSuccess(ResponseBase):
    def __init__(self, check_runs:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._check_runs = check_runs
        self._total_count = total_count
        return
        
    

    
    def _getcheck_runs(self):
        return self._check_runs and [ entry and Checkrun(**entry) for entry in self._check_runs ]
        
    check_runs = property(_getcheck_runs)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class ChecksListSuitesForRefSuccess(ResponseBase):
    def __init__(self, check_suites:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._check_suites = check_suites
        self._total_count = total_count
        return
        
    

    
    def _getcheck_suites(self):
        return self._check_suites and [ entry and Checksuite(**entry) for entry in self._check_suites ]
        
    check_suites = property(_getcheck_suites)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class Reposcreateorupdatefilecontents_committer(ResponseBase):
    """The person that committed the file. Default: the authenticated user. """
    def __init__(self, email:str, name:str, date:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._email = email
        self._name = name
        self._date = date
        return
        
    

    
    def _getemail(self):
        return self._email
        
    email = property(_getemail, doc="""The email of the author or committer of the commit. You'll receive a `422` status code if `email` is omitted. """)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the author or committer of the commit. You'll receive a `422` status code if `name` is omitted. """)

    def _getdate(self):
        return self._date
        
    date = property(_getdate)


    
##
##
##
class Reposcreateorupdatefilecontents_author(ResponseBase):
    """The author of the file. Default: The `committer` or the authenticated user if you omit `committer`. """
    def __init__(self, email:str, name:str, date:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._email = email
        self._name = name
        self._date = date
        return
        
    

    
    def _getemail(self):
        return self._email
        
    email = property(_getemail, doc="""The email of the author or committer of the commit. You'll receive a `422` status code if `email` is omitted. """)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the author or committer of the commit. You'll receive a `422` status code if `name` is omitted. """)

    def _getdate(self):
        return self._date
        
    date = property(_getdate)


    
##
##
##
class Reposdeletefile_committer(ResponseBase):
    """object containing information about the committer. """
    def __init__(self, name:str=None, email:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._name = name
        self._email = email
        return
        
    

    
    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the author (or committer) of the commit """)

    def _getemail(self):
        return self._email
        
    email = property(_getemail, doc="""The email of the author (or committer) of the commit """)


    
##
##
##
class Reposdeletefile_author(ResponseBase):
    """object containing information about the author. """
    def __init__(self, name:str=None, email:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._name = name
        self._email = email
        return
        
    

    
    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the author (or committer) of the commit """)

    def _getemail(self):
        return self._email
        
    email = property(_getemail, doc="""The email of the author (or committer) of the commit """)


    
##
##
##
class ReposCreateDeployment202(ResponseBase):
    def __init__(self, message:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)


    
##
##
##
class ReposGetAllEnvironmentsSuccess(ResponseBase):
    def __init__(self, total_count:int=None, environments:list=[], **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._total_count = total_count
        self._environments = environments
        return
        
    

    
    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count, doc="""The number of environments in this repository """)

    def _getenvironments(self):
        return self._environments and [ entry and Environment(**entry) for entry in self._environments ]
        
    environments = property(_getenvironments)


    
##
##
##
class Reposcreateorupdateenvironment_reviewers(ResponseBase):
    def __init__(self, type:str=None, id:int=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._type = type
        self._id = id
        return
        
    

    
    def _gettype(self):
        return self._type
        
    type = property(_gettype)

    def _getid(self):
        return self._id
        
    id = property(_getid, doc="""The id of the user or team who can review the deployment """)


    
##
##
##
class Gitcreatecommit_author(ResponseBase):
    """Information about the author of the commit. By default, the `author` will be the authenticated user and the current date. See the `author` and `committer` object below for details. """
    def __init__(self, email:str, name:str, date:datetime=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._email = email
        self._name = name
        self._date = date
        return
        
    

    
    def _getemail(self):
        return self._email
        
    email = property(_getemail, doc="""The email of the author (or committer) of the commit """)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the author (or committer) of the commit """)

    def _getdate(self):
        return self._date and datetime.datetime.fromisoformat(self._date[0:-1])
        
    date = property(_getdate, doc="""Indicates when this commit was authored (or committed). This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. """)


    
##
##
##
class Gitcreatecommit_committer(ResponseBase):
    """Information about the person who is making the commit. By default, `committer` will use the information set in `author`. See the `author` and `committer` object below for details. """
    def __init__(self, name:str=None, email:str=None, date:datetime=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._name = name
        self._email = email
        self._date = date
        return
        
    

    
    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the author (or committer) of the commit """)

    def _getemail(self):
        return self._email
        
    email = property(_getemail, doc="""The email of the author (or committer) of the commit """)

    def _getdate(self):
        return self._date and datetime.datetime.fromisoformat(self._date[0:-1])
        
    date = property(_getdate, doc="""Indicates when this commit was authored (or committed). This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. """)


    
##
##
##
class Gitcreatetag_tagger(ResponseBase):
    """An object with information about the individual creating the tag. """
    def __init__(self, email:str, name:str, date:datetime=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._email = email
        self._name = name
        self._date = date
        return
        
    

    
    def _getemail(self):
        return self._email
        
    email = property(_getemail, doc="""The email of the author of the tag """)

    def _getname(self):
        return self._name
        
    name = property(_getname, doc="""The name of the author of the tag """)

    def _getdate(self):
        return self._date and datetime.datetime.fromisoformat(self._date[0:-1])
        
    date = property(_getdate, doc="""When this object was tagged. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. """)


    
##
##
##
class Gitcreatetree_tree(ResponseBase):
    def __init__(self, path:str=None, mode:str=None, type:str=None, sha:str=None, content:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._path = path
        self._mode = mode
        self._type = type
        self._sha = sha
        self._content = content
        return
        
    

    
    def _getpath(self):
        return self._path
        
    path = property(_getpath, doc="""The file referenced in the tree. """)

    def _getmode(self):
        return self._mode
        
    mode = property(_getmode, doc="""The file mode; one of `100644` for file (blob), `100755` for executable (blob), `040000` for subdirectory (tree), `160000` for submodule (commit), or `120000` for a blob that specifies the path of a symlink. """)

    def _gettype(self):
        return self._type
        
    type = property(_gettype, doc="""Either `blob`, `tree`, or `commit`. """)

    def _getsha(self):
        return self._sha
        
    sha = property(_getsha, doc="""The SHA1 checksum ID of the object in the tree. Also called `tree.sha`. If the value is `null` then the file will be deleted.  
  
**Note:** Use either `tree.sha` or `content` to specify the contents of the entry. Using both `tree.sha` and `content` will return an error. """)

    def _getcontent(self):
        return self._content
        
    content = property(_getcontent, doc="""The content you want this file to have. GitHub will write this blob out and use that SHA for this entry. Use either this, or `tree.sha`.  
  
**Note:** Use either `tree.sha` or `content` to specify the contents of the entry. Using both `tree.sha` and `content` will return an error. """)


    
##
##
##
class Reposcreatewebhook_config(ResponseBase):
    """Key/value pairs to provide settings for this webhook. [These are defined below](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-hook-config-params). """
    def __init__(self, url:str=None, content_type:str=None, secret:str=None, insecure_ssl=None, token:str=None, digest:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._content_type = content_type
        self._secret = secret
        self._insecure_ssl = insecure_ssl
        self._token = token
        self._digest = digest
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getcontent_type(self):
        return self._content_type
        
    content_type = property(_getcontent_type)

    def _getsecret(self):
        return self._secret
        
    secret = property(_getsecret)

    def _getinsecure_ssl(self):
        return self._insecure_ssl
        
    insecure_ssl = property(_getinsecure_ssl)

    def _gettoken(self):
        return self._token
        
    token = property(_gettoken)

    def _getdigest(self):
        return self._digest
        
    digest = property(_getdigest)


    
##
##
##
class Reposupdatewebhook_config(ResponseBase):
    """Key/value pairs to provide settings for this webhook. [These are defined below](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#create-hook-config-params). """
    def __init__(self, url:str, content_type:str=None, secret:str=None, insecure_ssl=None, address:str=None, room:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._url = url
        self._content_type = content_type
        self._secret = secret
        self._insecure_ssl = insecure_ssl
        self._address = address
        self._room = room
        return
        
    

    
    def _geturl(self):
        return self._url
        
    url = property(_geturl)

    def _getcontent_type(self):
        return self._content_type
        
    content_type = property(_getcontent_type)

    def _getsecret(self):
        return self._secret
        
    secret = property(_getsecret)

    def _getinsecure_ssl(self):
        return self._insecure_ssl
        
    insecure_ssl = property(_getinsecure_ssl)

    def _getaddress(self):
        return self._address
        
    address = property(_getaddress)

    def _getroom(self):
        return self._room
        
    room = property(_getroom)


    
##
##
##
class Issuescreate_labels(ResponseBase):
    def __init__(self, id:int=None, name:str=None, description:str=None, color:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._name = name
        self._description = description
        self._color = color
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getcolor(self):
        return self._color
        
    color = property(_getcolor)


    
##
##
##
class Issuesupdate_labels(ResponseBase):
    def __init__(self, id:int=None, name:str=None, description:str=None, color:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._id = id
        self._name = name
        self._description = description
        self._color = color
        return
        
    

    
    def _getid(self):
        return self._id
        
    id = property(_getid)

    def _getname(self):
        return self._name
        
    name = property(_getname)

    def _getdescription(self):
        return self._description
        
    description = property(_getdescription)

    def _getcolor(self):
        return self._color
        
    color = property(_getcolor)


    
##
##
##
class ActivityMarkRepoNotificationsAsRead202(ResponseBase):
    def __init__(self, message:str=None, url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._url = url
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class Reposcreatepagessite_source(ResponseBase):
    """The source branch and directory used to publish your Pages site. """
    def __init__(self, branch:str, path:str='/', **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._branch = branch
        self._path = path
        return
        
    

    
    def _getbranch(self):
        return self._branch
        
    branch = property(_getbranch, doc="""The repository branch used to publish your site's source files. """)

    def _getpath(self):
        return self._path
        
    path = property(_getpath, doc="""The repository directory that includes the source files for the Pages site. Allowed paths are `/` or `/docs`. Default: `/` """)


    
##
##
##
class Reposupdateinformationaboutpagessite_source(ResponseBase):
    """Update the source for the repository. Must include the branch name and path. """
    def __init__(self, path:str, branch:str, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._path = path
        self._branch = branch
        return
        
    

    
    def _getpath(self):
        return self._path
        
    path = property(_getpath, doc="""The repository directory that includes the source files for the Pages site. Allowed paths are `/` or `/docs`. """)

    def _getbranch(self):
        return self._branch
        
    branch = property(_getbranch, doc="""The repository branch used to publish your site's source files. """)


    
##
##
##
class PullsMerge405(ResponseBase):
    def __init__(self, message:str=None, documentation_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._documentation_url = documentation_url
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getdocumentation_url(self):
        return self._documentation_url
        
    documentation_url = property(_getdocumentation_url)


    
##
##
##
class PullsMerge409(ResponseBase):
    def __init__(self, message:str=None, documentation_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._documentation_url = documentation_url
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getdocumentation_url(self):
        return self._documentation_url
        
    documentation_url = property(_getdocumentation_url)


    
##
##
##
class Pullscreatereview_comments(ResponseBase):
    def __init__(self, body:str, path:str, position:int=None, line:int=None, side:str=None, start_line:int=None, start_side:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._body = body
        self._path = path
        self._position = position
        self._line = line
        self._side = side
        self._start_line = start_line
        self._start_side = start_side
        return
        
    

    
    def _getbody(self):
        return self._body
        
    body = property(_getbody, doc="""Text of the review comment. """)

    def _getpath(self):
        return self._path
        
    path = property(_getpath, doc="""The relative path to the file that necessitates a review comment. """)

    def _getposition(self):
        return self._position
        
    position = property(_getposition, doc="""The position in the diff where you want to add a review comment. Note this value is not the same as the line number in the file. For help finding the position value, read the note below. """)

    def _getline(self):
        return self._line
        
    line = property(_getline)

    def _getside(self):
        return self._side
        
    side = property(_getside)

    def _getstart_line(self):
        return self._start_line
        
    start_line = property(_getstart_line)

    def _getstart_side(self):
        return self._start_side
        
    start_side = property(_getstart_side)


    
##
##
##
class PullsUpdateBranch202(ResponseBase):
    def __init__(self, message:str=None, url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._url = url
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _geturl(self):
        return self._url
        
    url = property(_geturl)


    
##
##
##
class ActionsListEnvironmentSecretsSuccess(ResponseBase):
    def __init__(self, secrets:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._secrets = secrets
        self._total_count = total_count
        return
        
    

    
    def _getsecrets(self):
        return self._secrets and [ entry and ActionsSecret(**entry) for entry in self._secrets ]
        
    secrets = property(_getsecrets)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class SearchCodeSuccess(ResponseBase):
    def __init__(self, items:list, incomplete_results:bool, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._items = items
        self._incomplete_results = incomplete_results
        self._total_count = total_count
        return
        
    

    
    def _getitems(self):
        return self._items and [ entry and CodeSearchResultItem(**entry) for entry in self._items ]
        
    items = property(_getitems)

    def _getincomplete_results(self):
        return self._incomplete_results
        
    incomplete_results = property(_getincomplete_results)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class SearchCommitsSuccess(ResponseBase):
    def __init__(self, items:list, incomplete_results:bool, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._items = items
        self._incomplete_results = incomplete_results
        self._total_count = total_count
        return
        
    

    
    def _getitems(self):
        return self._items and [ entry and CommitSearchResultItem(**entry) for entry in self._items ]
        
    items = property(_getitems)

    def _getincomplete_results(self):
        return self._incomplete_results
        
    incomplete_results = property(_getincomplete_results)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class SearchIssuesAndPullRequestsSuccess(ResponseBase):
    def __init__(self, items:list, incomplete_results:bool, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._items = items
        self._incomplete_results = incomplete_results
        self._total_count = total_count
        return
        
    

    
    def _getitems(self):
        return self._items and [ entry and IssueSearchResultItem(**entry) for entry in self._items ]
        
    items = property(_getitems)

    def _getincomplete_results(self):
        return self._incomplete_results
        
    incomplete_results = property(_getincomplete_results)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class SearchLabelsSuccess(ResponseBase):
    def __init__(self, items:list, incomplete_results:bool, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._items = items
        self._incomplete_results = incomplete_results
        self._total_count = total_count
        return
        
    

    
    def _getitems(self):
        return self._items and [ entry and LabelSearchResultItem(**entry) for entry in self._items ]
        
    items = property(_getitems)

    def _getincomplete_results(self):
        return self._incomplete_results
        
    incomplete_results = property(_getincomplete_results)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class SearchReposSuccess(ResponseBase):
    def __init__(self, items:list, incomplete_results:bool, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._items = items
        self._incomplete_results = incomplete_results
        self._total_count = total_count
        return
        
    

    
    def _getitems(self):
        return self._items and [ entry and RepoSearchResultItem(**entry) for entry in self._items ]
        
    items = property(_getitems)

    def _getincomplete_results(self):
        return self._incomplete_results
        
    incomplete_results = property(_getincomplete_results)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class SearchTopicsSuccess(ResponseBase):
    def __init__(self, items:list, incomplete_results:bool, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._items = items
        self._incomplete_results = incomplete_results
        self._total_count = total_count
        return
        
    

    
    def _getitems(self):
        return self._items and [ entry and TopicSearchResultItem(**entry) for entry in self._items ]
        
    items = property(_getitems)

    def _getincomplete_results(self):
        return self._incomplete_results
        
    incomplete_results = property(_getincomplete_results)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class SearchUsersSuccess(ResponseBase):
    def __init__(self, items:list, incomplete_results:bool, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._items = items
        self._incomplete_results = incomplete_results
        self._total_count = total_count
        return
        
    

    
    def _getitems(self):
        return self._items and [ entry and UserSearchResultItem(**entry) for entry in self._items ]
        
    items = property(_getitems)

    def _getincomplete_results(self):
        return self._incomplete_results
        
    incomplete_results = property(_getincomplete_results)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class TeamsAddOrUpdateProjectPermissionsLegacyForbidden(ResponseBase):
    def __init__(self, message:str=None, documentation_url:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._message = message
        self._documentation_url = documentation_url
        return
        
    

    
    def _getmessage(self):
        return self._message
        
    message = property(_getmessage)

    def _getdocumentation_url(self):
        return self._documentation_url
        
    documentation_url = property(_getdocumentation_url)


    
##
##
##
class AppsListInstallationsForAuthenticatedUserSuccess(ResponseBase):
    def __init__(self, installations:list, total_count:int, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._installations = installations
        self._total_count = total_count
        return
        
    

    
    def _getinstallations(self):
        return self._installations and [ entry and Installation(**entry) for entry in self._installations ]
        
    installations = property(_getinstallations)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)


    
##
##
##
class AppsListInstallationReposForAuthenticatedUserSuccess(ResponseBase):
    def __init__(self, repositories:list, total_count:int, repository_selection:str=None, **kwargs):
        ResponseBase.__init__(self, kwargs)
        self._repositories = repositories
        self._total_count = total_count
        self._repository_selection = repository_selection
        return
        
    

    
    def _getrepositories(self):
        return self._repositories and [ entry and Repository(**entry) for entry in self._repositories ]
        
    repositories = property(_getrepositories)

    def _gettotal_count(self):
        return self._total_count
        
    total_count = property(_gettotal_count)

    def _getrepository_selection(self):
        return self._repository_selection
        
    repository_selection = property(_getrepository_selection)


    

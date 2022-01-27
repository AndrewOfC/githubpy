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

class Git(object):


    #
    # post /repos/{owner}/{repo}/git/blobs
    #
    def GitCreateBlob(self, owner:str, repo:str,content:str, encoding:str='utf-8'):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/git#create-a-blob
        /repos/{owner}/{repo}/git/blobs
        
        arguments:
        owner -- 
        repo -- 
        content -- The new blob's content.
        encoding -- The encoding used for `content`. Currently, `"utf-8"` and `"base64"` are supported.
        

        """
    
        data = {
        'content': content,
        'encoding': encoding,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/git/blobs", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return ShortBlob(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 409:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/git/commits
    #
    def GitCreateCommit(self, owner:str, repo:str,tree:str, message:str, parents:list=[], author:dict=None, committer:dict=None, signature:str=None):
        """Creates a new Git [commit object](https://git-scm.com/book/en/v1/Git-Internals-Git-Objects#Commit-Objects).

**Signature verification object**

The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:

| Name | Type | Description |
| ---- | ---- | ----------- |
| `verified` | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified. |
| `reason` | `string` | The reason for verified value. Possible values and their meanings are enumerated in table below. |
| `signature` | `string` | The signature that was extracted from the commit. |
| `payload` | `string` | The value that was signed. |

These are the possible values for `reason` in the `verification` object:

| Value | Description |
| ----- | ----------- |
| `expired_key` | The key that made the signature is expired. |
| `not_signing_key` | The "signing" flag is not among the usage flags in the GPG key that made the signature. |
| `gpgverify_error` | There was an error communicating with the signature verification service. |
| `gpgverify_unavailable` | The signature verification service is currently unavailable. |
| `unsigned` | The object does not include a signature. |
| `unknown_signature_type` | A non-PGP signature was found in the commit. |
| `no_user` | No user was associated with the `committer` email address in the commit. |
| `unverified_email` | The `committer` email address in the commit was associated with a user, but the email address is not verified on her/his account. |
| `bad_email` | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature. |
| `unknown_key` | The key that made the signature has not been registered with any user's account. |
| `malformed_signature` | There was an error parsing the signature. |
| `invalid` | The signature could not be cryptographically verified using the key whose key-id was found in the signature. |
| `valid` | None of the above errors applied, so the signature is considered to be verified. |
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/git#create-a-commit
        /repos/{owner}/{repo}/git/commits
        
        arguments:
        owner -- 
        repo -- 
        tree -- The SHA of the tree object this commit points to
        message -- The commit message
        parents -- The SHAs of the commits that were the parents of this commit. If omitted or empty, the commit will be written as a root commit. For a single parent, an array of one SHA should be provided; for a merge commit, an array of more than one should be provided.
        author -- Information about the author of the commit. By default, the `author` will be the authenticated user and the current date. See the `author` and `committer` object below for details.
        committer -- Information about the person who is making the commit. By default, `committer` will use the information set in `author`. See the `author` and `committer` object below for details.
        signature -- The [PGP signature](https://en.wikipedia.org/wiki/Pretty_Good_Privacy) of the commit. GitHub adds the signature to the `gpgsig` header of the created commit. For a commit signature to be verifiable by Git or GitHub, it must be an ASCII-armored detached PGP signature over the string commit as it would be written to the object database. To pass a `signature` parameter, you need to first manually create a valid PGP signature, which can be complicated. You may find it easier to [use the command line](https://git-scm.com/book/id/v2/Git-Tools-Signing-Your-Work) to create signed commits.
        

        """
    
        data = {
        'tree': tree,
        'message': message,
        'parents': parents,
        'author': author,
        'committer': committer,
        'signature': signature,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/git/commits", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return GitCommit(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/git/refs
    #
    def GitCreateRef(self, owner:str, repo:str,sha:str, ref:str, key:str=None):
        """Creates a reference for your repository. You are unable to create new references for empty repositories, even if the commit SHA-1 hash used exists. Empty repositories are repositories without branches.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/git#create-a-reference
        /repos/{owner}/{repo}/git/refs
        
        arguments:
        owner -- 
        repo -- 
        sha -- The SHA1 value for this reference.
        ref -- The name of the fully qualified reference (ie: `refs/heads/master`). If it doesn't start with 'refs' and have at least two slashes, it will be rejected.
        key -- 
        

        """
    
        data = {
        'sha': sha,
        'ref': ref,
        'key': key,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/git/refs", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return GitReference(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/git/tags
    #
    def GitCreateTag(self, owner:str, repo:str,type:str, object:str, message:str, tag:str, tagger:dict=None):
        """Note that creating a tag object does not create the reference that makes a tag in Git. If you want to create an annotated tag in Git, you have to do this call to create the tag object, and then [create](https://docs.github.com/enterprise-server@3.3/rest/reference/git#create-a-reference) the `refs/tags/[tag]` reference. If you want to create a lightweight tag, you only have to [create](https://docs.github.com/enterprise-server@3.3/rest/reference/git#create-a-reference) the tag reference - this call would be unnecessary.

**Signature verification object**

The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:

| Name | Type | Description |
| ---- | ---- | ----------- |
| `verified` | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified. |
| `reason` | `string` | The reason for verified value. Possible values and their meanings are enumerated in table below. |
| `signature` | `string` | The signature that was extracted from the commit. |
| `payload` | `string` | The value that was signed. |

These are the possible values for `reason` in the `verification` object:

| Value | Description |
| ----- | ----------- |
| `expired_key` | The key that made the signature is expired. |
| `not_signing_key` | The "signing" flag is not among the usage flags in the GPG key that made the signature. |
| `gpgverify_error` | There was an error communicating with the signature verification service. |
| `gpgverify_unavailable` | The signature verification service is currently unavailable. |
| `unsigned` | The object does not include a signature. |
| `unknown_signature_type` | A non-PGP signature was found in the commit. |
| `no_user` | No user was associated with the `committer` email address in the commit. |
| `unverified_email` | The `committer` email address in the commit was associated with a user, but the email address is not verified on her/his account. |
| `bad_email` | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature. |
| `unknown_key` | The key that made the signature has not been registered with any user's account. |
| `malformed_signature` | There was an error parsing the signature. |
| `invalid` | The signature could not be cryptographically verified using the key whose key-id was found in the signature. |
| `valid` | None of the above errors applied, so the signature is considered to be verified. |
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/git#create-a-tag-object
        /repos/{owner}/{repo}/git/tags
        
        arguments:
        owner -- 
        repo -- 
        type -- The type of the object we're tagging. Normally this is a `commit` but it can also be a `tree` or a `blob`.
        object -- The SHA of the git object this is tagging.
        message -- The tag message.
        tag -- The tag's name. This is typically a version (e.g., "v0.0.1").
        tagger -- An object with information about the individual creating the tag.
        

        """
    
        data = {
        'type': type,
        'object': object,
        'message': message,
        'tag': tag,
        'tagger': tagger,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/git/tags", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return GitTag(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/git/trees
    #
    def GitCreateTree(self, owner:str, repo:str,tree:list, base_tree:str=None):
        """The tree creation API accepts nested entries. If you specify both a tree and a nested path modifying that tree, this endpoint will overwrite the contents of the tree with the new path contents, and create a new tree structure.

If you use this endpoint to add, delete, or modify the file contents in a tree, you will need to commit the tree and then update a branch to point to the commit. For more information see "[Create a commit](https://docs.github.com/enterprise-server@3.3/rest/reference/git#create-a-commit)" and "[Update a reference](https://docs.github.com/enterprise-server@3.3/rest/reference/git#update-a-reference)."
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/git#create-a-tree
        /repos/{owner}/{repo}/git/trees
        
        arguments:
        owner -- 
        repo -- 
        tree -- Objects (of `path`, `mode`, `type`, and `sha`) specifying a tree structure.
        base_tree -- The SHA1 of an existing Git tree object which will be used as the base for the new tree. If provided, a new Git tree object will be created from entries in the Git tree object pointed to by `base_tree` and entries defined in the `tree` parameter. Entries defined in the `tree` parameter will overwrite items from `base_tree` with the same `path`. If you're creating new changes on a branch, then normally you'd set `base_tree` to the SHA1 of the Git tree object of the current latest commit on the branch you're working on.
If not provided, GitHub will create a new Git tree object from only the entries defined in the `tree` parameter. If you create a new commit pointing to such a tree, then all files which were a part of the parent commit's tree and were not defined in the `tree` parameter will be listed as deleted by the new commit.

        

        """
    
        data = {
        'tree': tree,
        'base_tree': base_tree,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/git/trees", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return GitTree(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/git/refs/{ref}
    #
    def GitDeleteRef(self, owner:str, repo:str, ref:str):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/git#delete-a-reference
        /repos/{owner}/{repo}/git/refs/{ref}
        
        arguments:
        owner -- 
        repo -- 
        ref -- ref parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/git/refs/{ref}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/git/blobs/{file_sha}
    #
    def GitGetBlob(self, owner:str, repo:str, file_sha:str):
        """The `content` in the response will always be Base64 encoded.

_Note_: This API supports blobs up to 100 megabytes in size.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/git#get-a-blob
        /repos/{owner}/{repo}/git/blobs/{file_sha}
        
        arguments:
        owner -- 
        repo -- 
        file_sha -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/git/blobs/{file_sha}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return Blob(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/git/commits/{commit_sha}
    #
    def GitGetCommit(self, owner:str, repo:str, commit_sha:str):
        """Gets a Git [commit object](https://git-scm.com/book/en/v1/Git-Internals-Git-Objects#Commit-Objects).

**Signature verification object**

The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:

| Name | Type | Description |
| ---- | ---- | ----------- |
| `verified` | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified. |
| `reason` | `string` | The reason for verified value. Possible values and their meanings are enumerated in table below. |
| `signature` | `string` | The signature that was extracted from the commit. |
| `payload` | `string` | The value that was signed. |

These are the possible values for `reason` in the `verification` object:

| Value | Description |
| ----- | ----------- |
| `expired_key` | The key that made the signature is expired. |
| `not_signing_key` | The "signing" flag is not among the usage flags in the GPG key that made the signature. |
| `gpgverify_error` | There was an error communicating with the signature verification service. |
| `gpgverify_unavailable` | The signature verification service is currently unavailable. |
| `unsigned` | The object does not include a signature. |
| `unknown_signature_type` | A non-PGP signature was found in the commit. |
| `no_user` | No user was associated with the `committer` email address in the commit. |
| `unverified_email` | The `committer` email address in the commit was associated with a user, but the email address is not verified on her/his account. |
| `bad_email` | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature. |
| `unknown_key` | The key that made the signature has not been registered with any user's account. |
| `malformed_signature` | There was an error parsing the signature. |
| `invalid` | The signature could not be cryptographically verified using the key whose key-id was found in the signature. |
| `valid` | None of the above errors applied, so the signature is considered to be verified. |
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/git#get-a-commit
        /repos/{owner}/{repo}/git/commits/{commit_sha}
        
        arguments:
        owner -- 
        repo -- 
        commit_sha -- commit_sha parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/git/commits/{commit_sha}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return GitCommit(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/git/ref/{ref}
    #
    def GitGetRef(self, owner:str, repo:str, ref:str):
        """Returns a single reference from your Git database. The `:ref` in the URL must be formatted as `heads/<branch name>` for branches and `tags/<tag name>` for tags. If the `:ref` doesn't match an existing ref, a `404` is returned.

**Note:** You need to explicitly [request a pull request](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#get-a-pull-request) to trigger a test merge commit, which checks the mergeability of pull requests. For more information, see "[Checking mergeability of pull requests](https://docs.github.com/enterprise-server@3.3/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)".
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/git#get-a-reference
        /repos/{owner}/{repo}/git/ref/{ref}
        
        arguments:
        owner -- 
        repo -- 
        ref -- ref parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/git/ref/{ref}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return GitReference(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/git/tags/{tag_sha}
    #
    def GitGetTag(self, owner:str, repo:str, tag_sha:str):
        """**Signature verification object**

The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:

| Name | Type | Description |
| ---- | ---- | ----------- |
| `verified` | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified. |
| `reason` | `string` | The reason for verified value. Possible values and their meanings are enumerated in table below. |
| `signature` | `string` | The signature that was extracted from the commit. |
| `payload` | `string` | The value that was signed. |

These are the possible values for `reason` in the `verification` object:

| Value | Description |
| ----- | ----------- |
| `expired_key` | The key that made the signature is expired. |
| `not_signing_key` | The "signing" flag is not among the usage flags in the GPG key that made the signature. |
| `gpgverify_error` | There was an error communicating with the signature verification service. |
| `gpgverify_unavailable` | The signature verification service is currently unavailable. |
| `unsigned` | The object does not include a signature. |
| `unknown_signature_type` | A non-PGP signature was found in the commit. |
| `no_user` | No user was associated with the `committer` email address in the commit. |
| `unverified_email` | The `committer` email address in the commit was associated with a user, but the email address is not verified on her/his account. |
| `bad_email` | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature. |
| `unknown_key` | The key that made the signature has not been registered with any user's account. |
| `malformed_signature` | There was an error parsing the signature. |
| `invalid` | The signature could not be cryptographically verified using the key whose key-id was found in the signature. |
| `valid` | None of the above errors applied, so the signature is considered to be verified. |
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/git#get-a-tag
        /repos/{owner}/{repo}/git/tags/{tag_sha}
        
        arguments:
        owner -- 
        repo -- 
        tag_sha -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/git/tags/{tag_sha}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return GitTag(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/git/trees/{tree_sha}
    #
    def GitGetTree(self, owner:str, repo:str, tree_sha:str,recursive:str=None):
        """Returns a single tree using the SHA1 value for that tree.

If `truncated` is `true` in the response then the number of items in the `tree` array exceeded our maximum limit. If you need to fetch more items, use the non-recursive method of fetching trees, and fetch one sub-tree at a time.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/git#get-a-tree
        /repos/{owner}/{repo}/git/trees/{tree_sha}
        
        arguments:
        owner -- 
        repo -- 
        tree_sha -- 
        recursive -- Setting this parameter to any value returns the objects or subtrees referenced by the tree specified in `:tree_sha`. For example, setting `recursive` to any of the following will enable returning objects or subtrees: `0`, `1`, `"true"`, and `"false"`. Omit this parameter to prevent recursively returning objects or subtrees.
        
        """
        
        data = {}
        if recursive is not None:
            data['recursive'] = recursive
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/git/trees/{tree_sha}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return GitTree(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/git/matching-refs/{ref}
    #
    def GitListMatchingRefs(self, owner:str, repo:str, ref:str,per_page=30, page=1):
        """Returns an array of references from your Git database that match the supplied name. The `:ref` in the URL must be formatted as `heads/<branch name>` for branches and `tags/<tag name>` for tags. If the `:ref` doesn't exist in the repository, but existing refs start with `:ref`, they will be returned as an array.

When you use this endpoint without providing a `:ref`, it will return an array of all the references from your Git database, including notes and stashes if they exist on the server. Anything in the namespace is returned, not just `heads` and `tags`.

**Note:** You need to explicitly [request a pull request](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#get-a-pull-request) to trigger a test merge commit, which checks the mergeability of pull requests. For more information, see "[Checking mergeability of pull requests](https://docs.github.com/enterprise-server@3.3/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)".

If you request matching references for a branch named `feature` but the branch `feature` doesn't exist, the response can still include other matching head refs that start with the word `feature`, such as `featureA` and `featureB`.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/git#list-matching-references
        /repos/{owner}/{repo}/git/matching-refs/{ref}
        
        arguments:
        owner -- 
        repo -- 
        ref -- ref parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/git/matching-refs/{ref}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and GitReference(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}/git/refs/{ref}
    #
    def GitUpdateRef(self, owner:str, repo:str, ref:str,sha:str, force:bool=False):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/git#update-a-reference
        /repos/{owner}/{repo}/git/refs/{ref}
        
        arguments:
        owner -- 
        repo -- 
        ref -- ref parameter
        sha -- The SHA1 value to set this reference to
        force -- Indicates whether to force the update or to make sure the update is a fast-forward update. Leaving this out or setting it to `false` will make sure you're not overwriting work.
        

        """
    
        data = {
        'sha': sha,
        'force': force,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/git/refs/{ref}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return GitReference(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
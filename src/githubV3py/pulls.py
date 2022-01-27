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

class Pulls(object):


    #
    # get /repos/{owner}/{repo}/pulls/{pull_number}/merge
    #
    def PullsCheckIfMerged(self, owner:str, repo:str, pull_number:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#check-if-a-pull-request-has-been-merged
        /repos/{owner}/{repo}/pulls/{pull_number}/merge
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/merge", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return HttpResponse(r)
            
        
        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/pulls
    #
    def PullsCreate(self, owner:str, repo:str,base:str, head:str, title:str=None, body:str=None, maintainer_can_modify:bool=None, draft:bool=None, issue:int=None):
        """Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team and GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

To open or update a pull request in a public repository, you must have write access to the head or the source branch. For organization-owned repositories, you must be a member of the organization that owns the repository to open or update a pull request.

You can create a new pull request.

This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/guides/best-practices-for-integrators#dealing-with-rate-limits)" for details.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#create-a-pull-request
        /repos/{owner}/{repo}/pulls
        
        arguments:
        owner -- 
        repo -- 
        base -- The name of the branch you want the changes pulled into. This should be an existing branch on the current repository. You cannot submit a pull request to one repository that requests a merge to a base of another repository.
        head -- The name of the branch where your changes are implemented. For cross-repository pull requests in the same network, namespace `head` with a user like this: `username:branch`.
        title -- The title of the new pull request.
        body -- The contents of the pull request.
        maintainer_can_modify -- Indicates whether [maintainers can modify](https://help.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/) the pull request.
        draft -- Indicates whether the pull request is a draft. See "[Draft Pull Requests](https://help.github.com/en/articles/about-pull-requests#draft-pull-requests)" in the GitHub Help documentation to learn more.
        issue -- 
        

        """
    
        data = {
        'base': base,
        'head': head,
        'title': title,
        'body': body,
        'maintainer_can_modify': maintainer_can_modify,
        'draft': draft,
        'issue': issue,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/pulls", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return PullRequest(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies
    #
    def PullsCreateReplyForReviewComment(self, owner:str, repo:str, pull_number:int, comment_id:int,body:str):
        """Creates a reply to a review comment for a pull request. For the `comment_id`, provide the ID of the review comment you are replying to. This must be the ID of a _top-level review comment_, not a reply to that comment. Replies to replies are not supported.

This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#create-a-reply-for-a-review-comment
        /repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        comment_id -- comment_id parameter
        body -- The text of the review comment.
        

        """
    
        data = {
        'body': body,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return PullRequestReviewComment(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/pulls/{pull_number}/reviews
    #
    def PullsCreateReview(self, owner:str, repo:str, pull_number:int,commit_id:str=None, body:str=None, event:str=None, comments:list=[]):
        """This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.

Pull request reviews created in the `PENDING` state do not include the `submitted_at` property in the response.

**Note:** To comment on a specific line in a file, you need to first determine the _position_ of that line in the diff. The GitHub REST API v3 offers the `application/vnd.github.v3.diff` [media type](https://docs.github.com/enterprise-server@3.3/rest/overview/media-types#commits-commit-comparison-and-pull-requests). To see a pull request diff, add this media type to the `Accept` header of a call to the [single pull request](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#get-a-pull-request) endpoint.

The `position` value equals the number of lines down from the first "@@" hunk header in the file you want to add a comment. The line just below the "@@" line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#create-a-review-for-a-pull-request
        /repos/{owner}/{repo}/pulls/{pull_number}/reviews
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        commit_id -- The SHA of the commit that needs a review. Not using the latest commit SHA may render your review comment outdated if a subsequent commit modifies the line you specify as the `position`. Defaults to the most recent commit in the pull request when you do not specify a value.
        body -- **Required** when using `REQUEST_CHANGES` or `COMMENT` for the `event` parameter. The body text of the pull request review.
        event -- The review action you want to perform. The review actions include: `APPROVE`, `REQUEST_CHANGES`, or `COMMENT`. By leaving this blank, you set the review action state to `PENDING`, which means you will need to [submit the pull request review](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#submit-a-review-for-a-pull-request) when you are ready.
        comments -- Use the following table to specify the location, destination, and contents of the draft review comment.
        

        """
    
        data = {
        'commit_id': commit_id,
        'body': body,
        'event': event,
        'comments': comments,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/reviews", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return PullRequestReview(**r.json())
            
        if r.status_code == 422:
            return ValidationErrorSimple(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/pulls/{pull_number}/comments
    #
    def PullsCreateReviewComment(self, owner:str, repo:str, pull_number:int,body:str, commit_id:str=None, path:str=None, position:int=None, side:str=None, line:int=None, start_line:int=None, start_side:str=None, in_reply_to:int=None):
        """
Creates a review comment in the pull request diff. To add a regular comment to a pull request timeline, see "[Create an issue comment](https://docs.github.com/enterprise-server@3.3/rest/reference/issues#create-an-issue-comment)." We recommend creating a review comment using `line`, `side`, and optionally `start_line` and `start_side` if your comment applies to more than one line in the pull request diff.

You can still create a review comment using the `position` parameter. When you use `position`, the `line`, `side`, `start_line`, and `start_side` parameters are not required.

**Note:** The position value equals the number of lines down from the first "@@" hunk header in the file you want to add a comment. The line just below the "@@" line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.

This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#create-a-review-comment-for-a-pull-request
        /repos/{owner}/{repo}/pulls/{pull_number}/comments
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        body -- The text of the review comment.
        commit_id -- The SHA of the commit needing a comment. Not using the latest commit SHA may render your comment outdated if a subsequent commit modifies the line you specify as the `position`.
        path -- The relative path to the file that necessitates a comment.
        position -- **Required without `comfort-fade` preview unless using `in_reply_to`**. The position in the diff where you want to add a review comment. Note this value is not the same as the line number in the file. For help finding the position value, read the note above.
        side -- **Required with `comfort-fade` preview unless using `in_reply_to`**. In a split diff view, the side of the diff that the pull request's changes appear on. Can be `LEFT` or `RIGHT`. Use `LEFT` for deletions that appear in red. Use `RIGHT` for additions that appear in green or unchanged lines that appear in white and are shown for context. For a multi-line comment, side represents whether the last line of the comment range is a deletion or addition. For more information, see "[Diff view options](https://help.github.com/en/articles/about-comparing-branches-in-pull-requests#diff-view-options)" in the GitHub Help documentation.
        line -- **Required with `comfort-fade` preview unless using `in_reply_to`**. The line of the blob in the pull request diff that the comment applies to. For a multi-line comment, the last line of the range that your comment applies to.
        start_line -- **Required when using multi-line comments unless using `in_reply_to`**. To create multi-line comments, you must use the `comfort-fade` preview header. The `start_line` is the first line in the pull request diff that your multi-line comment applies to. To learn more about multi-line comments, see "[Commenting on a pull request](https://help.github.com/en/articles/commenting-on-a-pull-request#adding-line-comments-to-a-pull-request)" in the GitHub Help documentation.
        start_side -- **Required when using multi-line comments unless using `in_reply_to`**. To create multi-line comments, you must use the `comfort-fade` preview header. The `start_side` is the starting side of the diff that the comment applies to. Can be `LEFT` or `RIGHT`. To learn more about multi-line comments, see "[Commenting on a pull request](https://help.github.com/en/articles/commenting-on-a-pull-request#adding-line-comments-to-a-pull-request)" in the GitHub Help documentation. See `side` in this table for additional context.
        in_reply_to -- The ID of the review comment to reply to. To find the ID of a review comment with ["List review comments on a pull request"](#list-review-comments-on-a-pull-request). When specified, all parameters other than `body` in the request body are ignored.
        

        """
    
        data = {
        'body': body,
        'commit_id': commit_id,
        'path': path,
        'position': position,
        'side': side,
        'line': line,
        'start_line': start_line,
        'start_side': start_side,
        'in_reply_to': in_reply_to,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/comments", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return PullRequestReviewComment(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}
    #
    def PullsDeletePendingReview(self, owner:str, repo:str, pull_number:int, review_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#delete-a-pending-review-for-a-pull-request
        /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        review_id -- review_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return PullRequestReview(**r.json())
            
        if r.status_code == 422:
            return ValidationErrorSimple(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/pulls/comments/{comment_id}
    #
    def PullsDeleteReviewComment(self, owner:str, repo:str, comment_id:int):
        """Deletes a review comment.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#delete-a-review-comment-for-a-pull-request
        /repos/{owner}/{repo}/pulls/comments/{comment_id}
        
        arguments:
        owner -- 
        repo -- 
        comment_id -- comment_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/pulls/comments/{comment_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 204:
            return HttpResponse(r)
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals
    #
    def PullsDismissReview(self, owner:str, repo:str, pull_number:int, review_id:int,message:str, event:str=None):
        """**Note:** To dismiss a pull request review on a [protected branch](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#branches), you must be a repository administrator or be included in the list of people or teams who can dismiss pull request reviews.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#dismiss-a-review-for-a-pull-request
        /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        review_id -- review_id parameter
        message -- The message for the pull request review dismissal
        event -- 
        

        """
    
        data = {
        'message': message,
        'event': event,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return PullRequestReview(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationErrorSimple(**r.json())
            

        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/pulls/{pull_number}
    #
    def PullsGet(self, owner:str, repo:str, pull_number:int):
        """Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team and GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Lists details of a pull request by providing its number.

When you get, [create](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls/#create-a-pull-request), or [edit](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#update-a-pull-request) a pull request, GitHub Enterprise Server creates a merge commit to test whether the pull request can be automatically merged into the base branch. This test commit is not added to the base branch or the head branch. You can review the status of the test commit using the `mergeable` key. For more information, see "[Checking mergeability of pull requests](https://docs.github.com/enterprise-server@3.3/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)".

The value of the `mergeable` attribute can be `true`, `false`, or `null`. If the value is `null`, then GitHub Enterprise Server has started a background job to compute the mergeability. After giving the job time to complete, resubmit the request. When the job finishes, you will see a non-`null` value for the `mergeable` attribute in the response. If `mergeable` is `true`, then `merge_commit_sha` will be the SHA of the _test_ merge commit.

The value of the `merge_commit_sha` attribute changes depending on the state of the pull request. Before merging a pull request, the `merge_commit_sha` attribute holds the SHA of the _test_ merge commit. After merging a pull request, the `merge_commit_sha` attribute changes depending on how you merged the pull request:

*   If merged as a [merge commit](https://help.github.com/articles/about-merge-methods-on-github/), `merge_commit_sha` represents the SHA of the merge commit.
*   If merged via a [squash](https://help.github.com/articles/about-merge-methods-on-github/#squashing-your-merge-commits), `merge_commit_sha` represents the SHA of the squashed commit on the base branch.
*   If [rebased](https://help.github.com/articles/about-merge-methods-on-github/#rebasing-and-merging-your-commits), `merge_commit_sha` represents the commit that the base branch was updated to.

Pass the appropriate [media type](https://docs.github.com/enterprise-server@3.3/rest/overview/media-types/#commits-commit-comparison-and-pull-requests) to fetch diff and patch formats.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#get-a-pull-request
        /repos/{owner}/{repo}/pulls/{pull_number}
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return PullRequest(**r.json())
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 500:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}
    #
    def PullsGetReview(self, owner:str, repo:str, pull_number:int, review_id:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#get-a-review-for-a-pull-request
        /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        review_id -- review_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return PullRequestReview(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/pulls/comments/{comment_id}
    #
    def PullsGetReviewComment(self, owner:str, repo:str, comment_id:int):
        """Provides details for a review comment.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#get-a-review-comment-for-a-pull-request
        /repos/{owner}/{repo}/pulls/comments/{comment_id}
        
        arguments:
        owner -- 
        repo -- 
        comment_id -- comment_id parameter
        
        """
        
        data = {}
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/pulls/comments/{comment_id}", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return PullRequestReviewComment(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/pulls
    #
    def PullsList(self, owner:str, repo:str,state='open', head:str=None, base:str=None, sort='created', direction='desc', per_page=30, page=1):
        """Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team and GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#list-pull-requests
        /repos/{owner}/{repo}/pulls
        
        arguments:
        owner -- 
        repo -- 
        state -- Indicates the state of the issues to return. Can be either `open`, `closed`, or `all`.
        head -- Filter pulls by head user or head organization and branch name in the format of `user:ref-name` or `organization:ref-name`. For example: `github:new-script-format` or `octocat:test-branch`.
        base -- Filter pulls by base branch name. Example: `gh-pages`.
        sort -- What to sort results by. Can be either `created`, `updated`, `popularity` (comment count) or `long-running` (age, filtering by pulls updated in the last month).
        direction -- One of `asc` (ascending) or `desc` (descending).
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if state is not None:
            data['state'] = state
        if head is not None:
            data['head'] = head
        if base is not None:
            data['base'] = base
        if sort is not None:
            data['sort'] = sort
        if direction is not None:
            data['direction'] = direction
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/pulls", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and PullRequestSimple(**entry) for entry in r.json() ]
            
        if r.status_code == 304:
            return NotModified(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/comments
    #
    def PullsListCommentsForReview(self, owner:str, repo:str, pull_number:int, review_id:int,per_page=30, page=1):
        """List comments for a specific pull request review.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#list-comments-for-a-pull-request-review
        /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/comments
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        review_id -- review_id parameter
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/comments", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and LegacyReviewComment(**entry) for entry in r.json() ]
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/pulls/{pull_number}/commits
    #
    def PullsListCommits(self, owner:str, repo:str, pull_number:int,per_page=30, page=1):
        """Lists a maximum of 250 commits for a pull request. To receive a complete commit list for pull requests with more than 250 commits, use the [List commits](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-commits) endpoint.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#list-commits-on-a-pull-request
        /repos/{owner}/{repo}/pulls/{pull_number}/commits
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/commits", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and Commit(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/pulls/{pull_number}/files
    #
    def PullsListFiles(self, owner:str, repo:str, pull_number:int,per_page=30, page=1):
        """**Note:** Responses include a maximum of 3000 files. The paginated response returns 30 files per page by default.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#list-pull-requests-files
        /repos/{owner}/{repo}/pulls/{pull_number}/files
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/files", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and DiffEntry(**entry) for entry in r.json() ]
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 500:
            return BasicError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers
    #
    def PullsListRequestedReviewers(self, owner:str, repo:str, pull_number:int,per_page=30, page=1):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#list-requested-reviewers-for-a-pull-request
        /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return PullRequestReviewRequest(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/pulls/{pull_number}/comments
    #
    def PullsListReviewComments(self, owner:str, repo:str, pull_number:int,sort='created', direction='desc', since:datetime=None, per_page=30, page=1):
        """Lists all review comments for a pull request. By default, review comments are in ascending order by ID.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#list-review-comments-on-a-pull-request
        /repos/{owner}/{repo}/pulls/{pull_number}/comments
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
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
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/comments", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and PullRequestReviewComment(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/pulls/comments
    #
    def PullsListReviewCommentsForRepo(self, owner:str, repo:str,sort=None, direction='desc', since:datetime=None, per_page=30, page=1):
        """Lists review comments for all pull requests in a repository. By default, review comments are in ascending order by ID.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#list-review-comments-in-a-repository
        /repos/{owner}/{repo}/pulls/comments
        
        arguments:
        owner -- 
        repo -- 
        sort -- 
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
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/pulls/comments", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and PullRequestReviewComment(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # get /repos/{owner}/{repo}/pulls/{pull_number}/reviews
    #
    def PullsListReviews(self, owner:str, repo:str, pull_number:int,per_page=30, page=1):
        """The list of reviews returns in chronological order.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#list-reviews-for-a-pull-request
        /repos/{owner}/{repo}/pulls/{pull_number}/reviews
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        per_page -- Results per page (max 100)
        page -- Page number of the results to fetch.
        
        """
        
        data = {}
        if per_page is not None:
            data['per_page'] = per_page
        if page is not None:
            data['page'] = page
        
        
        r = self._session.get(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/reviews", 
                           params=data,
                           **self._requests_kwargs())
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return [ entry and PullRequestReview(**entry) for entry in r.json() ]
            
        
        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/pulls/{pull_number}/merge
    #
    def PullsMerge(self, owner:str, repo:str, pull_number:int,commit_title:str=None, commit_message:str=None, sha:str=None, merge_method:str=None):
        """This endpoint triggers [notifications](https://docs.github.com/enterprise-server@3.3/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#merge-a-pull-request
        /repos/{owner}/{repo}/pulls/{pull_number}/merge
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        commit_title -- Title for the automatic commit message.
        commit_message -- Extra detail to append to automatic commit message.
        sha -- SHA that pull request head must match to allow merge.
        merge_method -- Merge method to use. Possible values are `merge`, `squash` or `rebase`. Default is `merge`.
        

        """
    
        data = {
        'commit_title': commit_title,
        'commit_message': commit_message,
        'sha': sha,
        'merge_method': merge_method,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/merge", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return PullRequestMergeResult(**r.json())
            
        if r.status_code == 405:
            return PullsMerge405(**r.json())
            
        if r.status_code == 409:
            return PullsMerge409(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # delete /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers
    #
    def PullsRemoveRequestedReviewers(self, owner:str, repo:str, pull_number:int):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#remove-requested-reviewers-from-a-pull-request
        /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        
        """
        
        data = {}
        
        
        r = self._session.delete(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers", 
                           params=data,
                           **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
    
        
        if r.status_code == 200:
            return PullRequestSimple(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        
        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers
    #
    def PullsRequestReviewers(self, owner:str, repo:str, pull_number:int,reviewers:list=[], team_reviewers:list=[]):
        """This endpoint triggers [notifications](https://docs.github.com/enterprise-server@3.3/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#request-reviewers-for-a-pull-request
        /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        reviewers -- An array of user `login`s that will be requested.
        team_reviewers -- An array of team `slug`s that will be requested.
        

        """
    
        data = {
        'reviewers': reviewers,
        'team_reviewers': team_reviewers,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 201:
            return PullRequestSimple(**r.json())
            
        if r.status_code == 422:
            return HttpResponse(r)
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events
    #
    def PullsSubmitReview(self, owner:str, repo:str, pull_number:int, review_id:int,event:str, body:str=None):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#submit-a-review-for-a-pull-request
        /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        review_id -- review_id parameter
        event -- The review action you want to perform. The review actions include: `APPROVE`, `REQUEST_CHANGES`, or `COMMENT`. When you leave this blank, the API returns _HTTP 422 (Unrecognizable entity)_ and sets the review action state to `PENDING`, which means you will need to re-submit the pull request review using a review action.
        body -- The body text of the pull request review
        

        """
    
        data = {
        'event': event,
        'body': body,
        
        }
        

        
        r = self._session.post(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return PullRequestReview(**r.json())
            
        if r.status_code == 404:
            return BasicError(**r.json())
            
        if r.status_code == 422:
            return ValidationErrorSimple(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}/pulls/{pull_number}
    #
    def PullsUpdate(self, owner:str, repo:str, pull_number:int,title:str=None, body:str=None, state:str=None, base:str=None, maintainer_can_modify:bool=None):
        """Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team and GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

To open or update a pull request in a public repository, you must have write access to the head or the source branch. For organization-owned repositories, you must be a member of the organization that owns the repository to open or update a pull request.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls/#update-a-pull-request
        /repos/{owner}/{repo}/pulls/{pull_number}
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        title -- The title of the pull request.
        body -- The contents of the pull request.
        state -- State of this Pull Request. Either `open` or `closed`.
        base -- The name of the branch you want your changes pulled into. This should be an existing branch on the current repository. You cannot update the base branch on a pull request to point to another repository.
        maintainer_can_modify -- Indicates whether [maintainers can modify](https://help.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/) the pull request.
        

        """
    
        data = {
        'title': title,
        'body': body,
        'state': state,
        'base': base,
        'maintainer_can_modify': maintainer_can_modify,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return PullRequest(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/pulls/{pull_number}/update-branch
    #
    def PullsUpdateBranch(self, owner:str, repo:str, pull_number:int,expected_head_sha:str=None):
        """Updates the pull request branch with the latest upstream changes by merging HEAD from the base branch into the pull request branch.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#update-a-pull-request-branch
        /repos/{owner}/{repo}/pulls/{pull_number}/update-branch
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        expected_head_sha -- The expected SHA of the pull request's HEAD ref. This is the most recent commit on the pull request's branch. If the expected SHA does not match the pull request's HEAD, you will receive a `422 Unprocessable Entity` status. You can use the "[List commits](https://docs.github.com/enterprise-server@3.3/rest/reference/repos#list-commits)" endpoint to find the most recent commit SHA. Default: SHA of the pull request's current HEAD ref.
        

        """
    
        data = {
        'expected_head_sha': expected_head_sha,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/update-branch", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 202:
            return PullsUpdateBranch202(**r.json())
            
        if r.status_code == 422:
            return ValidationError(**r.json())
            
        if r.status_code == 403:
            return BasicError(**r.json())
            

        return UnexpectedResult(r)
    #
    # put /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}
    #
    def PullsUpdateReview(self, owner:str, repo:str, pull_number:int, review_id:int,body:str):
        """Update the review summary comment with new text.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#update-a-review-for-a-pull-request
        /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}
        
        arguments:
        owner -- 
        repo -- 
        pull_number -- 
        review_id -- review_id parameter
        body -- The body text of the pull request review.
        

        """
    
        data = {
        'body': body,
        
        }
        

        
        r = self._session.put(f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return PullRequestReview(**r.json())
            
        if r.status_code == 422:
            return ValidationErrorSimple(**r.json())
            

        return UnexpectedResult(r)
    #
    # patch /repos/{owner}/{repo}/pulls/comments/{comment_id}
    #
    def PullsUpdateReviewComment(self, owner:str, repo:str, comment_id:int,body:str):
        """Enables you to edit a review comment.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#update-a-review-comment-for-a-pull-request
        /repos/{owner}/{repo}/pulls/comments/{comment_id}
        
        arguments:
        owner -- 
        repo -- 
        comment_id -- comment_id parameter
        body -- The text of the reply to the review comment.
        

        """
    
        data = {
        'body': body,
        
        }
        

        
        r = self._session.patch(f"{self._url}/repos/{owner}/{repo}/pulls/comments/{comment_id}", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return PullRequestReviewComment(**r.json())
            

        return UnexpectedResult(r)
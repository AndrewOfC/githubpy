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

class Markdown(object):


    #
    # post /markdown
    #
    def MarkdownRender(self, text:str, mode:str='markdown', context:str=None):
        """
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/markdown#render-a-markdown-document
        /markdown
        
        arguments:
        text -- The Markdown text to render in HTML.
        mode -- The rendering mode. Can be either `markdown` or `gfm`.
        context -- The repository context to use when creating references in `gfm` mode.  For example, setting `context` to `octo-org/octo-repo` will change the text `#42` into an HTML link to issue 42 in the `octo-org/octo-repo` repository.
        

        """
    
        data = {
        'text': text,
        'mode': mode,
        'context': context,
        
        }
        

        
        r = self._session.post(f"{self._url}/markdown", 
                          json=data,
                          **self._requests_kwargs({'Content-Type':  'application/json'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return DataResponse(r.content)
            
        if r.status_code == 304:
            return NotModified(**r.json())
            

        return UnexpectedResult(r)
    #
    # post /markdown/raw
    #
    def MarkdownRenderRaw(self, text:str):
        """You must send Markdown as plain text (using a `Content-Type` header of `text/plain` or `text/x-markdown`) to this endpoint, rather than using JSON format. In raw mode, [GitHub Flavored Markdown](https://github.github.com/gfm/) is not supported and Markdown will be rendered in plain format like a README.md file. Markdown content must be 400 KB or less.
        
        https://docs.github.com/enterprise-server@3.3/rest/reference/markdown#render-a-markdown-document-in-raw-mode
        /markdown/raw
        
        arguments:
        text -- 
        

        """
    
        

        
        r = self._session.post(f"{self._url}/markdown/raw", 
                          data=text,
                          **self._requests_kwargs({'Content-Type':  'text/x-markdown'}))
        self._updateStats(r.headers)
                          
        
        if r.status_code == 200:
            return DataResponse(r.content)
            
        if r.status_code == 304:
            return NotModified(**r.json())
            

        return UnexpectedResult(r)
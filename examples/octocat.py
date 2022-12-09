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

import sys
import argparse

from githubV3py import *


def main():
    
    parser = argparse.ArgumentParser(description="Simple program to draw the 'Octocat' with ascii art")
    
    parser.add_argument('text', nargs='?', default="Hello World")
    parser.add_argument("-t", "--token", default='', help="Access Token from https://github.com/settings/tokens/new")
    parser.add_argument("-v", "--verbose", action='store_true', help="display remaining rate-limit")
    
    options = parser.parse_args()
    
    ghc = GitHubClient(token=options.token)
    response = ghc.MetaGetOctocat(options.text)
    if not response.ok:
        print(f"Bad response({response.status_code}): {response.message}", file=sys.stderr)
        sys.exit(2)

    ascii_art = response.data.decode('utf-8')
    
    print(ascii_art)
    
    if options.verbose:
        print(f"rate-limit remaining={ghc.rateLimitRemaining}   reset: {ghc.rateLimitReset.strftime('%c')}")
    
    
if __name__ == '__main__':
    main()
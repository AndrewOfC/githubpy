
import sys
import argparse

from githubV3py import *


def main():
    
    parser = argparse.ArgumentParser(description="Simple program to draw the 'Octocat' with ascii art")
    
    parser.add_argument('text', nargs='?', default="Hello World")
    parser.add_argument("-t", "--token", default='', help="Github Access Token")
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
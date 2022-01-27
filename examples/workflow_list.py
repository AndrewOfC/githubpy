
from operator import attrgetter

from githubV3py import GitHubClient


def main():
    import argparse
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-t", "--token")
    parser.add_argument("-o", "--owner")
    parser.add_argument("-r", "--repo")
    parser.add_argument("-v", "--verbose", action='store_true')
    
    options = parser.parse_args()
    
    ghc = GitHubClient(token=options.token)
    
    for run in GitHubClient.generate(ghc.ActionsListWorkflowRunsForRepo, options.owner, options.repo, extractor=attrgetter('workflow_runs')):
        print(f"{run.id} created: {run.created_at:%x %X}")
    
    if options.verbose:
        print(f"remaining {ghc.rateLimitRemaining}")
    
    return 

if __name__ == '__main__':
    main()
    
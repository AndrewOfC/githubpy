
import githubV3py

def main():
    import argparse
        
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-o", "--owner")
    parser.add_argument("-r", "--repo") 
    parser.add_argument("-t", "--token")
    parser.add_argument("-s", "--sha")

    options = parser.parse_args()
    

    ghc = githubV3py.GitHubClient(token=options.token)
    
    commits = ghc.SearchCommits(f"hash:{options.sha} merge:false")
    
    print(f"Commit {options.sha}:  {commits.items[0].commit.message}")
      
    return

if __name__ == '__main__':
    main()
        
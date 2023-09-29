#!/usr/bin/python3
"""
Python script that fetches and displays information about the latest 10 commits
from a GitHub repository.

Usage: ./100-github_commits.py <repository_name> <repository_owner>
"""

import sys
import requests

def fetch_github_commits(repo_name, repo_owner):
    # Construct the GitHub API URL for the commits of the specified repository
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"

    try:
        # Send a GET request to the GitHub API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            commits = response.json()
            
            # Display information for the latest 10 commits
            for commit in commits[:10]:
                sha = commit.get("sha")
                author_name = commit.get("commit").get("author").get("name")
                print(f"{sha}: {author_name}")
        else:
            print(f"Error: Unable to fetch commits. Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <repository_owner>")
        sys.exit(1)

    repo_name = sys.argv[1]
    repo_owner = sys.argv[2]

    fetch_github_commits(repo_name, repo_owner)


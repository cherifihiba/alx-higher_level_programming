#!/usr/bin/python3
"""
Module to retrieve the number of commits in a GitHub repository.
"""
import requests
import sys

def get_repo_commits(repo_name, owner_name):
    """
    Function to get the number of commits in a GitHub repository.

    Args:
        repo_name (str): The name of the repository.
        owner_name (str): The owner of the repository.

    Returns:
        int: The number of commits in the repository.
    """
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)
    commits = response.json()
    return len(commits)

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    print(get_repo_commits(repo_name, owner_name))

#!/usr/bin/python3
"""
Module to get GitHub user id using GitHub API
"""

import requests
import sys

def get_github_id(username: str, token: str) -> str:
    """
    Function to get GitHub user id using GitHub API

    Args:
        username (str): GitHub username
        token (str): GitHub personal access token

    Returns:
        str: GitHub user id
    """
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, auth=(username, token))
    data = response.json()
    return data.get('id')

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    print(get_github_id(username, token))

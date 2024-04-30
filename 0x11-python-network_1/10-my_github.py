#!/usr/bin/python3
"""
This script takes GitHub credentials (username and password) and uses the GitHub API
to display the user's id. It uses Basic Authentication with a personal access token
as the password to access user information (only read:user permission is needed).
"""

import sys
import sys

def get_github_id(username, password):
    """
    Get GitHub user id using GitHub API with Basic Authentication.

    Args:
        username (str): GitHub username.
        password (str): Personal access token.

    Returns:
        int: GitHub user id if successful, None otherwise.
    """
    url = 'https://api.github.com/user'
    try:
        response = requests.get(url, auth=(username, password))
        if response.status_code == 200:
            return response.json().get('id')
        else:
            return None
    except Exception as e:
        return None

if __name__ == "__main__":
    if len(sys.argv) == 3:
        username = sys.argv[1]
        password = sys.argv[2]
        github_id = get_github_id(username, password)
        print(github_id if github_id else "None")
    else:
        print("Usage: ./10-my_github.py <username> <password>")

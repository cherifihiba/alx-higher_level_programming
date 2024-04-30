#!/usr/bin/python3
"""
This script takes GitHub credentials (username and personal access token) and uses the GitHub API
to display the user's id.
"""

import sys
import requests

def get_github_id(username, password):
    """
    Get GitHub user ID using GitHub API with Basic Authentication.
    
    Args:
        username (str): GitHub username.
        password (str): Personal access token as password.
        
    Returns:
        int: GitHub user ID.
    """
    url = f"https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    user_data = response.json()
    return user_data.get('id')

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    github_id = get_github_id(username, password)
    print(github_id)

#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    payload = {'q': q}
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        json_response = response.json()
        if isinstance(json_response, dict) and json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        elif isinstance(json_response, dict) and not json_response:
            print("No result")
        else:
            print("Not a valid JSON")
    except ValueError:
        print("Not a valid JSON")

#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response
# Display only the body of a 200 status code response
response=$(curl -sL -w "%{http_code}" "$1" -o /dev/null)
status_code="${response: -3}"

if [ "$status_code" -eq 200 ]; then
    curl -sL "$1"
fi

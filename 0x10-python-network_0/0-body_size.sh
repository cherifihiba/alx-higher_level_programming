#!/bin/bash
# This script takes a URL as an argument, sends a request to that URL using curl,
# and displays the size of the response body in bytes.

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request to the provided URL and display the size of the response body
curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r'


#!/bin/bash
# This Bash script sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
file_content=$(cat "$2" 2>/dev/null)
if [ $? -eq 0 ]; then
    echo "$file_content" | jq empty 2>/dev/null
    if [ $? -eq 0 ]; then
        curl -sX POST -H "Content-Type: application/json" -d @"$2" $1
    else
        echo "Not a valid JSON"
        exit 1
    fi
else
    echo "Could not read file"
    exit 1
fi

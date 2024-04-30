#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument,
# with the contents of a file passed as the second argument
response=$(curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1")
echo "$response" | grep -q "Valid JSON" && echo "$response" || echo "Not a valid JSON"

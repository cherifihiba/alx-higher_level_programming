#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument,
# with the contents of a file passed as the second argument
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1" | grep -q "Valid JSON" && cat || echo "Not a valid JSON"

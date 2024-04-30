#!/bin/bash
# Sends a JSON POST request to a URL with file contents in the body

curl -sX POST "$1" -H "Content-Type: application/json" -d @"$2"

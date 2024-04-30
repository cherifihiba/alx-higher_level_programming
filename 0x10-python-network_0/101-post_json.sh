#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument,
# with the contents of a file passed as the second argument
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1" | awk '/Valid JSON/{p=1;next} p' | sed 's/Valid JSON//g'

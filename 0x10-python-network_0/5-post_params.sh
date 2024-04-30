#!/bin/bash
# This Bash script takes in a URL, sends a POST request with email and subject parameters, and displays the body of the response
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" $1

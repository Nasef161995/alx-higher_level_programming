#!/bin/bash
#Bash script takes in a URL, sends a request to that URL
curl -sI "$1" | grep -i "Allow" | awk -F ": " '{print $2}'


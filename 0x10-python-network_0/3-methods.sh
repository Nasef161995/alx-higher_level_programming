#!/bin/bash
#Bash script takes in a URL, sends a request to that URL
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-

#!/bin/bash
#Bash script takes in a URL, sends a request to that URL
curl -w "%{size_download}\n" -o /dev/null -s $1

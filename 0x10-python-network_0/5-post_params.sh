#!/bin/bash
#Bash script takes in a URL, sends a request to that URL
curl -sL -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

#!/usr/bin/python3

import re
import sys

# Get the command-line argument
arg = sys.argv[1]

# Match the pattern against the argument
match = re.match(r"[A-Za-z\s]+", arg)

if match:
    print("Pattern matched!")
else:
    print("Pattern not matched.")

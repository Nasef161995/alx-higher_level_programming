#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct

    except (TypeError, ValueError) as error:
        print("Exception:", error, file=sys.stderr)

    return result

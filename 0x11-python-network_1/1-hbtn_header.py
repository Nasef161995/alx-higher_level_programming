#!/usr/bin/python3
"""Python script that fetches webpage"""

if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as r:
        headers = r.headers
        id = headers.get("X-Request-Id")
        print(id)

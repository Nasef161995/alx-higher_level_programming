#!/usr/bin/python3
"""Python script that fetches webpage"""

if __name__ == "__main__":
    import urllib.request
    import sys
    from urllib.error import HTTPError
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as r:
            body = r.read().decode('utf-8')
            print(body)
    except HTTPError as error:
        print("Error code:", error.code)

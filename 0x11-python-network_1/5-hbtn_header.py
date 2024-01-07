#!/usr/bin/python3
"""Python script that fetches webpage"""

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    response = requests.get(url)
    headers = response.headers
    id = headers.get("X-Request-Id")
    print(id)

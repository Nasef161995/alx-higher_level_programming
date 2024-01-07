#!/usr/bin/python3
"""Python script that fetches webpage"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    email = sys.argv[2]
    url = sys.argv[1]
    value = {'email': email}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as r:
        body = r.read().decode('utf-8')
        print(body)

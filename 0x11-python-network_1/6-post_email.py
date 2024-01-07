#!/usr/bin/python3
"""Python script that fetches webpage"""

if __name__ == "__main__":
    import requests
    import sys
    email = sys.argv[2]
    url = sys.argv[1]
    data = {"email": email}
    response = requests.post(url, data)
    print(response.text)

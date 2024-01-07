#!/usr/bin/python3
"""Python script that fetches webpage"""

if __name__ == "__main__":
    import requests
    import sys
    from urllib.error import HTTPError
    url = sys.argv[1]
    try:
        response = requests.get(url)
        print(response.text)
    except HTTPError as error:
        print("Error code:", error.code)

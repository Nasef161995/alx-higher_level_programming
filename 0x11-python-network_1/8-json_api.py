#!/usr/bin/python3
"""Python script that fetches webpage"""

if __name__ == "__main__":
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    if sys.argv[1] == 0:
        q = ""
    else:
        q = sys.argv[1]
    data = {"q": q}
    response = requests.post(url, data)
    try:
        jason = response.jason()
        if jason:
            id = jason.get('id')
            name = jason.get('name')
            print("[{}] {}".format(id, name))
        else:
            print("No result")
    except valueError:
        print("Not a valid JSON")

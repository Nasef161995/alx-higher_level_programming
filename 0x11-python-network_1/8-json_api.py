#!/usr/bin/python3
"""Python script that fetches webpage"""

if __name__ == "__main__":
    import requests
    import sys
    url = 'http://0.0.0.0:5000/search_user'
    if (len(sys.argv)) > 1:
        q = sys.argv[1]
    else:
        q = ""
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
    except ValueError:
        print("Not a valid JSON")

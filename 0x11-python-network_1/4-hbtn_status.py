#!/usr/bin/python3
"""Python script that fetches webpage"""

if __name__ == "__main__":
    import requests
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))

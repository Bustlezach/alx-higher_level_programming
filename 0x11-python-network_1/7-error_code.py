#!/usr/bin/python3
"""
This script sends a request to the URL and
displays the body of the response
"""
from requests import get
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    r = get(url)
    if r.status_code >= 400:
        print(f'Error code: {r.status_code}')
    else:
        print(r.text)


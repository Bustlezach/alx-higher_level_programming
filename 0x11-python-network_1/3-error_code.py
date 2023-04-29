#!/usr/bin/python3
"""
This script sends a request to the URL and displays the body of
the response (decoded in utf-8).
"""

from urllib import request
from urllib import error
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    url_req = request.Request(url)
    try:
        with request.urlopen(url_req) as resp:
            print(resp.read().decode("ascii"))
    except error.HTTPError as e:
        print(e.code)


#!/usr/bin/python3
"""This script fetches 'https://alx-intranet.hbtn.io/status'"""

from urllib import request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    url_req = request.Request(url)
    with request.urlopen(url_req) as response:
        page = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page.decode("utf-8")))

#!/usr/bin/python3
# This script fetches 'https://alx-intranet.hbtn.io/status'

from urllib import request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    url_req = request.Request(url)
    with request.urlopen(url_req) as req:
        page = req.read()
        print("Body response:")
        print(f"\t- type: {type(page)}")
        print(f"\t- type: {page}")
        print(f"\t- type: {page.decode("utf-8")}")


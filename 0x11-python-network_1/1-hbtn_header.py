#!/usr/bin/python3
"""This script  displays the value of the X-Request-Id"""

from urllib import request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    url_req = request.Request(url)
    with request.urlopen(url_req) as response:
        header = response.info()
        # print(header)
        x_req_id = header['X-Request-Id']
        print(x_req_id)

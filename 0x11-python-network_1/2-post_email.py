#!/usr/bin/python3
"""
This script sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

from urllib import request
from urllib import parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}
    mail = parse.urlencode(value)
    data = mail.encode('ascii')
    url_req = request.Request(url, data)
    with request.urlopen(url_req) as resp:
        body = resp.read()
        body_str = body.decode('utf-8')
        print(body_str)

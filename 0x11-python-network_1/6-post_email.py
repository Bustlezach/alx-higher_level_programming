#!/usr/bin/python3
"""
This script sends a POST request to the passed URL
with the email as a parameter,
and finally displays the body of the response.
"""
from requests import post
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    mail = {'email': argv[2]}
    r = post(url, data=mail)
    print(r.text)


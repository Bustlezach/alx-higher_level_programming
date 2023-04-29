#!/usr/bin/python3
"""
This script sends a POST request to the passed URL
with the email as a parameter,
and finally displays the body of the response.
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    r = requests.get(url, params=values)
    print(r.text)


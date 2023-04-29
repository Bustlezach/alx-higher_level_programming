#!/usr/bin/python3
"""
sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""
import requests
from sys import argv

if __name__ == "__main__":
    data = argv[1]
    r = requests.get(data)
    print(r.headers.get('X-Request-Id'))


#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
'http://0.0.0.0:5000/search_user' with the letter as a parameter.
"""
from requests import post
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        q = {'q': argv[1]}
    else:
        q = {'q': ''}
    r = post(url, params=q)
    try:
        obj = r.json()
        if len(obj) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(obj['id'], obj['name']))
    except ValueError:
        print('Not a valid JSON')


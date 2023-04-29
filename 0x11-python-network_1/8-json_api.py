#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
'http://0.0.0.0:5000/search_user' with the letter as a parameter.
"""
from requests import post
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        q = {'key': argv[1]}
    else:
        q = {'key': ''}
    url = 'http://0.0.0.0:5000/search_user'
    r = post(url, params=q)
    try:
        data = r.json()
        if len(data) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(data['id'], data['name']))
    except ValueError:
        print('Not a valid JSON')


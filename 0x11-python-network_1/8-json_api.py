#!/usr/bin/python3
"""This script uses the GitHub API to display a GitHub ID based on given credentials."""

from sys import argv
from requests import post, get


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if argv[1] is not None:
        letter = argv[1]
    else:
        letter = ""
    q = {'q': letter}
    r = post(url, params=q)
    try:
        obj = r.json()
        if obj == {}:
            print('No result')
        else:
            print('[{}] {}'.format(obj.get('id'), obj.get('name')))
    except ValueError:
        print('Not a valid JSON')


#!/usr/bin/python3
"""This script uses the GitHub API to display a GitHub ID based on given credentials."""

from sys import argv
from requests import get


if __name__ == "__main__":
    usr = argv[2]
    repo = argv[1]
    url = f'https://developer.github.com/{usr}/{repo}/commits/'

    r = get(url)
    obj = r.json()
    try:
        for i in range(10):
            print('{}: {}'.format(obj[i].get('sha'), obj[i].get('commit').get('author').get('name')))
            if i < 10:
                print('Commit is less than 10')
                break
    except ValueError:
        pass
    

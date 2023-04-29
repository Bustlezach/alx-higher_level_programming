#!/usr/bin/python3
"""This script fetches 'https://alx-intranet.hbtn.io/status'."""
from requests import get

if __name__ == "__main__":
    r = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print(f'\t- type: {type(r.text)}')
    print(f'\t- type: {r.text}')


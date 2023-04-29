#!/usr/bin/python3
"""
This script fetches 'https://alx-intranet.hbtn.io/status'
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    reqs = requests.get(url)
    r = reqs.text
    print('Body response:')
    print(f'\t- type: {type(r)}')
    print(f'\t- type: {r}')

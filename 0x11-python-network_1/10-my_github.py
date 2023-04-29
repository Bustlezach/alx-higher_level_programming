#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials."""

from sys import argv
from requests import get
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    data = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = get("https://api.github.com/user", auth=data)
    print(r.json().get("id"))


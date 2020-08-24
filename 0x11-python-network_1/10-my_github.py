#!/usr/bin/python3
"""takes your Github credentials (username and password) and
uses the Github API to display your id"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == '__main__':
    lien = 'https://api.github.com/user'
    r = requests.get(lien, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    r = requests.get(lien, auth=(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))

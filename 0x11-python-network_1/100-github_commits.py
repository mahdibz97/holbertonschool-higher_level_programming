#!/usr/bin/python3
"""Python scriptthat takes 2 arguments in order to list 10 commits
that uses github api"""
import requests
import sys


if __name__ == '__main__':
    lien = 'https://api.github.com/repos/' + sys.argv[2] + '/' + sys.argv[1] +\
            '/commits'
    r = requests.get(lien)
    commits = r.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))

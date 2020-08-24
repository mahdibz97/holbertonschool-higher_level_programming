#!/usr/bin/python3
"""Python script that takes in a URL and an email address sends a POST
request to the URL with the email as a parameter and displays response
"""
import requests
from sys import argv


if __name__ == '__main__':
    email = {'email': argv[2]}
    r = requests.post(argv[1], data=email)
    print(r.text)

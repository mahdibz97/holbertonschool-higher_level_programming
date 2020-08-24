#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) == 2:
        qv = sys.argv[1]
    else:
        qv = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': qv})
    try:
        r_dict = r.json()
        id = r_dict.get('id')
        name = r_dict.get('name')
        if len(r_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    except BaseException:
        print("Not a valid JSON")

#!/usr/bin/python3
"""script that takes a URL a email sends POST request to the passed URL with
the email as a parameter and displays the body of the response"""
import urllib.request
import sys


if __name__ == "__main__":
    val = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(val)
    data = data.encode('ascii')
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        html = response.read()
    print(html.decode(encoding="utf-8"))

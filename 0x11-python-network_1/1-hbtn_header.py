#!/usr/bin/python3
""" get specific header from provided url """
from urllib import request
from sys import argv

with request.urlopen(argv[1]) as response:
    headers = response.info()
    print(headers['X-Request-Id'])

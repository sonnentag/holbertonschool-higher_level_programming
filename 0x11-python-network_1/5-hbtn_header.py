#!/usr/bin/python3
""" get specific header from provided url """
import requests
from sys import argv

print(requests.get(argv[1]).headers['X-Request-Id'])

#!/usr/bin/python3
""" POST email address to url and print the response """
import requests
from sys import argv

print(requests.post(argv[1], data={'email': argv[2]}))

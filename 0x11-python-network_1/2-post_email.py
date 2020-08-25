#!/usr/bin/python3
""" POST email address to url and print the response """

from sys import argv
from urllib import request, parse

url = argv[1]
email = argv[2]

data = parse.urlencode({'email': email})

with request.urlopen(url, data.encode('utf-8')) as response:
    print(response.read().decode('utf8'))

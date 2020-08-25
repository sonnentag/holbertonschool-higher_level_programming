#!/usr/bin/env python3
""" url status """
from urllib import request

with request.urlopen('https://intranet.hbtn.io/status') as response:
    for line in response:
        print("Body response:")
        print("\t- type: {}".format(type(line)))
        print("\t- content: {}".format(line))
        print("\t- utf8 content: {}".format(line.decode('utf-8').rstrip()))

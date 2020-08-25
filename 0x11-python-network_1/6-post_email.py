#!/usr/bin/python3
""" POST email address to url and print the response """

import requests
from sys import argv


if __name__ == '__main__':
    ''' main '''

    print(requests.post(argv[1], {'email': argv[2]}).text)

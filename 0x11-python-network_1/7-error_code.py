#!/usr/bin/python3
""" POST email address to url and print the response """

import requests
from sys import argv


if __name__ == '__main__':
    ''' main '''

    r = requests.get(argv[1])

    if r.status_code >= 400:
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)

#!/usr/bin/python3
""" get specific header from provided url """

import requests
from sys import argv


if __name__ == '__main__':
    ''' main '''

    print(requests.get(argv[1]).headers['X-Request-Id'])

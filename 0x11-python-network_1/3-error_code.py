#!/usr/bin/python3
""" POST email address to url and print the response """

from sys import argv
from urllib import request, parse


if __name__ == '__main__':
    ''' main '''

    data = parse.urlencode({'email': argv[2]})

    with request.urlopen(argv[1], data.encode('ascii')) as response:
        print(response.read().decode('utf8'))

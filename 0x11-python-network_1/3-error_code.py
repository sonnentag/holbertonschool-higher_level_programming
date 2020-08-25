#!/usr/bin/python3
""" POST email address to url and print the response """

from sys import argv
from urllib import request, parse, error


if __name__ == '__main__':
    ''' main '''

    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))

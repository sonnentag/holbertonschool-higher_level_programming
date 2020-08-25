#!/usr/bin/python3
""" url status """

import requests


if __name__ == '__main__':
    ''' main '''

    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))

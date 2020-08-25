#!/usr/bin/python3
""" POST email address to url and print the response """

from sys import argv
from urllib import request, parse

data = parse.urlencode({'email': argv[2]})

with request.urlopen(argv[1], data.encode('ascii')) as response:
    print(response.read().decode('utf8'))


    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf8')
            print(html)
    except urllib.error.HTTPError as e:
        # e = HTTP Error 401: UNAUTHORIZED
        e = str(e)
        e = e.rsplit(' ')[2].replace(':', '')
        print('Error code: {}'.format(e))

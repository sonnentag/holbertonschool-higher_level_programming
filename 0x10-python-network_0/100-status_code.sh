#!/bin/bash
# get http status code from request to provided url
curl -s -o /dev/null -w "%{http_code}" "$1"

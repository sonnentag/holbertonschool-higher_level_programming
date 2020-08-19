#!/bin/bash
# send header with GET to provided url
curl -sH 'X-HolbertonSchool-User-Id:98' -G "$1"

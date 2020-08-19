#!/bin/bash
# send post params to provided url
curl -sbG "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"

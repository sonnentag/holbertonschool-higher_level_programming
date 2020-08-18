#!/bin/bash
# print a url's allowed methods
curl -sI -G "$1" | awk -F': ' '/^Allow/ {print $2 }'

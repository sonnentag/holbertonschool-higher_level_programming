#!/usr/bin/env bash
# get size of body of site at first argument
curl -sbG "$1" | wc -c

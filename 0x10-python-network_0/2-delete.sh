#!/usr/bin/env bash
# send delete request to url provided
curl -sX delete -G "$1"

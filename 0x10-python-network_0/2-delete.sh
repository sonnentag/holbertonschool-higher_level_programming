#!/bin/bash
# send delete request to url provided
curl -sX delete -G "$1"

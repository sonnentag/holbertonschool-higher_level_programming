#!/bin/bash
# follow provided url passing parameters and header
curl -sL -H 'Origin: HolbertonSchool' -d 'user_id=98' 0.0.0.0:5000/catch_me -X put

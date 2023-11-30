#!/usr/bin/env bash

python3 response.py | tr -d '"' | tr -d '{' | tr -d '}' | awk '{ if($0 !~ /^[[:space:]]*$/) print $0 }' | sed '$!s/$/,/' | sed 's/^ *//g' > agents.csv

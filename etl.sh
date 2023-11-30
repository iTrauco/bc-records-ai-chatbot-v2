#!/usr/bin/env bash

python3 response.py | tr -d '"' | tr -d '{' | tr -d '}' | awk '{ if($0 !~ /^[[:space:]]*$/) print $0 }' | sed '$!s/$/,/' | sed 's/^ *//g' > agents.csv
python3 create_new_entity.py | tr -d '"' | tr -d '{' | tr -d '}' | awk '{ if($0 !~ /^[[:space:]]*$/) print $0 }' | sed '$!s/$/,/' | sed 's/^ *//g' > new_entity.csv
#python3 create_new_entity.py  > new_entity.csv

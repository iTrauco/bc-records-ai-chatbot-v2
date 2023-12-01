#!/usr/bin/env bash

python3 response.py | tr -d '"' | tr -d '{' | tr -d '}' | awk '{ if($0 !~ /^[[:space:]]*$/) print $0 }' | sed '$!s/$/,/' | sed 's/^ *//g' > agents.csv

python3 entities.py | tr -d '"' | tr -d '{' | tr -d '}' | awk '{ if($0 !~ /^[[:space:]]*$/) print $0 }' | sed '$!s/$/,/' | sed 's/^ *//g' > entities.csv

python3 list_intents.py | tr -d '"' | tr -d '{' | tr -d '}' | awk '{ if($0 !~ /^[[:space:]]*$/) print $0 }' | sed '$!s/$/,/' | sed 's/^ *//g' > list_intents.csv

# python3 list_intents.py | tr -d '"' | tr -d '{' | tr -d '}' | awk '{ if($0 !~ /^[[:space:]]*$/) print $0 }'  | sed 's/^ *//g' > intents.csv

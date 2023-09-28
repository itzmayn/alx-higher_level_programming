#!/bin/bash

if [ $# -lt 2 ]; then
  echo "Usage: $0 <URL> <JSON_FILENAME>"
  exit 1
fi

curl -sX POST "$1" -H "Content-Type: application/json" -d @"$2" -L
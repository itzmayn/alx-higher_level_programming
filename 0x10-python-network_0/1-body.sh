#!/bin/bash

if [ $# -eq 0 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

url=$1

# Send a GET request to the URL and filter the body if the status code is 200
curl -s -o /dev/null -w "%{http_code}" "$url" | {
    read -r status_code
    if [ "$status_code" -eq 200 ]; then
        curl -s "$url"
    else
        echo "HTTP status code: $status_code"
    fi
}

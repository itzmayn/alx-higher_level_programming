#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays the
body of the response (decoded in utf-8).

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors and displays the error code.
"""
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: ./3-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    req = Request(url)

    try:
        # Send the request and handle HTTP errors
        with urlopen(req) as response:
            body = response.read().decode("utf-8")
            print(body)
    except HTTPError as e:
        print("Error code: {}".format(e.code))


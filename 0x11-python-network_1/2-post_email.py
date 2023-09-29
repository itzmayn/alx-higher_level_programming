#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8).
"""
from sys import argv
from urllib.parse import urlencode
from urllib.request import Request, urlopen


if __name__ == "__main__":
    my_url = argv[1]
    v = {"email": argv[2]}
    data = urlencode(v).encode("ascii")
    req = Request(my_url, data)

    with urlopen(req) as response:
        print(response.read().decode("utf-8", "replace"))

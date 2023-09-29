#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status."""
import urllib.request

def fetch_and_display_status(url):
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            utf8_content = content.decode('utf-8')
            print("Body response:")
            print("    - type:", type(content))
            print("    - content:", content)
            print("    - utf8 content:", utf8_content)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch_and_display_status(url)


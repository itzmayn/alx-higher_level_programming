#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

sage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
from sys import argv
import requests


import requests
import sys

def search_user_by_letter(letter):
    url = 'http://0.0.0.0:5000/search_user'
    params = {'q': letter}

    try:
        response = requests.post(url, data=params)
        response_data = response.json()

        if response_data:
            print(f"[{response_data['id']}] {response_data['name']}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    search_user_by_letter(letter)


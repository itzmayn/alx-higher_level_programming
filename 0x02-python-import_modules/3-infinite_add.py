#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    total = 0
    length = len(argv)
    
    for i in range(1, length):
        total += int(argv[i])
    print(f"{total}")

#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print(f"{value}")
    except:
        return False
    else:
        return True

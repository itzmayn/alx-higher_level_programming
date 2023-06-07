#!/usr/bin/python3
import random

# Generate a random signed number between -10000 and 10000
number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10

# Determine the message based on the last digit
message = "Last digit of " + str(number) + " is " + str(last_digit)

if last_digit > 5:
    message += " and is greater than 5"
elif last_digit == 0:
    message += " and is 0"
else:
    message += " and is less than 6 and not 0"

# Print the message
print(message)

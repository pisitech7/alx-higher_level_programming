#!/usr/bin/python3

import random

# Assigning a random signed number to the variable 'number'
number = random.randint(-10000, 10000)

# Finding the last digit of the number
last_digit = number % 10  # Remove abs() to maintain sign

# Printing the last digit and its characteristics
print(f"Last digit of {number} is {last_digit}", end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

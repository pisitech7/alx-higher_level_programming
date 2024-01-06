#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Check if the character is lowercase using ASCII values
        # Convert lowercase to uppercase using ASCII difference
        if 97 <= ord(char) <= 122:
            uppercase_char = chr(ord(char) - 32)
            print("{}".format(uppercase_char), end='')
        else:
            print("{}".format(char), end='')

    print()  # Print a new line after printing the uppercase string

#!/usr/bin/python3def uppercase(s):
    result = ""
    for char in s:
        if 97 <= ord(char) <= 122:  # Checking if character is lowercase
            uppercase_char = chr(ord(char) - 32)  # Convert to uppercase using ASCII difference
            result += uppercase_char
        else:
            result += char

    print("{}".format(result))  # Print the uppercase string

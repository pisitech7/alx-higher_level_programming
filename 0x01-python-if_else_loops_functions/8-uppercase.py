#!/usr/bin/python
def uppercase(s):
    upper_str = ''
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            upper_char = chr(ord(char) - 32)
            upper_str += upper_char
        else:
            upper_str += char

    print("{}".format(upper_str))

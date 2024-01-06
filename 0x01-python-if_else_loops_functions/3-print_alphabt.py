#!/usr/bin/python3

# Printing the lowercase ASCII alphabet excluding 'q' and 'e' without a new line
for letter in range(ord('a'), ord('z') + 1):
    if chr(letter) not in 'qe':
        print(chr(letter), end='')

#!/usr/bin/python3
# Printing the lowercase ASCII alphabet excluding 'q' and 'e' without a new line
output = ''.join(chr(letter) for letter in range(ord('a'), ord('z') + 1) if chr(letter) not in 'qe')
print('{}'.format(output), end='')

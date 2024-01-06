#!/usr/bin/python3
# Printing the lowercase ASCII alphabet without a new line using format
print('{}'.format(''.join(chr(i) for i in range(ord('a'), ord('z') + 1))), end='')

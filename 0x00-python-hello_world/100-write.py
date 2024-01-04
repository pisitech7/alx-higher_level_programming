#!/usr/bin/python3
import sys
file_content = "and that piece of art is useful - Dora Korpar, 2015-10-19"
with open('output.txt', 'w') as file:
    file.write(file_content)
# Exiting with status code 1
sys.exit(1)

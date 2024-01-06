#!/usr/bin/python3
# Printing numbers from 0 to 98 in decimal and hexadecimal format
for i in range(99):
    if i < 10:
        print(f"0{i} 0x0{i}")
    else:
        print(f"{i} 0x{i}")

#!/usr/bin/python3

# Printing numbers from 0 to 99 in the specified format
for i in range(100):
    if i < 10:
        print(f"0{i}", end=", " if i < 99 else "\n")
    else:
        print(f"{i}", end=", " if i < 99 else "\n")

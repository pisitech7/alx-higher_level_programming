#!/usr/bin/python3.8.x
import dis
import os

def print_hidden_names():
    if os.path.exists('hidden_4.pyc'):
        with open('hidden_4.pyc', 'rb') as file:
            code = file.read()
            dis.dis(code)
    else:
        print("File 'hidden_4.pyc' not found.")

if __name__ == "__main__":
    print_hidden_names()

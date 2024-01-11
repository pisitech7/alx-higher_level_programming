#!/usr/bin/python3.8.x 
import dis
import os

def print_hidden_names():
if __name__ == "__main__":
    file_path = 'hidden_4.pyc'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            code = file.read()
            dis.dis(code)
    else:
        print("File 'hidden_4.pyc' not found.")
    print_hidden_names()

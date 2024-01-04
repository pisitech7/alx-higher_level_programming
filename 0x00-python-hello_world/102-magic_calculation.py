#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    return (a ** b) + (b ** a)

dis.dis(magic_calculation)


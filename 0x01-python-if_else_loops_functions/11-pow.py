#!/usr/bin/python3
def pow(a, b):
    # Handle the cases when the exponent (b) is positive, negative, or zero
    if b == 0:
        return 1
    elif b > 0:
        result = 1
        for _ in range(b):
            result *= a
        return result
    else:
        result = 1.0
        for _ in range(abs(b)):
            result /= a
        return result

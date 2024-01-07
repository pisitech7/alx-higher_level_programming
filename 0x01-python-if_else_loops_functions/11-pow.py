#!/usr/bin/python3
def pow(a, b):
    # Handle the cases when the exponent (b) is positive, negative, or zero
    if b == 0:
        return 1
    elif b > 0:
        result = 1
        for i in range(b):
            result *= a
        return result
    else:
        result = 1.0
        for i in range(abs(b)):
            result /= a
        return result

# Test the function
result = pow(2, 3)
print("Result:", result)


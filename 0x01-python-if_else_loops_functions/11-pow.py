#!/usr/bin/python3
def pow(a, b):
    # Initialize the result to 1
    result = 1

    # Handle the cases when the exponent (b) is positive, negative, or zero
    if b > 0:
        for i in range(b):
            result *= a
    elif b < 0:
        for i in range(abs(b)):
            result /= a
    # If the exponent is zero, the result is 1
    else:
        return 1

    return result

# Test the function
result = pow(2, 3)
print("Result:", result)

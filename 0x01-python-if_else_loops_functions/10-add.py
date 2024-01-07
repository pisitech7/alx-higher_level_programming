#!/usr/bin/python3
def add(a, b):
    # Calculate the sum of a and b
    result = a + b

    # Return only the last digit of the result
    return result % 10

# Test the function
result = add(2, 3)
print(result)


#!/usr/bin/python3
def print_last_digit(number):
    # Ensure number is positive
    number = abs(number)

    # Get the last digit by using modulo 10
    last_digit = number % 10

    # Print the last digit
    print("The last digit is:", last_digit)

    # Return the last digit value
    return last_digit

# Test the function
number = 987654321
result = print_last_digit(number)

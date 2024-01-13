#!/usr/bin/python3
from functools import reduce

def square_matrix_lambda(matrix=[]):
    # Use map and lambda to compute the square of each element
    result_matrix = list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
    return result_matrix

# Test case
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_lambda(matrix)
print(new_matrix)
print(matrix)  # Original matrix remains unchanged

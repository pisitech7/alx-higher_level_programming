#!/usr/bin/python3
a = 10
b = 5

from calculator_1 import add, sub, mul, div

add_result = add(a, b)
sub_result = sub(a, b)
mul_result = mul(a, b)
div_result = div(a, b)

result_format = "{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {}"
print(result_format.format(a, b, add_result, a, b, sub_result, a, b, mul_result, a, b, div_result))

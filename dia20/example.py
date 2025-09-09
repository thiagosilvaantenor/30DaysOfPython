#!/usr/bin/env python3
# Maps -> like comprehensions, takes a function and a iterable, applyes to each item the function
from operator import methodcaller


def cube_number(number:int):
    return number ** 3


numbers = [2,3]

cubbed_numbers = map(cube_number,numbers)
# to print you need to iterated over
print(*cubbed_numbers, sep=',')

## using more than one iterable
def add(n1,n2):
    return n1 + n2


odds = [1,3,5,7]
evens = [2,4,6,8]
total = map(add,odds,evens)
print(*total, sep=',')

# map is better for simple functions, is better to use lambda expressions
cubed_numbers = map(lambda number: numbers ** 3, numbers)
# operator methodcaller, calls a method

names = ['tomas', 'Lyly', 'RoMan']
title_names = map(methodcaller('title'), names )
# more readable alternative: 
title_names = map(lambda name: name.title(), names )
# conditional comprehensions
numbers = [1,2,3,4,5,6,7]
evens = [number for number in numbers if number % 2 == 0]
print(*evens, sep=' - ')

# filter -> similar to map, calls a function(predicate) that must returns True | False
# only one colletion a time 
def is_even(num):
    return num % 2 == 0

filtered_numbers = filter(is_even, numbers)
# it is a lazy objetc, just like map, so it will only calculate when we iterated over
print(*filtered_numbers, sep=' - ')

# Using None in filter
values = [0, "Hello", [], {}, 435, -4.2, ""]
truthy_values = filter(None, values)

print(*truthy_values, sep=", ")  # Hello, 435, -4.2


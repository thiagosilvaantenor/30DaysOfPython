#!/usr/bin/env python3
# 1) Create a function that accepts any number of numbers as positional arguments and prints the sum of those numbers. 
# Remember that we can use the sum function to add the values in an iterable.

def any_sum(*numbers):
    total = sum(numbers)
    print(total)



any_sum(1,2,3)
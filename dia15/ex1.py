#!/bin/python3
# 1) Convert the following for loop into a comprehension:
# numbers = [1, 2, 3, 4, 5]
# squares = []

# for number in numbers:
#     squares.append(number ** 2)

numbers = [1,2,3,4,5]
squares = [number ** 2 for number in numbers]

print(squares)
#!/usr/bin/env python3
# 3) Use filter to remove all negative numbers from the following range: range(-5, 11).
# Print the remaining numbers to the console.

numbers = range(-5,11)
filtred_numbers = filter(lambda number: number > 0, numbers)
print(*filtred_numbers, sep=",")

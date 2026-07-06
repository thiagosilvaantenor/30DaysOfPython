#Below you'll find a list containing several tuples full of numbers:

numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]

# Use the `map` function to find the sum of the numbers in each tuple. 
# Use manual iteration to print the first two results provided by the resulting map object.

sum_nums= map(sum, numbers)

print(next(sum_nums))
print(next(sum_nums))
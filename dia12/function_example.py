#!/bin/python3

# # base function
# def get_even_numbers():
#     print('Even numbers!')
#     for n in range(0,11,2):
#         print(n)


# function with arguments
def get_even_numbers(amount):
    for n in range(0, amount + 1):
        print(n * 2)


get_even_numbers(20)

# function with more than 1 parameters/arguments
def x_print(txt, times):
    # use _ to especify that the loop variable is unimportant
    for _ in range(0,times+1):
        print(txt)


# x_print('uwu', 5)

# using keyword arguments to especify the parameters
x_print(times=2, txt='Test')
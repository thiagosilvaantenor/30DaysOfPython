#!/bin/python3
# Global scope
print(globals())

# local scope
def print_x_y(x,y):
    print(locals())
    greeting = 'Hello :)'
    print(locals())
    print(greeting, '\n', x, y)
print_x_y('a','b')
print(locals())

# return
def my_func():
    return 'OK OK'
    print("This line will never run")

print(my_func())

# Empty return equals None
def print_x_y(x,y):
    return

print(print_x_y(2,2))

# Multiple returns
def divide(a, b):
    if b == 0:
        return "You can't divide by 0!"

    return a / b

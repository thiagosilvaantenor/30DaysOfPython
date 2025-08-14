#!/bin/python3
#1) Define four functions: add, subtract, divide, and multiply. 
#Each function should take two arguments, and they should print the result of the arithmetic operation indicated by the function name.

def add(n1,n2):
    print(n1+n2)


def subtract(n1,n2):
    print(n1-n2)


def divide(n1,n2):
    if n1 == 0 or n2 == 0:
        print('Cannot divide zero')
    else:
        print(n1/n2)


def multiply(n1,n2):
    print(n1*n2)

option = input('1-Add\n2-Subtract\n3-Divide\n4-Multiply\n5-Quit\n')
if option != '5':
    n1 = float(input('Enter the first number'))
    n2 = float(input('Enter the second number'))
    match(option):
        case '1': 
            add(n1,n2)
        case '2': 
            subtract(n1,n2)
        case '3': 
            divide(n1,n2)
        case '4': 
            multiply(n1,n2)
        case _:
            print('Ops... invalid option')

else:
    print('Closing the program....')
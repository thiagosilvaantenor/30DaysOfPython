#!/bin/python3
# exercicio3

#3) Ask the user to enter a number. Tell the user whether the number is 
# positive, negative, or zero.
print('Exercise 3')
num = int(input('Hello! Please, enter a number: '))

if (num == 0):
    print(f'The number is zero: {num}')
elif (num < 0):
    print(f'The number is negative: {num}')
else:
    print(f'The number is positive: {num}')
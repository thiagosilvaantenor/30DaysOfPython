#!/bin/python3
# exercicio2

# 2) Try to use the is operator or the id function to investigate the difference between this:
#numbers = [1, 2, 3, 4]
#new_numbers = numbers + [5]
# and this
#numbers = [1, 2, 3, 4]
#numbers.append(5)
# Are new_numbers and numbers the same thing? What about numbers before and after we append 5?
print('Exercise 2:')
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
print( numbers is new_numbers)

print('Second exemple')
numbers = [1, 2, 3, 4]
print(id(numbers))
numbers.append(5)
print(id(numbers))

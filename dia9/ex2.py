#!/bin/python3
# 2) Unpack the following tuple into 4 variables:

# ("John Smith", 11743, ("Computer Science", "Mathematics"))

# The data represents a student's name, their student id number, and their major and minor disciplines in that order.

student = ("John Smith", 11743, ("Computer Science", "Mathematics"))

name, id_number, (major_discipline, minor_discipline) = student

print(f'{name} , {id_number} , {major_discipline} , {minor_discipline}')
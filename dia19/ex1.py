#!/usr/bin/env python3
# 1) Create a short program that prompts the user for a list of grades separated by commas.
# Split the string into individual grades and use a list comprehension to convert each string to an integer.
# You should use a try statement to inform the user when the values they entered cannot be converted.


grades = input("Enter the grades, separeted by commas: ")
try:
    list_grades = grades.split(',')
    grades_integers = [int(grade) for grade in list_grades]
except (TypeError, ValueError):
        print("Invalid value, enter only numbers")
else:
    print(grades_integers)


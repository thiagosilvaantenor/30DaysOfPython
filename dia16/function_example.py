#!/usr/bin/env python3
# using functions in variables
# def add(a, b):
#     print(a + b)

# adder = add
# del add

# adder(5, 4)   # 9
# print(adder)  # <function add at 0x7f03780ae1f0>

# using functions in arguments/parameters
# Here we provided the get_grade_average function as an argument for max, and max called this function for us internally to 
# determine the order of the items in our list.
# It then correctly returned this dictionary as the student with the highest grade average:

def get_grade_average(student):
    return student["grade_average"]

students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]

valedictorian = max(students, key=get_grade_average)
print(valedictorian)

# Returning functions within functions
def add(a, b):
    print(a + b)

def subtract(a, b):
    print(a - b)

def multiply(a, b):
    print(a * b)

def divide(a, b):
    if b == 0:
        print("You can't divide by 0!")
    else:
        print(a / b)

#Referencing the functions by the variables names
operations = {
    "a": add,
    "s": subtract,
    "m": multiply,
    "d": divide
}

selected_option = input("""Please select one of the following options:

a: add
s: subtract
m: multiply
d: divide

What would you like to do? """)

# Uses the get() methot form dictionary
operation = operations.get(selected_option)

if operation:
    a = int(input("Please enter a value for a: "))
    b = int(input("Please enter a value for b: "))

    operation(a, b)
else:
    print("Invalid selection")

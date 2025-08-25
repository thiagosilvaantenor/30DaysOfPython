#!/usr/bin/env python3
# lambda expressions: single expressions functions, cannot use if
# lambda a,b : a + b

students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]
# Now we use a lambda to replace the function, with this we save a few lines and achive the same result 
valedictorian = max(students, key=lambda student: student["grade_average"])
print(valedictorian)

# Example 2 : operator mapping dictionary

# We cannot use if with lambda expressions, so we have to define a function to this operation
def divide(a, b):
    if b == 0:
        return "You can't divide by 0!"
    else:
        return a / b

# The rest of the operations we just use a lambda function
operations = {
    "a": lambda a, b: a + b,
    "s": lambda a, b: a - b,
    "m": lambda a, b: a * b,
    "d": divide
}

selected_option = input("""Please select one of the following options:

a: add
s: subtract
m: multiply
d: divide

What would you like to do? """)

operation = operations.get(selected_option)

if operation:
    a = int(input("Please enter a value for a: "))
    b = int(input("Please enter a value for b: "))

    print(operation(a, b))
else:
    print("Invalid selection")



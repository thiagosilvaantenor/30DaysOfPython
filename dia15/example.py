#!/bin/python3
# # Comprehensions - Colections loops with less lines for simple operations
# to transform each name 
names = ['Igor', 'THIAGO', 'JhOnnY']
# The old way:
    # processed_names = []
    # for i in names:
    #     processed_names.append(i.title())
# With List compreehensions:
names = [name.title() for name in names]
# "Put name.title() in the new list for every name in names".

# A more complex operation:
#The old way:

# names = ("mary", "Richard", "Noah", "KATE")
# ages = (36, 21, 40, 28)

# people = []

# for name, age in zip(names, ages):
#     person_data = (name.title(), age)
#     people.append(person_data)

# With Tuples comprehension:
names = ("mary", "Richard", "Noah", "KATE")
ages = (36, 21, 40, 28)

people = [
    (name.title, age)
    for name, age in zip(names,ages)
    ]


# Set comprehension:
names = ["mary", "Richard", "Noah", "KATE"]
names = {name.title() for name in names}

# dictionary old way:
student_ids = (112343, 134555, 113826, 124888)
names = ("mary", "Richard", "Noah", "KATE")

students = {}

for id, name in zip(student_ids, names):
    # {key:values}
    student = {id:name.title()}
    students.update(student)

# With dictionary comprehension:
student_ids = (112343, 134555, 113826, 124888)
names = ("mary", "Richard", "Noah", "KATE")

student = {
    student_id:name.title()
    for student_id, student_name in zip(student_ids,names)
}
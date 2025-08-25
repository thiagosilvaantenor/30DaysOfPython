# 1) Use the sort method to put the following list in alphabetical order with regards to the students' names:
students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]
# You're going to need to pass in a function as a key here, and it's up to you whether you use a lambda expression, or whether you define a function with def.

students.sort(key=lambda student: student["name"])

print(students)
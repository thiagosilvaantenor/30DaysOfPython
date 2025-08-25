#!/usr/bin/env python3 
# examples of flexible function
# function that recieves multiple arguments
# using *args, when you dont know the argument can be anything
def multigreet(*args):
    for name in args:
        print(f"Hello, {name}!")

multigreet("Rolf", "Bob", "Anne")
# Since we do know that multigreet will receive 'names' the corret way is to explicit tell
def multigreet(*names):
    for name in names:
        print(f'Hello, {name}')


# **kwargs: each keyword is a key and the argument is a value
# dict(name="Phil", age=29, city="Budapest", nationality="British")
def pretty_print(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

pretty_print(title="The Matrix", director="Wachowski", year=1999)

# title: The Matrix
# director: Wachowski
# year: 1999

# destructuring (unpacking) an iterable into individual values with the '*' operator 
numbers = [1 , 2 , 3, 4]
print(*numbers, sep='|')

# destructuring a dictionary with the '**' operator
def print_movie(*args):
    for value in args:
        print(value)

movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}

print_movie(*movie.values())

# The Matrix
# Wachowski
# 1999

# Using **kwargs and dictionary destructuring:
def print_movie(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}

print_movie(studio="Warner Bros", **movie)

# studio: Warner Bros
# title: The Matrix
# director: Wachowski
# year: 1999

# using format
book_template = "{title}, by {author} ({year})"

def show_books(books):
    # Adds an empty line before the output
    print()

    for book in books:
        print(book_template.format(**book))

    print()


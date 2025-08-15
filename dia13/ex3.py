#!/bin/python3
# 3) Write a function that takes in a tuple containing information about an actor and returns this data as a dictionary. 
# The data should be in the following format:

# ("Tom Hardy", "English", 42)  # name, nationality, age

# You can choose whatever key names you like for the dictionary.

data = ("Tom Hardy", "English", 42)

def tuple_to_dictionary(data:tuple):
    name, nationality, age = data
    dictionary = {'name': name,
                  'nationality': nationality,
                  'age': age}
    return dictionary

print(tuple_to_dictionary(data))
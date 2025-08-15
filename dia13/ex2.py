#!/bin/python3
# 2) Define a process_string function which takes in a string and returns a new string which has been converted to lowercase, 
# and has had any excess whitespace removed.

def process_string(string:str):
    # lowercase the string
    string = string.lower().strip()
    return string

print( process_string( input('Enter the string to be lowercase and have any excess whitespace removed') ) )
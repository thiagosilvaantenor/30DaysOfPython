#!/usr/bin/env python3
# 2) Create a function that accepts any number of positional and keyword arguments, and that prints them back to the user.
# Your output should indicate which values were provided as positional arguments, and which were provided as keyword arguments.
def any_args_keyword(*args,**keywords):
    print('Args')
    for arg in args:
        print(arg)
    
    print('Keywords')
    for key, value in keywords.items():
        print(f'{key} : {value}')

numbers = [1,2,3]

contact = {
    'name': 'Joe',
    'number': '1140028922'
}

any_args_keyword(*numbers, **contact)

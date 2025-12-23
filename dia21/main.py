#!/usr/bin/env python3
# spliting code, importing files and using functions from other files
# everything that works with modules works with imported files

# import dia21.user_interactions.myfile as myfile
# from user_interactions.myfile import get_user_age

import user_interactions.myfile

# try:
#     # myfile.get_user_age()
#     get_user_age()
# except ValueError:
#     print("Invalid age. Please enter a number.")

# module mode
print(__name__) # first line belongs to myfile and second to main

# script mode




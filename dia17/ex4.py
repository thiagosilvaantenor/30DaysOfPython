#!/usr/bin/env python3
# 4) Using * unpacking and range, print the numbers 1 to 20, separated by commas. 
# You will have to provide an argument for print function's sep parameter for this exercise.


numbers = range(1,21)
print(*numbers,sep=',')
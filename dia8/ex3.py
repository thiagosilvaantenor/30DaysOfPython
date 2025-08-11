#!/usr/bin/python3
# ex3.py
# 3) Using one of the examples from earlier—or a solution entirely of your own—create a program that prints out every prime number between 1 and 100.

j = 0

for i in range(2,101):
  for j in range(2, i):
    if i % j == 0:
      break
  else:
    print(i)
 

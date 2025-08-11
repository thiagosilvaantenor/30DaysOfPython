#!/usr/bin/python3
# ex2.py
# 2) Use a loop and the continue keyword to print out every character in the string "Python", except the "o".

for keyword in 'Python':
  if 'o' in keyword:
    # Se a letra for = a 'o', pula essa iteracao
    continue
  print(keyword);

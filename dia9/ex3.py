#!/bin/python3
#3) Investigate what happens when you try to zip two iterables of different lengths. 
# For example, try to zip a list containing three items, and a tuples containing four items.

lista = [1 , 2 , 3]

tupla = (2, 4 , 6 ,8)

for n1, n2 in zip(lista, tupla):
    print(f'{n1} e {n2}')

#!/usr/bin/python3
# ex1
#  Ask the user to enter their given name and surname in response to a single prompt. Use split to extract the names, and then assign each name to a different variable. For this exercise, you can assume that the user has a single given name and a single surname.

complete_name = input("Olá, informe seu nome e sobrenome: ");

name_and_surname = complete_name.split();

name = name_and_surname[0];
surname = name_and_surname[1];

print(f'name: {name}, surname: {surname}');

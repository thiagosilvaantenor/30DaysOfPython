#Using the variable below, print "Hello, world!".
greeting = "Hello, world"
print(f'{greeting}!')

#Ask the user for their name, and then greet the user, using their name as part of the greeting. The name should be in title case, and shouldn't be surrounded by any excess white space.
#For example, if the user enters "lewis ", your output should be something like this:
# Hello, Lewis!
nome = input('Informe seu nome: ').title()
greeting = 'Hello, '
print(f'{greeting}{nome.strip()}!')

#Concatenate the string "I am " and the integer 29 to produce a string which reads "I am 29".
#Remember that we can only concatenate strings to other strings, so you will have to convert the integer to a string before you can perform the concatenation.
s = 'I am '
num = 29
s = s + str(num)
print(s)
# Format and print the information below using string interpolation:
title = "Django"
director = "Quentin Tarantino"
release_year = 2019

print(f'Filme: {title}, Diretor: {director}, ano de lançamento: {str(release_year)}')
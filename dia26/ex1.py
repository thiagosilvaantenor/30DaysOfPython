# 1) Define a Movie tuple using namedtuple that accepts 
# a title, a director, a release year, and a budget. 
# Prompt the user to provide information for each of these fields
# and create an instance of the Movie tuple you defined.

from collections import namedtuple
Movie = namedtuple("Movie", ["title", "director", "release_year", "budget"])

title = input('Inform the title of the movie: ')
director = input('Inform the name of the director: ')
year = int(input('Inform the year of release: '))
budget = int(input('Inform the budget of the movie: '))

movie = Movie(title=title, director=director, release_year=year, budget=budget)

print(*movie,sep=',')



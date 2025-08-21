#!/bin/python3
# 2) Use a dictionary comprehension to create a new dictionary from the dictionary below, where each of the values is title case.
movie = {
    "title": "thor: ragnarok",
    "director": "taika waititi",
    "producer": "kevin feige",
    "production_company": "marvel studios"
}

movie_title_case = {
    key:val.title()
    for key,val in movie.items()
}

print(movie_title_case)
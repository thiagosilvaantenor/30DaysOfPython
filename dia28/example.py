from typing import Optional, Union

Movie = tuple[str, str, int]


def find_movie(search_term: str, movies: list[Movie]) -> Optional[Movie]:
    for title, director, year in movies:
        if title == search_term:
            return (title, director, year)

    return None


def show_movies(movies: list[Movie]):
    for movie in movies:
        print_movie(movie)


def print_movie(movie: Movie):
    title, director, year = movie
    print(f"{title} ({year}), by {director}")


movies: list[Movie] = [
    ("Finding Nemo", "Andrew Stanton", 2005),
    ("Inside Out", "Pete Docter", 2015),
    ("Toy Story 3", "Lee Unkrich", 2010),
]

show_movies(movies)

search_result: Union[Movie, None] = find_movie("Finding Nemo", movies)

if search_result:
    print_movie(search_result)
else:
    print("Couldn't find movie.")

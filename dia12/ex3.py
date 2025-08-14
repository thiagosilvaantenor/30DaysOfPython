# Iterate over the list of shows bellow and use the show_info to print the info of them
series = [
{"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
{"title": "Fargo", "seasons": 4, "initial_release": 2014},
{"title": "Firefly", "seasons": 1, "initial_release": 2002},
{"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
{"title": "True Detective", "seasons": 3, "initial_release": 2014},
{"title": "Westworld", "seasons": 3, "initial_release": 2016},
]
def print_show_info(tv_show:dict):
    title = tv_show.get('title')
    year = tv_show.get('initial_release')
    num_seasons = tv_show.get('seasons')
    print(f'{title} ({year}) - {num_seasons} seasons')

for show in series:
    print_show_info(show)
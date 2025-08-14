# 2) Define a function called print_show_info that has a single parameter.
# The argument passed to it will be a dictionary with some information about a T.V. show. For example:
tv_show = {
"title": "Breaking Bad",
"seasons": 5,
"initial_release": 2008
}

# print_show_info(tv_show)
# The print_show_info function should print the information stored in the dictionary, in a nice way.
# Example:  Breaking Bad (2008) - 5 seasons
# Answer
def print_show_info(tv_show:dict):
    title = tv_show.get('title')
    year = tv_show.get('initial_release')
    num_seasons = tv_show.get('seasons')
    print(f'{title} ({year}) - {num_seasons} seasons')


print_show_info(tv_show=tv_show)
    
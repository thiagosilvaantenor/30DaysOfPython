import pandas as pd

movies = {
    "title": ("Inception", "Pirates of Carribean: The Curse of the Black Pearl"),
    "director": ("Christopher Nolan", "Gore Verbinski"),
    "year": (2010, 2003),
}

df = pd.DataFrame(movies)
# Using inplace to modify the existin df
df.rename(columns={"year": "release_year"}, inplace=True)
# df.drop(columns="director", inplace=True)
# deleting columns using double [] to access columns, if using only one will acess the series(lines)
df = df[["title", "release_year"]]

# Filtering by values
latest_movies = df.query("year == 2026")
# string data should be wrapped with ''
nolan_movies = df.query("director == 'Christopher Nolan'")

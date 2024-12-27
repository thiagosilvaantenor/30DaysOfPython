#!/usr/bin/python3
# movie_budget.py
# Calculate the average budget of all movies in the data set. Print out every movie that has a budget higher than the average you calculated.You should also print out how much higher than the average the movie's budget was.Print out how many movies spent more than the average you calculated.If you want a little extra challenge, allow users to add more movies to the data set before running the calculations.

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

# pergunta se e quantos filmes o usuário deseja adicionar
add_movie = str(input('Deseja adicionar filmes na lista? Y=sim,N=não : '))

if add_movie.upper() == 'Y':
  num = int(input("Quantos filmes deseja adicionar?"))
  for i in range(1, (num+1)):
    
    movie = str(input('Informe o nome do filme: '));
    budget = float(input('Informe o orçamento do filme: '));
    movie_tuple = (movie), (budget);
    movies.append(movie_tuple);


# realiza a média dos orçamentos
avg = 0.0;
for budget in movies :
  avg = avg + budget[1];

avg = avg / len(movies);

# exibe os orçamentos com valor maior que a média
higher = 0;
count = 0;
print(f'The average of budgets: {avg}');
for movie in movies:
  if movie[1] > avg :
    higher = movie[1] - avg;
    print(f'Movie: {movie[0]} has a budget higher than the average, the budget was {higher} higher than the average');
    count = count + 1;
    
print(f'{count} movies spend more than the average')
    
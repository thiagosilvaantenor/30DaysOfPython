#Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name, the release year of the movie, and the movie’s budget.
#Use the input function to gather information about another movie. You need a title, director’s name, release year, and budget.
#Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the tuple you wrote in the movies list.
#Use an f-string to print the movie name and release year by accessing your new movie tuple.
#Add the new movie tuple to the movies collection using append.
#Print both movies in the movies collection.
#Remove the first movie from movies. Use any method you like.

# 1 - Criar uma lista com uma tupla contendo: (Filme, Diretor, Ano lançamento, orçamento do filme)
movies = [('Dune','Denis Villeneuve',2021, 'US$ 165.000.000')]

# 2 - Usar input() para receber informações sobre outro filme
movie = input("Informe o nome do filme: ")
director = input("Informe o nome do diretor do filme: ")
year_relase = input('Informe o ano de lançamento do filme: ')
budget = input('Por fim, informe o orçamento do filme: ')

# 3 - Criar outra tupla com os valores recebidos
outherMovie = (movie, director, year_relase, budget)

# 4 - Use uma f-string para exibir o nome do filme e ano de lançamento atraves da nova tupla de filme
print(f'filme: {outherMovie[0]}, ano de lançamento: {outherMovie[2]}')

# 5 - Adicione a nova tupla na coleção movies usando o método append
movies.append(outherMovie)

# 6 - Mostre ambos os filmes da coleção movies
#print(movies)

# 7 - Remova o primeiro filme da coleção. Use o método que quiser
movies.pop(0)
print(movies) # Exibe a coleção pós remoção da primeira tupla
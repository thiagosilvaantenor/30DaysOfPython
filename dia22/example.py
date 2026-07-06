# ./.venv/python3
# Iterators and iterables:

# strings, lists, tuples, dictionaries, sets, range objects, zip objects, enumerate objects, map objects, filter objects


# They are lazy, so we cannot determine the lenght of a iterable until we perfome a operation on them

from operator import methodcaller

words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
# filter is going to wait until we request the values to calculate anything
a_words = filter(methodcaller("startswith", "a"), words)


# changes to mutable collections can affect an iterator
words.append("apple")

# Using next to request one value a time

# print(f'first value: {next(a_words)}')
# print(f'second value: {next(a_words)}')
# print(f'third value: {next(a_words)}')
# print(f'fourth value: {next(a_words)}') 
# Watch out for the StopIteration exception
#try:
#    print(f'fifth value: {next(a_words)}')# Raises exception
#except StopIteration:
#    print('The iterable has no more values left to give') 

# Iterator consumes values
for word in a_words:
    print(word) # normal output

for word in a_words:
    print(word) # no output

a_words = list(a_words)
print(a_words) # []
#!/usr/bin/pyhton3
# ex2.py
# Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method. Remember that you can only join collections of strings, so you’re going to need to do some initial processing of the list of numbers.

numbers = [1, 2, 3, 4, 5];
strings = [];
for num in numbers : 
    strings.append(str(num));

strings = ' | '.join(strings);

print(strings);


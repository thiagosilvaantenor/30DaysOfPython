#!/usr/bin/env python3
from operator import methodcaller
# 1) Use map to call the strip method on each string in the following list:

humpty_dumpty = [
    "  Humpty Dumpty sat on a wall,  ",
    "Humpty Dumpty had a great fall;     ",
    "  All the king's horses and all the king's men ",  
    "    Couldn't put Humpty together again."
]

# Print the lines of the nursery rhyme on different lines in the console.

# rhymes = map(lambda line: line.strip(), humpty_dumpty)
rhymes = map(methodcaller('strip'), humpty_dumpty)
print(*rhymes, sep="\n")
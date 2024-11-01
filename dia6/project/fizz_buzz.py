#!/bin/python3
# fizz_buzz

# Fizz Buzz
# A game where one player starts by saying the number 1, then each players takes it in turns to say the next number, one a at time. If the number is divisible by 3, instead of saying the number, the player should say, "Fizz".If the number is divisible by 5, instead of saying the number, the player should say, "Buzz".If the number is divisible by 3and5, instead of saying the number, the player should say, "Fizz Buzz".

# In this version, the computer is the only player, and it's going to play the first 100 rounds by itself. In other words, we need to print out the first 100 items in the sequence, starting from 1

for num in range(1,101) :
    if num % 3 == 0 and num % 5 == 0:
        print('Fizz Buzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

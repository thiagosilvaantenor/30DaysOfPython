#!/usr/bin/env python3
import random as rd
# 4) Use the randint function from the exercise above to create a new version of the guessing game we made in day 8. 
# This time the program should generate a random number, and you should tell the user whether their guess was too high, or too low, until they get the right number.


def guessing_game():
    num = rd.randint(1,100)
    game_continue = True
    while(game_continue):
        guess = int(input('Enter the guess, remember the number is between 1 and 100: '))
        if guess == num:
            print(f'Congrats you win, the number is {num}')
            game_continue = False
        elif guess > num:
            print(f'Wrong, the number is lower than {guess}')
        else:
            print(f'Wrong, the number is higher than {guess}')


guessing_game()
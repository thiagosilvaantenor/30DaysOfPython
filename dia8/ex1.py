#!/usr/bin/python3
# ex1.py
# 1) Write a short guessing game program using a while loop. The user should be prompted to guess a number between 1 and 100, and you should tell them whether their guess was too high or too low after each guess. The loop should keeping running until the user guesses the number correctly.

guess = 17
answer = input("Olá, descubra o número que estou pensando, ele esta entre 1 a 100")

while int(answer) != int(guess):
  if int(answer) > int(guess):
    print('Sua resposta foi maior que o núméro que pensei')
    answer = input("Olá, descubra o número que estou pensando, ele esta entre 1 a 100")
  elif int(answer) < int(guess):
    print('Sua resposta foi menor que o número que pensei')
    answer = input("Olá, descubra o número que estou pensando, ele esta entre 1 a 100")

print(f'Você acertou o número que pensei foi: {guess} ')
#!/usr/bin/python3
# ex4.py
# Ask the user to enter a word, and then print out the length of the word. You should account for any excess whitespace in the user’s input, so you’re going to have to process the string before you find its length.

#If you want to take this a little bit further, you an ask the user for a long piece of text. You can then tell them how many how many characters are in the text overall, and you can also provide them a word count.

word = input("Olá, informe uma palavra: ");


word = word.strip();

print(f'A quantidade de caracteries em: {word} é: {len(word)}')

phrase = input("Agora informe uma frase: ")

w_count = 0;
c_count = 0;

phrase = phrase.strip()
words = phrase.split()
w_count = len(words)
for w in words:
    for c in w:
        c_count = c_count + 1;


print(f'A quantidade de palvras na frase foi: {w_count} \ne a quantidade de caracteries foi: {c_count} ')
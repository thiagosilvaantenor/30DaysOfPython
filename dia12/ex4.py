# 4) Create a function to test if a word is a palindrome. A palindrome is a string of characters that are identical
# whether read forwards or backwards. For example, “was it a car or a cat I saw” is a palindrome.

def palindrome_word(word:str):
    #clean the word of whitespaces
    word.strip()
    #lower the word
    word = word.lower()
    #transfer each letter to a list with the original order of the word
    array_word = []
    for letter in word:
        array_word.append(letter)

    # creates a copy of the list, revert the order of each letter
    reverse_word = array_word.copy()
    reverse_word.reverse()
    #reverts the original list
    array_word.reverse()
    #test the two list, if it is equals than its a palindrome
    if array_word == reverse_word:
        print(f'The word {word} is a palindrome')
    else:
        print(f'The word {word} is not a palindrome')

    
palindrome_word(input('Enter the word to see if it is a palindrome: '))
    

#!/usr/bin/env python3
# A json reading list 
import json

#Verify if the json file exists
def create_book_file():
    try: # try to create the file
        with open("/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia18/project/books.json", "x") as reading_list:
            json.dump([], reading_list)
    # if already exists then raises a exeception and ignores it
    except FileExistsError:
        pass


def menu():
    option = '3'
    while '4' not in option:
        print("Enter the option:\n")
        option = input('1- Add book\n2- Show books\n3- Search a book in the file\n4- Quit : ')
        match option:
            case '1':
                add_book()
            case '2':
                books = read_books(file_path="/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia18/project/books.json")
                better_print_of_books(books)
            case '3':
                find_book(name=input('Enter the name of the book: '))
            case '4':
                print('Closing the program....')


def add_book():
    # get the list of books already written
    books = read_books("/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia18/project/books.json")
    stop = False
    while (stop != True):
        # reads the input
        book_name = input("Enter the book's name: ")
        book_author = input("Enter the author's name: ")
        book_year = int(input("Enter the book's year of publication: "))
        # apprends the new book on the list
        books.append({'name': book_name.strip(), 'author': book_author.strip(), 'year': book_year})
        # ask the user if they will add another book
        choice = input('Do you wish to add another book? y/n: ')
        if 'n'.lower() in choice.lower():
            stop = True
    
    with open("/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia18/project/books.json", mode="w") as f:
        # break the line
        json.dump(books, f)


def read_books(file_path:str):
    # open the file on the path
    with open(file_path, mode='r') as f:
        # reads and transforms the json in a list of dictionaries
        books:list = json.load(f)
        return books


def better_print_of_books(books:list):
        # iterates over the list of books
        for i in books:
            # for each dict on the list, takes the headers and values to print
            h_name, h_author, h_year = i.keys()
            i_name, i_author, i_year = i.values()
            print(f'{h_name.capitalize()}: {i_name} - {h_author.capitalize()}: {i_author} - {h_year.capitalize()}: {i_year} ')


def find_book(name:str):
    with open("/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia18/project/books.json", mode="r") as f:
        # Reads the json to a list of dictionaries
        books = json.load(f)
        is_in_the_list = False
        # iterates over the list to find the book with the given name
        for i in books:
            if name in i.values():
                # if it is, print the headers and the book
                headers = i.keys()
                book = i.values()
                print(" | ".join(headers))
                print(*book)
                is_in_the_list = True
        
        if is_in_the_list == False:
            print(f'The book: {name}, is not in the json list')
            
# calls the function to verify the json file when the program is executed
create_book_file()
# calls the menu when the program is executed
menu()

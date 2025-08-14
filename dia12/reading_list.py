# For this project the application needs to have the following functionality:

# Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
# The program should store information about all of these books in a Python list.
# Users should be able to display all the books in their reading list, and these books should be printed out in a user-friendly format.
# Users should be able to select these options from a text menu, and they should be able 
# to perform multiple operations without restarting the program.

books = []

def add_book():
    title = input('Enter the title of the book: ')
    author = input("Enter the author's name of the book: ")
    year = input('Enter the year of publication of the book: ')

    book = {'title': title, 
        "author": author,
        "year": year }

    books.append(book)

def view_books():
    for i in books:
        print(f'{i.get('title')} by {i.get('author')} published in {i.get('year')}')

option = ''
while(option != '3'):
    option = input('1-Add book\n2-Show all books\n3-Quit\n: ')
    match(option):
        case '1':
            add_book()
        case '2':
            view_books()
        case '3':
            print('Closing the program ...')
        case _:
            print('Opção invalida...')

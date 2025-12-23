#/usr/bin/env python3
# Operations for managing books

from file.file import get_all_books, save_all_books

BOOKS_FILE = 'books.json'

def get_book_file():
    return BOOKS_FILE

def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')
    #Transform the name to title case
    mark_book_as_read(name.title())


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    save_all_books(books)
#/usr/bin/env python3
# Operations for managing books

from file.file import save_all_books, delete_book

def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')
    # Transform the name and author to title case
    insert_book(name.title(), author.title())


def insert_book(name, author):
    from file.file import get_all_books
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    save_all_books(books)

def list_books():
    from file.file import get_all_books
    for book in get_all_books():
        read = 'YES' if book['read'] == '1' else 'NO'  # book[3] will be a falsy value (0) if not read
        print(f"{book['name']} by {book['author']} — Read: {read}")


def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')
    #Tramsform the name to title case
    delete_book(name.title())

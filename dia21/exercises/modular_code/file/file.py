# !/usr/bin/env python3
# File operations for managing books
import json


BOOKS_FILE = "books.json"

def create_book_table():
    try:
        with open(BOOKS_FILE, 'x') as file:
            json.dump([], file)  # initialize file as empty list
    except FileExistsError:
        pass

def get_all_books():
    with open(BOOKS_FILE, 'r') as json_file:
        return json.load(json_file)

def save_all_books(books):
    with open(BOOKS_FILE, 'w') as file:
        json.dump(books, file)

def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    save_all_books(books)
#/usr/bin/env python3
# Menu for the book management application
import book.operations as book_ops
import book.info_book as info_book
import file.file as file_ops

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """
BOOKS_FILE = 'books.json'


def menu():
    file_ops.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            book_ops.prompt_add_book()
        elif user_input == 'l':
            book_ops.list_books()
        elif user_input == 'r':
            info_book.prompt_read_book()
        elif user_input == 'd':
            book_ops.prompt_delete_book()

        user_input = input(USER_CHOICE)

menu()
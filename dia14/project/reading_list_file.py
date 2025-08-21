#!/bin/python3
# reading list that stores the data in a csv file
# For this project the application needs to have the following functionality:
#     Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
#     The program should store information about all of these books in a file called books.csv, and this data should be stored in CSV format.
#     Users should be able to retrieve the books in their reading list, and these books should be printed out in a user-friendly format.
#     Users should be able to search for a specific book by providing a book title.
#     Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program.


def menu():
    option = '4'
    while '3' not in option:
        print("Enter the option:\n")
        option = input('1- Add book\n2- Show books\n3-quit : ')
        match option:
            case '1':
                # reads the input
                book_name = input("Enter the book's name: ")
                book_autor = input("Enter the autor's name: ")
                book_year = int(input("Enter the book's year of publication: "))

                book = {'name': book_name.strip(), 'autor': book_autor.strip(), 'year': book_year}
                add_book(book)
            case '2':
                read_books(file_path="/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia14/assets/books.csv")
            case '3':
                print('Closing the program....')



def create_headers(headers):
    with open("/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia14/assets/books.csv", mode="w") as f:
        f.write(",".join(headers))


def stores_in_csv_file(book:dict):
    with open("/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia14/assets/books.csv", mode="a") as f:
        # break the line
        f.write("\n") 
        for count,info in enumerate(book.values()):
            # if is not the last item then write the info and a comma
            if count < (len(book) -1):
                f.write(f"{str(info)},")
            else:
                # if it is the last one, then just write the info
                f.write(str(info))
        

def add_book(book:dict):
    # Reads the file to see if it is the first book
    with open("/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia14/assets/books.csv", mode="r") as f:
        if len(f.readlines()) == 0: # if it its, then create the headers
            create_headers(book.keys())
    # stores in the file
        stores_in_csv_file(book)


def read_books(file_path:str):
    with open(file_path, mode='r') as f:
        books = f.readlines()
        headers = books[0].strip().split(',')
        for i in books[1:]:
            h_name, h_autor, h_year = headers
            i_name, i_autor, i_year = i.split(',')
            print(f'{h_name.capitalize()}: {i_name} - {h_autor.capitalize()}: {i_autor} - {h_year.capitalize()}: {i_year} ')

menu()

        



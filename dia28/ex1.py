# Day 14 projct with type hinting
from typing import Union

Book = dict[str, Union[str, int]]


def menu():
    option: str = "4"
    while "3" not in option:
        print("Enter the option:\n")
        option: str = input(
            "1- Add book\n2- Show books\n3- Search a book in the file\n4- Quit : "
        )
        match option:
            case "1":
                # reads the input
                book_name: str = input("Enter the book's name: ")
                book_autor: str = input("Enter the autor's name: ")
                book_year: int = int(input("Enter the book's year of publication: "))

                book: Book = {
                    "name": book_name.strip(),
                    "autor": book_autor.strip(),
                    "year": book_year,
                }
                add_book(book)
            case "2":
                read_books(
                    file_path="/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia14/assets/books.csv"
                )
            case "3":
                find_book(name=input("Enter the name of the book: "))
            case "4":
                print("Closing the program....")


def create_headers(headers: str):
    with open(
        "/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia14/assets/books.csv",
        mode="w",
    ) as f:
        f.write(",".join(headers))


def stores_in_csv_file(book: Book):
    with open(
        "/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia14/assets/books.csv",
        mode="a",
    ) as f:
        # break the line
        f.write("\n")
        for count, info in enumerate(book.values()):
            # if is not the last item then write the info and a comma
            if count < (len(book) - 1):
                f.write(f"{str(info)},")
            else:
                # if it is the last one, then just write the info
                f.write(str(info))


def add_book(book: Book):
    # Reads the file to see if it is the first book
    with open(
        "/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia14/assets/books.csv",
        mode="r",
    ) as f:
        if len(f.readlines()) == 0:  # if it its, then create the headers
            # fallback incase keys returns a int
            headers: str = str(book.keys())
            create_headers(headers)
        # stores in the file
        stores_in_csv_file(book)


def read_books(file_path: str):
    with open(file_path, mode="r") as f:
        books: list[str] = f.readlines()
        headers: list[str] = books[0].strip().split(",")
        for i in books[1:]:
            h_name, h_autor, h_year = headers
            i_name, i_autor, i_year = i.split(",")
            print(
                f"{h_name.capitalize()}: {i_name} - {h_autor.capitalize()}: {i_autor} - {h_year.capitalize()}: {i_year} "
            )


def find_book(name: str):
    with open(
        "/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia14/assets/books.csv",
        mode="r",
    ) as f:
        end: bool = False
        # Reads the header first
        line: str = f.readline()
        # Search the name in the book
        while end != True:
            # If find it print the book and quit the loop
            if name.lower() in line.lower():
                book: list[str] = line.split(",")
                print(", ".join(book))
                end = True
            # If not, then go to the next line
            line = f.readline()


menu()

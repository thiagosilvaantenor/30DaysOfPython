## namedtuple

from collections import defaultdict, namedtuple

# Creates a template for a tuple with keyword arguments
Book = namedtuple("Book", ["title", "author", "year"])

book = Book(title="The Book Thief", author="Markus Zusak", year=2005)

print(f"{book.title} ({book.year}), by {book.author}")


# partial

from functools import partial

def exponentiate(base, exponent):
    return base ** exponent

# creates a new function using a existing one as base and declaring a value for one of the arguments
square = partial(exponentiate, exponent=2)
cube = partial(exponentiate, exponent=3)

print(f'square function: 4² = {square(4)}')
print(f'cube function: 5³ = {cube(5)}')
print(f'exponentiate function: base= 4, exponent= 4  = {exponentiate(4,4)}')


# defaultdict

from collections import defaultdict



User = namedtuple("User", ["name", "username", "location"])

# Takes a function that will be call when it dosent find the key in the dictionary inform
users = defaultdict(
    lambda: "Could not find a user matching that user id;",
    {
        "0001": User("Phil", "pbest", "Hungary"),
        "0002": User("Joseph", "joeph", "Canada"),
        "0003": User("Alan", "alanzoka", "Brazil")
    }
)

user_id = input("Please enter a user id: ")
print(users[user_id])

# int makes defaultdict useful for count 
inventory = defaultdict(int)

def add_item(item, amount):
    inventory[item] += amount

# if (item not yet in inventory then 0 + amount)
add_item("bow", 1)
add_item("arrow", 20)
# if (item alredy in inventory then old_amount + new_amount)
add_item("arrow", 20) 
add_item("bracer", 2)     

print(inventory)



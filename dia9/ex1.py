#/bin/python3
# Notes:
# Enumerate - unpack or destructing elements

# names = ['Jhon', 'Will', 'Rachel']

# for counter, name in enumerate(names,start=1):
#     print(f'{counter}. {name}')

# Zip - Use list(zip()) to avoid bugs with iterators

# pet_owners = ["Paul", "Andrea", "Marta"]
# pets = ["Fluffy", "Bubbles", "Captain Catsworth"]

# for owner, pet in zip(pet_owners, pets):
#     print(f"{owner} owns {pet}.")
# ////////////////////Exercice///////////////////////////////////
main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

#1. Write a for loop that uses destructuring so that you can print each tuple in the following format:

# BoJack Horseman is a horse voiced by Will Arnet.

for counter, (character, actor, animal),  in enumerate(main_characters):
    print(f'{character} is a {animal.lower()} voiced by {actor}.')

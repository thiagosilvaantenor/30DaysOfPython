# Ex1: Ask the user for an integer between 1 and 10 (inclusive). 
# If the number they give is outside of the specified range,
# raise a ValueError and inform them that their choice was invalid.


def identify(num):
    try:
        i_num = int(num)
    except ValueError as e:
        raise ValueError(f"Oops, this program only works with numbers, but you inform something else: {num}")
    if i_num <= 0 or i_num > 10:
        raise ValueError(f"Oops, you inform a number outside the especific range: {i_num}")
    else:
        print(f"Your choice was correct: {i_num}")



num = input("Hello, please inform a number between 1 and up to 10: ")
identify(num)
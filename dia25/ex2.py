import string


def ascii_str_check(value):
    for character in value:
        if character not in (string.ascii_letters):
            print(f"{value} is not a string with exclusively ASCII letters")
            return
    print(f"{value} is a string with exclusively ASCII letters")


ascii_str_check(input("Inform a string to be tested: "))

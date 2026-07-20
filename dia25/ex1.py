def greet_user():
    return input("What's your name? ").strip().title() or "World"


print(greet_user())

# AND evaluetes the values
# if the first value is False, returns the first evaluation
v1 = 0
v2 = True
print(v1 and v2)
# If the first is evaluation is True, returns the evaluation of the second withou checking
print(v2 and v2)
v1 = True
v2 = False
print(v1 and v2)
print(v2 and v1)

# OR: returns the first operand if it's truthy, otherwise it returns the second operand
v1 = 4
v2 = 0
print(v1 or v2)
print(v2 and v1)

# using or to replace falsy values
name = input("Please enter your name: ").strip().title() or "Player"

# using and
result = 6 / 2

if result and result.is_integer():
    print(f"the division produces an integer result")

# check multiple values using in

proceed = input("Would u like to continue? ").strip().lower()

if proceed in ("y", "yes", "continue"):
    ...

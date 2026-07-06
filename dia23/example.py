## Iter
numbers = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers)

# print(numbers_iter)  # <list_iterator object at 0x7f57d138af70>
print(next(numbers_iter))  # 1
print(next(numbers_iter))  # 2

## Replicating for with iter

numbers = [1,2,3,4]
numbers_iter = iter(numbers)

while True:
    try:
        number = next(numbers_iter)
    except StopIteration:
        break
    else:
        print(number)


## Generator
# def first_hundred():
#     print("First value requested\n")
#     for num in range(1,101):
#         print("Starting new iteration")
#         yield num
#         print("Ending this iteration\n")

# # Generates a iterator
# g = first_hundred()
# # print(g) # <generator object first_hundred at 0x7fbc0f90cee0>
# print(next(g)) # 1
# print(next(g)) # 2
# print(next(g)) # 3

## Generator Expressions - Kinda like the comphreesions
squares = (number ** 2 for number in range(1,11))
print(squares) # <generator object <genexpr> at 0x7f33225a0c80>

for square in squares:
    print(square)

squares = (number ** 2 for number in range(1,11))

print(*squares, sep=", ")

#You don't need the () when using generator expressions as a sole argument in functions or methods
squares = sum(number ** 2 for number in range(1,11))
print(squares)

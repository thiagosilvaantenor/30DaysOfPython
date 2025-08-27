#!/usr/bin/env python3
# Exception Handling
import math

# Trying to convert a input str in a int
# while True:
#     try:
#         number = int(input("Please enter a whole number: "))
#         break
#     except ValueError:
#         print("You didn't enter a valid integer!")

# Dealing with multiple exceptions
def average(numbers):
    try:
        mean = math.fsum(numbers) / len(numbers)
        print(mean)
    except ZeroDivisionError:
        print(0)
    except TypeError:
        print("You provided invalid values!")
    # except (ZeroDivisionError, TypeError):
    #     print("An average cannot be calculated for the values you provided.")

# finally executes everytime, with or without exception
def finally_flex():
    try:
        return
    finally:
        print("You return when I say you can return...")

finally_flex()

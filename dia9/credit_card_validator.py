#!/bin/python3
# Recevies a Credit Card number from user to validate with the Lumn algorithm

original_number = input('Type the credit card number you want to test it ')
original_number = original_number.strip()

original_list = list(original_number)

# Remove the rightmost digit from the card number. This number is called the checking digit, and it will be excluded from most of our calculations.
last_digit = original_list.pop()
# Reverse the order of the remaining digits.
original_list.reverse()

#Create a list to sum the integers
numbers_list = []

# For this sequence of reversed digits, 
# take the digits at each of the even indices (0, 2, 4, 6, etc.) and double them.
# If any of the results are greater than 9, subtract 9 from those numbers.
for index, i in enumerate(original_list):
    # Verify if index is even
    if ((index % 2) == 0):
        # if is then double the value
        double_i = int(i)*2
        if (double_i > 9):
            double_i = double_i - 9
        numbers_list.append(double_i)
    else:
        numbers_list.append(int(i))

# Add together all of the results and add the checking digit.
sum_numbers = int(last_digit) + sum(numbers_list)

# If the result is divisible by 10, the number is a valid card number.
if ((sum_numbers % 10) == 0):
    print(f'The card number: {original_number} is a valid card number')
# If it's not, the card number is not valid
else:
    print(f'The card number: {original_number} is not a valid card number')
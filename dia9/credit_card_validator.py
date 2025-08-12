# /bin/python3
# Recevies a Credit Card number from user to validate with the Lumn algorithm

original_number = str(input('Type the credit card number you want to test it '))
original_number = original_number.strip()

lista = list(original_number)
original_list = lista

# Remove the rightmost digit from the card number. This number is called the checking digit, and it will be excluded from most of our calculations.
last_digit = lista.pop()
# Reverse the order of the remaining digits.
lista.reverse()

# For this sequence of reversed digits, 
# take the digits at each of the even indices (0, 2, 4, 6, etc.) and double them.
# If any of the results are greater than 9, subtract 9 from those numbers.
for counter, item in enumerate(lista):
    # Verify if index is even
    index = counter
    if ((index % 2) == 0):
        # if is then double the value
        double_i = int(item)*2
        if (double_i > 9):
            double_i = double_i - 9
        lista[index] = str(double_i)

# Add together all of the results and add the checking digit.
sum = 0

for i in lista:
    sum = sum + int(i)
sum = sum + int(last_digit)

# If the result is divisible by 10, the number is a valid card number.
if ((sum % 10) == 0):
    print(f'The card number: {original_number} is a valid card number')
# If it's not, the card number is not valid
else:
    print(f'The card number: {original_number} is not a valid card number')
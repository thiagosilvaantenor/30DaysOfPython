#4) Write a function that takes in a single number and returns True or False depending on whether or not the number is prime.

def is_prime(number:int):
    for i in range(2,number):
        if (number % i) == 0:
            return False
    return True

print( is_prime( number= int( input('Enter the number to see if it is a prime number') ) ) )
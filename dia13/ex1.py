#/bin/python3
# 1) Define a exponentiate function that takes in two numbers.
# The first is the base, and the second is the power to raise the base to.
# The function should return the result of this operation. Remember we can perform exponentiation using the ** operator.

def expo(base:int, exponent:int):
    return base ** exponent

print( expo( base= int( input('Enter the base number') ), exponent= int( input('Enter the power to raise') ) ) )
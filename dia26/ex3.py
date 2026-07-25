# 3) Use the mul function in the operator module to create a 
# partial called double that always provides 2 as the first argument.

from functools import partial
from operator import mul


double = partial(mul, 2)


b = int(input('Inform the a number to me muliply for 2: '))

print(double(b))

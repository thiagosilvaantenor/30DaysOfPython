#!/usr/bin/env python3
# imports


# basic imports
import math

# varibles from the import, example varible with the value of pi
print(f'pi = {math.pi}')

# functions from the import, example fsum is a better alternative to 'sum' when using floats
numbers = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
print(f'fsum = {math.fsum(numbers)}')

# Importing specific things from modules
from math import pi,tau
print(pi, tau)

#using alias
# import numpy as np
# the line above is commented because you need to install numpy since is a third party module

# the bad way of importing
from math import *
print(globals())
# this can lead to name conflicts
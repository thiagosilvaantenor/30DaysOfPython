#!/usr/bin/env python3
# 5) Modify your code from exercise 4 so that each number prints on a different line.
# You can only use a single print call.

numbers = range(1,21)
print(*numbers,sep='\n')
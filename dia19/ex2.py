#!/usr/bin/env python3
# 2) Investigate what happens when there is a return statement in both the try clause and finally clause of a try statement.

def try_finnaly_return():
    try:
        return 'Try'
    finally:
        return 'Finnaly'

print(try_finnaly_return())
# Skips the return in the try block and prints Finnaly
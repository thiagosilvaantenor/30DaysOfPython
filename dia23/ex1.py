# 1) Write a generator that generates prime numbers in a specified range. You can make use of your solution to exercise 3 from day 8 as a starting point.

def prime_generator(limit: int):
    j = 0

    for i in range(2,limit+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i


result = prime_generator(int(input("Hi, inform the specific range of prime numbers: ")))

while True:
    try:
        prime = next(result)
    except StopIteration:
        break
    else:
        print(prime)
 

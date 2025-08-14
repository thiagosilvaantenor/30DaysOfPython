#1) Try to approximate the behaviour of the is operator using ==. Remember we have the id function for finding the memory address for a given value, and we can compare memory addresses to check for identity.
print('Exercise 1:')
a = [1,2,3]
b = [1,2,3]

print(id(a) is id(b))
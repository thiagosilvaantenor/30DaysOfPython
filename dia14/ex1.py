# 1. Rewrite the following piece of code using a context manager:

#  f = open("hello_world.txt", "w")
#  f.write("Hello, World!")
#  f.close()

with open("/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia14/assets/hello_word.txt",  mode="w") as f:
    f.write("Hello, World!")


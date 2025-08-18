# 2. Use append mode to write "How are you?" on the second line of the hello_world.txt file above.

with open("/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia14/assets/hello_word.txt",  mode="a") as f:
    f.write("\nHow are you")
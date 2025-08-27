# 3) Imagine you have a file named data.txt with this content:

# 'There is some data here!'

# Open it for reading using Python, but make sure to use a try block to catch an exception that arises if the file doesn't exist. 
# Once you've verified your solution works with an actual file, delete the file and see if your try block is able to handle it.
# When files don't exist when you try to open them, the exception raised is FileNotFoundError.

try:
    # Change the PATH and test it
    with open('/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia19/data.txt', mode='r') as f:
        # since it needs to have something in this block
        pass
except FileNotFoundError:
    print('File not found!')

        
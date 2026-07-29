# 4) Create a read function using a partial that opens 
# a file in read ("r") mode.

from functools import partial
from pathlib import Path


read_partial = partial(open, mode='r')

# Get the directory
script_dir = Path(__file__).parent.resolve()
# get the file location
file_loc = script_dir / "./assets/ex4_reading_file.md"

with read_partial(file=file_loc) as reader:
    print(reader.readlines())
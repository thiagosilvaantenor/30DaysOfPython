# Exceptions advanced
from pathlib import Path


"/home/thiago/projetos/estudos/30DaysOfPython/"

script_dir = Path(__file__).parent.resolve()

file_path = script_dir / "./numbers.txt"
# "/home/thiago/projetos/estudos/30DaysOfPython/dia24/numbers.txt"
print(file_path)

def identify(number):
    try:
        return int(number)
    except ValueError:
        try:
            flo_number = float(number)
        except ValueError:
            raise ValueError(f"could not convert string to an integer: {number}") from None
        else:
            return round(flo_number)

with open(file_path, "r") as numbers_file:
    numbers = [identify(number) for number in numbers_file]

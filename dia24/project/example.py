import argparse

parser = argparse.ArgumentParser(description="Returns a number raised to a specified power.")

parser.add_argument("base", type=float, help="A number to raise to the specified power")

parser.add_argument(
"-e", 
"--exponent", 
type=float,
default=2,
help="A power to raise the provided base number"
)

args = parser.parse_args()

print(args.base ** args.exponent)
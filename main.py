#!/usr/bin/env python3

"""The main module for the decimal-to-binary converter program.

This program allows the user to input a non-zero number of real
numbers to convert to their binary equivalent. It is assumed that
the input is, in fact, real numbers.

This file can be run as `./main.py [-h] args [args ...]`
"""


import argparse


from src.conversion import Converter


def main():
    """Run the decimal-to-binary program."""
    parser = argparse.ArgumentParser(
        prog="Decimal to Binary Converter",
        description="A python script to convert decimal integers and floats to their binary equivalent.",
        usage="./main.py [-h] args [args ...]",
    )

    parser.add_argument(
        "decNum", nargs="+", help="Decimal number(s) to be converted to binary."
    )

    args = parser.parse_args()

    converter = Converter(args.decNum)

    print(converter.output())


if __name__ == "__main__":
    main()

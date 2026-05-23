#!/usr/bin/env python3

"""The main entry point for the decimal-to-base converter program

This program allows the user to input a non-zero base to convert
to and a non-zero amount of real, decimal numbers to convert to their chosen
base equivalent. It is assumed that the input is, in fact, real numbers.
"""


import argparse

from src import Converter


def main():
    parser = argparse.ArgumentParser(
        prog="Base-10 to Base-X Converter",
        description="Script to convert decimal numbers to another base",
    )

    parser.add_argument("base_num", help="Base to convert to")

    parser.add_argument(
        "dec_num", nargs="+", help="Decimal number(s) to be converted to another base"
    )

    parser.add_argument(
        "-r",
        "--round",
        type=int,
        default=8,
        help="Maximum number of decimal points allowed for in the output (default: 8)",
    )

    args = parser.parse_args()

    converter = Converter(args.base_num, args.dec_num, args.round)

    print(converter.output())


if __name__ == "__main__":
    main()

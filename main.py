#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(
            prog="Decimal to Binary Converter",
            description="A python script to convert decimal integers and floats to their binary equivalent.")

    parser.add_argument(
            'decimals',
            nargs='+',
            help="Decimal number(s) to be converted to binary.")

    args = parser.parse_args()

    print(args)

    return

if __name__ == "__main__":
    main()

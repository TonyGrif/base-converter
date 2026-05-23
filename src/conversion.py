"""This module holds the Converter class for base conversions"""

from typing import Union


class Converter:
    """Responsible for converting a base-10 input to the new given base

    Attributes:
        base: The target base to convert to
        conversions: A list of dictionaries of conversions
            This contains [base-10] and [base-{base}] fields
        length: Maximum number of fractional digits in the output
    """

    def __init__(
        self, base: int, decimals: list[Union[int, float]], length: int = 8
    ) -> None:
        """Constructor for the Converter class

        Parameters:
            base: The base to convert to
            decimals: List of decimals to be converted
            length: Maximum number of fractional digits in the output
        """
        self.length = length

        self.base = int(base)
        base_val = f"base-{str(base)}"

        self.conversions = []

        for num in decimals:
            conversion: dict[str, Union[int, float, str]] = {}
            conversion["base-10"] = num
            conversion[base_val] = self.convert_to_base(self.base, num)
            self.conversions.append(conversion)

    def convert_to_base(self, base: int, num: Union[int, float]) -> str:
        """Converts a base-10 number to the new base given

        Parameters:
            base: The base number to convert to
            num: The number to be converted

        Returns:
            base_str: The base string representation
        """
        parts = []

        if float(num) < 0:
            parts.append("-")

            if float(num).is_integer():
                num = abs(int(num))
            else:
                num = abs(float(num))

        if float(num) >= 1:
            str_num = str(num).split(".")
            parts.extend(self._int_part_to_base(base, int(str_num[0])))

            try:
                dec_num = float("." + str_num[1])
                parts.append(".")
                parts.extend(self._decimal_part_to_base(base, dec_num))
            except IndexError:
                pass
        else:
            parts.append("0.")
            parts.extend(self._decimal_part_to_base(base, float(num)))

        return "".join(parts)

    def _int_part_to_base(self, base: int, num: int) -> list[str]:
        """Convert integer part of a number to the given base

        Parameters:
            base: The base to convert to
            num: The number to be converted

        Returns:
            digits: List of digit characters representing the integer part
        """
        digits = []
        integer = int(num)

        for _ in range(self.length):
            rem = integer % base
            digits.append(str(rem))
            integer = integer // base

            if integer < 1:
                break

        digits.reverse()
        return digits

    def _decimal_part_to_base(self, base: int, num: float) -> list[str]:
        """Convert decimal point number to the given base

        Parameters:
            base: The base to convert to
            num: The number to be converted

        Returns:
            digits: List of digit characters representing the fractional part
        """
        digits = []
        bit = float(num)

        for _ in range(self.length):
            bit *= base
            digit = int(bit)
            digits.append(str(digit))
            bit -= digit
            if bit == 0:
                return digits

        return digits

    def output(self) -> str:
        """Returns a formatted table to the user with the conversions

        This table will be formatted as such:

        | Base-10 | Base-X |
        | ------- | ------ |
        |  {Dec}  |  {Num} |

        Returns:
            table: A string containing the table
        """
        base_val = f"base-{self.base}"
        base_header = f"Base {self.base}"
        dec_header = "Base 10"

        col1 = (
            max(len(dec_header), max(len(str(c["base-10"])) for c in self.conversions))
            + 2
        )
        col2 = (
            max(len(base_header), max(len(str(c[base_val])) for c in self.conversions))
            + 2
        )

        table = (
            "| " + dec_header.center(col1) + " | " + base_header.center(col2) + " |\n"
        )
        table += "| " + "-" * col1 + " | " + "-" * col2 + " |\n"

        for conversion in self.conversions:
            table += (
                "| "
                + str(conversion["base-10"]).center(col1)
                + " | "
                + str(conversion[base_val]).center(col2)
                + " |\n"
            )

        return table

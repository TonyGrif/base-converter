"""This module holds the Converter class."""


class Converter:
    """Responsible for converting a base-10 input to the new base given.

    Attributes:
        base (int): The base to convert to.
        conversions (list): A list of dictionaries of conversions.
            This contains [base-10] and [base-{base}] fields.
    """

    def __init__(self, base: int, decimals: list) -> None:
        """Constructor for the Converter class.

        Parameters:
            base (int): The base to convert to.
            decimals (list): List of decimals to be converted.
        """
        self._length = 8  # Max number of digits

        self.base = int(base)
        base_val = f"base-{str(base)}"

        self.conversions = []

        for _, num in enumerate(decimals):
            conversion = {}
            conversion["base-10"] = num
            conversion[base_val] = self.convert_to_base(self.base, num)
            self.conversions.append(conversion)

    def convert_to_base(self, base: int, num: int or float) -> str:
        """Converts a base-10 number to the new base given.

        Parameters:
            base (int): The base number to convert to.
            num (int or float): The number to be converted.

        Returns:
            base_str (str): The base string representation.
        """
        base_str = ""

        if float(num) < 0:
            base_str += "-"

            if float(num).is_integer():
                num = abs(int(num))
            else:
                num = abs(float(num))

        if float(num) >= 1:
            str_num = str(num).split(".")

            int_num = str_num[0]

            # TODO: handle different base case
            base_str += self._int_part_to_binary(int(int_num))

            # TODO: clean up
            try:
                dec_num = str_num[1]
                dec_num = float("." + dec_num)

                base_str += "."
                base_str += self._decimal_part_to_base(self.base, float(dec_num))
            except IndexError:
                pass
        else:
            # Run just decimal conversion
            base_str += "0."
            base_str += self._decimal_part_to_base(self.base, float(num))

        return base_str

    def _decimal_part_to_base(self, base: int, num: float) -> str:
        """Convert decimal point number to base.

        Parameters:
            base (int): The base to convert to.
            num (float): The number to be converted.

        Returns:
            base_str (str): The base string representation.
        """
        base_str = ""

        bit = float(num)

        for _ in range(self._length):
            bit = bit * base

            if bit > 1:
                split = str(bit).split(".")

                base_str += split[0]
                bit = bit - int(split[0])

                if bit == 0:
                    return base_str
            elif bit == 1:
                base_str += "1"
                return base_str
            else:
                base_str += "0"

        return base_str

    def _int_part_to_binary(self, num: int) -> str:
        """Convert integer part of a number to binary.

        Parameters:
            num (int): The number to be converted.

        Returns:
            bin_str (str): The binary string representation.
        """
        bin_str = ""
        integer = int(num)

        for _ in range(self._length):
            rem = integer % 2

            if rem == 1:
                bin_str += "1"
            else:
                bin_str += "0"

            integer = integer // 2

            if integer < 1:
                break

        return bin_str[::-1]

    def output(self) -> str:
        """Returns a formatted table to the user with the conversions.

        This table will be formatted as such:

        | Base-10 | Base-2 |
        | ------- | ------ |
        |  {Dec}  |  {Bin} |

        Returns:
            table (str): A string containing the table.
        """
        base_val = "base-" + str(self.base)
        spacing = self._length + 3
        table = ""

        table += "| " + "Base 10".center(spacing) + " | "
        table += f"Base {self.base}".center(spacing) + " |" + " \n"

        table += "| " + "-" * spacing + " | " + "-" * spacing + " |" + "\n"

        for conversion in self.conversions:
            table += (
                "| "
                + str(conversion["base-10"]).center(spacing)
                + " | "
                + str(conversion[base_val]).center(spacing)
                + " |"
                + "\n"
            )

        return table

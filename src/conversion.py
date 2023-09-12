"""This module holds the Converter class."""


class Converter:
    """Responsible for converting a decimal input to binary.

    Attributes:
        conversions (list): A list of dictionaries of conversions.
            This contains [base-10] and [base-2] fields.
    """

    def __init__(self, decimals: list) -> None:
        """Constructor for the Converter class.

        Parameters:
            decimals (list): List of decimals to be converted.
        """
        self._length = 8  # Max number of digits

        self.conversions = []

        for _, num in enumerate(decimals):
            conversion = {}
            conversion["base-10"] = num
            conversion["base-2"] = self.convert_to_binary(num)
            self.conversions.append(conversion)

    def convert_to_binary(self, num: int or float) -> str:
        """Converts a decimal number to its binary representation.

        Parameters:
            num (int or float): The number to be converted.

        Returns:
            bin_str (str): The binary string representation.
        """
        bin_str = ""
        int_num = None
        dec_num = None
        
        if float(num) < 0:
            bin_str += "-"
            num = abs(float(num))
        else:
            pass

        if float(num) >= 1:
            str_num = str(num).split('.')

            int_num = str_num[0]
            bin_str += self._int_part_to_binary(int(int_num))

            try:
                dec_num = str_num[1]
            except IndexError:
                pass

            return bin_str
        else:
            # Run just decimal conversion
            bin_str += "0."
            bin_str += self._decimal_part_to_binary(num)

            return bin_str

    def _decimal_part_to_binary(self, num: float) -> str:
        """Convert decimal point number to binary.

        Parameters:
            num (float): The number to be converted.

        Returns:
            bin_str (str): The binary string representation.
        """
        bin_str = ""

        bit = float(num)

        for _ in range(self._length):
            bit = bit * 2

            if bit > 1:
                bin_str += "1"
                bit = bit - 1
            elif bit == 1:
                bin_str += "1"
                return bin_str
            else:
                bin_str += "0"

        return bin_str

    def _int_part_to_binary(self, num: int) -> str:
        """Convert integer part of a number to binary.

        Parameters:
            num (int): The number to be converted.

        Returns:
            bin_str (str): The binary string representation.
        """
        bin_str = ""
        bit = int(num)

        for _ in range(self._length):
            rem = bit % 2

            if rem == 1:
                bin_str += "1"
            else:
                bin_str += "0"

            bit = bit // 2

            if bit < 1:
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
        spacing = self._length + 3
        table = ""

        table += "| " + "Base 10".center(spacing) + " | "
        table += "Base 2".center(spacing) + " |" + " \n"

        table += "| " + "-" * spacing + " | " + "-" * spacing + " |" + "\n"

        for conversion in self.conversions:
            table += (
                "| "
                + str(conversion["base-10"]).center(spacing)
                + " | "
                + str(conversion["base-2"]).center(spacing)
                + " |"
                + "\n"
            )

        return table

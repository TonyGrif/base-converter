"""This module holds the Converter class."""


class Converter:
    """Responsible for converting a decimal input to binary.

    Attributes:
        conversions (dictionary): A dictionary of conversions.
            This contains [base-10] and [base-2] fields.
    """

    def __init__(self, decimals: list) -> None:
        """Constructor for the Converter class.

        Parameters:
            decimals (list): List of decimals to be converted.
        """
        self._length = 8
        
        self.conversions = {}

        for count, num in enumerate(decimals):
            self.conversions[count] = {}
            self.conversions[count]["base-10"] = num
            self.conversions[count]["base-2"] = self.convert_to_binary(num)


    def convert_to_binary(self, num: int or float) -> str:
        """Converts an integer of float number to its binary representation.

        Parameters:
            num (int or float): The number to be converted.

        Returns:
            binStr (str): The binary string representation.
        """
        binStr = ""

        if float(num) < 1:
            binStr += "0."

        bit = float(num)

        for x in range(self._length):
            bit = bit * 2
            print(str(bit) + "\n")

            if bit > 1:
                binStr += '1'
                bit = bit - 1
            elif bit == 1:
                binStr += '1'
                return binStr
            else:
                binStr += '0'

        return binStr

    def output(self) -> str:
        """Returns a formatted table to the user with the conversions.

        This table will be formatted as such:

        | Base-10 | Base-2 |
        | ------- | ------ |
        |  {Dec}  |  {Bin} |

        Returns:
            table (str): A string containing the table.
        """
        table = ""

        table += "| " + "Base 10".center(self._length) + " |"
        table += " Base 2".center(self._length) + " |" + " \n"

        table += "| " + "-" * self._length + " | " + "-" * self._length + " |" + "\n"

        for count in range(len(self.conversions)):
            table += (
                "| "
                + str(self.conversions[count]["base-10"]).center(self._length)
                + " | "
                + str(self.conversions[count]["base-2"]).center(self._length)
                + " |"
                + "\n"
            )

        return table

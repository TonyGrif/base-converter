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
        # bit = num * 2

        # if remainder == 1

        return None

    def output(self) -> str:
        """Returns a formatted table to the user with the conversions.

        Returns:
            table (str): A string containing the table.
        """
        table = ""

        table += "| " + "Base 10".center(8) + " | " + "Base 2".center(8) + " |" + " \n"
        table += "| " + "-"*8 + " | " + "-"*8 + " |" + "\n"

        for count in range(len(self.conversions)):
            table += "| " + str(self.conversions[count]["base-10"]).center(8) + " | " + str(self.conversions[count]["base-2"]).center(8) + " |" + "\n"

        return table

"""This module holds the Converter class."""


class Converter:
    """Responsible for converting a numerical input to its binary representation.

    Attributes:
        decimals (list): Numbers to be converted to base-2. 
        binaries (list): Binary numbers post-conversion.
    """

    def __init__(self, decimals: list) -> None:
        """Constructor for the Converter class.

        Parameters:
            decimals (list): List of decimals to be converted.
        """
        self.conversions = {}

        for num in decimals:
            self.conversions[num] = {}
            self.conversions[num]["base-2"] = self.convert_to_binary(num)


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
        pass

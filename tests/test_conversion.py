import pytest


from conversion import Converter 


class TestConverstion:
    def test_positiveInteger(self):
        pass

    def test_negativeInteger(self):
        pass

    def test_positiveDecimal(self):
        convert = Converter([0.5, 0.25, 0.75])

        # assert convert.conversions[0.5]["base-2"] == "0.1"
        # assert convert.conversions[0.25]["base-2"] == "0.01"
        # assert convert.conversions[0.75]["base-2"] == "0.11"
        pass

    def test_negativeDecimal(self):
        pass

    def test_output(self):
        pass

import pytest


from conversion import Converter 


class TestConverstion:
    def test_positiveInteger(self):
        pass

    def test_negativeInteger(self):
        pass

    def test_positiveDecimal(self):
        assert Converter.convertToDecimal(0.5) == "0.1"
        assert Converter.convertToDecimal(0.25) == "0.01"
        assert Converter.convertToDecimal(0.75) == "0.11"

    def test_negativeDecimal(self):
        pass

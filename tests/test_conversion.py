import pytest


from conversion import Converter


@pytest.fixture
def converter():
    return Converter([0.5, 0.25, 0.75])


@pytest.fixture
def intConverter():
    return Converter([1, 2, 10, 16, 17])


class TestConverstion:
    def test_positiveDecimal(self, converter):
        assert converter.conversions[0]["base-2"] == "0.1"
        assert converter.conversions[1]["base-2"] == "0.01"
        assert converter.conversions[2]["base-2"] == "0.11"

        assert converter.convert_to_binary(0.2) == "0.00110011"
        assert converter.convert_to_binary(0.142857) == "0.00100100"

    def test_negativeDecimal(self):
        converter = Converter([-0.5, -0.25, -0.75])

        assert converter.conversions[0]["base-2"] == "-0.1"
        assert converter.conversions[1]["base-2"] == "-0.01"
        assert converter.conversions[2]["base-2"] == "-0.11"

        assert converter.convert_to_binary(-0.2) == "-0.00110011"
        assert converter.convert_to_binary(-0.142857) == "-0.00100100"

    def test_positiveInteger(self, intConverter):
        assert intConverter.conversions[0]["base-2"] == "1"
        assert intConverter.conversions[1]["base-2"] == "10"
        assert intConverter.conversions[2]["base-2"] == "1010"
        assert intConverter.conversions[3]["base-2"] == "10000"
        assert intConverter.conversions[4]["base-2"] == "10001"

    def test_negativeInteger(self):
        converter = Converter([-1, -2, -10, -16, -17])

        assert converter.conversions[0]["base-2"] == "-1"
        assert converter.conversions[1]["base-2"] == "-10"
        assert converter.conversions[2]["base-2"] == "-1010"
        assert converter.conversions[3]["base-2"] == "-10000"
        assert converter.conversions[4]["base-2"] == "-10001"

    def test_output(self, converter, intConverter):
        assert "Base 10" in converter.output()
        assert "Base 2" in converter.output()

        assert "Base 10" in intConverter.output()
        assert "Base 2" in intConverter.output()

        for conversion in converter.conversions:
            assert str(conversion["base-10"]) in converter.output()
            assert str(conversion["base-2"]) in converter.output()

        for conversion in intConverter.conversions:
            assert str(conversion["base-10"]) in intConverter.output()
            assert str(conversion["base-2"]) in intConverter.output()

import pytest


from src import Converter


@pytest.fixture
def converter():
    return Converter(2, [0.5, 0.25, 0.75])


@pytest.fixture
def int_converter():
    return Converter(2, [1, 2, 10, 16, 17])


class TestBinaryConversion:
    def test_positive_decimal(self, converter):
        assert converter.conversions[0]["base-2"] == "0.1"
        assert converter.conversions[1]["base-2"] == "0.01"
        assert converter.conversions[2]["base-2"] == "0.11"

        assert converter.convert_to_base(2, 0.2) == "0.00110011"
        assert converter.convert_to_base(2, 0.142857) == "0.00100100"

    def test_negative_decimal(self):
        converter = Converter(2, [-0.5, -0.25, -0.75])

        assert converter.conversions[0]["base-2"] == "-0.1"
        assert converter.conversions[1]["base-2"] == "-0.01"
        assert converter.conversions[2]["base-2"] == "-0.11"

        assert converter.convert_to_base(2, -0.2) == "-0.00110011"
        assert converter.convert_to_base(2, -0.142857) == "-0.00100100"

    def test_positive_integer(self, int_converter):
        assert int_converter.conversions[0]["base-2"] == "1"
        assert int_converter.conversions[1]["base-2"] == "10"
        assert int_converter.conversions[2]["base-2"] == "1010"
        assert int_converter.conversions[3]["base-2"] == "10000"
        assert int_converter.conversions[4]["base-2"] == "10001"

    def test_negative_integer(self):
        converter = Converter(2, [-1, -2, -10, -16, -17])

        assert converter.conversions[0]["base-2"] == "-1"
        assert converter.conversions[1]["base-2"] == "-10"
        assert converter.conversions[2]["base-2"] == "-1010"
        assert converter.conversions[3]["base-2"] == "-10000"
        assert converter.conversions[4]["base-2"] == "-10001"

    def test_floating_point(self):
        converter = Converter(2, [1.5, 2.25, 10.75, -16.5, -17.25])

        assert converter.conversions[0]["base-2"] == "1.1"
        assert converter.conversions[1]["base-2"] == "10.01"
        assert converter.conversions[2]["base-2"] == "1010.11"

        assert converter.conversions[3]["base-2"] == "-10000.1"
        assert converter.conversions[4]["base-2"] == "-10001.01"

    def test_length(self):
        assert Converter(2, [0.2], length=4).conversions[0]["base-2"] == "0.0011"
        assert Converter(2, [0.2], length=2).conversions[0]["base-2"] == "0.00"

    def test_output(self, converter, int_converter):
        assert "Base 10" in converter.output()
        assert "Base 2" in converter.output()

        assert "Base 10" in int_converter.output()
        assert "Base 2" in int_converter.output()

        for conversion in converter.conversions:
            assert str(conversion["base-10"]) in converter.output()
            assert str(conversion["base-2"]) in converter.output()

        for conversion in int_converter.conversions:
            assert str(conversion["base-10"]) in int_converter.output()
            assert str(conversion["base-2"]) in int_converter.output()

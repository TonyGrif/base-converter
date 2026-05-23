import pytest

from src import Converter


@pytest.fixture
def dec_nums():
    return [0.5, 0.25, 0.75, 0.8]


@pytest.fixture
def eight_convert(dec_nums):
    return Converter(8, dec_nums)


@pytest.fixture
def sixty_convert(dec_nums):
    return Converter(60, dec_nums)


class TestBaseConversions:
    def test_positive_decimal(self, eight_convert, sixty_convert):
        assert eight_convert.conversions[0]["base-8"] == "0.4"
        assert eight_convert.conversions[1]["base-8"] == "0.2"
        assert eight_convert.conversions[2]["base-8"] == "0.6"
        assert eight_convert.conversions[3]["base-8"] == "0.63146314"

        assert sixty_convert.conversions[0]["base-60"] == "0.30"
        assert sixty_convert.conversions[1]["base-60"] == "0.15"
        assert sixty_convert.conversions[2]["base-60"] == "0.45"
        assert sixty_convert.conversions[3]["base-60"] == "0.48"

    def test_negative_decimal(self, dec_nums):
        neg_nums = [-num for num in dec_nums]

        neg_eight = Converter(8, neg_nums)
        assert neg_eight.conversions[0]["base-8"] == "-0.4"
        assert neg_eight.conversions[1]["base-8"] == "-0.2"
        assert neg_eight.conversions[2]["base-8"] == "-0.6"
        assert neg_eight.conversions[3]["base-8"] == "-0.63146314"

        neg_sixty = Converter(60, neg_nums)
        assert neg_sixty.conversions[0]["base-60"] == "-0.30"
        assert neg_sixty.conversions[1]["base-60"] == "-0.15"
        assert neg_sixty.conversions[2]["base-60"] == "-0.45"
        assert neg_sixty.conversions[3]["base-60"] == "-0.48"

    def test_positive_integer(self):
        eight_int = Converter(8, [1, 8, 64, 15])
        assert eight_int.conversions[0]["base-8"] == "1"
        assert eight_int.conversions[1]["base-8"] == "10"
        assert eight_int.conversions[2]["base-8"] == "100"
        assert eight_int.conversions[3]["base-8"] == "17"

        sixty_int = Converter(60, [1, 60, 3600])
        assert sixty_int.conversions[0]["base-60"] == "1"
        assert sixty_int.conversions[1]["base-60"] == "10"
        assert sixty_int.conversions[2]["base-60"] == "100"

    def test_negative_integer(self):
        eight_int = Converter(8, [-1, -8, -64, -15])
        assert eight_int.conversions[0]["base-8"] == "-1"
        assert eight_int.conversions[1]["base-8"] == "-10"
        assert eight_int.conversions[2]["base-8"] == "-100"
        assert eight_int.conversions[3]["base-8"] == "-17"

        sixty_int = Converter(60, [-1, -60, -3600])
        assert sixty_int.conversions[0]["base-60"] == "-1"
        assert sixty_int.conversions[1]["base-60"] == "-10"
        assert sixty_int.conversions[2]["base-60"] == "-100"

    def test_floating_point(self):
        eight_float = Converter(8, [1.5, 8.25])
        assert eight_float.conversions[0]["base-8"] == "1.4"
        assert eight_float.conversions[1]["base-8"] == "10.2"

        sixty_float = Converter(60, [1.5])
        assert sixty_float.conversions[0]["base-60"] == "1.30"

    def test_output(self, eight_convert, sixty_convert):
        eight_str = eight_convert.output()
        assert "Base 10" in eight_str
        assert "Base 8" in eight_str

        for conversion in eight_convert.conversions:
            assert str(conversion["base-10"]) in eight_str
            assert str(conversion["base-8"]) in eight_str

        sixty_str = sixty_convert.output()
        assert "Base 10" in sixty_str
        assert "Base 60" in sixty_str

        for conversion in sixty_convert.conversions:
            assert str(conversion["base-10"]) in sixty_str
            assert str(conversion["base-60"]) in sixty_str

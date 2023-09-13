import pytest


from conversion import Converter


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
        # TODO: asserts for eight

        assert sixty_convert.conversions[0]["base-60"] == "0.30"
        assert sixty_convert.conversions[1]["base-60"] == "0.15"
        assert sixty_convert.conversions[2]["base-60"] == "0.45"
        assert sixty_convert.conversions[3]["base-60"] == "0.48"

    def test_negative_decimal(self, dec_nums):
        #TODO: asserts for eight

        neg_nums = []
        for num in dec_nums:
            neg_nums.append(-num)

        neg_sixty = Converter(60, neg_nums)

        assert neg_sixty.conversions[0]["base-60"] == "-0.30"
        assert neg_sixty.conversions[1]["base-60"] == "-0.15"
        assert neg_sixty.conversions[2]["base-60"] == "-0.45"
        assert neg_sixty.conversions[3]["base-60"] == "-0.48"

    def test_positive_integer(self):
        pass

    def test_negative_integer(self):
        pass

    def test_floating_point(self):
        pass

    def test_output(self, eight_convert, sixty_convert):
        # TODO: asserts for eight

        sixty_str = sixty_convert.output()
        assert "Base 10" in sixty_str
        assert "Base 60" in sixty_str

        for conversion in sixty_convert.conversions:
            assert str(conversion["base-10"]) in sixty_str
            assert str(conversion["base-60"]) in sixty_str



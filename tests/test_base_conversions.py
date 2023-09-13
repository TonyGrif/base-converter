import pytest


from conversion import Converter


@pytest.fixture
def dec_nums():
    return [0.5, 0.75, 0.8, 0.16666]


@pytest.fixture
def eight_convert(dec_nums):
    return Converter(8, dec_nums)


@pytest.fixture
def sixty_convert(dec_nums):
    return Converter(60, dec_nums)


class TestBaseConversions:
    def test_positive_decimal(self, eight_convert, sixty_convert):
        # TODO: asserts for eight

        assert sixty_convert[0]["base-60"] == "0.30"
        assert sixty_convert[1]["base-60"] == "0.15"
        assert sixty_convert[2]["base-60"] == "0.45"
        assert sixty_convert[3]["base-60"] == "0.48"
        assert sixty_convert[4]["base-60"] == "0.10"

    def test_negative_decimal(self):
        pass

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



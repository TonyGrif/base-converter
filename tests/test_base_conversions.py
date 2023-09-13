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
    def test_positive_decimal(self, eight_convert):
        pass

    def test_negative_decimal(self):
        pass

    def test_positive_integer(self):
        pass

    def test_negative_integer(self):
        pass

    def test_floating_point(self):
        pass

    def test_output(self):
        pass

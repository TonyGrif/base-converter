import pytest


from conversion import Converter 


@pytest.fixture
def converter():
    return Converter([0.5, 0.25, 0.75])


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

    def test_output(self, converter):
        assert "Base 10" in converter.output() 
        assert "Base 2" in converter.output()

        for count in range(len(converter.conversions)):
            assert str(converter.conversions[count]["base-10"]) in converter.output()
            assert str(converter.conversions[count]["base-2"]) in converter.output()



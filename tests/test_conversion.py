import pytest


from conversion import Converter 


@pytest.fixture
def converter():
    return Converter([0.5, 0.25, 0.75])


class TestConverstion:
    def test_positiveInteger(self):
        pass

    def test_negativeInteger(self):
        converter = Converter([-0.5, -0.25, -0.75])

        assert converter.conversions[0]["base-2"] == "-0.1"
        assert converter.conversions[1]["base-2"] == "-0.01"
        assert converter.conversions[2]["base-2"] == "-0.11"
        
        assert converter.convert_to_binary(-0.2) == "-0.00110011"
        assert converter.convert_to_binary(-0.142857) == "-0.00100100"

    def test_positiveDecimal(self, converter):
        assert converter.conversions[0]["base-2"] == "0.1"
        assert converter.conversions[1]["base-2"] == "0.01"
        assert converter.conversions[2]["base-2"] == "0.11"

        assert converter.convert_to_binary(0.2) == "0.00110011"
        assert converter.convert_to_binary(0.142857) == "0.00100100"

    def test_negativeDecimal(self):
        pass

    def test_output(self, converter):
        assert "Base 10" in converter.output() 
        assert "Base 2" in converter.output()

        for count in range(len(converter.conversions)):
            assert str(converter.conversions[count]["base-10"]) in converter.output()
            assert str(converter.conversions[count]["base-2"]) in converter.output()



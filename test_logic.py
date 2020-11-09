import pytest

from logic import format_number

NO_NUMBER_ERROR = "Sorry, I need a numerical value"

def test_no_decimals():
    assert "1.00" == format_number(1)
    assert "22.00" == format_number(22)
    assert "0.00" == format_number(0)
    
def test_not_a_number():
    assert NO_NUMBER_ERROR == format_number("a")
    assert NO_NUMBER_ERROR == format_number("11.1a")
    assert NO_NUMBER_ERROR == format_number("234asbdweqefewr.dsadwqewqe")
    assert NO_NUMBER_ERROR == format_number("1234125.O22222")

def test_filling_decimals():
    assert "1.10" == format_number(1.1)
    assert "12313.90" == format_number(12313.9)
    assert "12313.00" == format_number(12313.0)

def test_rounding_decimals():
    assert "1.10" == format_number(1.099)
    assert "12313.03" == format_number(12313.034)
    assert "12313.01" == format_number(12313.009)


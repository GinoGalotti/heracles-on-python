import pytest

from logic import format_number

NO_NUMBER_ERROR = "Sorry, I need a numerical value"

def test_0():
    assert "0.00" == format_number(0)

def test_2_digits():
    assert "22.00" == format_number(22)

def test_no_decimals():
    assert "1.00" == format_number(1)
    
def test_not_a_number():
    assert NO_NUMBER_ERROR == format_number("a")
    assert NO_NUMBER_ERROR == format_number("11.1a")
    assert NO_NUMBER_ERROR == format_number("234asbdweqefewr.dsadwqewqe")
    assert NO_NUMBER_ERROR == format_number("1234125.O22222")

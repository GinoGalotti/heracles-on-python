import pytest

from logic import format_number

def test_0():
    assert "0.00" == format_number(0)

def test_2_digits():
    assert "22.00" == format_number(22)

def test_no_decimals():
    assert "1.00" == format_number(1)

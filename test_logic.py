import pytest

from logic import format_number

def test_0():
    assert "0" == format_number(0)

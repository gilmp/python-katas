import pytest
from src.RomanNumerals import RomanNumerals


class TestRomanNumerals:
    def test_one(self):
        rm = RomanNumerals()
        assert rm.convert(1) == "I"


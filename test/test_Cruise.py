from src.Cruise import Cruise
import pytest


def test_Cruise():
    Cruise1 = Cruise(10, 5000, 30)
    assert Cruise1.is_worth_it() == 4932.5


def test_Exception():
    Cruise2 = Cruise(60, 500, 8000)
    with pytest.raises(ValueError):
        Cruise2.is_worth_it()

        
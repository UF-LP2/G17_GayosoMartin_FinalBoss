import pytest

from src.Ship import Ship



def test_ship():

    Ship1 = Ship(4000, 300)
    assert Ship1.is_worth_it() == 3550  


def test_exception():
    Ship2 = Ship(10, 40)
    with pytest.raises(ValueError):
        Ship2.is_worth_it()




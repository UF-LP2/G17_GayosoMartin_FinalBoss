from src.Cargo import Cargo
import pytest

def test_cargo():
    Cargo1 = Cargo(250, 0.5, 2000, 7)
    assert Cargo1.is_worth_it() == 1489.5

def test_Exception():
    Cargo2 = Cargo(79, 1, 150, 90)
    with pytest.raises(ValueError):
        Cargo2.is_worth_it()

def test_ExceptionQuality():
    Cargo2 = Cargo(79, 3, 150, 90)
    with pytest.raises(ValueError):
        Cargo2.is_worth_it()

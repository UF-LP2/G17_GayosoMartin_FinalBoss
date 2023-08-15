from src.Ship import Ship
from src.Cargo import Cargo
from src.Cruise import Cruise


def test_ship():
    cShip = Ship(4000, 300)
    assert cShip.is_worth_it() == 3550  

def test_cargo():
    cCargo = Cargo(250, 0.5, 2000, 7)
    assert cCargo.is_worth_it() == 1987.5

def test_Cruise():
    cCruise = Cruise(10, 5000, 30)
    assert cCruise.is_worth_it() == 4932.5

from src.Ship import Ship


class Cargo(Ship):
    def init(self, cargo, quality, draft, crew):
        Ship.init(draft, crew)

        self.cargo = cargo
        self.quality = quality

def is_worth_it(self)-> float:
    Final_Weight = self.draft - (self.crew * 1,5)

    if self.quality == 1:
        Final_Weight = Final_Weight - 3,5

    elif self.quality == (0,5):
        Final_Weight = Final_Weight - 2

    elif self.quality == (0,25):
        Final_Weight = Final_Weight - 0,5
    return Final_Weight
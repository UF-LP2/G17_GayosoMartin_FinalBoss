from src.Ship import Ship


class Cruise(Ship):
    def init(self, passengers, draft, crew):
        Ship.init(draft, crew)
        self.passengers = passengers

def is_worth_it(self)-> float:
    Final_Weight = self.draft - (self.crew * 1,5)  - (self.passengers * 2,25)
    return Final_Weight
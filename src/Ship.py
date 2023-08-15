class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        Final_Weight = self.draft - (self.crew * 1.5)
        print("Weight of the Ship: ",Final_Weight)
        if Final_Weight > 20:
            print("Saqueamos el Barco")
        else: 
            raise ValueError("Menor a 20, no saquear")



        
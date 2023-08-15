from src.Ship import Ship


class Cargo(Ship):
    contadorCa = 0
    def __init__(self, cargo, quality, draft, crew):
        Ship.__init__(self, draft, crew)

        self.cargo = cargo
        self.quality = quality
        Cargo.contadorCa = Cargo.contadorCa + 1

    def is_worth_it(self)->float:
        Final_Weight = self.draft - (self.crew * 1.5)
     
        if self.quality == 1:
            Final_Weight = Final_Weight - 3.5

        elif self.quality == (0.5):
            Final_Weight = Final_Weight - 2

        elif self.quality == (0.25):
            Final_Weight = Final_Weight - 0.5
        else:
            raise ValueError("Error de dato")

        if Final_Weight > 20:
            print("Saqueamos el Barco")
          
        else: 
            raise ValueError("Menor a 20, no saquear")

        return Final_Weight

from src.Ship import Ship

class Cargo(Ship):
    
    def __init__(self, cargo, quality, draft, crew):
        Ship.__init__(self, draft, crew)

        self.cargo = cargo
        self.quality = quality
        

    def is_worth_it(self)->float:
        Final_Weight = float(self.draft) - (float(self.crew) * 1.5)
     
        if self.quality == 1:
            Final_Weight = Final_Weight - (3.5 * float(self.cargo))

        elif self.quality == (0.5):
            Final_Weight = Final_Weight - (2 * float(self.cargo))

        elif self.quality == (0.25):
            Final_Weight = Final_Weight - (0.5 * float(self.cargo))
        else:
            raise ValueError("Error de dato")
        
        if Final_Weight > 0:
             print(" Weight of the Cargo: ",Final_Weight)
        else :
             print("CARGO Negative Weight : ",Final_Weight, "Revisar Datos Posible error ")

        if Final_Weight > 20:
            print("Saqueamos el CARGO")
          
        else: 
            raise ValueError("Menor a 20, no saquear")

        return Final_Weight

from src.Ship import Ship


class Cruise(Ship):
   
    def __init__(self, passengers, draft, crew):
        Ship.__init__(self, draft, crew)
        self.passengers = passengers
       

    def is_worth_it(self)->float:
        Final_Weight = self.draft - (self.crew * 1.5)  - (self.passengers * 2.25)
        
        if Final_Weight > 0:
             print(" Weight of the Cruise: ",Final_Weight)
        else :
             print("CRUISE Negative Weight : ",Final_Weight, "Revisar Datos Posible error ")

        if Final_Weight > 20:
            print("Saqueamos el CRUISE")
            
        else: 
            raise ValueError("Menor a 20, no saquear")
        return Final_Weight

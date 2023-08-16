class Ship:
    contadorS = 0
    def __init__(self, draft, crew):
        Ship.contadorS = Ship.contadorS + 1
        self.draft = draft
        self.crew = crew
       

    def is_worth_it(self) ->float:
        Final_Weight = float(self.draft) - (float(self.crew) * 1.5)
        if Final_Weight > 0:
             print("Weight of the Ship: ",Final_Weight)
        else :
             print("SHIP, Negative Weight : ",Final_Weight, "Revisar Datos Posible error ")
        if Final_Weight > 20:
            print("Saqueamos el Ship")
            
        else: 
            raise ValueError("Menor a 20, no saquear")
        return Final_Weight
        
class Cruise(Ship):
   
    def __init__(self, passengers, draft, crew):
        Ship.__init__(self, draft, crew)
        self.passengers = passengers
       

    def is_worth_it(self)->float:
        Final_Weight = float(self.draft) - (float(self.crew) * 1.5) - (float(self.passengers) * 2.25)
        
        if Final_Weight > 0:
             print(" Weight of the Cruise: ",Final_Weight)
        else :
             print("CRUISE Negative Weight : ",Final_Weight, "Revisar Datos Posible error ")

        if Final_Weight > 20:
            print("Saqueamos el CRUISE")
            
        else: 
            raise ValueError("Menor a 20, no saquear")
        return Final_Weight

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

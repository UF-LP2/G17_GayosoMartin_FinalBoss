class Ship:
    contadorS = 0
    def __init__(self, draft, crew):
        Ship.contadorS = Ship.contadorS + 1
        self.draft = draft
        self.crew = crew
       

    def is_worth_it(self) ->float:
        Final_Weight = self.draft - (self.crew * 1.5)
        if Final_Weight > 0:
             print("Weight of the Ship: ",Final_Weight)
        else :
             print("SHIP, Negative Weight : ",Final_Weight, "Revisar Datos Posible error ")
        if Final_Weight > 20:
            print("Saqueamos el Ship")
            
        else: 
            raise ValueError("Menor a 20, no saquear")
        return Final_Weight


        
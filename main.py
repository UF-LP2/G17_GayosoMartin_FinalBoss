from src.Clasesships import Ship
from src.Clasesships import Cargo
from src.Clasesships import Cruise
from src.LecturaArch import LecturaArch

def main() -> None:
  
  listaBarcos = LecturaArch()

  for i in range(1,len(listaBarcos)):
    if listaBarcos[i][0] and listaBarcos[i][1] and not listaBarcos[i][2] and not listaBarcos[i][3]:   
      # si tiene solo las primera dos columnas con datos es un Ship
      EsShip = Ship(listaBarcos[i][0],listaBarcos[i][1])
      try: 
        EsShip.is_worth_it()
      except ValueError as e:
        print("Error: ", e)

    elif listaBarcos[i][0] and listaBarcos[i][1] and listaBarcos[i][2] and listaBarcos[i][3]:
      # Si tiene las cuatro columnas con datos es un Cargo
      cargo = listaBarcos[i][2]
      q = listaBarcos[i][3]
      draft = listaBarcos[i][0]
      crew = listaBarcos[i][1]
      EsCargo = Cargo(cargo, q, draft, crew)
      try:
        EsCargo.is_worth_it()
      except ValueError as e:
        print("Error:", e)

    elif listaBarcos[i][0] and listaBarcos[i][1] and not listaBarcos[i][2] and listaBarcos[i][3]:
      # Si tiene las  columnas 0,1,3 por lo tanto tiene quality
      # pero no tiene cargo lo tomamos como que es un Cargo
      cargo = 0.0
      q = listaBarcos[i][3]
      draft = listaBarcos[i][0]
      crew = listaBarcos[i][1]
      EsCargo = Cargo(cargo, q, draft, crew)
      try:
        EsCargo.is_worth_it()
      except ValueError as e:
        print("Error:", e)
      

    elif listaBarcos[i][0] and listaBarcos[i][1] and listaBarcos[i][2] and not listaBarcos[i][3]:
      # Si tiene las primeras 3 columnas con datos es un Cruise
      EsCruise = Cruise(listaBarcos[i][2], listaBarcos[i][0], listaBarcos[i][1])
      try:
        EsCruise.is_worth_it()
      except ValueError as e:
        print("Error: ", e)

    else:
       print("Datos necesarios no proporcionados")

  print("Cantidad de Barcos vistos: ", EsShip.contadorS)


if __name__ == "__main__":
  main()

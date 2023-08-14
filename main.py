import csv
from src.Ship import Ship
from src.Cargo import Cargo
from src.Cruise import Cruise
from src.LecturaArch import LecturaArch


def main() -> None:
  
  listaBarcos = LecturaArch()

  for i in range(1,len(listaBarcos)):
    if listaBarcos[i][0] and listaBarcos[i][1] and not listaBarcos[i][2] and not listaBarcos[i][3]:
      EsShip = Ship(listaBarcos[i][0],listaBarcos[i][1])
      EsShip.saqueo()

    elif listaBarcos[i][0] and listaBarcos[i][1] and listaBarcos[i][2] and listaBarcos[i][3]:
      EsCargo = Cargo(listaBarcos[i][2],listaBarcos[i][3],listaBarcos[i][0],listaBarcos[i][1])
      EsCargo.saqueo()

    elif listaBarcos[i][0] and listaBarcos[i][1] and listaBarcos[i][2] and not listaBarcos[i][3]:
      EsCruise = Cruise(listaBarcos[i][2],listaBarcos[i][0],listaBarcos[i][1])
      EsCruise.saqueo()

  if __name__ == "__main__":
   main()

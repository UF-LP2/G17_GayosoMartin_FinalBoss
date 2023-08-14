import csv

def main() -> None:
 barcos = []
 with open("ships.csv") as file:
    reader  = csv.reader(file)
    for row in reader:
      barcos.append(row)
      print(barcos)
      print(" ")
      



if __name__ == "__main__":
  main()

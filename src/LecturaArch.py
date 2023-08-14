
import csv
def LecturaArch():
    barcos = []
    with open(r"ships.csv") as file:
        reader  = csv.reader(file)
        for row in reader:
            barcos.append(row)
    return barcos
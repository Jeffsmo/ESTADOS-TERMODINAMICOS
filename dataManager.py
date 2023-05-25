import csv

class TableManager:

    def __init__(self, archivo):
        self.archivo= archivo
    
    def crearMatrizNum(self):
        with open(self.archivo) as file:
                matriz = []
                lector_csv = csv.reader(file, delimiter=',')
                for fila in lector_csv:
                    fila_num = []
                    for item in fila:
                        fila_num.append(float(item))
                    matriz.append(fila_num)
                    #print(fila)
        return matriz

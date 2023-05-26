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
    

class DataManager:
     
     def __init__(self, DataMatriz) -> None:
          self.matriz= DataMatriz

     def interpolarTemperaturas(self, Temperatura):

        tempValues = [fila[0] for fila in self.matriz]
        temp_igual_o_aprox = None
        temp_previa = None

        if Temperatura in tempValues:
            temp_igual_o_aprox = Temperatura
        else:
            temp_redondeada = round(Temperatura)
            index = None

            for i, value in enumerate(tempValues):
                if value >= temp_redondeada:
                    index = i
                    break

            if index is not None:
                temp_igual_o_aprox = tempValues[index]
                if index > 0:
                    temp_previa = tempValues[index - 1]
                    

        return print('La temperatura aproximada encontrada es: ' + str(temp_igual_o_aprox)), print('La temperatura previa aproximada encontrada es: ' + str(temp_previa)), temp_igual_o_aprox, temp_previa


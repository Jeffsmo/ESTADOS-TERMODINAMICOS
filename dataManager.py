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
            index= tempValues.index(Temperatura)
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
                    

        return temp_igual_o_aprox, temp_previa, index

     def calcularVolumenesLiqSat(self, temperatura, temperaturaAprox, temperaturaPrev, index):
        volValues = [fila[2] for fila in self.matriz]

        volumeAprox=volValues[index]
        volumePrev= volValues[index-1]
        if temperaturaPrev is not None:
            m=(volumeAprox-volumePrev)/(temperaturaAprox-temperaturaPrev)
            volumeF= m*(temperatura-temperaturaPrev)+volumePrev
        else:
            volumeF = volValues[index]
        return volumeF
     
     def calcularVolumenesVapSat(self, temperatura, temperaturaAprox, temperaturaPrev, index):
        volValues = [fila[3] for fila in self.matriz]

        volumeAprox=volValues[index]
        volumePrev= volValues[index-1]
        if temperaturaPrev is not None:
            m=(volumeAprox-volumePrev)/(temperaturaAprox-temperaturaPrev)
            volumeG= m*(temperatura-temperaturaPrev)+volumePrev
        else:
            volumeG=volValues[index]
        return volumeG
     
     def interpolarPresiones(self, presion):
         presValues = [fila[1] for fila in self.matriz]
         PresionAprox = None
         PresionPrev = None

         if presion in presValues:
            index= presValues.index(presion)
            PresionAprox = presion
         else:
            temp_redondeada = round(presion)
            index = None

            for i, value in enumerate(presValues):
                if value >= temp_redondeada:
                    index = i
                    break

            if index is not None:
                PresionAprox = presValues[index]
                if index > 0:
                    PresionPrev= presValues[index - 1]
            
            return  PresionAprox, PresionPrev,index
         
     def tomarTemperaturaPresion(self, index):
         tempValues = [fila[0] for fila in self.matriz]

         temperatura= tempValues[index]
         return temperatura
     
     def calcularVolumenesLiqPres(self, presion, presionAprox, presionPrev, index):
        volValues = [fila[2] for fila in self.matriz]

        volumeAprox=volValues[index]
        volumePrev= volValues[index-1]
        if presionPrev is not None:
            m=(volumeAprox-volumePrev)/(presionAprox-presionPrev)
            volumeF= m*(presion-presionPrev)+volumePrev
        else:
            volumeF = volValues[index]
        return volumeF

     def calcularVolumenesVapPres(self, presion, presionAprox, presionPrev, index):
        volValues = [fila[3] for fila in self.matriz]

        volumeAprox=volValues[index]
        volumePrev= volValues[index-1]
        if presionPrev is not None:
            m=(volumeAprox-volumePrev)/(presionAprox-presionPrev)
            volumeGPres= m*(presion-presionPrev)+volumePrev
        else:
            volumeGPres=volValues[index]
        return volumeGPres
     

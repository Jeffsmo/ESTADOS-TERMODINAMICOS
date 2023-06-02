import matplotlib.pyplot as plt
import numpy as np
from dataManager import DataManager


class GraficadorTablas:

    def __init__(self, matriz):
        self.matriz= matriz

    
    def graficarDatos(self, valorLinea, vf, vg, tempPresion, presion, escala, index):
        # Obtener los datos de la matriz en las columnas específicas
        columna1 = [fila[0] for fila in self.matriz]  # Temperatura
        columna2=  [fila[1] for fila in self.matriz]  # Presión
        columna3 = [fila[2] for fila in self.matriz]  # Vf
        columna4 = [fila[3] for fila in self.matriz]  # Vg

        # Crear una lista con el mismo número de puntos que columna3
        lineaRectaTemp = [valorLinea] * len(np.linspace(0,250))

        # Puntos de corte con las gráficas columna 3
        puntosCorteXLiq = []
        puntosCorteYLiq = []

        for i in range(len(columna3)):
            x1 = columna3[i]
            y1 = columna1[i]
            if y1 == valorLinea:
                puntosCorteXLiq.append(x1)
                puntosCorteYLiq.append(y1)
        # Puntos de corte con las gráficas columna 4
        puntosCorteXVap = []
        puntosCorteYVap = []

        for i in range(len(columna4)):
            x2 = columna4[i]
            y2 = columna1[i]
            if y2 == valorLinea:
                puntosCorteXVap.append(x2)
                puntosCorteYVap.append(y2)

        #Graficar la linea de presión:

        #lineaPresion = [tempPresion]*len(np.linspace(0,250))

        # Puntos de corte linea de presión:
        puntosCorteXLiqPres = []
        puntosCorteYLiqPres = []
        puntosCorteXVapPres = []
        puntosCorteYVapPres = []

        for i in range(len(columna3)):
         x = columna3[i]
         y = columna1[i]
         if y == tempPresion:
             puntosCorteXLiqPres.append(x)
             puntosCorteYLiqPres.append(y)
        # Puntos de corte con las gráficas columna 4
        puntosCorteXVap = []
        puntosCorteYVap = []

        for i in range(len(columna4)):
            x = columna4[i]
            y = columna1[i]
            if y == tempPresion:
                puntosCorteXVapPres.append(x)
                puntosCorteYVapPres.append(y)

            
        # Graficar las funciones
        plt.plot(columna3, columna1, color='gray', linestyle='-')
        plt.plot(columna4, columna1, color='gray', linestyle='-')

        # Graficar la línea recta de temperatura
        plt.plot(np.linspace(0,250), lineaRectaTemp, label=(f"Temperatura = {valorLinea} °C \n\nPresión Sat ={columna2[index]} kPa"), color='red', linestyle='--')      
        plt.xlim(0, escala)

        # Graficar linea recta de presión
        #plt.plot(np.linspace(0,250), lineaPresion, label=('Presión = '+ str(presion) + ' kPa'), color='purple', linestyle='--')      
        # Graficar los puntos de corte en Liquido Presion
        plt.scatter(puntosCorteXLiqPres, puntosCorteYLiqPres, color='black')

        # Graficar los puntos de corte en Vapor Presion
        plt.scatter(puntosCorteXVapPres, puntosCorteYVapPres, color='black')
        # Graficar los puntos de corte en Liquido Temperatura
        plt.scatter(puntosCorteXLiq, puntosCorteYLiq, color='blue', label=('Vf= '+str(vf)+'m³/kg'))

        # Graficar los puntos de corte en Vapor Temperatura
        plt.scatter(puntosCorteXVap, puntosCorteYVap, color='blue', label=('Vg= '+str(vg)+'m³/kg'))

        # Agregar leyendas y títulos
        plt.legend(loc='right', bbox_to_anchor=(1, 1))
        plt.xlabel('Volumen específico (m³/kg)')
        plt.ylabel('Temperatura (°C)')
        plt.title('Diagrama de Fase')

        # Mostrar el gráfico
        plt.show()


    def graficarLineasDePresion(self, vf,vg,tempPresion,escala,presion):
            x1 = [0, vf]
            y1 = [0, tempPresion]
            x2 = [vf, vg]
            y2 = [tempPresion, tempPresion]
            
            if escala <=1:
                y3 = [tempPresion, 374]
                x3 = [vg,escala]
            
            elif escala >1:
                y3 = [tempPresion, 374]
                x3 = [vg,escala/5]

            # Graficar el segmento de línea recta
            plt.plot(x1, y1, color='purple', linestyle='-')
            plt.plot(x2, y2, color='purple', linestyle='-')
            plt.plot(x3, y3, color='purple', linestyle='-', label=('Presion = '+ str(presion)+' kPa'))
            
    def guardarGrafico(self, valorLinea, vf, vg, tempPresion, presion, escala, index, nombre):
        # Obtener los datos de la matriz en las columnas específicas
        columna1 = [fila[0] for fila in self.matriz]  # Temperatura
        columna2=  [fila[1] for fila in self.matriz]  # Presión
        columna3 = [fila[2] for fila in self.matriz]  # Vf
        columna4 = [fila[3] for fila in self.matriz]  # Vg

        # Crear una lista con el mismo número de puntos que columna3
        lineaRectaTemp = [valorLinea] * len(np.linspace(0,250))

        # Puntos de corte con las gráficas columna 3
        puntosCorteXLiq = []
        puntosCorteYLiq = []

        for i in range(len(columna3)):
            x1 = columna3[i]
            y1 = columna1[i]
            if y1 == valorLinea:
                puntosCorteXLiq.append(x1)
                puntosCorteYLiq.append(y1)
        # Puntos de corte con las gráficas columna 4
        puntosCorteXVap = []
        puntosCorteYVap = []

        for i in range(len(columna4)):
            x2 = columna4[i]
            y2 = columna1[i]
            if y2 == valorLinea:
                puntosCorteXVap.append(x2)
                puntosCorteYVap.append(y2)

        #Graficar la linea de presión:

        #lineaPresion = [tempPresion]*len(np.linspace(0,250))

        # Puntos de corte linea de presión:
        puntosCorteXLiqPres = []
        puntosCorteYLiqPres = []
        puntosCorteXVapPres = []
        puntosCorteYVapPres = []

        for i in range(len(columna3)):
         x = columna3[i]
         y = columna1[i]
         if y == tempPresion:
             puntosCorteXLiqPres.append(x)
             puntosCorteYLiqPres.append(y)
        # Puntos de corte con las gráficas columna 4
        puntosCorteXVap = []
        puntosCorteYVap = []

        for i in range(len(columna4)):
            x = columna4[i]
            y = columna1[i]
            if y == tempPresion:
                puntosCorteXVapPres.append(x)
                puntosCorteYVapPres.append(y)

            
        # Graficar las funciones
        plt.plot(columna3, columna1, color='gray', linestyle='-')
        plt.plot(columna4, columna1, color='gray', linestyle='-')

        # Graficar la línea recta de temperatura
        plt.plot(np.linspace(0,250), lineaRectaTemp, label=(f"Temperatura = {valorLinea} °C \n\nPresión Sat ={columna2[index]} kPa"), color='red', linestyle='--')      
        plt.xlim(0, escala)

        # Graficar linea recta de presión
        #plt.plot(np.linspace(0,250), lineaPresion, label=('Presión = '+ str(presion) + ' kPa'), color='purple', linestyle='--')      
        # Graficar los puntos de corte en Liquido Presion
        plt.scatter(puntosCorteXLiqPres, puntosCorteYLiqPres, color='black')

        # Graficar los puntos de corte en Vapor Presion
        plt.scatter(puntosCorteXVapPres, puntosCorteYVapPres, color='black')
        # Graficar los puntos de corte en Liquido Temperatura
        plt.scatter(puntosCorteXLiq, puntosCorteYLiq, color='blue', label=('Vf= '+str(vf)+'m³/kg'))

        # Graficar los puntos de corte en Vapor Temperatura
        plt.scatter(puntosCorteXVap, puntosCorteYVap, color='blue', label=('Vg= '+str(vg)+'m³/kg'))

        # Agregar leyendas y títulos
        plt.legend(loc='right', bbox_to_anchor=(1, 1))
        plt.xlabel('Volumen específico (m³/kg)')
        plt.ylabel('Temperatura (°C)')
        plt.title('Diagrama de Fase')

        # Mostrar el gráfico
        plt.savefig(nombre+'.jpg', format= 'jpg')

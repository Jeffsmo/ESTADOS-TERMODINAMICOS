import matplotlib.pyplot as plt
import numpy as np

class GraficadorTablas:

    def __init__(self, matriz):
        self.matriz= matriz

    
    def graficarDatos(self, valorLinea):
        # Obtener los datos de la matriz en las columnas específicas
        columna1 = [fila[0] for fila in self.matriz]  # Primera columna
        columna3 = [fila[2] for fila in self.matriz]  # Tercera columna
        columna4 = [fila[3] for fila in self.matriz]  # Cuarta columna

        # Crear una lista con el mismo número de puntos que columna3
        puntoCorteLiq = [valorLinea for _ in range(len(columna3))]
        lineaRectaTemp = [valorLinea] * len(np.linspace(0,250))

        # Puntos de corte con las gráficas columna 3
        puntosCorteXLiq = []
        puntosCorteYLiq = []

        for i in range(len(columna3)):
            x = columna3[i]
            y = columna1[i]
            if y == valorLinea:
                puntosCorteXLiq.append(x)
                puntosCorteYLiq.append(y)
        # Puntos de corte con las gráficas columna 4
        puntosCorteXVap = []
        puntosCorteYVap = []

        for i in range(len(columna4)):
            x = columna4[i]
            y = columna1[i]
            if y == valorLinea:
                puntosCorteXVap.append(x)
                puntosCorteYVap.append(y)

        # Graficar las funciones
        plt.plot(columna3, columna1, color='gray', linestyle='--')
        plt.plot(columna4, columna1, color='gray', linestyle='--')

        # Graficar la línea recta
        plt.plot(np.linspace(0,250), lineaRectaTemp, label=('Temperatura = '+ str(valorLinea) + ' °C'), color='red', linestyle='--')      
        plt.xlim(0, 0.08)

        # Graficar los puntos de corte en Liquido
        plt.scatter(puntosCorteXLiq, puntosCorteYLiq, color='blue', label='Vf')

        # Graficar los puntos de corte en Vapor
        plt.scatter(puntosCorteXVap, puntosCorteYVap, color='blue', label='Vg')

        # Agregar leyendas y títulos
        plt.legend(loc='right', bbox_to_anchor=(1, 1))
        plt.xlabel('Volumen específico (m³/kg)')
        plt.ylabel('Temperatura (°C)')
        plt.title('Gráfico de Funciones')

        # Mostrar el gráfico
        plt.show()
import matplotlib.pyplot as plt
import numpy as np

class GraficadorTablas:

    def __init__(self, matriz):
        self.matriz= matriz

    
    def graficarDatos(self, Presion):
        # Obtener los datos de la matriz en las columnas específicas
        columna1 = [fila[0] for fila in self.matriz]  # Primera columna
        columna3 = [fila[2] for fila in self.matriz]  # Tercera columna
        columna4 = [fila[3] for fila in self.matriz]  # Cuarta columna

        valorLinea = Presion

        #Crear una lista con el mismo valor ingresado repetido para cada punto en el eje x
        lineaRecta = [valorLinea] * len(np.linspace(0,250))

        # Graficar las funciones
        plt.plot(columna3, columna1,color='gray',linestyle= '--', label='Función 1')  # Gráfica de la primera función
        plt.plot(columna4, columna1,color='gray',linestyle= '--', label='Función 2')  # Gráfica de la segunda función
        plt.xlim(0, 0.08)
        # Graficar la línea recta
        plt.plot(np.linspace(0,250), lineaRecta, label='Presión', color='red', linestyle='--')



        #plt.xticks(np.arange(0, 1.01, 0.01))

        # Agregar leyendas y títulos
        plt.xlabel('Volumen específico (m³/kg)')  # Etiqueta del eje x
        plt.ylabel('Temperatura (°C)')  # Etiqueta del eje y
        plt.title('Gráfico de Funciones')  # Título del gráfico

        # Mostrar el gráfico
        plt.show()


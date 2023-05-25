import sys
if sys.version_info[0] == 3:
    from tkinter import*
    import matplotlib.pyplot as plt
    from matplotlib import*
    from numpy import*
else:
    import Tkinter as tk

import numpy as np
from dataManager import TableManager
from graficas import GraficadorTablas

file='Tablas Termodinamica.csv'
presion= 110

data=TableManager(file)
matrizDatos = data.crearMatrizNum()
graficador = GraficadorTablas(matrizDatos)
#graficador.graficarDatos()

#definiendo la raíz
raiz=Tk()
raiz.title("Titulo proyecto")
#raiz.iconbitmap("atomo.ico")
raiz.geometry("400x300")
raiz.resizable(False, False)
raiz.config(bg="white")
raiz.option_add( "*font", "Verdana 10" )


#validar entradas
def validar():
    try:
        float(entrada1.get())
        float(entrada2.get())
        return True
    except:
        return False
    


#frame contenido en la raíz
frame=Frame(raiz)
frame.config(bg="lightblue", width="400", height="400")
frame.pack(padx=20, pady=20)

titulo=Label(frame, text='FASES DEL AGUA - TERMODINÁMICA')
titulo.grid(row="0", column="0", columnspan=2, padx=10, pady=10)
titulo.config(bg="white", border=5)

#subtítulos y entradas de información
label1=Label(frame, text='Presión 1 (kPa)')
label1.grid(row="1", column="0", pady=20, sticky="w")
label1.config(bg="#021663", fg="white", border=5)
entrada1=Entry(frame)
entrada1.grid(row="1", column="1", pady=20)
entrada1.config(bg="#2E49AF", highlightthickness=4,highlightbackground="#021663", highlightcolor="#021663", fg="white",
    insertbackground="white")

label2=Label(frame, text='Temperatura (°C)')
label2.grid(row="2", column="0", pady=10, sticky="e")
label2.config(bg="#021663", fg="white", border=5)
entrada2=Entry(frame)
entrada2.grid(row="2", column="1", pady=10)
entrada2.config(bg="#2E49AF", highlightthickness=4,highlightbackground="#021663", highlightcolor="#021663", fg="white",
    insertbackground="white")

#botón para graficar
boton=Button(frame, text='Graficar', command=graficador.graficarDatos(entrada1))
boton.grid(row="3", column="1", pady=10)

#label para el mensaje de error
label3=Label(frame, text='')
label3.grid(row="4", column="0", columnspan=2, pady=10)
label3.config(bg="lightblue")

raiz.mainloop()
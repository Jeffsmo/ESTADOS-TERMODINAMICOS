
from tkinter import*
import matplotlib.pyplot as plt
from matplotlib import*
from numpy import*
from PIL import Image
import tkinter as tk
from tkinter import messagebox
from dataManager import TableManager
from graficas import GraficadorTablas
from guardarDatos import GuardarDatos
from dataManager import DataManager
import datetime


file='Tablas Termodinamica.csv'
presion= 110

data=TableManager(file)
matrizDatos = data.crearMatrizNum()
graficador = GraficadorTablas(matrizDatos)
control = DataManager(matrizDatos)

#graficador.graficarDatos()

#definiendo la raíz
raiz=Tk()
raiz.title("Graficador Diagrama de Fase")
#raiz.iconbitmap("atomo.ico")
raiz.geometry("1000x800")
raiz.resizable(False, False)
raiz.config(bg="lightblue")
raiz.option_add( "*font", "Verdana 12" )


#validar entradas
def validar():
    try:
        float(entrada1.get())
        float(entrada2.get())
        float(entrada3.get())
        return True
    except:
        return False
    
# Función para graficar
def graficar():
    try:
        temperatura = float(entrada2.get())
        presion = float(entrada1.get())
        escala = float(entrada3.get())
        presionAprox, presionPrev, indexPres = buscarPresion()
        temperaturaPres= control.tomarTemperaturaPresion(indexPres)
        vfPres = control.calcularVolumenesLiqPres(presion, presionAprox, presionPrev, indexPres)
        vgPres = control.calcularVolumenesVapPres(presion, presionAprox, presionPrev, indexPres)
        tempAprox, tempPrev, index = buscarTemperatura()
        vf=control.calcularVolumenesLiqSat(temperatura,tempAprox,tempPrev,index)
        vg=control.calcularVolumenesVapSat(temperatura,tempAprox,tempPrev,index)
        graficador.graficarLineasDePresion(vfPres,vgPres,temperaturaPres,escala, presion)
        #graficador.graficarLineasDePresion(vf,vg,temperatura,escala,index)
        graficador.graficarDatos(temperatura, vf, vg, temperaturaPres, presion, escala, index)
    except ValueError:
        messagebox.showerror("Error", "Error al graficar")

def buscarTemperatura():
    temperatura = float(entrada2.get())
    temperaturaAprox, temperaturaPrevia, index = control.interpolarTemperaturas(temperatura)
    
    #messagebox.showinfo("Resultados", f"Temperatura aproximada encontrada: {temperaturaAprox}\nTemperatura previa aproximada encontrada: {temperaturaPrevia}")
    
    return temperaturaAprox, temperaturaPrevia, index

def buscarPresion():
    presion=float(entrada1.get())
    presionAprox, presionPrev, index = control.interpolarPresiones(presion)

    return presionAprox, presionPrev, index

def buscarTabla():
    Uf, Ug, hf, hg, sf, sg = control.buscarEstadoSaturacion()

def guardarDatos():
    try:
        nombre = str(entrada4.get())
        temperatura = float(entrada2.get())
        presion = float(entrada1.get())
        historial = GuardarDatos(presion,temperatura)
        date = datetime.datetime.now()
        historial.guardarDatos(date, nombre)
        messagebox.showinfo("Guardar","Datos guardados exitosamente")
    except ValueError:
        messagebox.showerror("Error", "Error al escribir registro")



def guardarGrafico():
    try:
        nombre= str(entrada4.get())
        #graficador.guardarGrafico(nombre)
        temperatura = float(entrada2.get())
        presion = float(entrada1.get())
        escala = float(entrada3.get())
        presionAprox, presionPrev, indexPres = buscarPresion()
        temperaturaPres= control.tomarTemperaturaPresion(indexPres)
        vfPres = control.calcularVolumenesLiqPres(presion, presionAprox, presionPrev, indexPres)
        vgPres = control.calcularVolumenesVapPres(presion, presionAprox, presionPrev, indexPres)
        tempAprox, tempPrev, index = buscarTemperatura()
        vf=control.calcularVolumenesLiqSat(temperatura,tempAprox,tempPrev,index)
        vg=control.calcularVolumenesVapSat(temperatura,tempAprox,tempPrev,index)
        graficador.graficarLineasDePresion(vfPres,vgPres,temperaturaPres,escala, presion)
        #graficador.graficarLineasDePresion(vf,vg,temperatura,escala,index)
        graficador.guardarGrafico(temperatura, vf, vg, temperaturaPres, presion, escala, index, nombre)
        messagebox.showinfo("Guardar", "Figura guardada con éxito ")
    except ValueError:
        messagebox.showerror("Error", "Error al guardar archivo")



#frame contenido en la raíz
frame=Frame(raiz)
frame.config(bg="lightblue", width="1000", height="1200")
frame.pack(padx=100, pady=100)

titulo=Label(frame, text='FASES DEL AGUA - TERMODINÁMICA')
titulo.grid(row="0", column="0", columnspan=2, padx=10, pady=10)
titulo.config(bg="blue", border=5)

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

label3=Label(frame, text='Escala (0-206)')
label3.grid(row="3", column="0", pady=5, sticky="e")
label3.config(bg="#021663", fg="white", border=5)
entrada3=Entry(frame)
entrada3.grid(row="3", column="2", pady=5)
entrada3.config(bg="#2E49AF", highlightthickness=4,highlightbackground="#021663", highlightcolor="#021663", fg="white",
    insertbackground="white")

label4=Label(frame, text='Nombre Gráfica')
label4.grid(row="6", column="0", pady=5, sticky="e")
label4.config(bg="#021663", fg="white", border=5)
entrada4=Entry(frame)
entrada4.grid(row="6", column="2", pady=5)
entrada4.config(bg="#2E49AF", highlightthickness=4,highlightbackground="#021663", highlightcolor="#021663", fg="white",
    insertbackground="white")

# Botón para graficar
boton = Button(frame, text='Graficar', command=graficar)
boton.grid(row="10", column="15", pady=10)


# Botón para interpolar temperatura
boton1 = Button(frame, text='Guardar Registro', command=guardarDatos)
boton1.grid(row="9", column="1", pady=10)

#boton guardar grafica

boton2= Button(frame, text='Guardar grafica', command=guardarGrafico)
boton2.grid(row='6', column='1')
#label para el mensaje de error
label3=Label(frame, text='')
label3.grid(row="8", column="4", columnspan=2, pady=15)
label3.config(bg="lightblue")

raiz.mainloop()
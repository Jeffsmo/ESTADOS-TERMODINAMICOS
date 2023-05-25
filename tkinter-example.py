from tkinter import*
import matplotlib.pyplot as plt
from matplotlib import*
from numpy import*

#definiendo la raíz
raiz=Tk()
raiz.title("Titulo proyecto")
#raiz.iconbitmap("atomo.ico")
raiz.geometry("400x300")
raiz.resizable(False, False)
raiz.config(bg="white")
raiz.option_add( "*font", "Verdana 10" )

#Funcion para validar los valores que serán ingresados
def validar():
    try:
        float(entrada1.get())
        float(entrada2.get())
        return True
    except:
        return False

#Funcion para graficar el movimiento
def graficar():

    if (validar()==True and float(entrada1.get())>0) and 0<float(entrada2.get())<90:
        #definiendo variables importantes
        label3.config(bg="lightblue", text='Hola')
        v0=float(entrada1.get())
        angulo=float(entrada2.get())*pi/180
        v0x=v0*cos(angulo)
        v0y=v0*sin(angulo)
        xmax=v0**2*sin(2*angulo)/(9.81)

        if angulo>0:
            x=arange(0, xmax+xmax/10, 0.01)
        else:
            x=arange(0, 15, 0.01)
       
        t=x/v0x
        tv=abs(2*v0*sin(angulo)/(9.81))
        def funcion(t):
            return v0y*t-0.5*9.81*t**2
       
        f=[funcion(i) for i in t]
       
        ymax=v0**2*(sin(angulo))**2/(2*9.81)

        #graficando el alcance, la altura máxima, el tiempo de vuelo, la línea del eje x, la trayectoria
        plt.plot(xmax, 0, "o", label=('Alcance x = '+str(round(xmax, 2))+' m'), color="blue")
        plt.plot(xmax/2, ymax, "o", label=('Altura máxima y = '+str(round(ymax, 2))+' m'), color="green")
        plt.plot(0, 0, "o", color="white", label=('Tiempo de vuelo t = '+str(round(tv, 2))+' s'))
        plt.plot([i for i in range(0, int(xmax)+2, 1)], [0 for i in range(0, int(xmax)+2, 1)], color="black",
            linestyle="dashed")
        plt.plot(x, f, color="red")
        plt.legend()
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
        plt.title('Trayectoria del objeto')
        plt.show()

    else:
        label3.config(bg="white", text='¡Los valores ingresados no son válidos!')


#frame contenido en la raíz
frame=Frame(raiz)
frame.config(bg="lightblue", width="400", height="400")
frame.pack(padx=20, pady=20)

titulo=Label(frame, text='Movimiento Parabólico')
titulo.grid(row="0", column="0", columnspan=2, padx=10, pady=10)
titulo.config(bg="white", border=5)

#subtítulos y entradas de información
label1=Label(frame, text='Velocidad inicial (m/s)')
label1.grid(row="1", column="0", pady=20, sticky="w")
label1.config(bg="#021663", fg="white", border=5)
entrada1=Entry(frame)
entrada1.grid(row="1", column="1", pady=20)
entrada1.config(bg="#2E49AF", highlightthickness=4,highlightbackground="#021663", highlightcolor="#021663", fg="white",
    insertbackground="white")

label2=Label(frame, text='Ángulo inicial (°)')
label2.grid(row="2", column="0", pady=10, sticky="e")
label2.config(bg="#021663", fg="white", border=5)
entrada2=Entry(frame)
entrada2.grid(row="2", column="1", pady=10)
entrada2.config(bg="#2E49AF", highlightthickness=4,highlightbackground="#021663", highlightcolor="#021663", fg="white",
    insertbackground="white")

#botón para graficar
boton=Button(frame, text='Graficar', command=graficar)
boton.grid(row="3", column="1", pady=10)

#label para el mensaje de error
label3=Label(frame, text='')
label3.grid(row="4", column="0", columnspan=2, pady=10)
label3.config(bg="lightblue")

raiz.mainloop()
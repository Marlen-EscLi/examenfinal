import tkinter
from tkinter import *
import datetime
import math
#iniciar operaciones
ventana = tkinter.Tk()
ventana.title("Examen Final")
ventana.geometry("550x350")


etiqueta = tkinter.Label(ventana, text = "BIENVENIDO", font = ("Verdana", 30))
etiqueta.pack()

#labels 
#etiqueta1 = tkinter.Label(ventana, text = "Nombre", font = ("Century Gothic", 18)).place(x = 70, y = 40)
#etiqueta2 = tkinter.Label(ventana, text = "Apellido", font = ("Century Gothic", 18)).place(x = 70, y = 67)
#etiqueta3 = tkinter.Label(ventana, text = "Día", font = ("Century Gothic", 18)).place(x = 70, y = 95)
#etiqueta4 = tkinter.Label(ventana, text = "Mes", font = ("Century Gothic", 18)).place(x = 70, y = 125)
#etiqueta5 = tkinter.Label(ventana, text = "Año", font = ("Century Gothic", 18)).place(x = 70, y = 155)

#campo de texto
#entrada = StringVar()
#textetiqueta1 = Entry(ventana, textvariable = entrada).place(x = 180, y = 43)
#textetiqueta2 = Entry(ventana, textvariable = entrada).place(x = 180, y = 73)
#textetiqueta3 = Entry(ventana, textvariable = entrada).place(x = 180, y = 100)
#textetiqueta4 = Entry(ventana, textvariable = entrada).place(x = 180, y = 130)
#textetiqueta5 = Entry(ventana, textvariable = entrada).place(x = 180, y = 160)
#Campo de texto y labels

self.entrada1 = StringVar()
etiqueta1 = tkinter.Label(ventana, text = "Nombre", font = ("Century Gothic", 18)).place(x = 75, y = 40)
textetiqueta1 = Entry(ventana, textvariable = entrada1, width = 30).place(x = 185, y = 43)

self.entrada2 = StringVar()
etiqueta2 = tkinter.Label(ventana, text = "Apellido", font = ("Century Gothic", 18)).place(x = 75, y = 67)
textetiqueta2 = Entry(ventana, textvariable = entrada2, width = 30).place(x = 185, y = 73)


self.entrada3 = StringVar()
etiqueta3 = tkinter.Label(ventana, text = "Día", font = ("Century Gothic", 18)).place(x = 75, y = 95)
textetiqueta3 = Entry(ventana, textvariable = entrada3, width = 30).place(x = 185, y = 100)

self.entrada4 = StringVar()
etiqueta4 = tkinter.Label(ventana, text = "Mes", font = ("Century Gothic", 18)).place(x = 75, y = 125)
textetiqueta4 = Entry(ventana, textvariable = entrada4, width = 30).place(x = 185, y = 130)

self.entrada5 = StringVar()
etiqueta5 = tkinter.Label(ventana, text = "Año", font = ("Century Gothic", 18)).place(x = 75, y = 155)
textetiqueta5 = Entry(ventana, textvariable = entrada5, width = 30).place(x = 185, y = 160)

#Creación de los botones
botonf1 = Button(ventana, text = "Función 1", command = self.fn1, font = ("Century Gothic", 16), width = 8).place (x = 45, y = 198)
botonf2 = Button(ventana, text = "Función 2", command = self.fn2, font = ("Century Gothic", 16), width = 8).place (x = 136, y = 198)
botonf3 = Button(ventana, text = "Función 3", command = self.fn3, font = ("Century Gothic", 16), width = 8).place (x = 227, y = 198)
botonf4 = Button(ventana, text = "Función 4", command = self.fn4, font = ("Century Gothic", 16), width = 8).place (x = 318, y = 198)
botonf5 = Button(ventana, text = "Función 5", command = self.fn5, font = ("Century Gothic", 16), width = 8).place (x = 409 , y = 198)

#label de respuestas

#creación de variables
 self.message = Label(text = '', fg = 'white').place(x = 250, y = 220)
 
    
 def fn1(self):
    dia=int(self.entrada3.get())
    mes=int(self.entrada4.get())
    anio=int(self.entrada5.get())

    bindia=format(dia, '0b' )
    binmes=format(mes, '0b')
    binanio=format(anio, '0b')

    self.message['text'] = 'La fecha es: {}/{}/{} y  en binario es:{}/{}/{}'.format(dia,mes,anio,bindia,binmes,binanio)



ventana.mainloop()




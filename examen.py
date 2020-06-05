import tkinter
from tkinter import *

ventana = tkinter.Tk()
ventana.title("Examen Final")
ventana.geometry("500x400")

etiqueta = tkinter.Label(ventana, text = "BIENVENIDO", font = ("Verdana", 25))
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


ventana.mainloop()


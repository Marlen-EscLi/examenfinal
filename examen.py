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

entrada1 = StringVar()
etiqueta1 = tkinter.Label(ventana, text = "Nombre", font = ("Century Gothic", 18)).place(x = 70, y = 40)
textetiqueta1 = Entry(ventana, textvariable = entrada1).place(x = 180, y = 43)

entrada2 = StringVar()
etiqueta2 = tkinter.Label(ventana, text = "Apellido", font = ("Century Gothic", 18)).place(x = 70, y = 67)
textetiqueta2 = Entry(ventana, textvariable = entrada2).place(x = 180, y = 73)


entrada3 = StringVar()
etiqueta3 = tkinter.Label(ventana, text = "Día", font = ("Century Gothic", 18)).place(x = 70, y = 95)
textetiqueta3 = Entry(ventana, textvariable = entrada3).place(x = 180, y = 100)

entrada4 = StringVar()
etiqueta4 = tkinter.Label(ventana, text = "Mes", font = ("Century Gothic", 18)).place(x = 70, y = 125)
textetiqueta4 = Entry(ventana, textvariable = entrada4).place(x = 180, y = 130)

entrada5 = StringVar()
etiqueta5 = tkinter.Label(ventana, text = "Año", font = ("Century Gothic", 18)).place(x = 70, y = 155)
textetiqueta5 = Entry(ventana, textvariable = entrada5).place(x = 180, y = 160)



ventana.mainloop()


import tkinter
from tkinter import *

ventana = tkinter.Tk()
ventana.title("Examen Final")
ventana.geometry("500x400")

etiqueta = tkinter.Label(ventana, text = "BIENVENIDO", font = ("Verdana", 25))
etiqueta.pack()


ventana.mainloop()


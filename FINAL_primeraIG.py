#-*- coding: utf-8 -*-

from tkinter import * #importo todas las clases de este paquete/libreria

raiz = Tk() #construyo la raiz con el nombre de variable Tk (es una clase)

raiz.title('Ventana de pruebas') #metodo que da titulo

raiz.resizable(0, 0) #método para hacer que el tamaño de la  ventana no se pueda redimensionar
#Son parámetros booleanos True/False. En este caso los dos son False. No se puede redimensionar
#Cualquier numero distinto de 0 sería interpretado como True
raiz.resizable(56, 0) #en este caso solo se puede redimensionar anchura (width)

raiz.resizable(0, 1) # " " altura (heigth). 

raiz.iconbitmap("capturaw.ico") #cambia el icono de la IG que por defecto era una pluma

raiz.geometry("650x350") #dimensiones de la ventana (WxH)

raiz.config(bg="green") #metodo que sirve para muchas cosas: como cambiar el color de fondo

raiz.mainloop() #método. Sirve para que la ventana esté abierta, esté a la escucha del usuario

# SI EJECUTAMOS ESTE ARCHIVO .py DESDE EL DIRECTORIO DONDE ESTÁ ALOJADO, SE ABRIRÁ CON LA
#CONSOLA DE PYTHON, QUE QUEDARÁ POR DETRÁS DE LA IG. SI NO QUISIÉRAMOS QUE QUEDARA LA CONSOLA
#POR DETRAS, DE MANERA QUE SOLO SE ABRIERA LA VENTANA DE LA IG, GUARDA EL .py CON EXTENSIÓN .pyw


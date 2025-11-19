# CBTIS 89
# Elizabeth Lara Acuña 
# 3°B Programa T.M
# Programa que puedas eleguir una carrera
import tkinter as tk 
from tkinter import ttk
#Creae ventana principal 
ventana=tk.Tk()
ventana.title("Selecciona una carrera")
ventana.geometry("300x200")
#Etiqueta de instruccion
etiqueta=tk.Label(ventana,text="Elige una opcion:")
etiqueta.pack(pady=10)
#Crearlista desplegable (Combobox)
opciones=["ARH","Arquitectura","Comercio electronico","Comercio internacioneles y aduanas ","Construccion","Contabilidad","Mecatronica"]
Combocarreras=ttk.Combobox(ventana,values=opciones,state="readonly")
Combocarreras.pack(pady=5)
def mostrar_seleccion(event):
    seleccion=Combocarreras.get()#Obtine el valor seleccionado 
    etiqueta_resultado.config(text=f"Estas en la carrera:{seleccion}")

#Asociar evento al seleccionarun elemento 
Combocarreras.bind("<<ComboboxSelected>>",mostrar_seleccion)
    
#Etiqueta para mostrar el resultado 
etiqueta_resultado=tk.Label(ventana, text="Aun no has seleccionado nada")
etiqueta_resultado.pack(pady=20)
#Iniciar bucle principal 
ventana.mainloop()
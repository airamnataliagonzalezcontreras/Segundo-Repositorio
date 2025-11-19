#airam natalia
#CBTIS 89
#3 B programacion

import tkinter as tk
import tkinter as tk


ventana = tk.Tk()
ventana.title("airam natalia gonzalez contreras")
ventana.geometry("400x400")
ventana.resizable(False, False) 


etiqueta_nombre = tk.Label(ventana, text="nombre del trabajador")
etiqueta_nombre.pack()

entrada_nombre = tk.Entry(ventana, justify="center")
entrada_nombre.pack()


etiqueta_sueldo = tk.Label(ventana, text="sueldo mensual")
etiqueta_sueldo.pack(pady=10)

entrada_sueldo = tk.Entry(ventana, justify="center")
entrada_sueldo.pack()



etiqueta_meses = tk.Label(ventana, text="meses trabajados")
etiqueta_meses.pack()

entrada_meses = tk.Entry(ventana, justify="center")
entrada_meses.pack()


etiqueta_bono = tk.Label(ventana, text="tipo de bono")
etiqueta_bono.pack()



      
        

Seleccion = tk.IntVar()

radioB1=tk.Radiobutton(ventana, text="completo (10%)", variable=Seleccion)
radioB2=tk.Radiobutton(ventana, text="parcial 5%)", variable=Seleccion)
radioB3=tk.Radiobutton(ventana, text="sin bono (0%)", variable=Seleccion)

radioB1.pack(pady=10)
radioB2.pack(pady=10)
radioB3.pack(pady=10)

def calcular_sueldo():

    entrada_sueldo=entrada_sueldo*entrada_meses




btn_calcular=tk.Button(
  ventana,
  text="Calcular sueldo total",
  command=calcular_sueldo,
  bg="#da9086"
)
btn_calcular.pack(pady=5)

etiqueta_resultado=tk.Label(
  ventana,
  text=" ",
  font=("Arial",12,"bold")                                                     
)
etiqueta_resultado.pack(pady=15)





ventana.mainloop()
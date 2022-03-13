from tkinter import *

#def = tikinter
ventana = Tk()
ventana.title("calculadora_instagram")

i = 0

#def = entradasDSD
e_texto = Entry(ventana, font=("calibri 20"))
e_texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


#Funciones
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def delete():
    e_texto.delete(0, END)
    i = 0

def Calculate():
    ecu = e_texto.get()
    result = eval(ecu)
    e_texto.delete(0, END)
    e_texto.insert(0, result)
    i = 0



#botones
Boton1 = Button(ventana, text="1", width=5, height=4, command = lambda: click_boton(1))
Boton2 = Button(ventana, text="2", width=5, height=4, command = lambda: click_boton(2))
Boton3 = Button(ventana, text="3", width=5, height=4, command = lambda: click_boton(3))
Boton4 = Button(ventana, text="4", width=5, height=4, command = lambda: click_boton(4))
Boton5 = Button(ventana, text="5", width=5, height=4, command = lambda: click_boton(5))
Boton6 = Button(ventana, text="6", width=5, height=4, command = lambda: click_boton(6))
Boton7 = Button(ventana, text="7", width=5, height=4, command = lambda: click_boton(7))
Boton8 = Button(ventana, text="8", width=5, height=4, command = lambda: click_boton(8))
Boton9 = Button(ventana, text="9", width=5, height=4, command = lambda: click_boton(9))
Boton0 = Button(ventana, text="0", width=16, height=4, command = lambda: click_boton(0))

Boton_borrar = Button(ventana, text="AC", width=5, height=4, command = lambda: delete())
Boton_parentesis1 = Button(ventana, text="(", width=5, height=4, command = lambda: click_boton("("))
Boton_parentesis2 = Button(ventana, text=")", width=5, height=4, command = lambda: click_boton(")"))
Boton_punto = Button(ventana, text=".", width=5, height=4)

Boton_div = Button(ventana, text="/", width=5, height=4, command = lambda: click_boton("/"))
Boton_mul = Button(ventana, text="x", width=5, height=4, command = lambda: click_boton("*"))
Boton_suma = Button(ventana, text="+", width=5, height=4, command = lambda: click_boton("+"))
Boton_resta = Button(ventana, text="-", width=5, height=4, command = lambda: click_boton("-"))
Boton_igual = Button(ventana, text="=", width=5, height=4, command = lambda: Calculate())



# Defincion de Layout de botones
Boton_borrar.grid(row=1, column=0, padx=5, pady=5)
Boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
Boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
Boton_div.grid(row=1, column=3, padx=5, pady=5)

Boton7.grid(row=2, column=0, padx=5, pady=5)
Boton8.grid(row=2, column=1, padx=5, pady=5)
Boton9.grid(row=2, column=2, padx=5, pady=5)
Boton_mul.grid(row=2, column=3, padx=5, pady=5)

Boton4.grid(row=3, column=0, padx=5, pady=5)
Boton5.grid(row=3, column=1, padx=5, pady=5)
Boton6.grid(row=3, column=2, padx=5, pady=5)
Boton_suma.grid(row=3, column=3, padx=5, pady=5)

Boton1.grid(row=4, column=0, padx=5, pady=5)
Boton2.grid(row=4, column=1, padx=5, pady=5)
Boton3.grid(row=4, column=2, padx=5, pady=5)
Boton_resta.grid(row=4, column=3, padx=5, pady=5)

Boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
Boton_punto.grid(row=5, column=2, padx=5, pady=5)
Boton_igual.grid(row=5, column=3, padx=5, pady=5)

ventana.mainloop()

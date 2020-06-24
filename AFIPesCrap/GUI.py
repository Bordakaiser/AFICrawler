from tkinter import *

root = Tk()
root.title("Consultas Facturación")
root.resizable(300,300)

ingreso = Label(root, text= 'Ingrese sus datos', fg = 'white', background='purple', width=50)
ingreso.grid(row=0, column=0, sticky=N, columnspan=5)
cuit = Label(root, text='CUIT')
cuit.grid(row=1, column=0,sticky=W, padx=2, pady=1)
clave = Label(root, text='Clave')
clave.grid(row=2, column=0,sticky=W, padx=2, pady=1)
fecdes = Label(root, text='Desde')
fecdes.grid(row=3, column=0,sticky=W, padx=2, pady=1)
fechas = Label(root, text='Hasta')
fechas.grid(row=4, column=0,sticky=W, padx=2, pady=1)

def UniEntry(val,wid,fil,col):
    entrada = Entry(root,text = val, width = wid,)
    entrada.grid(row = fil, column = col)
    return entrada

val1, val2, val3, val4 = StringVar(), StringVar(), IntVar(), IntVar()

e1 = UniEntry(val1,20,1,1)
e2 = UniEntry(val2,20,2,1)
e3 = UniEntry(val3,20,3,1)
e4 = UniEntry(val4,20,4,1)



root.mainloop()
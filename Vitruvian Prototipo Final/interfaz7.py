from interfaz8 import btn7
from tkinter import*
from tkinter import messagebox

import tkinter as tk

btn6 = None

def btn6():
    
   
    
    if True:
        window7 = tk.Toplevel()
        window7.title("VITRUVIAN") #titulo de la ventana
        window7.resizable(0,0) #metodo que nos permite decidir si redimensionamos la ventana (booleano)
        window7.iconbitmap("1.ico") #icono
        window7.geometry("505x505") #dimensiones
        window7.config(bg="#000000")
        
        #Desarrollo del frame
        fr2 = Frame() #contenedor de widgets(elementos)
        fr2.pack(fill="both", expand="true") #mete al frame en la raiz (importante)
        fr2.config(bg="#000000")
        fr2.config(width="499", height="499")

        lab = Label(window7, text="¿QUÉ TAL SOS DURANTE EL DÍA?",
            font=("Arial", 18,"bold italic"), fg="#FFFFFF", bg="#000000").place(x=65, y=60)
        
        lab1 = Label(window7, text="HUEVÓN/A",
            font=("Arial", 14,"bold italic"), fg="#FFFFFF", bg="#000000").place(x=65, y=120)
        
        lab2 = Label(window7, text="LE HAGO GANAS",
            font=("Arial", 14,"bold italic"), fg="#FFFFFF", bg="#000000").place(x=65, y=190)
        
        lab3 = Label(window7, text="PILAS",
            font=("Arial", 14,"bold italic"), fg="#FFFFFF", bg="#000000").place(x=65, y=260)
        
        lab4 = Label(window7, text="MÁQUINA",
            font=("Arial", 14,"bold italic"), fg="#FFFFFF", bg="#000000").place(x=65, y=330)

        #Boton con evento para salir

        goBack = None

        window7.protocol('WM_DELETE_WINDOW', goBack)

        def goBack():

            if messagebox.askyesno("INICIO", "¿Seguro que quieres regresar?"):
                window7.destroy()
            
        exitbut = Button(window7, text="REGRESAR",
                         font=("Century Gothic", 9,"bold italic"), bg=("red"),foreground=("white"),
                         activebackground=("red"), activeforeground=("white"),
                         command=goBack).place(x=415,y=455)
        
        next = Button(window7, text="→",
                     font=("Century Gothic", 8,"bold"), bg="pink"
                     , activebackground=("white"),
                     command = btn7).place(x=245, y=420)
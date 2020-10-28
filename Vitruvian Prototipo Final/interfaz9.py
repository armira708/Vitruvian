from interfaz10 import btn9
from tkinter import*
from tkinter import messagebox

import tkinter as tk

btn8 = None

def btn8():
    
   
    
    if True:
        window9 = tk.Toplevel()
        window9.title("VITRUVIAN") #titulo de la ventana
        window9.resizable(0,0) #metodo que nos permite decidir si redimensionamos la ventana (booleano)
        window9.iconbitmap("1.ico") #icono
        window9.geometry("505x505") #dimensiones
        window9.config(bg="#000000")
        
        #Desarrollo del frame
        fr2 = Frame() #contenedor de widgets(elementos)
        fr2.pack(fill="both", expand="true") #mete al frame en la raiz (importante)
        fr2.config(bg="#000000")
        fr2.config(width="499", height="499")

        lab = Label(window9, text="YA SIN MIEDO \n¿CUÁNTO MEDÍS?",
            font=("Arial", 18,"bold italic"), fg="#FFFFFF", bg="#000000").place(x=150, y=60)

        #Boton con evento para salir

        goBack = None

        window9.protocol('WM_DELETE_WINDOW', goBack)

        def goBack():

            if messagebox.askyesno("INICIO", "¿Seguro que quieres regresar?"):
                window2.destroy()
            
        exitbut = Button(window9, text="REGRESAR",
                         font=("Century Gothic", 9,"bold italic"), bg=("red"),foreground=("white"),
                         activebackground=("red"), activeforeground=("white"),
                         command=goBack).place(x=415,y=455)
        
        next = Button(window9, text="→",
                     font=("Century Gothic", 8,"bold"), bg="pink"
                     , activebackground=("white"),
                     command = btn9).place(x=245, y=420)
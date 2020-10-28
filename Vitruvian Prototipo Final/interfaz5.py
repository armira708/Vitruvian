from interfaz6 import btn5
from tkinter import*
from tkinter import messagebox

import tkinter as tk

btn4 = None

def btn4():
    
   
    
    if True:
        window5 = tk.Toplevel()
        window5.title("VITRUVIAN") #titulo de la ventana
        window5.resizable(0,0) #metodo que nos permite decidir si redimensionamos la ventana (booleano)
        window5.iconbitmap("1.ico") #icono
        window5.geometry("505x505") #dimensiones
        window5.config(bg="#000000")
        
        #Desarrollo del frame
        fr2 = Frame() #contenedor de widgets(elementos)
        fr2.pack(fill="both", expand="true") #mete al frame en la raiz (importante)
        fr2.config(bg="#000000")
        fr2.config(width="499", height="499")
        
        lab = Label(window5, text="SIN PELOS EN LA LENGUA \n¿QUÉ TANTO QUERÉS SUBIR Ó BAJAR?",
            font=("Arial", 15,"bold italic"), fg="#FFFFFF", bg="#000000").place(x=55, y=60)

        #Boton con evento para salir

        goBack = None

        window5.protocol('WM_DELETE_WINDOW', goBack)

        def goBack():

            if messagebox.askyesno("INICIO", "¿Seguro que quieres regresar?"):
                window5.destroy()
            
        exitbut = Button(window5, text="REGRESAR",
                         font=("Century Gothic", 9,"bold italic"), bg=("red"),foreground=("white"),
                         activebackground=("red"), activeforeground=("white"),
                         command=goBack).place(x=415,y=455)
        
        next = Button(window5, text="→",
                     font=("Century Gothic", 8,"bold"), bg="pink"
                     , activebackground=("white"),
                     command = btn5).place(x=245, y=420)
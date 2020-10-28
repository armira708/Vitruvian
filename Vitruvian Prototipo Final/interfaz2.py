from interfaz3 import btn2
from tkinter import*
from tkinter import messagebox

import tkinter as tk

btn1 = None

def btn1():
    
   
    
    if True:
        window2 = tk.Toplevel()
        window2.title("VITRUVIAN") #titulo de la ventana
        window2.resizable(0,0) #metodo que nos permite decidir si redimensionamos la ventana (booleano)
        window2.iconbitmap("1.ico") #icono
        window2.geometry("505x505") #dimensiones
        window2.config(bg="#000000")
        
        #Desarrollo del frame
        fr2 = Frame() #contenedor de widgets(elementos)
        fr2.pack(fill="both", expand="true") #mete al frame en la raiz (importante)
        fr2.config(bg="#000000")
        fr2.config(width="499", height="499")
        
        lab = Label(window2, text="QUÉ ONDA \nCÓMO VAS...?",
            font=("Arial", 38,"bold italic"), fg="#FFFFFF", bg="#000000").place(x=75, y=150)

        #Boton con evento para salir

        goBack = None

        window2.protocol('WM_DELETE_WINDOW', goBack)

        def goBack():

            if messagebox.askyesno("INICIO", "¿Seguro que quieres regresar?"):
                window2.destroy()
            
        exitbut = Button(window2, text="REGRESAR",
                         font=("Century Gothic", 9,"bold italic"), bg=("red"),foreground=("white"),
                         activebackground=("red"), activeforeground=("white"),
                         command=goBack).place(x=415,y=455)
        
        next1 = Button(window2, text="→",
                     font=("Century Gothic", 8,"bold"), bg="pink"
                     , activebackground=("white"),
                     command = btn2).place(x=245, y=420)
        
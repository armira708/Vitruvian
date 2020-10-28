from interfaz13 import btn12
from tkinter import*
from tkinter import messagebox

import tkinter as tk

btn11 = None

def btn11():
    
   
    
    if True:
        window12 = tk.Toplevel()
        window12.title("VITRUVIAN") #titulo de la ventana
        window12.resizable(0,0) #metodo que nos permite decidir si redimensionamos la ventana (booleano)
        window12.iconbitmap("1.ico") #icono
        window12.geometry("505x505") #dimensiones
        window12.config(bg="#000000")
        
        #Desarrollo del frame
        fr2 = Frame() #contenedor de widgets(elementos)
        fr2.pack(fill="both", expand="true") #mete al frame en la raiz (importante)
        fr2.config(bg="#000000")
        fr2.config(width="499", height="499")
        
        lab = Label(window12, text="NITIDO \n¡EMPECEMOS CON TODO!",
            font=("Arial", 22,"bold italic"), fg="#FFFFFF", bg="#000000").place(x=75, y=150)
        


        #Boton con evento para salir

        goBack = None

        window12.protocol('WM_DELETE_WINDOW', goBack)

        def goBack():

            if messagebox.askyesno("INICIO", "¿Seguro que quieres regresar?"):
                window12.destroy()
            
        exitbut = Button(window12, text="REGRESAR",
                         font=("Century Gothic", 9,"bold italic"), bg=("red"),foreground=("white"),
                         activebackground=("red"), activeforeground=("white"),
                         command=goBack).place(x=415,y=455)
        
        next = Button(window12, text="→",
                     font=("Century Gothic", 8,"bold"), bg="pink"
                     , activebackground=("white"),
                     command = btn12).place(x=245, y=420)
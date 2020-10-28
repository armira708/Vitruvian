from interfaz11 import btn10
from tkinter import*
from tkinter import messagebox

import tkinter as tk

btn9 = None

def btn9():
    
   
    
    if True:
        window10 = tk.Toplevel()
        window10.title("VITRUVIAN") #titulo de la ventana
        window10.resizable(0,0) #metodo que nos permite decidir si redimensionamos la ventana (booleano)
        window10.iconbitmap("1.ico") #icono
        window10.geometry("505x505") #dimensiones
        window10.config(bg="#000000")
        
        #Desarrollo del frame
        fr2 = Frame() #contenedor de widgets(elementos)
        fr2.pack(fill="both", expand="true") #mete al frame en la raiz (importante)
        fr2.config(bg="#000000")
        fr2.config(width="499", height="499")
        
        lab = Label(window10, text="QUÉ TAN RUCO/A ESTÁS?",
            font=("Arial", 18,"bold italic"), fg="#FFFFFF", bg="#000000").place(x=100, y=60)

        #Boton con evento para salir

        goBack = None

        window10.protocol('WM_DELETE_WINDOW', goBack)

        def goBack():

            if messagebox.askyesno("INICIO", "¿Seguro que quieres regresar?"):
                window10.destroy()
            
        exitbut = Button(window10, text="REGRESAR",
                         font=("Century Gothic", 9,"bold italic"), bg=("red"),foreground=("white"),
                         activebackground=("red"), activeforeground=("white"),
                         command=goBack).place(x=415,y=455)
        
        next = Button(window10, text="→",
                     font=("Century Gothic", 8,"bold"), bg="pink"
                     , activebackground=("white"),
                     command = btn10).place(x=245, y=420)
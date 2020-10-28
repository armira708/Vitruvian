from interfaz9 import btn8
from tkinter import*
from tkinter import messagebox

import tkinter as tk

btn7 = None

def btn7():
    
   
    
    if True:
        window8 = tk.Toplevel()
        window8.title("VITRUVIAN") #titulo de la ventana
        window8.resizable(0,0) #metodo que nos permite decidir si redimensionamos la ventana (booleano)
        window8.iconbitmap("1.ico") #icono
        window8.geometry("505x505") #dimensiones
        window8.config(bg="#000000")
        
        #Desarrollo del frame
        fr2 = Frame() #contenedor de widgets(elementos)
        fr2.pack(fill="both", expand="true") #mete al frame en la raiz (importante)
        fr2.config(bg="#000000")
        fr2.config(width="499", height="499")
        
        lab = Label(window8, text="ASI SIN PAJAS \n¿CUÁNTO PESAS?",
            font=("Arial", 18,"bold italic"), fg="#FFFFFF", bg="#000000").place(x=150, y=60)
   

        #Boton con evento para salir

        goBack = None

        window8.protocol('WM_DELETE_WINDOW', goBack)

        def goBack():

            if messagebox.askyesno("INICIO", "¿Seguro que quieres regresar?"):
                window8.destroy()
            
        exitbut = Button(window8, text="REGRESAR",
                         font=("Century Gothic", 9,"bold italic"), bg=("red"),foreground=("white"),
                         activebackground=("red"), activeforeground=("white"),
                         command=goBack).place(x=415,y=455)
        
        next = Button(window8, text="→",
                     font=("Century Gothic", 8,"bold"), bg="pink"
                     , activebackground=("white"),
                     command = btn8).place(x=245, y=420)
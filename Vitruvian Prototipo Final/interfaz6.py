from interfaz7 import btn6
from tkinter import*
from tkinter import messagebox

import tkinter as tk

btn5 = None

def btn5():
    
   
    
    if True:
        window6 = tk.Toplevel()
        window6.title("VITRUVIAN") #titulo de la ventana
        window6.resizable(0,0) #metodo que nos permite decidir si redimensionamos la ventana (booleano)
        window6.iconbitmap("1.ico") #icono
        window6.geometry("505x505") #dimensiones
        window6.config(bg="#000000")
        
        #Desarrollo del frame
        fr2 = Frame() #contenedor de widgets(elementos)
        fr2.pack(fill="both", expand="true") #mete al frame en la raiz (importante)
        fr2.config(bg="#000000")
        fr2.config(width="499", height="499")
        
        lab = Label(window6, text="CON EL DEBIDO RESPETO \n¿SOS MACHO O ERES HEMBRA?",
            font=("Arial", 15,"bold italic"), fg="#FFFFFF", bg="#000000").place(x=85, y=60)

        #Boton con evento para salir

        goBack = None

        window6.protocol('WM_DELETE_WINDOW', goBack)

        def goBack():

            if messagebox.askyesno("INICIO", "¿Seguro que quieres regresar?"):
                window6.destroy()
            
        exitbut = Button(window6, text="REGRESAR",
                         font=("Century Gothic", 9,"bold italic"), bg=("red"),foreground=("white"),
                         activebackground=("red"), activeforeground=("white"),
                         command=goBack).place(x=415,y=455)
        
        next = Button(window6, text="→",
                     font=("Century Gothic", 8,"bold"), bg="pink"
                     , activebackground=("white"),
                     command = btn6).place(x=245, y=420)
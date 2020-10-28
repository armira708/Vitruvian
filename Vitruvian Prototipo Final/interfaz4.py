from interfaz5 import btn4
from tkinter import*
from tkinter import messagebox

import tkinter as tk

btn3 = None

def btn3():
    
   
    
    if True:
        window4 = tk.Toplevel()
        window4.title("VITRUVIAN") #titulo de la ventana
        window4.resizable(0,0) #metodo que nos permite decidir si redimensionamos la ventana (booleano)
        window4.iconbitmap("1.ico") #icono
        window4.geometry("505x505") #dimensiones
        window4.config(bg="#000000")
        
        #Desarrollo del frame
        fr2 = Frame() #contenedor de widgets(elementos)
        fr2.pack(fill="both", expand="true") #mete al frame en la raiz (importante)
        fr2.config(bg="#000000")
        fr2.config(width="499", height="499")
        
        lab = Label(window4, text="¿EN QUE TE HECHO LA MANO?",
            font=("Arial", 18,"bold italic"), fg="#FFFFFF", bg="#000000").place(x=65, y=60)
        
        lab = Label(window4, text="PONERTE TORO/A",
            font=("Arial", 14,"bold italic"), fg="#FFFFFF", bg="#000000").place(x=65, y=120)
        
        lab = Label(window4, text="MANTENERTE CALIDÁ",
            font=("Arial", 14,"bold italic"), fg="#FFFFFF", bg="#000000").place(x=65, y=190)
        
        lab = Label(window4, text="BAJAR LA TIMBA",
            font=("Arial", 14,"bold italic"), fg="#FFFFFF", bg="#000000").place(x=65, y=260)

        #Boton con evento para salir

        goBack = None

        window4.protocol('WM_DELETE_WINDOW', goBack)

        def goBack():

            if messagebox.askyesno("INICIO", "¿Seguro que quieres regresar?"):
                window4.destroy()
            
        exitbut = Button(window4, text="REGRESAR",
                         font=("Century Gothic", 9,"bold italic"), bg=("red"),foreground=("white"),
                         activebackground=("red"), activeforeground=("white"),
                         command=goBack).place(x=415,y=455)
        
        next = Button(window4, text="→",
                     font=("Century Gothic", 8,"bold"), bg="pink"
                     , activebackground=("white"),
                     command = btn4).place(x=245, y=420)
        
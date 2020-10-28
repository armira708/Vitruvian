from interfaz12 import btn11
from tkinter import*
from tkinter import messagebox

import tkinter as tk

btn10 = None

def btn10():
    
   
    
    if True:
        window11 = tk.Toplevel()
        window11.title("VITRUVIAN") #titulo de la ventana
        window11.resizable(0,0) #metodo que nos permite decidir si redimensionamos la ventana (booleano)
        window11.iconbitmap("1.ico") #icono
        window11.geometry("505x505") #dimensiones
        window11.config(bg="#000000")
        
        #Desarrollo del frame
        fr2 = Frame() #contenedor de widgets(elementos)
        fr2.pack(fill="both", expand="true") #mete al frame en la raiz (importante)
        fr2.config(bg="#000000")
        fr2.config(width="499", height="499")
        
        lab = Label(window11, text="AQUÍ EN CONFIANZA \n¿CÓMO QUERÉS QUE TE DIGA?",
            font=("Arial", 18,"bold italic"), fg="#FFFFFF", bg="#000000").place(x=70, y=60)

        #Boton con evento para salir

        goBack = None

        window11.protocol('WM_DELETE_WINDOW', goBack)

        def goBack():

            if messagebox.askyesno("INICIO", "¿Seguro que quieres regresar?"):
                window11.destroy()
            
        exitbut = Button(window11, text="REGRESAR",
                         font=("Century Gothic", 9,"bold italic"), bg=("red"),foreground=("white"),
                         activebackground=("red"), activeforeground=("white"),
                         command=goBack).place(x=415,y=455)
        
        next = Button(window11, text="→",
                     font=("Century Gothic", 8,"bold"), bg="pink"
                     , activebackground=("white"),
                     command = btn11).place(x=245, y=420)
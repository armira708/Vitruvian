from interfaz4 import btn3
from tkinter import*
from tkinter import messagebox

import tkinter as tk

btn2 = None

def btn2():
    
   
    
    if True:
        window3 = tk.Toplevel()
        window3.title("VITRUVIAN") #titulo de la ventana
        window3.resizable(0,0) #metodo que nos permite decidir si redimensionamos la ventana (booleano)
        window3.iconbitmap("1.ico") #icono
        window3.geometry("505x505") #dimensionesN
        window3.config(bg="#000000")
        
        #Desarrollo del frame
        fr2 = Frame() #contenedor de widgets(elementos)
        fr2.pack(fill="both", expand="true") #mete al frame en la raiz (importante)
        fr2.config(bg="#000000")
        fr2.config(width="499", height="499")
        
        lab1 = Label(window3, text="NECESITO HACERTE UNAS PREGUNTAS PARA \nECHARME LA MATE DE LO QUE TE PUEDO \nSUGERIR PARA CONSEGUIR EL CUERPO TAN \n'TUANIS' QUE QUERÉS!",
           font=("Arial", 13,"bold italic"), fg="#FFFFFF", bg="#000000").place(x=55, y=150)
        
    
        #Boton con evento para salir

        goBack = None

        window3.protocol('WM_DELETE_WINDOW', goBack)

        def goBack():

            if messagebox.askyesno("INICIO", "¿Seguro que quieres regresar?"):
                window2.destroy()
            
        exitbut = Button(window3, text="REGRESAR",
                         font=("Century Gothic", 9,"bold italic"), bg=("red"),foreground=("white"),
                         activebackground=("red"), activeforeground=("white"),
                         command=goBack).place(x=415,y=455)
        next2 = Button(window3, text="→",
                     font=("Century Gothic", 8,"bold"), bg="pink"
                     , activebackground=("white"),
                     command = btn3).place(x=245, y=420)
        
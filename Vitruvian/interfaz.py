from tkinter import*
from tkinter import messagebox

import time
#archivos

window = Tk()

#Desarrollo de la ventana raiz contenedor general
window.title("VITRUVIAN") #titulo de la ventana
window.resizable(0,0) #metodo que nos permite decidir si redimensionamos la ventana (booleano)
window.iconbitmap("1.ico") #icono
window.geometry("495x495") #dimensiones
window.config(bg="#000000")

#Desarrollo del frame
fr = Frame() #contenedor de widgets(elementos)
fr.pack(fill="both", expand="true") #mete al frame en la raiz (importante)
fr.config(bg="#000000")
fr.config(width="499", height="499")

#Titulo

nameReg = Label(window, text="Vitruvian ®", font=("Century Gothic", 8,"bold italic"),bg="#000000", fg="#FFFFFF").place(x=425, y=475)


#Imagenes
img1= PhotoImage(file = "1.png")

#Desarrollo de Label text para titulo

lab = Label(fr, image=img1).place(x=0, y=0)


#Botones

#Boton con evento que da informacion del programa LISTO

intel = None

window.protocol(intel)

def intel():
    
    if messagebox.askyesno("Vitruvian info",
                           "Integrantes Desarrolladores \n¿Desea ver info. general?"):
        info = Toplevel()
        info.title('INFORMACION GENERAL')
        info.resizable(0,0)
        info.iconbitmap("1.ico")
        info.geometry("350x150")
        
        labinfo = Label(info, text= "VITRUVIAN developed by:", font=("Century Gothic", 8, "italic")).pack(pady=15)
        labint = Label(info, text= "Andres Alejandro Armira Barco #201183 \nJuan Gomez #201630\n",
                       font=("Century Gothic", 9)).pack(pady=10)
        labint2= Label(info, text="Proyecto Final, Algoritmos y  programación básica", font=("Century Gothic", 6)).pack()  

infobut = Button(window, text="INFORMACION",
                  font=("Century Gothic", 9,"bold italic"), bg=("pink"),foreground=("black"),
                  activebackground=("purple"), activeforeground=("white"),
                  command=intel).place(x=375, y=25)

#Boton con evento para salir LISTO

salir = None

window.protocol('WM_DELETE_WINDOW', salir)

def salir():
    
    
    if messagebox.askyesno("SALIR", "¿Seguro que quieres salir?"):
        window.destroy()
                    
exitbut = Button(window, text="SALIR",
                 font=("Century Gothic", 9,"bold italic"), bg=("red"),foreground=("white"),
                 activebackground=("red"), activeforeground=("white"),
                 command=salir).place(x=355,y=550)
#BotonesInfos

btn1 = None

def btn1():
    
   
    
    if True:
        ati = Toplevel()
        ati.resizable(0,0) #metodo que nos permite decidir si redimensionamos la ventana (booleano)
        ati.iconbitmap("1.ico") #icono
        ati.geometry("499x499") #dimensiones
        ati.config(bg="#000000")
        
        
        #Botones optativos
    #----------------------------------------------------------------------#
        def patga():
            if True:
                
                galle = Toplevel()
                galle.resizable(0,0)
                galle.iconbitmap("fish.ico")
                galle.geometry("550x280")
                galle.config(bg="#9FF781")
                
                            
                goBack = None

                ati.protocol('WM_DELETE_WINDOW', goBack)

                def goBack():

                    if messagebox.askyesno("INICIO", "¿Seguro que quieres regresar?"):
                        galle.destroy()
            
                exitbut = Button(galle, text="REGRESAR",
                                 font=("Century Gothic", 9,"bold italic"), bg=("red"),foreground=("white"),
                                 activebackground=("red"), activeforeground=("white"),
                                 command=goBack).pack(pady=25)
                
        img2 = PhotoImage("2.png")
        photoimage = img2.subsample(3, 3)
        
        butati = Button(ati, image = photoimage, 
                    compound = LEFT).pack(side = TOP)
    
        

        #Boton con evento para salir

        goBack = None

        ati.protocol('WM_DELETE_WINDOW', goBack)

        def goBack():

            if messagebox.askyesno("INICIO", "¿Seguro que quieres regresar?"):
                ati.destroy()
            
        exitbut = Button(ati, text="REGRESAR",
                         font=("Century Gothic", 9,"bold italic"), bg=("red"),foreground=("white"),
                         activebackground=("red"), activeforeground=("white"),
                         command=goBack).place(x=295,y=385)
           

LagoAtitlan = Button(window, text="→",
                     font=("Century Gothic", 8,"bold"), bg="pink"
                     , activebackground=("white"),
                     command = btn1).place(x=245, y=420)
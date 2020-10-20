import tkinter as tk

from tkinter import *
  
root = Tk()      
canvas = Canvas(root, width = 500, height = 500)   
   
canvas.pack()      
img = PhotoImage(file="1.png")      
canvas.create_image(0,0, anchor=NW, image=img)    

button1 = tk.Button(root, text="-->", bg = "black", fg = "pink").place(x=240, y=440)


mainloop()
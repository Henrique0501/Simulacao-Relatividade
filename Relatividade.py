# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 10:39:21 2021

@author: Samaung
"""

from PIL import Image, ImageTk, ImageSequence
import tkinter as tk

class App:
    def __init__(self, parent):
        self.sinc=0
        self.sinc1=0
        self.parent=parent
        self.canvas=tk.Canvas(parent,width=1200,height=400, bg="black", highlightbackground= 'purple', highlightcolor="purple")
        self.canvas.pack()
        
        self.sequence1=[ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('Viagem1.gif'))]
        self.image1=self.canvas.create_image(350,200, image=self.sequence1[0])
        
        self.sequence2=[ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('Relogio_piloto1.gif'))]
        self.image2=self.canvas.create_image(800,100, image=self.sequence2[0])
        
        self.sequence3=[ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('Relogio_Terra1.gif'))]
        self.image3=self.canvas.create_image(800,300, image=self.sequence3[0])
        
        self.sequence4=[ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('Lorentz2.gif'))]
        self.image4=self.canvas.create_image(1050,200, image=self.sequence4[0])
        
        self.animate1(1)
        self.animate2(1)
        self.animate3(1)
        self.animate4(1)
        
    def sincronizar(self):
        self.sinc=1
        self.sinc1=1
        
    def animate1(self, counter):
        self.canvas.itemconfig(self.image1, image=self.sequence1[counter])
        self.parent.after(int(-74*Scale_velocidade.get()+75), lambda: self.animate1((counter+1)%len(self.sequence1)))
        
    def animate2(self, counter):
        self.canvas.itemconfig(self.image2, image=self.sequence2[counter])
        if self.sinc==1:
            counter=0
            self.sinc=0
        self.parent.after(4*33, lambda: self.animate2((counter+1)%len(self.sequence2)))
        #self.parent.after(20, lambda: self.animate2((counter+1)%len(self.sequence2)))
    def animate3(self, counter):
        self.canvas.itemconfig(self.image3, image=self.sequence3[counter])
        if self.sinc1==1:
            counter=0
            self.sinc1=0
        self.parent.after(round(4*33*(1-Scale_velocidade.get()**2)**0.5-round(Scale_velocidade.get()*5)), lambda: self.animate3((counter+1)%len(self.sequence3)))
  
    def animate4(self, counter):
        self.canvas.itemconfig(self.image4, image=self.sequence4[counter])
        self.parent.after(20, lambda: self.animate4((counter+1)%len(self.sequence4)))
        Velocidade["text"]=int(299792458*Scale_velocidade.get())
        
root=tk.Tk()
root.title("Relatividade Restrita")
root.geometry("+75+150")
root.resizable(False, False)

frame=tk.Frame(root)
frame.grid(row=0,column=0)

v0=tk.DoubleVar()

Scale_velocidade=tk.Scale(root, from_=0.001, to=0.999, orient=tk.HORIZONTAL,
                          length=200, highlightbackground= 'purple', highlightcolor="purple",
                          bg="SpringGreen2", label="Razão v/c\n ", fg="black", troughcolor="purple",tickinterval=0.998, 
                          resolution=-1, bd=10, variable=v0, activebackground="SpringGreen1")
Scale_velocidade.place(x=450, y=50)
Scale_velocidade.set(0.001)

Entrada=tk.Entry(root, textvariable=v0, bg="SpringGreen2", width=10)
Entrada.place(x=540, y=60)

Velocidade=tk.Label(root, bg="black", fg="SpringGreen2")
Velocidade.place(x=1040,y=225)

Nave=tk.Label(root, bg="black", fg="SpringGreen2", text="Nave")
Nave.place(x=880,y=110)

Terra=tk.Label(root, bg="black", fg="SpringGreen2", text="Terra")
Terra.place(x=880,y=310)

app = App(frame)

Bot=tk.Button(root, text="Sincronizar Relógios", command=lambda: app.sincronizar(),
              bg="SpringGreen2",activebackground="SpringGreen1")
Bot.place(x=1000, y=50)
#root.iconphoto(False, tk.PhotoImage(file='Relatividade.ico'))
root.iconbitmap('Relatividade1.ico')
root.mainloop()

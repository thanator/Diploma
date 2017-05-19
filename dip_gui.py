from tkinter import *
from choose import *
from create import *

from tkinter import filedialog
from tkinter import ttk
import threading

import matplotlib
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class CREATE_GUI:
    
    def __init__(self, master):
        self.size = 0
        self.ent = Entry(root, width=5)
        self.but = Button(root,text="Вывести", command = self.output)
        self.tex = Text(root,width=20,height=3,font="12",wrap=WORD)
        self.lab = Label(root, text="Введите размерматрицы для анаморфирования (1-20).", font="Arial 12")
        self.butt = Button(root, text = "Make it!",command=self.Work)

        self.frame = Frame(master)
        self.frame = Frame(width=150, height=500, bg="lightblue", bd=1, relief=SUNKEN)

        root.minsize(width=500,height=300)

        self.m = Menu(root)
        root.config(menu=self.m)

        self.sm = Menu(self.m)
        self.m.add_cascade(label="Menu",menu=self.sm)
        self.sm.add_command(label="Create",command=self.Create)
        self.init_plot(master)
        self.canvas
        self.ac
        

        #self.but.bind("<Button-1>",self.output)
    def init_plot(self, master):

        b = Figure(figsize=(8, 6),  dpi=100)
        self.ac = b.add_subplot(111)
        self.ac.plot(10,10) 
        self.ac.set_title('Current tour plot')
        self.ac.set_xlabel('X axis coordinates')
        self.ac.set_ylabel('Y axis coordinates')
        self.ac.grid(True)
        self.canvas = FigureCanvasTkAgg(b, master)
        self.canvas.draw()
        #canvas.get_tk_widget().grid(row=1, column=1, sticky=W)
        
    def plot_appear(self):
        self.canvas.get_tk_widget().grid(row=1, column=1, sticky=W)
    def plot_dissappear(self):
        self.canvas.get_tk_widget().grid_forget()

    def Create(self):
        self.tex.delete(1.0,END)
        self.lab.grid(row=0, column =0, columnspan = 3, padx = 10, pady = 10)
        self.ent.grid(row=1,column=0,padx=20)
        self.but.grid(row=1,column=1)
        self.tex.grid(row=1,column=2,padx=20,pady=10)
        self.plot_dissappear()

    def Work(self):
        self.lab.grid_forget()
        self.ent.grid_forget()
        self.but.grid_forget()
        self.tex.grid_forget()
        self.butt.grid_forget()
        self.ac.clear()
        create(self.size)
        x, y = Anamorph("example.xls")
        
        for i in range(len(x)):
           self.ac.plot(x[i], y[i])
        
        self.canvas.draw()
        self.canvas.show()
        self.plot_appear()

    

        


    def output(self):
        s = self.ent.get()
        self.ent.delete(0, 'end')
        
        try:
            self.size = int(s)
        except Exception:
            self.tex.insert(END, "Введите число от 1 до 20")
            self.size = 0
            self.butt.grid_forget()
            pass
    
        if (self.size > 1 and self.size < 21):
            self.tex.delete(1.0,END)
            self.tex.insert(END,"Будет " + s + "*" + s + " ячеек")
            self.butt.grid(row = 2, column = 1)
        else:
            self.size = 0
            self.tex.delete(1.0,END)
            self.tex.insert(END, "Введите число от 1 до 20")
            self.butt.grid_forget()
        
     



root = Tk()

Obj = CREATE_GUI(root)

root.mainloop() 
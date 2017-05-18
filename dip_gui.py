from tkinter import *
from choose import *



class CREATE_GUI:
    
    def __init__(self, master):
        self.size = 0
        self.ent = Entry(root, width=5)
        self.but = Button(root,text="Вывести", command = self.output)
        self.tex = Text(root,width=20,height=3,font="12",wrap=WORD)
        self.lab = Label(root, text="Введите размерматрицы для анаморфирования (1-20).", font="Arial 12")
        self.butt = Button(root, text = "Make it!",command=self.Work)

        root.minsize(width=500,height=300)

        self.m = Menu(root)
        root.config(menu=self.m)

        self.sm = Menu(self.m)
        self.m.add_cascade(label="Menu",menu=self.sm)
        self.sm.add_command(label="Create",command=self.Create)
        self.sm.add_command(label="Let's work!",command=self.Work)
        #self.but.bind("<Button-1>",self.output)
    
    
        

        
    def Create(self):
        
        self.lab.grid(row=0, column =0, columnspan = 3, padx = 10, pady = 10)
        self.ent.grid(row=1,column=0,padx=20)
        self.but.grid(row=1,column=1)
        self.tex.grid(row=1,column=2,padx=20,pady=10)
        



    def Work(self):
        self.lab.grid_forget()
        self.ent.grid_forget()
        self.but.grid_forget()
        self.tex.grid_forget()
        self.butt.grid_forget()
        Anamorph("book_1.xls")
        
        


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
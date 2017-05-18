from tkinter import *
root = Tk()

but = Button(root, text = "Create!", width=20,height=2)
ent = Entry(root, width=20, bd=3)
lab = Label(root, text="Введите размерматрицы для анаморфирования (1-20).", font="Arial 18")
fra = Frame(root,width=700,height=500,bg="White")

def hide_me(event):
    event.widget.pack_forget()

def Create():
    fra.destroy()
    root.minsize(width=500,height=300)
    ent.pack()
    but.pack()

    
    
def Work():
    lab.bind
    fra.pack()
    fra.config(width=700)
    fra.config(height=500)



m = Menu(root)
root.config(menu=m)

sm = Menu(m)
m.add_cascade(label="Menu",menu=sm)
sm.add_command(label="Create",command=Create)
sm.add_command(label="Let's work!",command=Work)

root.mainloop()
from tkinter import *

root = Tk()

var0 = StringVar()  # значение каждого флажка ...
var1 = StringVar()  # ... хранится в собственной переменной
var2 = StringVar()
# если флажок установлен, то в ассоциированную переменную ...
# ...(var0,var1 или var2) заносится значение onvalue, ...
# ...если флажок снят, то - offvalue.
ch0 = Checkbutton(root, text="Окружность", variable=var0,
                  onvalue="circle", offvalue="-")
ch1 = Checkbutton(root, text="Квадрат", variable=var1,
                  onvalue="square", offvalue="-")
ch2 = Checkbutton(root, text="Треугольник", variable=var2,
                  onvalue="triangle", offvalue="-")

lis = Listbox(root, height=3)


def result(event):
    v0 = var0.get()
    v1 = var1.get()
    v2 = var2.get()
    l = [v0, v1, v2]  # значения переменных заносятся в список
    lis.delete(0, 2)  # предыдущее содержимое удаляется из Listbox
    for v in l:  # содержимое списка l последовательно ...
        lis.insert(END, v)  # ...вставляется в Listbox

but = Button(root, text="Получить значения")
but.bind('<Button-1>', result)

ch0.deselect()  # "по умолчанию" флажки сняты
ch1.deselect()
ch2.deselect()

ch0.pack()
ch1.pack()
ch2.pack()
but.pack()
lis.pack()

root.mainloop()

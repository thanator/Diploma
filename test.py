import os
import matplotlib.pyplot as plt

def save(name='', fmt='png'):
    pwd = os.getcwd()
    os.chdir('./pictures/%s' % fmt)
    plt.savefig('%s.%s' % (name, fmt), fmt='png')
    os.chdir(pwd)
    #plt.close()

    
import matplotlib.pyplot as plt

fig = plt.figure()
# Добавление на рисунок прямоугольной (по умолчанию) области рисования
ax = fig.add_axes([0, 0, 1, 1])
print (type(ax))
plt.scatter(1.0, 1.0)
plt.savefig('example 142a.png', fmt='png')


fig = plt.figure()
# Добавление на рисунок круговой области рисования
ax = fig.add_axes([0, 0, 1, 1], polar=True)
plt.scatter(0.0, 0.5)
plt.savefig('example 142b.png', fmt='png')

# смотри преамбулу
save('pic_1_4_2', fmt='pdf')
save('pic_1_4_2', fmt='png')

plt.show()


##

from matplotlib import pyplot as plt
import tkinter as tkt

class LineBuilder:
    def __init__(self, line):
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        print('click', event)
        if event.inaxes!=self.line.axes: return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('click to build line segments')
line, = ax.plot([0], [0])  # empty line
linebuilder = LineBuilder(line)

plt.show()
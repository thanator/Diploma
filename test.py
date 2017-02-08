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
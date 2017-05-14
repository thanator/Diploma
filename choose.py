import matplotlib.pyplot as plt
import math
import copy
import xlrd
import xlwt

# функция для преобращования массива с координатами в массив для рисования
def Setka_to_XY(X_temp, Y_temp, Setka):
    k_temp = 1
    j_temp = 0
    i_temp = 0
    l_temp = 0
    x_all = 0
    y_all = 0
    x_pis = [0] * kol_yach
    y_pis = [0] * kol_yach
    for i_temp in range(kol_yach):
        x_pis[i_temp] = [0]
        y_pis[i_temp] = [0]
        # создание будущего массива с центральными точками (костыли)
    i_temp = 0
    for i_temp in range(kol_yach):
        while k_temp == Setka[j_temp][1][0]:
            X_temp[i_temp][l_temp] = Setka[j_temp][0][0]
            Y_temp[i_temp][l_temp] = Setka[j_temp][0][1]
            # занесение из входного массива в массив выводной
            x_all += Setka[j_temp][0][0][0]
            y_all += Setka[j_temp][0][1][0]
            # суммирование всех координат (для дальнейшего рассчёта центральной
            # точки)
            l_temp += 1
            if k_temp != Setka[j_temp + 1][1][0]:
                x_all = x_all / l_temp
                y_all = y_all / l_temp
                # вычисление центральной точки
                X_temp[i_temp][l_temp] = X_temp[i_temp][0]
                Y_temp[i_temp][l_temp] = Y_temp[i_temp][0]
                # Говнище для добавления последней соединяющей линии (последняя
                # и первая точка)
                x_pis[i_temp][0] = x_all
                y_pis[i_temp][0] = y_all
                # Говнище для добавления центральной точки
                X_temp[i_temp][l_temp + 1] = x_pis[i_temp]
                Y_temp[i_temp][l_temp + 1] = y_pis[i_temp]
                # тоже центральная точка, но уже в массиве
            j_temp += 1
        x_all = 0
        y_all = 0
        l_temp = 0
        k_temp += 1

# функция для вычисления площади

def Plosh(X_temp, Y_temp, S_temp, Koef_temp):
    i_temp = 0
    k_temp = 1
    j_temp = 0
    schet_temp = 0
    
    for i_temp in range(kol_yach):
        S_temp[i_temp]=0

    i_temp = 0

    for i_temp in range(kol_yach): # кол-во ячеек
        while k_temp == Kord_setka[j_temp][1][0]:
            if k_temp == Kord_setka[j_temp + 1][1][0]:
                S_temp[i_temp] += (X_temp[i_temp][schet_temp][0] - X_temp[i_temp][schet_temp + 1][
                                   0]) * (Y_temp[i_temp][schet_temp][0] + Y_temp[i_temp][schet_temp + 1][0])
            else:
                S_temp[i_temp] += (X_temp[i_temp][schet_temp][0] - X_temp[i_temp][0][0]) * (
                    Y_temp[i_temp][schet_temp][0] + Y_temp[i_temp][0][0])
                S_temp[i_temp] = S_temp[i_temp] / 2
            j_temp += 1
            schet_temp += 1
        schet_temp = 0
        k_temp += 1

# функция для смещения координат

def Smech(X_temp, Y_temp, x_smes, y_smes, ind_i, ind_j):
    vrem_x = X_temp[ind_i][ind_j][0]
    vrem_y = Y_temp[ind_i][ind_j][0]
    i_ind = 0
    j_ind = 0
    while(i_ind<kol_yach):
        j_ind = 0
        while(j_ind<len(X_temp[i_ind])-2):
            
            if(X_temp[i_ind][j_ind][0] == vrem_x):
                if(Y_temp[i_ind][j_ind][0] == vrem_y):
                    X_temp[i_ind][j_ind][0] += x_smes
                    Y_temp[i_ind][j_ind][0] += y_smes

            j_ind += 1
        i_ind += 1

RB = xlrd.open_workbook('book_1.xls', formatting_info=True)
# выбираем активный лист
SHEET = RB.sheet_by_index(0)

# COL_OF_YACH = SHEET.row_values(1, 2, 3) -> 2

NUM_STROK = len(SHEET.col_values(6, 3))

i = 0

Kord_setka = [0] * NUM_STROK
for i in range(NUM_STROK):
    Kord_setka[i] = [0] * 2
    Kord_setka[i][0] = [0] * 2
    # создание массива для считывания экселевского файла

Koef_t_Anamorph = []

num_yach = list(set())
i = 0
kol_yach = 0
while i < NUM_STROK:

    Kord_setka[i][1] = SHEET.row_values(i + 3, 6, 7)    # ->Num
    if i != 0 and Kord_setka[i][1] != Kord_setka[i - 1][1]:
        Koef_t_Anamorph += SHEET.row_values(i + 2, 7, 8)
        kol_yach += 1
    Kord_setka[i][0][0] = SHEET.row_values(i + 3, 4, 5)  # ->X
    Kord_setka[i][0][1] = SHEET.row_values(i + 3, 5, 6)  # ->Y
    i += 1
# считывание экселевского файла
sis = 0
for pis in range(kol_yach):
    sis += Koef_t_Anamorph[pis]

sis = (sis / (len(Koef_t_Anamorph)))

Koef_t_Anamorph.append(sis)
# Пoдсчёт коэф-то анаморфирования
x = [0] * kol_yach
y = [0] * kol_yach
# будущие Х и У
i = 0
k = 1
j = 0
schet = 0
for i in range(kol_yach):
    while k == Kord_setka[j][1][0]:
        j += 1
        schet += 1
    schet += 2
    x[i] = [0] * schet
    y[i] = [0] * schet
    schet = 0
    k += 1

zero_x = copy.deepcopy(x)
zero_y = copy.deepcopy(y)
# создание массива для будущего вывода
Setka_to_XY(x, y, Kord_setka)

# вызов подсчёта площади

Ploshad = [0] * kol_yach
Ploshad_t = [0]*kol_yach

Plosh(x, y, Ploshad, 1)

# делаем из ячеек якобы круги. вычисляем их радиусы
# 

R = [0] * kol_yach
R_shtr = [0] * kol_yach
i = 0

for s in Ploshad:
    Ploshad[i]= math.fabs(s)
    i += 1
i = 0

for s in Ploshad:
    R_shtr[i] = math.sqrt(((s * Koef_t_Anamorph[i]) / (math.pi * Koef_t_Anamorph[kol_yach])))
    R[i] = math.sqrt((s) / (math.pi))
    i += 1

for s in range(kol_yach):
    Ploshad[s] = Ploshad[s]*Koef_t_Anamorph[s] / Koef_t_Anamorph[kol_yach]

# Тут начнётся пункт 11-ый. и тут будет цикл, в котором будет происходить
# какая-то фигня постоянно.

i = 0

i_for_cen = 0;
k = 1
schet = 0
x_smesh = 0
y_smesh = 0

for i in range(kol_yach):
    plt.plot(x[i], y[i])
plt.show()

test = len(x)
kol_kor = 0
while (test != 0):
    kol_kor += len(x[test-1])
    test -= 1
flag = 0
count = 0
while (flag == 0):
    temp_x = copy.deepcopy(zero_x)
    temp_y = copy.deepcopy(zero_y)
    t = 0
    while (t < kol_yach):

        j = 0
        while (j < len(x[t]) - 1):
            
            x_smesh = 0
            y_smesh = 0

            i = 0
            x_i = x[t][j][0]
            y_i = y[t][j][0]
            while (i < kol_yach):               
               
                x_c = x[i][len(x[i]) - 1][0]
                y_c = y[i][len(y[i]) - 1][0]
                
                L = math.sqrt((x_c - x_i)**2 + (y_c - y_i)**2)
                
                if (L <= R[i]):
                    L_sm = L * (R_shtr[i]/R[i] - 1)
                else:
                    L_sm = math.sqrt(L**2 + ((R_shtr[i])**2 - (R[i])**2)) - L
                if (x_c == x_i and y_c == y_i):
                    Alpha = 0
                elif (x_c == x_i):
                    Alpha = 1.570796327
                elif (y_c == y_i):
                    Alpha = 0
                else:
                    Alpha = math.atan(math.fabs(y_c - y_i)/math.fabs(x_c - x_i))
                
                XX = L_sm*math.cos(Alpha)
                if (x_c > x_i):
                    XX = -XX
                YY = L_sm*math.sin(Alpha)
                if (y_c > y_i):
                    YY = -YY

                x_smesh += XX
                y_smesh += YY

                i += 1
            
            temp_x[t][j] = x_smesh
            temp_y[t][j] = y_smesh
            j += 1

        t += 1
    
    t = 0

    while (t < kol_yach):
        j = 0
        while (j < len(x[t]) - 1):
            x[t][j][0] += temp_x[t][j]
            y[t][j][0] += temp_y[t][j]
            j += 1
        t += 1

    schet = 0
    while (schet != kol_yach):
        schet_1 = 0
        schet_2 = 0
        k = 0
        while (k < len(x[schet])-2):
            schet_1 += x[schet][k][0]
            schet_2 += y[schet][k][0]
            k += 1
        x[schet][-1][0] = schet_1/k
        y[schet][-1][0] = schet_2/k
        schet += 1

    temp_x = copy.deepcopy(zero_x)
    temp_y = copy.deepcopy(zero_y)

    schet = 0
    Plosh(x ,y , Ploshad_t, 1)
    for pis in range(kol_yach):     # проверка на окончание этой адской фигни
        if (math.fabs(Ploshad_t[pis]-Ploshad[pis])<=0.01):
            flag = 0
    for i in range(kol_yach):
        plt.plot(x[i], y[i])

    plt.show()
    



'''
flag = 0
count = 0
while(flag==0):
    temp_x = copy.deepcopy(zero_x)
    temp_y = copy.deepcopy(zero_y)
    i = 0
    # для рассчёта всякого по i and j
    while(i < kol_yach):
        j = 0
        while (j < len(x[i])-2):
            i_for_cen = 0
            #  пункт 11 - расстояние до центра
            while (i_for_cen < kol_yach):
                Rasst = 0
                Rasst = math.sqrt(((x[i_for_cen][-1][0] - x[i][j][0])**2) + (y[i_for_cen][-1][0] - y[i][j][0])**2)

                # пункт 12 - сдвиг

                Sdvig = 0

                if Rasst <= R[i]:
                    Sdvig = Rasst * (R_shtr[i] / R[i] - 1)
                else:
                    Sdvig = math.sqrt((Rasst)**2 + ((R_shtr[i])**2 - (R[i])**2)) - Rasst
                i_cen = 0
                while (i_cen < kol_yach):
                    # пункт 13 - угол

                    Alpha = 0

                    if x[i][j][0] == x[i_cen][-1][0] and y[i][j][0] == y[i_cen][-1][0]:
                        Alpha = 0
                    elif x[i][j][0] == x[i_cen][-1][0]:
                        Alpha = 1.570796327
                    elif y[i][j][0] == y[i_cen][-1][0]:
                        Alpha = 0
                    else:
                        Alpha = math.atan(math.fabs(y[i_cen][-1][0] - y[i][j][0])/math.fabs(x[i_cen][-1][0] - x[i][j][0]))

                    # пункт 14 - смещение координат
                    if (x[i_cen][-1][0] > x[i][j][0]):
                        x_smesh = -1*( Sdvig*math.cos(Alpha))
                    else:
                        x_smesh = Sdvig*math.cos(Alpha)
                    if (y[i_cen][-1][0] > y[i][j][0]):
                        y_smesh = -1*(Sdvig*math.sin(Alpha))
                    else:
                        y_smesh = Sdvig*math.sin(Alpha)
                    temp_x[i][j] += x_smesh
                    temp_y[i][j] += y_smesh
                    #Smech(x,y,x_smesh,y_smesh,i,j)

                    i_cen += 1
                    i_for_cen += 1
                
                j += 1
                if (j == len(x[i])-2):          # для запихивания в конец (предпосл. место) первой точки, для правильной отрисовки
                    temp_x[i][j] = temp_x[i][0]
                    temp_y[i][j] = temp_y[i][0]

        

        p = 0
        while (p < kol_yach):
            o = 0
            while (o < len(x[p]) - 2):
                
                x[p][o][0] += temp_x[p][o]
                y[p][o][0] += temp_y[p][o]


                o += 1
            p += 1


        i += 1
        if (i == kol_yach):                 # рассчёт центральной точки
            schet = 0
            while (schet != kol_yach):
                schet_1 = 0
                schet_2 = 0
                k = 0
                while (k < len(x[schet])-2):
                    schet_1 += x[schet][k][0]
                    schet_2 += y[schet][k][0]
                    k += 1
                x[schet][-1][0] = schet_1/k
                y[schet][-1][0] = schet_2/k
                schet += 1

            # переразчёт плозади
            Plosh(x ,y , Ploshad_t, 1)

            flag = 1
            count += 1
            for pis in range(kol_yach):     # проверка на окончание этой адской фигни
                if ((Ploshad_t[pis]-Ploshad[pis])<=0.01):
                    flag = 0
            print (count, end='\n')

            #temp_x = copy.deepcopy(x)
            #temp_y = copy.deepcopy(y)

            if (count%999==0):
                #  f = open('output_bef.txt', 'w')

                #  for item in range(kol_yach):
                #     f.write(str(x[item]) + "--" + y[item] + '\n')
                #  f.close()
                
                #for i in range(kol_yach):
                #   plt.plot(temp_x[i], temp_y[i])
                #plt.show()
                
                #  q = open('output_aft.txt','w')
                #  for item in range(x):
                #     q.write(str(x[item]) + "--" + y[item] + '\n')
                #  q.close()
                print('New Iteration')
            #del temp_x[:]
            #del temp_y[:]
# тут будет конец общего геморра
'''
for i in range(kol_yach):
    plt.plot(x[i], y[i])

plt.show()

for pis in range(len(Koef_t_Anamorph)):
    print(Koef_t_Anamorph[pis])

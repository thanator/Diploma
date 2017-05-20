import matplotlib.pyplot as plt
import math
import copy
import xlrd
import xlwt

# функция для преобращования массива с координатами в массив для рисования
def Setka_to_XY(X_temp, Y_temp, Setka, kol_yach):
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

def Plosh(X_temp, Y_temp, S_temp, Koef_temp, kol_yach):
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
                S_temp[i_temp] = math.fabs(S_temp[i_temp])
            j_temp += 1
            schet_temp += 1
        schet_temp = 0
        k_temp += 1

def Plosh_new(X_temp, Y_temp, S_temp, Koef_temp, kol_yach, Kord_setka):
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
                S_temp[i_temp] += (X_temp[i_temp][schet_temp][0]*Y_temp[i_temp][schet_temp + 1][0] - X_temp[i_temp][schet_temp + 1][
                                   0] * Y_temp[i_temp][schet_temp][0] )
            else:
                S_temp[i_temp] += (X_temp[i_temp][schet_temp][0]*Y_temp[i_temp][0][0] - X_temp[i_temp][0][
                                   0] * Y_temp[i_temp][schet_temp][0] )
                S_temp[i_temp] = S_temp[i_temp] / 2
                S_temp[i_temp] = math.fabs(S_temp[i_temp])
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

def setka(open_it):
    
    RB = xlrd.open_workbook(open_it, formatting_info=True)
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
    Setka_to_XY(x, y, Kord_setka, kol_yach)
    return x, y
    
def Anamorph(open_it):

    RB = xlrd.open_workbook(open_it, formatting_info=True)
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
    Setka_to_XY(x, y, Kord_setka, kol_yach)

    # вызов подсчёта площади

    Ploshad = [0] * kol_yach
    Ploshad_t = [0]*kol_yach

    Plosh_new(x, y, Ploshad, 1, kol_yach, Kord_setka)

    # делаем из ячеек якобы круги. вычисляем их радиусы
    # 

    R = [0] * kol_yach
    R_shtr = [0] * kol_yach
    i = 0

    for s in Ploshad:
        Ploshad[i]= math.fabs(s)
        print(s)
        i += 1
    i = 0

    for s in Ploshad:
        R_shtr[i] = math.sqrt((s * Koef_t_Anamorph[i]) / (math.pi * Koef_t_Anamorph[kol_yach])) # Rcp
        R[i] = math.sqrt((s) / (math.pi))   # Rrl
        i += 1

    for s in range(kol_yach):
        Ploshad[s] = Ploshad[s]*Koef_t_Anamorph[s] / Koef_t_Anamorph[kol_yach]
        print(Ploshad[s])


    # Тут начнётся пункт 11-ый. и тут будет цикл, в котором будет происходить
    # какая-то фигня постоянно.

    i = 0

    i_for_cen = 0;
    k = 1
    schet = 0
    x_smesh = 0
    y_smesh = 0

    # for i in range(kol_yach):
    #     plt.plot(x[i], y[i])
    # plt.show()

    test = len(x)
    kol_kor = 0
    while (test != 0):
        kol_kor += len(x[test-1])
        test -= 1
    flag = 0
    count = 0
    while (flag == 0):
        # проверка на окончание
        temp_x = copy.deepcopy(zero_x)
        temp_y = copy.deepcopy(zero_y)
        t = 0
        while (t < kol_yach):
            # самое начало - для каждой из ячеек
            j = 0
            
            while (j < len(x[t]) - 2):
                # для каждой из точек
                
                i = 0
                x_i = x[t][j][0]
                y_i = y[t][j][0]
                while (i < kol_yach):
                    # по всем центрам            
                
                    x_c = x[i][-1][0]
                    y_c = y[i][-1][0]
                    
                    L = math.sqrt((x_c - x_i)**2 + (y_c - y_i)**2)
                    # смещение точки 
                    if (L <= R[i]):
                        L_sm = L * (R_shtr[i]/R[i] - 1)
                    else:
                        L_sm = math.sqrt(L**2 + ((R_shtr[i])**2 - (R[i])**2)) - L
                    # расчёт угла
                    if (x_c == x_i and y_c == y_i):
                        Alpha = 0
                    elif (x_c == x_i):
                        Alpha = 1.570796327
                    elif (y_c == y_i):
                        Alpha = 0
                    else:
                        Alpha = math.atan(math.fabs(y_c - y_i)/math.fabs(x_c - x_i))
                    
                    
                    
                    # if (R_shtr[i] > R[i]):
                    #     L_sm *= -1
                    
                    
                    # расчёт смещения

                    XX = L_sm*math.cos(Alpha)
                    if (x_c > x_i):
                        XX = -1*XX
                    YY = L_sm*math.sin(Alpha)
                    if (y_c > y_i):
                        YY = -1*YY

                    temp_x[t][j] += XX
                    temp_y[t][j] += YY

                    i += 1
                x[t][j][0] += temp_x[t][j]
                y[t][j][0] += temp_y[t][j]           
                    
                j += 1
                if (j == len(x[t]) - 2):
                    x[t][j][0] = x[t][0][0]
                    y[t][j][0] = y[t][0][0]

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

        schet = 0

        Ploshad = copy.deepcopy(Ploshad_t)
        Plosh_new(x ,y , Ploshad_t, 1, kol_yach, Kord_setka)
        pis = 0

        for s in Ploshad_t:
            #R_shtr[pis] = math.sqrt(((s * Koef_t_Anamorph[pis]) / (math.pi * Koef_t_Anamorph[kol_yach]))) # Rcp
            R[pis] = math.sqrt((s) / (math.pi))   # Rrl
            pis += 1
        
        for s in range(kol_yach):
            Ploshad_t[s] = Ploshad_t[s]*Koef_t_Anamorph[s] / Koef_t_Anamorph[kol_yach]    
            print(Ploshad_t[s])

        for pis in range(kol_yach):     # проверка на окончание этой адской фигни
            if (math.fabs(Ploshad_t[pis]-Ploshad[pis])<=0.1):
                i_for_cen += 1
        if (i_for_cen/kol_yach > 0.75):
            flag=1
        else:
            i_for_cen=0
        for i in range(kol_yach):
            plt.plot(x[i], y[i])
        plt.savefig("foo.jpg")

        # plt.show()
        

    # for i in range(kol_yach):
    #     plt.plot(x[i], y[i])

    # plt.show()
    i = 0
    # for i in range(kol_yach):
    #     x[i][-1].pop(0)
    #     y[i][-1].pop(0)

    return x, y

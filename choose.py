import matplotlib.pyplot as plt


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
            # суммирование всех координат (для дальнейшего рассчёта центральной точки)
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

num_yach = list(set())
i = 0
kol_yach = 0
while i < NUM_STROK:

    Kord_setka[i][1] = SHEET.row_values(i + 3, 6, 7)    # ->Num
    if i != 0 and Kord_setka[i][1] != Kord_setka[i - 1][1]:
        kol_yach += 1
    Kord_setka[i][0][0] = SHEET.row_values(i + 3, 4, 5)  # ->X
    Kord_setka[i][0][1] = SHEET.row_values(i + 3, 5, 6)  # ->Y
    i += 1
# считывание экселевского файла

x = [0] * kol_yach
y = [0] * kol_yach

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
# создание массива для будущего вывода
Setka_to_XY(x, y, Kord_setka)

for i in range(kol_yach):
    plt.plot(x[i], y[i])

plt.show()

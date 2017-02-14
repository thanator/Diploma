import matplotlib.pyplot as plt


import xlrd
import xlwt


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
    schet += 1
    x[i] = [0] * schet
    y[i] = [0] * schet
    schet = 0
    k += 1

k = 1
j = 0
i = 0
l = 0
for i in range(kol_yach):
    while k == Kord_setka[j][1][0]:
        x[i][l] = Kord_setka[j][0][0]
        y[i][l] = Kord_setka[j][0][1]
        if k != Kord_setka[j+1][1][0]:
            x[i][l+1] = x[i][0]
            y[i][l+1] = y[i][0]
        l += 1
        j += 1
    l = 0
    k += 1

for i in range(kol_yach):
    plt.plot(x[i], y[i])

plt.show()

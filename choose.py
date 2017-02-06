import xlrd
import xlwt
# открываем файл
RB = xlrd.open_workbook('book_1.xls', formatting_info=True)
# выбираем активный лист
SHEET = RB.sheet_by_index(0)

# COL_OF_YACH = SHEET.row_values(1, 2, 3) -> 2
class Yach:

    def __init__(self):
        self.iks = []
        self.igrik = []
        self.number = 0

NUM_STROK = len(SHEET.col_values(6, 3))

# YACH_1.iks = SHEET.col_values(4, 3) -> x
# YACH_1.igrik = SHEET.col_values(5, 3) -> y

# print(YACH_1.iks, YACH_1.igrik)

#a = [ [[10, 20],1], [[11, 22],2] ]
# print(a[0][0][1]) -> 20
# print(a[0][1]) -> 1
# print(a[0][0][1]) -> 20

# print(num_stok)
i = 0

Kord_setka = [0]*NUM_STROK
for i in range(NUM_STROK):
    Kord_setka[i] = [0]*2
    Kord_setka[i][0] = [0]*2



i = 0
while i < NUM_STROK:

    Kord_setka[i][1] = SHEET.row_values(i+3, 6, 7)
    Kord_setka[i][0][0] = SHEET.row_values(i+3, 4, 5) # ->X
    Kord_setka[i][0][1] = SHEET.row_values(i+3, 5, 6) # ->Y
    i += 1


print(Kord_setka)
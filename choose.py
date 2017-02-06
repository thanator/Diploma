import xlrd
import xlwt
# открываем файл
RB = xlrd.open_workbook('book_1.xls', formatting_info=True)
# выбираем активный лист
SHEET = RB.sheet_by_index(0)

val = SHEET.row_values(1, 2)

print(val)
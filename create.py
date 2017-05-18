import xlrd
import xlwt




def create(size):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet', cell_overwrite_ok=True)
    x = y = 10
    #ws.write(2, 0, 1) # 2 - y, 0 - x, 1 - value 
    x_size = 0
    while (x_size < size):
        y_size = 0
        while (y_size < size):
            i = 0
            while (i < 8):
                if (i < 3):
                    ws.write(3 + y_size*8 + i, 4, x)
                    ws.write(3 + y_size*8 + i, 5, y)
                    ws.write(3 + y_size*8 + i, 6, y_size)
                    x += 3
                elif (i < 5):
                    ws.write(3 + y_size*8 + i, 4, x)
                    ws.write(3 + y_size*8 + i, 5, y)
                    ws.write(3 + y_size*8 + i, 6, y_size)
                    y += 3
                elif (i < 7):
                    ws.write(3 + y_size*8 + i, 4, x)
                    ws.write(3 + y_size*8 + i, 5, y)
                    ws.write(3 + y_size*8 + i, 6, y_size)
                    x -= 3
                else:
                    ws.write(3 + y_size*8 + i, 4, x)
                    ws.write(3 + y_size*8 + i, 5, y)
                    ws.write(3 + y_size*8 + i, 6, y_size)
                    y -= 3

                i += 1
            y_size += 1
        x_size += 1

    wb.save('example.xls')

create(2)


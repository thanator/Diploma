import xlrd
import xlwt
import math
import random
from pic_work import *




def create(size):
    koef = PicWork("test.jpg", size)
    
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet', cell_overwrite_ok=True)
    x = y = 7
    j = 0
    count = 0
    #ws.write(2, 0, 1) # 2 - y, 0 - x, 1 - value 
    x_size = 0
    while (x_size < size):
        y_size = 0
        while (y_size < size):
            i = 0
            while (i < 8):
                if (i < 3):
                    x += 3
                    ws.write(3 + j, 4, x)
                    ws.write(3 + j, 5, y)
                    ws.write(3 + j, 6, count+1)
                    
                elif (i < 5):
                    y += 3
                    ws.write(3 + j, 4, x)
                    ws.write(3 + j, 5, y)
                    ws.write(3 + j, 6, count+1)
                    
                elif (i < 7):
                    x -= 3
                    ws.write(3 + j, 4, x)
                    ws.write(3 + j, 5, y)
                    ws.write(3 + j, 6, count+1)
                    
                else:
                    y -= 3
                    ws.write(3 + j, 4, x)
                    ws.write(3 + j, 5, y)
                    ws.write(3 + j, 6, count+1)                   
                
                i += 1
                j += 1
            ws.write(2 + j, 7, koef[count]) # тут надо задавать коэф-фт
            x -= 3
            y += 3
            y_size += 1
            count += 1
        
        x_size += 1
        y -= 6*size
        x += 6
    ws.write(3 + j, 4, 0)
    ws.write(3 + j, 5, 0)
    ws.write(3 + j, 6, 0)
    ws.write (1, 2, count)

    wb.save('example.xls')




from PIL import Image, ImageDraw

from resizeimage import resizeimage
import xlrd
import xlwt


def res(mage, form, size):

    with open(mage + form, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [size, size])
            cover.save(mage + "_temp" + form, image.format)

def PicWork(mage, form, size):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet', cell_overwrite_ok=True)
    res(mage, form, size)
    image = Image.open(mage + "_temp" + form) #Открываем изображение. 
    draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
    width = image.size[0] #Определяем ширину. 
    height = image.size[1] #Определяем высоту. 	
    
    pix = image.load() #Выгружаем значения пикселей.
    count = 0
    koef = []
    for i in range(width):
    		for j in range(height):
                    a = pix[i, height - j-1][0]
                    b = pix[i,  height - j-1][1]
                    c = pix[i,  height - j-1][2]
                    S = (a + b + c) // 3
                    #S = 255 - S
                    if (S == 0):
                        S = 1
                    koef.append(S)
    return koef
                    
                    
                    
    

    
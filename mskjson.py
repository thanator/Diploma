import json
import xlrd
import xlwt
import random


wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet', cell_overwrite_ok=True)
with open('ao.geojson') as f:
        data = json.load(f)

tmp = ['45263000','45268000','45297000','45277000','45298000','45290000']
tem = ['45272000','45283000','45286000','45293000','45296000','45280000']
temp = []
for OKATO in tmp:
    i = 0
    while(data['features'][i]['properties']['OKATO'] != OKATO):
        i += 1
    temp.append(data['features'][i]['geometry']['coordinates'])
num = 0
count = 0
for j in temp:
    for i in j:
        for k in i:
            num += 1
            for l in k:
                ws.write(3 + count, 4, l[0])
                ws.write(3 + count, 5, l[1])
                ws.write(3 + count, 6, num)
                count+=1
            ws.write(2 + count, 7, random.randint(70,100))

temp = []
for OKATO in tem:
    i = 0
    while(data['features'][i]['properties']['OKATO'] != OKATO):
        i += 1
    temp.append(data['features'][i]['geometry']['coordinates'])

for j in temp:
    for i in j:
        num += 1
        for k in i:
                       
            ws.write(3 + count, 4, k[0])
            ws.write(3 + count, 5, k[1])
            ws.write(3 + count, 6, num)
            count+=1
        ws.write(2 + count, 7,  random.randint(20,50))
            
    

ws.write(3 + count, 4, 0)
ws.write(3 + count, 5, 0)
ws.write(3 + count, 6, 0)
ws.write (1, 2, len(temp))
wb.save('msk.xls')
import json
import xlrd
import xlwt





def make_it():
    
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet', cell_overwrite_ok=True)
    with open('AF.geojson') as f:
        data = json.load(f)

    tmp = data['features'][0]['geometry']['geometries'][0]['coordinates']
    count = 0
    for i in range(len(tmp[0])):
        ws.write(3 + i, 4, tmp[0][i][0])
        ws.write(3 + i, 5, tmp[0][i][1])
        ws.write(3 + i, 6, 1)
        count += 1
    ws.write(3 + count, 4, 0)
    ws.write(3 + count, 5, 0)
    ws.write(3 + count, 6, 0)
    ws.write (1, 2, 1)


    wb.save('afgan.xls')

        


    # for feature in data['features']:
    #     print (feature['geometry']['type'])
    #     feature['geometry']['geometries'][0]['coordinates']
make_it()
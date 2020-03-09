from openpyxl import load_workbook
from openpyxl.drawing.image import Image
import os

excel_name = 'test.xlsx'
wb = load_workbook(excel_name)
ws = wb.active
ws['A1'] = "hello_from_Workbook"
img = Image('sample.png')
ws.add_image(img, 'A2')
for i in range(0, 3):
    i = str(i)
    sheet_name = "sheet_kun" + i
    ws2 = wb.create_sheet(title=sheet_name)
    ws2['A1'] = "※画面キャプチャーを添付する"
wb.save(filename = "test.xlsx")
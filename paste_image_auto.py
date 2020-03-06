from openpyxl import Workbook
from openpyxl.drawing.image import Image
import os

wb = Workbook()

excel_name = ''
png_info = ''

img = Image(png_info)
ws.add_image(png_info, 'A1')
wb.save('add_png_file.xlsx')
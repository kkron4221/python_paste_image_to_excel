from openpyxl import Workbook
from openpyxl.drawing.image import Image
import os

/*Purpose: This code is automatic paste evidence task to excel sheet.
* 1. Get file name from evidence file.
* 2. Get file image from evidence file.
* 3. Connect excel sheet.
* 4. Add sheet in excel from file name.
* 5. Paste file image to same name's sheet.
*/

wb = Workbook()

excel_name = ''
png_info = ''

img = Image(png_info)
ws.add_image(png_info, 'A1')
wb.save('add_png_file.xlsx')
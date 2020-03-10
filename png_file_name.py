from openpyxl import load_workbook
from openpyxl.drawing.image import Image
import glob, os, re

# TODO: change excel's path and evidence folder path
excel_name = 'test.xlsx'
evidence_folder = "C:\\Users\\username\\Documents\\evidence"
#No.1, No.2, ...
folder_list = os.listdir(evidence_folder)
# 1-1-1, 1-1-2
re_word = r'([0-9]-){2}[0-9]'
check_list = []
center_num = 1
for folder_num in range(len(folder_list)):
    # 1-1-1.png, 1-1-2.png, 1-1-2_1.png, ....
    num_folder = evidence_folder + "\\" + folder_list[folder_num]
    png_list = os.listdir(num_folder)
    for png_num in range(len(png_list)):
        re_png_name = re.match(re_word, png_list[png_num])
        sheet_name_list = str(re_png_name).split("-")
        png_re_name = num_folder + "\\" + re_png_name.group() + "*"
        # get 1-1-1 groups (list)
        right_num_groups = glob.glob(png_re_name)
        if right_num_groups == check_list:
            continue
        print(right_num_groups)
        wb = load_workbook(filename = excel_name)
        sheet_name = str(folder_num + 1) + "-" + str(sheet_name_list[1]) + "-" + str(sheet_name_list[2])
        sheet_name = sheet_name.rstrip("\'>")
        ws2 = wb.create_sheet(title = sheet_name)
        ws2['A1'] = "※画面キャプチャーを添付する"
        for num in range(len(right_num_groups)):
            # img = Image(right_num_groups[num])            
            capture_num = num * 22 + 2
            capture_area = 'A' + str(capture_num)
            ws2.add_image(Image(right_num_groups[num]), capture_area)
        wb.save(filename = excel_name)
        check_list = right_num_groups
        center_num = center_num + 1
    center_num = 1
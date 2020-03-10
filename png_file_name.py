import glob
import os
import re

evidence_folder = "C:\\Users\\username\\Documents\\evidence"
#No.1, No.2, ...
folder_list = os.listdir(evidence_folder)
# 1-1-1, 1-1-2
re_word = r'([0-9]-){2}[0-9]'
check_list = []
for folder_num in range(len(folder_list)):
    # 1-1-1.png, 1-1-2.png, 1-1-2_1.png, ....
    num_folder = evidence_folder + "\\" + folder_list[folder_num]
    png_list = os.listdir(num_folder)
    for png_num in range(len(png_list)):
        re_png_name = re.match(re_word, png_list[png_num])
        png_re_name = num_folder + "\\" + re_png_name.group() + "*"
        # get 1-1-1 groups (list)
        right_num_groups = glob.glob(png_re_name)
        if right_num_groups == check_list:
            continue
        print(right_num_groups)
        check_list = right_num_groups
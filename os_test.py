import os 
from PIL import Image
png_folder = "C:\\Users\\username\\Documents\\evidence"
folder_list = os.listdir(png_folder)
file_list = []
for i in range(len(folder_list)):
    folder_name = png_folder + "\\" + folder_list[i]
    os.chdir(folder_name)
    file_list = os.listdir(folder_name)
    for j in range(len(file_list)):
        print(file_list[j])
        im = Image.open(file_list[j])
        im.show()
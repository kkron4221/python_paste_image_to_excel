import glob

# print(glob.__file__)
one_png = "1"
many_png = "3"
png_name = "1-1-"
png_re_name = 'C:\\Users\\kusano\\Documents\\evidence\\No.1\\' + png_name + one_png + "*"
png_list = glob.glob(png_re_name)
print(png_list)

png_re_name = 'C:\\Users\\kusano\\Documents\\evidence\\No.1\\' + png_name + many_png + "*"
png_list = glob.glob(png_re_name)
print(png_list)
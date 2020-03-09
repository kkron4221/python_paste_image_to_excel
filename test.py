sample_normal = "1-1-1"
sample_bar_first = "1-1-2_1"
sample_bar_second = "1-1-2_2"
sample_list = [sample_normal, sample_bar_first, sample_bar_second]
ans_list = []

for i in range(len(sample_list)):
    sample_list[i] = sample_list[i].split('_')
    try:
        check = sample_list[i][1]
        ans_list.append(sample_list[i])
    except:
        print(sample_list[i])
print(ans_list)
    
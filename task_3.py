from random import random

SIZE = 10
in_list = [round(100*random()) for _ in range(SIZE)]
print(in_list)


min_value = in_list[0]
min_ind = 0
max_value = 0
max_ind = 0
for i in range(len(in_list)):
    if in_list[i] >= max_value:
        max_value = in_list[i]
        max_ind = i
    elif in_list[i] < min_value:
        min_value = in_list[i]
        min_ind = i

in_list[min_ind], in_list[max_ind] = in_list[max_ind], in_list[min_ind]
print(in_list)


from random import random
import timeit

s1 = '''
from random import random
SIZE = 1000
in_matrix = [[round(100*random()) for _ in range(SIZE)] for _ in range(SIZE)]

min_list = []
for i in range(len(in_matrix)):
    min_value = in_matrix[0][i]
    for j in range(len(in_matrix[0])):
        if in_matrix[j][i] < min_value:
            min_value = in_matrix[j][i]
    min_list.append(min_value)

max_value = min_list[0]
for value in min_list:
    if value > max_value:
        max_value = value

'''
# print(timeit.timeit(s1, number=100))
# SIZE = 10 time = 0.006888125999921613
# SIZE = 100 time = 0.2568817019996459 ~ в 100 раз больше
# SIZE = 1000 time = 27.436560674999782 ~ в 100 раз больше
# вроде как O(n^2)


s2 = '''
from random import random
SIZE = 1000
in_matrix = [[round(100*random()) for _ in range(SIZE)] for _ in range(SIZE)]

min_list = []
for line in in_matrix:
    min_list.append(min(line))
max_value = max(min_list)
'''
# print(timeit.timeit(s2, number=100))
# SIZE = 10 time = 0.006755293999958667
# SIZE = 100 time = 0.2376118120000683
# SIZE = 1000 time = 20.942028159000074
# не лучше, также похоже на O(n^2)


SIZE = 10
in_matrix = [[round(100*random()) for _ in range(SIZE)] for _ in range(SIZE)]

min_list = []
for line in in_matrix:
    min_list.append(min(line))
print(max(min_list))




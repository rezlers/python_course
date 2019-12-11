from random import random

def pretty_print(matrix):
    for value in matrix:
        print(value)

SIZE = 10
in_matrix = [[round(100*random()) for _ in range(SIZE)] for _ in range(SIZE)]
pretty_print(in_matrix)

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

print('список минимальных по столбцам:\n', min_list)
print('максимальное среди минимальных:\n', max_value)


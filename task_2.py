
in_list = input("Введите числа через пробел:\n").split(' ')
in_list = [int(value) for value in in_list]
print(in_list)

new_list = []
for i in range(len(in_list)):
    if in_list[i] % 2 == 0:
        new_list.append(i)

print(new_list)


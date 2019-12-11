from random import random

SIZE = 10
in_list = [round(100*random()) for _ in range(SIZE)]
print(in_list)

counter = 1
counter_max = 1
value_max = in_list[0]
for i in range(len(in_list)):
    for j in range(len(in_list)):
        if in_list[i] == in_list[j] and i != j:
            counter += 1
    if counter > counter_max:
        counter_max = counter
        value_max = in_list[i]
    counter = 0

print(f"Значение: {value_max}\nКоличество раз: {counter_max}")




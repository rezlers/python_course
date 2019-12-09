def dig_num(number):
    odd_num = 0
    even_num = 0
    for char in number:
        if int(char) % 2 == 0:
            even_num += 1
        else:
            odd_num += 1
    return f"четных чисел: {even_num} нечетных чисел: {odd_num}"


res = dig_num(input('Введите число: '))
print(res)
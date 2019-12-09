def my_rever(str_in):
    int_str = int(str_in)
    if int_str // 10 == 0:
        return str(int_str)
    return str(int_str % 10) + my_rever(str(int_str // 10))

while True:
    res = input("Введите число: ")
    if res == '0':
        break
    print(my_rever(res))

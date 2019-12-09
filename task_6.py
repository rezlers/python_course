def guess_num(num):
    num = int(num)
    from random import random
    tries = 10
    rand_num = round(100 * random())

    while num != rand_num and tries != 0:
        if num > rand_num:
            print("Это число больше загаданого")
            tries = tries - 1
            num = input(f"Осталось попыток: {tries}\nВведите число: ")
            num = int(num)
        else:
            print("Это число меньше загаданого")
            tries = tries - 1
            num = input(f"Осталось попыток: {tries}\nВведите число: ")
            num = int(num)
    if(num == rand_num and tries > 0):
        return "Победа!"
    return "Проигрыш:("


while True:
    res = input("Игра началась! Осталось попыток: 10\nВведите число: ")
    if res == '0':
        break
    print(guess_num(res))

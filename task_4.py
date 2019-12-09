def geom_prog(n):
    n = int(n)
    return (1 - (-0.5)**(n + 1)) / (1 + 0.5)

while True:
    res = input("Введите число: ")
    if res == '0':
        break
    print(geom_prog(res))
START_POINT = 10
END_POINT = 100

for dig in range(2,START_POINT):
    print(str(dig) + ': ', end='')
    for value in range(START_POINT, END_POINT):
        if(value % dig == 0):
            print(value, end=' ')
    print()



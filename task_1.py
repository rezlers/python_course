def calc(expr):
    tmp_expr = ''
    a = None
    for char in expr:
        tmp_expr += char
        if char == '/' or char == '-' or char == '+' or char == '*':
            tmp_char = char
            tmp_expr = tmp_expr.strip(char)
            tmp_expr = tmp_expr.strip()
            if a is None:
                a = int(tmp_expr)
                tmp_expr = ''
            else:
                continue

    if tmp_char == '/':
        tmp_expr = tmp_expr.strip()
        if tmp_expr == '0':
            return 'Нельзя делить на ноль'
        return a / int(tmp_expr)

    elif tmp_char == '+':
        tmp_expr = tmp_expr.strip(' ')
        return a + int(tmp_expr)

    elif tmp_char == '-':
        tmp_expr = tmp_expr.strip(' ')
        return a - int(tmp_expr)

    tmp_expr = tmp_expr.strip(' ')
    return a * int(tmp_expr)


while True:
    expr = input("Введите выражение: ")
    if expr == '0':
        break
    print(calc(expr))

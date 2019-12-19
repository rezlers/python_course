import timeit
import math


def is_prime1(number):
    if number == 1:
        return 2
    in_list = [value for value in range(2, round(2*number*math.log1p(number)) + 1)]
    n = len(in_list)
    j = 0
    while j < n:
        for i in range(j + in_list[j], n, in_list[j]):
            in_list[i] = 0
        j += 1
        while j < n and in_list[j] == 0:
            j += 1
    try:
        while True:
            in_list.remove(0)
    except ValueError:
        print(in_list)
        return in_list[number - 1]


def is_prime2(number):
    value = 3
    counter = 1
    while counter < number:
        if is_prime(value):
            counter += 1
        value += 1
    return value - 1

# алгоритм решето-эратосфена
def prime1(in_list):
    n = len(in_list)
    j = 0
    while j < n:
        for i in range(j + in_list[j], n, in_list[j]):
            in_list[i] = 0
        j += 1
        while j < n and in_list[j] == 0:
            j += 1
    out_set = set(in_list)
    out_set.remove(0)
    return out_set


# алгоритм выявления простого числа
def is_prime(number):
    value = 2
    while value < number:
        if number % value == 0:
            break
        value += 1
    if value == number:
        return True
    else:
        return False


# обычный алгоритм
def prime2(in_list):
    for i in range(len(in_list)):
        if not is_prime(in_list[i]):
            in_list[i] = 0
    return list(set(in_list))[1:]


# in_list = [value for value in range(2, int(input("n: ")) + 1)]
# print(prime1(in_list))
s1 = '''
def is_prime(number):
    value = 2
    while value < number:
        if number % value == 0:
            break
        value += 1
    if value == number:
        return True
    else:
        return False


# обычный алгоритм
def prime2(in_list):
    for i in range(len(in_list)):
        if not is_prime(in_list[i]):
            in_list[i] = 0
    return list(set(in_list))[1:]
    
SIZE = 10000
in_list = [value for value in range(2, SIZE + 1)]
prime_list = prime2(in_list)
'''
# print(timeit.timeit(s1, number=100))
# SIZE = 100 time = 0.012703040000133115
# SIZE = 1000 time = 0.5547036840000601
# SIZE = 10000 time = 44.29672749500014


s2 = '''
def prime1(in_list):
    n = len(in_list)
    j = 0
    while j < n:
        for i in range(j + in_list[j], n, in_list[j]):
            in_list[i] = 0
        j += 1
        while j < n and in_list[j] == 0:
            j += 1
    out_set = set(in_list)
    out_set.remove(0)
    return out_set
    
SIZE = 1000000
in_list = [value for value in range(2, SIZE + 1)]
prime_list = prime1(in_list)
'''
# print(timeit.timeit(s2, number=100))
# SIZE = 100 time = 0.011893409000094834
# SIZE = 1000 time = 0.046536969999579014
# SIZE = 10000 time = 0.20950876699998844
# SIZE = 100000 time = 2.317455610000252
# SIZE = 1000000 time = 32.02792376599973
# наверное чуть больше O(n)

s3 = '''
import random
import math
def is_prime1(number):
    if number == 1:
        return 2
    in_list = [value for value in range(2, round(2*number*math.log1p(number)) + 1)]
    n = len(in_list)
    j = 0
    while j < n:
        for i in range(j + in_list[j], n, in_list[j]):
            in_list[i] = 0
        j += 1
        while j < n and in_list[j] == 0:
            j += 1
    try:
        while True:
            in_list.remove(0)
    except ValueError:
        return in_list[number - 1]
SIZE = 10000
res = is_prime1(SIZE)
'''
# print(timeit.timeit(s3, number=100))
# SIZE = 10 time = 0.012199856999814074
# SIZE = 100 time = 0.09998563600015586
# SIZE = 1000 time = 10.788120011000046
# Сложность : так как по теореме о распределении простых чисел колчиство чисел до n ~= nln(ln(n)) тогда сложность
# будет O(n*ln(ln(n))*ln(ln(n*ln(ln(n))))

s4 = '''
def is_prime(number):
    value = 2
    while value < number:
        if number % value == 0:
            break
        value += 1
    if value == number:
        return True
    else:
        return False
        
        
def is_prime2(number):
    value = 3
    counter = 1
    while counter < number:
        if is_prime(value):
            counter += 1
        value += 1
    return value - 1
SIZE = 1000


res = is_prime2(SIZE)
'''
# print(timeit.timeit(s4, number=100))
# SIZE = 10 time = 0.0023507709997829807
# SIZE = 100 time = 0.2064575720000903
# SIZE = 1000 time = 29.873552547000145
# похоже на более чем O(n^2), наверное по теореме о распределении O( (n*ln(ln(n)))^2 )





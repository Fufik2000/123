import math
from m1 import a as q,b as e, d as um
def a():
    print("\nДеление")
    a = q()
    b = e()
    if b == 0:
        return 0
    else:
        return a/b
def b():
    print("\nКвадратный корень")
    rez = um()
    return math.sqrt(rez)

def sred():
    print("\nСреднее значение\n")
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    c = int(input('Введите третье число: '))

    d = (a+b+c)/3
    return d

def mensh():
    print("\nНаименьшее число\n")
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    c = int(input('Введите третье число: '))

    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    elif c <= a and c <= b:
        return c
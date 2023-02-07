from m1 import a as n1, b as n2, d as n3
from m2 import a as n4, b as n5

def summa():
    print("Введите 2 числа: ")
    a = int(input())
    b = int(input())
    return a+b

def delen():
    print("Введите 2 числа: ")
    a = int(input())
    b = int(input())
    return a/b

def spisok():
    lst = [3,5,7,5,4]
    for i in range(len(lst)):
        print(lst[i])
    return lst

def spisok2():
    slst = [[3,5,7],[6,7,9]]
    print(slst[1][2]) 

def dct1():
    d = dict()
    d = {'k1': 'k1 value', 'k2': 'k2 value'}
    for key in d.keys():
        print(d.get(key))

def calc():

    print("\n1 - Сложение\n2 - Вычитание\n3 - Деление\n4 - Умножение\n5 - Квадратный корень умножения\n")
    vb = int(input("Введите номер операции: "))

    if vb == 1:
        print('\nОтвет: {}'.format(n1()))
    elif vb == 2:
        print('\nОтвет: {}'.format(n2()))
    elif vb == 3:
        print('\nОтвет: {}'.format(n4()))
    elif vb == 4:
        print('\nОтвет: {}'.format(n3()))
    elif vb == 5:
        print('\nОтвет: {}'.format(n5()))
    else:
        print('Нет такой операции')


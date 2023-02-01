def a(p1, p2):
    return p1+p2
def b(p1, p2):
    return p1*p2
def c(p1,p2):
    if p2 == 0:
        return 0
    return p1/p2

print(a(2,2))
print(b(3,4))
print(c(3,4))

def d(val):
    return type(val)
def e(val):
    # Проверка типа данных
    t = type(val)
    if t == str:
        return 'Строка'
    elif t == int:
        return 'Целое число'
    elif t == list:
        return 'Список'
    else:
        return 'Неизвестный тип'
print(e('sdas'))
print(d('hello, world'))
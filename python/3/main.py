import math
def a():
    lst = [2,3,4]
    return len(lst)
def b():
    lst = [5,6,7]
    sum = 0
    for i in lst:
        sum += i
    return sum
def c():
    return math.sqrt(b())
print(a(),b())
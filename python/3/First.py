class First:
    def __init__(self):
        q = 'second init'
    def a(self):
        print(First.q)

class Second:
    q = 'second'
    def __init__(self):
        e = 123
    @staticmethod
    def a():
        print('Method a from class Second')

class One:
    def __init__(self):
        self.one_var = 'value from class One'
    def a(self):
        print('method a into class One')
class Two(One):
    def b(self):
        print('method b into class Two')
"""
First.q = 'qwe'
a1 = First()
a1.x = 10
a1.y = 20
print(a1.x, a1.y, a1.q)
b1 = First()
b1.x = 30
b1.y = 40
print(b1.x, b1.y, b1.q)
c1 = Second()
d1 = Second()
"""
a1 = Two()
a1()
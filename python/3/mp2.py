class A:
    def __init__(self,obj):
        self.obj = obj
    def return_obj(self):
        return self.obj
class B(A):
    def get_obj_type(self):
        return type(self.obj)
    def get_sqrt(self):
        dt = self.get_obj_type()
    def get_array_size(self, t='size'):
        dt = self.get_obj_type()
        sum = 0
        more = 0
        if dt == list or dt == tuple:
            if t == 'size':
                return len(self.obj)
            elif t == 'sum':
                for i in self.obj:
                    sum += i
                return sum
            elif t == 'more':
                return max(self.obj)
        return tuple()
class C(B):
    pass

if __name__ == '__main__':
    a1 = C(obj=[1,2,3,4,5])
    print(a1.get_array_sume) 
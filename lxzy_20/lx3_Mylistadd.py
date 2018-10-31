class MyList:
    def __init__(self,iterable=()):
        self.list = [x for x in iterable]
    def __repr__(self):
        return 'Mylist(%s)' % self.list
    def __add__(self,rhs):
        return MyList(self.list + rhs.list)
    def __mul__(self,rhs):
        return MyList(self.list * rhs)
    def __rmul__(self,lhs):
        return MyList(self.list * lhs)
    def __iadd__(self,rhs):
        self.list.extend(rhs.list)
        # 因为没有产生新的对象
        return self
l1 = MyList(range(1,4))
l2 = MyList([4, 5, 6])
l3 = l1 + l2
print(l3)
l4 = l2 + l1
print(l4)
l5 = l1 * 2
print(l5)
# int类中不能识别自建类
l6 = 2 * l1
print(l6)
l1 += l2
print(l1)
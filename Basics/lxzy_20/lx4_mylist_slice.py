
# 此示例示意 索引和切片  运算符的重载
class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]
    
    def __repr__(self):
        return "MyList(%s)" % self.data
    
    def __getitem__(self, i):
        print("__getitem__被调用, i=", i)
        if type(i) is int:
            print("您正在执行索引操作")
        elif type(i) is slice:
            print("您正在执行切片操作")
            print(i.start, i.stop, i.step)
        return self.data[i]

    def __setitem__(self, i, v):
        print("__setitem__被调用, i=", i, 'v=', v)
        self.data[i] = v

    def __delitem__(self, i):
        del self.data[i]

L = MyList([1, -2, 3, -4, 5])
print(L[::2])

class A():
    def __init__(self, iterbale = ()):
        self.date = iterbale
    def __len__(self):
        return len(self.date)
    def __abs__(self):
        # 返回的是新的列表
        return A([abs(x) for x in self.date])
    def __repr__(self):
        return "mylist(%s)"%self.date
myl = A([1,-2,3,-4])
print(len(myl))
print(abs(myl))
print(myl)


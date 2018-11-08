
# 此示例示意将 MyList类型的对象改写为可迭代对象

class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]
    def __repr__(self):
        return "MyList(%s)" % self.data
    def __iter__(self):
        '''有此方法,此类创建的对象可以作为可迭代对象
        使用, 此方法必须返回 "迭代器" '''
        print("__iter__被调用")
        # 创建一个迭代器并返回
        return MyListIterator(self.data)
class MyListIterator:
    def __init__(self, target):
        self.data = target
        self.index = 0  # 表示即将要访问的索引
    def __next__(self):
        '''有此方法的对象被称为迭代器
        此方法必须实现迭代器协议
        '''
        print("__next__方法被调用")
        if self.index >= len(self.data):
            raise StopIteration

        r = self.data[self.index]
        self.index += 1  # 为下次迭代做准备
        return r

myl = MyList([100, 200, 500, 800])

it = iter(myl)  # it = myl.__iter__()
while True:
    try:
        x = next(it)  # x = it.__next__()
        print(x)  # 100, 200, 500, 800
    except StopIteration:
        break

print("-----　以下为for循环语句--------")
for x in myl:
    print(x)
print('-------以下为列表推导式--------')
L = [x**2 for x in myl]
print(L)  # [10000, 40000, 250000, 640000]
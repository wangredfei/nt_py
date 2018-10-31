
#   实现一个与系统内建的range类相同功能的类:
#       class MyRange:
#           def __init__(self, ....):
#               ...
#           def __iter__(self):
#               ...
#     实现如下功能:
#       L = list(MyRange(5))
#       print(L)  # [0, 1, 2, 3, 4]
#       print(sum(MyRange(1, 101)))  # 5050
#       L2 = [x**2 for x in MyRange(1, 10, 3)]
#       print(L2)  # [1, 16, 49]
#       for x in MyRange(10, 0, -3):
#           print(x)  # 10, 7, 4, 1
class MyRange:
    def __init__(self, start , stop = None , step = 1):
        l = []
        if stop is None :
            stop = start
            start = 0
        if step < 0:
            while  start > stop:
                l.append( start)
                start += step
        elif step > 0:
            while start < stop :
                l.append(start)
                start += step
        else :
            return
        self.date = l
    def __iter__(self):
        return MyRangeNext(self.date)
class MyRangeNext():
    def __init__ (self,date):
        self.date = date
        self.index = 0
    def __next__(self):

        if self.index >= len(self.date):
            raise StopIteration
            '''
            不报错的原因是, 其实报错
            迭代器协议是指对象能够使用next函数获取下一项数据,
            在没有下一项数据时出发一个StopIteration异常来终止迭代的约定
            '''
        r = self.date[self.index]
        self.index += 1
        return  r

L = list(MyRange(5))
print(L)  # [0, 1, 2, 3, 4]
print(sum(MyRange(1, 101)))  # 5050
L2 = [x**2 for x in MyRange(1, 10, 3)]
print(L2)  # [1, 16, 49]
for x in MyRange(10, 0, -3):
    print(x)  # 10, 7, 4, 1
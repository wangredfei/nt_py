
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
        
        if stop is None :
            stop = start
            start = 0
        self.start = start
        self.stop = stop
        self.step = step

        
    def __iter__(self):
        return MyRangeNext(self.start, self.stop, self.step)
class MyRangeNext():
    def __init__ (self,start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __next__(self):
        if self.step < 0:
            while  self.start > self.stop:
                r = self.start
                self.start += self.step
                return  r
        elif self.step > 0:
            while self.start < self.stop :
                r = self.start
                self.start += self.step
                return  r
        # 包含了步长为0的时候
        raise StopIteration 
            # 不报错的原因是, 其实报错
            # 迭代器协议是指对象能够使用next函数获取下一项数据,
            # 在没有下一项数据时出发一个StopIteration异常来终止迭代的约定
L = list(MyRange(5))
print(L)  # [0, 1, 2, 3, 4]
print(sum(MyRange(1, 101)))  # 5050
L2 = [x**2 for x in MyRange(1, 10, 3)]
print(L2)  # [1, 16, 49]
for x in MyRange(10, 0, -3):
    print(x)  # 10, 7, 4, 1
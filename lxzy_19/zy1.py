
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
        if 
    def __iter__(self):
        ...

L = list(MyRange(5))
print(L)  # [0, 1, 2, 3, 4]
print(sum(MyRange(1, 101)))  # 5050
L2 = [x**2 for x in MyRange(1, 10, 3)]
print(L2)  # [1, 16, 49]
for x in MyRange(10, 0, -3):
    print(x)  # 10, 7, 4, 1
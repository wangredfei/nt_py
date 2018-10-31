# 试运行一下程序的结果是什么
# L = [1, 2]
def fun(a , lst=[]):
    lst.append(a)
    print(lst)
    
# fun(1, L)
# fun(1, L)
fun(5)
fun(3)
fun(4)
fun(5)
# 1, 2, 1]
# [1, 2, 1, 1]
# [5]
# [5, 3]
# [5, 3, 4]
# [5, 3, 4, 5]

'''
L = [1, 2]
def fun(a , lst = None):
    if lst is None:
        lst = []
    lst.append(a)
    print(lst)
fun(1, L)
fun(2, L)
fun(5)
fun(3)
fun(4)
fun(5)
# [1, 2, 1]
# [1, 2, 1, 2]
# [5]
# [3]
# [4]
# [5]
 '''
 
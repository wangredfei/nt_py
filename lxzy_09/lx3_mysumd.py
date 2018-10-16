# 写一个函数,myadd,此函数可以传入两个,三个或者四个实参, 此函数功能时计算所有实参的和
# def myadd(a = 0 , b = 0 , c = 0 , d = 0):
#     return a+b+c+d
# print(myadd(10,20))
# print(myadd(100,200,300))
# print(myadd(1,2,3,4))



def myadd(a = 0 , b = 0 , c = 0 , d = 0, *args):
    s = a+b+c+d 
    print(*args)
    for i in args:
        s += i
    return s
# print(myadd(10,20))
# print(myadd(100,200,300))
print(myadd(1,2,3,4,5,6))


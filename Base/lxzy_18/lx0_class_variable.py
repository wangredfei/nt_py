# 示意类变量的定义,访问及赋值操作
class Human():
    total_count = 0 # 创建一个类变量
print('Human.total_count=',Human.total_count)
a = Human() # a 没有自己的变量, 他有类的变量
a.total_count = 100  # 创建实例变量
print('a.total_count=',a.total_count)
print('Human.total_count=',Human.total_count)
print("-"*50)
a.__class__.total_count = 200
print('a.total_count=',a.total_count)
print('Human.total_count=',Human.total_count)



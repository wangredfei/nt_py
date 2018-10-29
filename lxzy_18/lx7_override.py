# 覆盖 override.py
class A:
    def work(self):
        print("A.work被调用")
class B(A):
    '''会覆盖A中同名的方法'''
    def work(self):
        print("B.work被调用")    
    
b = B()
b.work()
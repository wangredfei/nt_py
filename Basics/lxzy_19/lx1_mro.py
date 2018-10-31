# mro.py

class A:
    def go(self):
        print('A')
        # super().go()  # 出错

class B(A):
    def go(self):
        print('B')
        super().go()  # 基于D的mro调用,B的上一级此时为C

class C(A):
    def go(self):
        print('C')
        super().go()

class D(B, C):
    def go(self):
        print("D")
        super().go()

d = D()
d.go()
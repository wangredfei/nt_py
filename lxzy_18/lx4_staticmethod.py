class A :
    @staticmethod
    def myadd(a,b):
        return a+b
print(A.myadd(100,200))
a = A()
print(a.myadd(30,40))
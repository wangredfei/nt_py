def make_pow(y):
    def fu(x):
        return x ** y
    return fu
a = make_pow(3)
print(a(5))

def A(x):
    def B(y):
       return x*y
    return B
haha = A(4)
print(haha(3))
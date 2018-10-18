def make_pow(y):
    def fu(x):
        return x ** y
    return fu
a = make_pow(3)
print(a(5))
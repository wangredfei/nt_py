a = 1
b = 2
c = 3

def fn(c,d):
    e = 300
    print(globals())
    print(locals())
    print(globals()["c"])
    print(a,b,c,d,e)
fn(100,200)

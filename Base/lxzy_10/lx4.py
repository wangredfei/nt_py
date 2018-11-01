def goodbye(L):
    for x in L:
        print("再见: ",x)
def hello(L):
    for x in L:
        print("您好: ",x)
def fx(fn,L):
    fn(L)

names = ['Tom', 'jerry', 'Spike', 'Tyke']
fx(hello,names)
fx(goodbye,names)
fx(goodbye,"你好")




def myinput(fn):
    L = [1, 3 , 5, 7 , 9]
    return fn(L)
print(myinput(max))
print(myinput(min))
print(myinput(sum))













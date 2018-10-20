# 关键字形参传入 当键是字符串时不用加引号
def A(**kwargs):
    for k,v in kwargs.items():
        print(k,'+',v)
A(a=1,b=2,c=3)

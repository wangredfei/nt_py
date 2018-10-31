# 汉诺塔

def panzi(a, b, c, n):
    # 判断是否等于一
    if n == 1:
        print(a+"---->"+c)
    # 找规律
    else :
        panzi(a, c, b,n-1)
        panzi(a, b, c,1)
        panzi(b, a, c,n-1)
    
panzi("1","2","3",3)
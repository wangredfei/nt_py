def A():
    print("AAA")
    
    a = 1
    # 内部变量不能给外部变量赋值 
a = 0

A()
print(a)
# print(v)
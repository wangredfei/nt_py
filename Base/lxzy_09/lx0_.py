def a(a,b,c):
    print(a)
    print(b)
    print(c)

# d = {"a":222 , "c":200 , "b" : 900}
# # print(**d)
# a(a= d['a'], b= d['b'], c= d['c'])
# a(**d) # 等同于上面
l = [1,2]
a(200 , *l)
a(*l , 200)
a( a = 200 ,  100 , c = 1000)

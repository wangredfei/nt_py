def f1():
    print("f1函数被调用")
f2 = f1 # 看清楚,不是f2 = f1()
print ("- -"*50)
f2()
f1()

f2 = f1()






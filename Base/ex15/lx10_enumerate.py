def fn():
    l = []
    while 1  :
        s = input("请输入")
        if s == "":
            break
        l.append(s)
    a = enumerate(l,start = 1)
    return a 
def text():
    for index,nr in fn():
        print("第{}行:{}".format(index , nr))
text()
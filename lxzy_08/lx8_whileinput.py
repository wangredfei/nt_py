def input_number():
    l = []
    while 1 :
        n = int(input("请输入整数"))
        if n < 0 :
            break 
        l.append(n)
    print("您输入的最大的数是",max(l))
    print("您输入的最小的数是",min(l))
    print("和是",sum(l))
    return l
L = input_number()
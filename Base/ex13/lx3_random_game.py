def random_game():
    import random
    # 用i统计输入次数
    x = random.randint(1,100)
    i = 1
    while 1:
        y = input("请输入一个整数")
        # -1 退出
        if y == "-1":
            break
        # 判断是不是纯数字
        if y.isdigit() is False:
            print("输入有误.请输入1-100整数")
            continue
        # 判断范围
        y = int(y)
        if  0 > y or y > 100:
            print("请输入0-100")
            continue
        if y > x :
            print("您猜大了")
        elif y < x:
            print("您猜小了")
        elif y == x:
            print("恭喜您猜对了")
            print("随机数是{},您输入了{}次".format(x,i))
            break
        print("第{}次".format(i))
        i += 1
    
random_game()
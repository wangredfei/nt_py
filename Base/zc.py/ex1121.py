'''猜数字游戏的升级版'''
import random

def judge_num(num,n):

    n = [int(x) for x in n]
    print(num)

    # 用于数字对的数
    l1 = []
    for i in n:
        if i in num:
            l1.append(l1)
    # 用于存储位置数值都对的数
    l2 = []
    for i in range(1,5):
        if num[i-1] == n[i-1]:
            l2.append(i)

    return len(l1),len(l2)

def main():
    # 创建一个四位数
    num = []
    for _ in range(4):
        num.append(random.randint(0,9))
        
    # 计数
    count = 0

    # 进入循环开始游戏
    while count<7:
        # 输入
        try:
            n = input("请输入一个四位数")
            # 如果输入是字母就except
            if n == "quit":
                break
            nn = int(n)
        except:
            print("请重新输入")
            continue
        if len(n) != 4 :
            print("输入错误,请重新输入")
            continue

        # 判断并输出
        l = judge_num(num,n)

        # 输出
        if l[1] == 4:
            print("答对了")
            break
        else:
            print("数值对的有%d个,数值和位置都对的时%d"%l)
        
        count += 1
        if count == 7 :
            print("次数用完,游戏结束")
            break 
        print("还有",7-count,"次")

main()

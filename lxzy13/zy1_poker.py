# 1. 模拟斗地主发牌,牌共54张
#    黑桃('\u2660'), 梅花('\u2663'), 红桃('\u2666')
#    方块('\u2665')
#    A2-10JQK
#    大王,小王
#    三个个,每人发17张牌,底牌留三张
#      输入回车,打印第1个人的17张牌
#      输入回车,打印第2个人的17张牌
#      输入回车,打印第3个人的17张牌
#      输入回车,显示三张底牌
from random import sample as s
# 把所有扑克传入列表
pokers = []
for i in [1,2,3,4,5,6,7,8,9,10,'J','Q','K']:
    pokers.append("{}\u2660".format(i))
    pokers.append("{}\u2663".format(i))
    pokers.append("{}\u2666".format(i))
    pokers.append("{}\u2665".format(i))
pokers.extend(["大王","小王"])
poker_s = set(pokers)
# 利用循环判断输入次数
i = 1
while 1 <= 4:
    if i <= 3 :
        n = input("点击回车查看player{}的牌".format(i))
        a = "player"+str(i)
        a = s(poker_s,17)
        poker_s.difference_update(a)
        print(a)
    else :
        n = input("查看底牌")
        print(poker_s)
        break
    i += 1



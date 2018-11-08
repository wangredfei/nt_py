# 1
# print("是偶数")
# print("是奇数")
# 如何只让一条执行
'''
inu = input("请输入一个整数")
inut = int(inu)
if inut % 2 == 0:
    print('是偶数')
else:
    print("是奇数")
'''

# - 练习 ：
#     - 任意输入一个整数
#     1. 判断这个数是否大于100
#     2. 判断这个数是否小于0
#     3. 判断这个数是否在50-100之间
#     4. 用if来实现 

inum = input("输入一个整数")
inumt = int(inum)
if inumt > 100:
    print("大于100")
elif inumt < 0:
    print("小于0")
elif 50 < inumt < 100 :
    print("在 50 到 100 之间")
else :
    print("不在50到100之间")
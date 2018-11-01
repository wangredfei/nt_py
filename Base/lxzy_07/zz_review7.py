# 1. 输入衣服按字符串,打印出这个字符串中出现过的字符及出现的次数 # 不要求打印顺序
'''
book = {}
s = input("请输入一个字符串")
for i in s:
    if i not in book :
        book[i] = 1
    else : 
        book[i] += 1
for k,v in book.items():
    print("{}:{}次".format(k, v))
'''
# 字典推导式 
'''
notes = [1,2,3,4,5]
names = ['anfuwei','zhangben','asdf','asdf','gggg']
book = {notes[i]: names[i] for i in range(5)}
print(book)
'''
#  生成前40个斐波那契数列 如` 1 ,1 , 2, 3, 5, 8, 13, 21....`  存入列表中,最后打印这个数
'''
l = [ 1, 1 ]
for i in range(38):
    l.append(l[-1]+l[-2] )
print(l)

# 99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        zw = '{}*{}={}'.format(j, i, i*j )
        print("{:<10}".format(zw),end =" ")
    print()
'''

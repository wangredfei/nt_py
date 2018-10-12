# 1. 输入衣服按字符串,打印出这个字符串中出现过的字符及出现的次数 # 不要求打印顺序

book = {}
n = input("请输入一段字符串")
for i in n:
    if i not in book:
        book[i] = 1
    else :
        book[i] += 1
print(book)
for k,v in book.items():       
    print(k ,":" ,v ,"次")
# 用户输入姓名和电话,姓名输入为空则停止输入,打印出来
book = {}
while 1:
    name = input("please input your name : ")
    if name == "":
        break
    pnb = int(input("please input your phonenumber: "))
    book[name] = pnb

print(book)
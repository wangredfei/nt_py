# def get_number():
#     s = input("请输入整数") or "0"
    
#     i = int(s)
#     return i
# try :
#     get_number()
# except :
#     print("错误")
# print(get_number())


def get_number():
    s = input("请输入整数")
    try:
        i = int(s)
    except:
        i = 0
    return i

print(get_number())

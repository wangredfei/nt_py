def get_age():
    age = int(input("请输入年龄 1~140之间 :"))
    if age < 1 or age > 140 :
        raise ValueError ('年龄超出范围')
    return age
try:
    age = get_age()
    print("用户输入的年龄是",age)
except ValueError as err:
    print("用户输入的不是1~140之间的整数,获取年龄失败",err)
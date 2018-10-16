# 此联系表示如何定义缺省参数
def fun(name, age = 1 , address= "buxiang" ,*args):
    print(name , "今年" , age , "岁, 家庭住址:",address)
fun("安付伟",35,"鹤壁")
fun("安付伟")
# fun() 出错,缺少参数

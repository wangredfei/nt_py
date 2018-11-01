def div_apple(n):
    a = int(input('想给几个人分苹果'))
    s = n/a
    print('{}人每人{}个苹果'.format(a,s))


try:
    div_apple(10)
    print("分苹果成功")
except (ValueError,ZeroDivisionError) as err:
    print("苹果不分了")
print('程序结束')
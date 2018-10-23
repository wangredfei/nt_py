def div_apple(n):
    a = int(input('想给几个人分苹果'))
    s = n/a
    print('{}人每人{}个苹果'.format(a,s))


try:
    div_apple(10)
    print("分苹果成功")
except (ValueError,ZeroDivisionError) as err:
    print("苹果不分了")
except:
    # 此处能够捕获除ValueError以外的全部错误
    # except 只能写在最后
    print("except 字句被执行,程序已转为正常状态")
print('程序结束')
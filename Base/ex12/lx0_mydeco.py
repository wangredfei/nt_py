# 此示例
def mudeco(fn):
    def fx():
        print("+++++++++")
        print("---------")
    return fx
@ mudeco
def myfunc():
    '''此函数讲作为被装饰函数'''
    print("myfunc被调用")
# 原理是让myfunc重新绑定mydeco返回回来的函数
# myfunc = mudeco(myfunc)
myfunc()
myfunc()
myfunc()
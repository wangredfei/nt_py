# 此示意表示在函数内部创建函数,在函数外部调用,需要用return语句送回来


def A():
    print("A1")
    def B():
        print("B 被调用")
    print("A调用结束")
    # return B
fn = A()
fn()
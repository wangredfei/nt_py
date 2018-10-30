# bool.py

# 此示例示意bool(obj) 函数的重写方法
class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]
   
    def __repr__(self):
        return "MyList(%s)" % self.data

    def __len__(self):
        print("__len__被调用")
        return len(self.data)

    def __bool__(self):
        print("__bool__被调用")
        return any(self.data)

myl = MyList([0, 0.01, False, None])
print(bool(myl))
if myl:
    print("myl的布尔值是 真")
else:
    print("myl的布尔值为 假")
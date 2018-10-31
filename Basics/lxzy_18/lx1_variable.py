class Human():
    total_count = 0
    def __init__(self):
        print("__init__被调用")
        self.__class__.total_count += 1
    def __del__ (self):
        self.__class__.total_count -= 1
    
h1 = Human()
l = []
l.append(Human())
l.append(Human())
l.append(Human)
del h1
del l
print("共有",Human.total_count)
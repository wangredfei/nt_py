def myyield():
    print("即将生成2")
    yield 2
    print("即将生成3")
    yield 3
    print("即将生成5")
    yield 5
    print("即将生成7")
    yield 7
    print("即将生成9")
    yield 9
    print("生成结束")
r = myyield()
it = iter(r)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
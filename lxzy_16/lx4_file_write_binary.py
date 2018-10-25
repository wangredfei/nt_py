# 此示例示意二进制文件的写操作
try:
    # 二进制写操作
    f = open("test_binary.abc","wb")
    # f.write(b"hello")# 出错
    f.write("")
except OSError:
    print("打开文件失败")
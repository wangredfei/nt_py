import tkinter

def ShowLabel():
    global baseFrame
    # 在函数中定义了一个label
    # label的父组件是baseFrame
    lb = tkinter.Label(baseFrame, text="显示")
    lb.pack()

baseFrame = tkinter.Tk()
# 生成一个一个Button
# common参数指示,当按钮按下,执行哪个函数
baseFrame.wm_title("此示例示意Button")
btn = tkinter.Button(baseFrame, text="Show Label", command=ShowLabel)
btn.pack()

baseFrame.mainloop()
import tkinter

base = tkinter.Tk()

# 负责标题
base.wm_title("Label Test")

lb = tkinter.Label(base, text = "python Laber")
lb.pack()

base.mainloop()

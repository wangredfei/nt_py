import tkinter as t
class Hello:
    def __init__(self, master):
        frame = t.Frame(master)
        frame.pack()

        self.hi_there = t.Button(frame, 
                            text="打招呼",
                             fg="green",
                             bg="black",
                             command = self.say_hi)
        self.hi_there.pack()
    def say_hi(self):
        print("您好")
root = t.Tk()
a = Hello(root)
root.mainloop()
'''
2048GUI
'''
import tkinter
import random

class Gui2048:
    def __init__(self): # 显示窗体
        self.data = [[0 for i in range(4)] for j in range(4)]
        self.scores = 0
        self.window = tkinter.Tk()
        self.window.title("2048")
 
        self.window.bind("<Key>", self.fangxiangEvent)
 
        self.canvasDa = tkinter.Canvas(self.window,
                                       width=400,
                                       height=400,
                                       bg="green")
        self.canvasDa.pack()

        frame = tkinter.Frame(self.window)
        frame.pack()

        self.buttonL = tkinter.Button(frame,
                                      text = "左",
                                      command = self.bleft).grid(row = 1, column = 1)
        self.buttonR = tkinter.Button(frame,
                                      text="右",
                                      command=self.bright).grid(row=1, column=2)
        self.buttonU = tkinter.Button(frame,
                                      text="上",
                                      command=self.bup).grid(row=1, column=3)
        self.buttonD = tkinter.Button(frame,
                                      text="下",
                                      command=self.bdown).grid(row=1, column=4)
        self.fenshu = tkinter.StringVar()
        tkinter.Label(frame,
                      textvariable = self.fenshu).grid(row=1, column = 5)

    def fangxiangEvent(self, event):
        if event.char == "w":
            self.bup()
        elif event.char == "s":
            self.bdown()
        elif event.char == "a":
            self.bleft()
        elif event.char == "d":
            self.bright()

    def myprint(self):   # 插入数据
        self.rand_num()
        self.fenshu.set(self.scores)
        for x, line in enumerate(self.data):
            print(line)
            for y, num in enumerate(line):
                self.labelXiao = tkinter.Label(self.canvasDa,
                                               width=10,
                                               height=5,
                                               bg="white",
                                               text=num if num != 0 else "",
                                               font='Helvetica -20 bold')
                self.labelXiao.grid(row=x + 1, column=y + 1)
        print("---------")

    def showit(self):  # 显示窗口
        self.window.mainloop()

    # 判断是否继续
    def wether_on(self):
        for i in range(4):
            x = y = 0
            for j in range(4):
                if i <= 2 and j <= 2:
                    if self.data[i][j] == self.data[i+1][j] or self.data[i][j] == self.data[i][j+1] or self.data[3][3] == self.data[2][3] or self.data[3][3] == self.data[3][2]:
                        return True
        else:
            return False

    # 碰撞移动之后，随机选择空白位置，填充一个随机数2或4
    def rand_num(self):
        values = [2, 4]
        zero_pos = [[k, _k] for k, v in enumerate(self.data) for _k, _v in enumerate(v) if _v == 0]
        if not zero_pos:
            if self.wether_on():
                return
            else:
                self.fenshu.set("结束，得分" + str(self.scores))
        pos = random.choice(zero_pos)
        self.data[pos[0]][pos[1]] = random.choice(values)

    def bleft(self):
        for i in range(4):
            list_data = []
            for j in range(4):
                temp = self.data[i][j]
                if temp != 0:
                    if not list_data:
                        list_data.append([temp])
                    elif list_data[-1][0] == temp and len(list_data[-1]) == 1:
                        list_data[-1].append(temp)
                        self.scores += 2 * temp
                    else:
                        list_data.append([temp])
            list_data = [sum(k) for k in list_data]
            for z in range(4):
                self.data[i][z] = 0
            for k, v in enumerate(list_data):
                self.data[i][k] = v
        self.myprint()

    def bright(self):
        for i in range(4):
            list_data = []
            for j in range(4):
                temp = self.data[i][j]
                if temp != 0:
                    if not list_data:
                        list_data.append([temp])
                    elif list_data[-1][0] == temp and len(list_data[-1]) == 1:
                        list_data[-1].append(temp)
                        self.scores += 2 * temp
                    else:
                        list_data.append([temp])
            list_data = [sum(k) for k in list_data]
            for z in range(4):
                self.data[i][z] = 0
            for m, n in enumerate(list_data):
                self.data[i][4 - len(list_data) + m] = n
        self.myprint()

    def bup(self):
        for i in range(4):
            list_data = []
            for j in range(4):
                temp = self.data[j][i]
                if temp != 0:
                    if not list_data:
                        list_data.append([temp])
                    elif list_data[-1][0] == temp and len(list_data[-1]) == 1:
                        list_data[-1].append(temp)
                        self.scores += 2 * temp
                    else:
                        list_data.append([temp])
            list_data = [sum(k) for k in list_data]
            for z in range(4):
                self.data[z][i] = 0
            for m, n in enumerate(list_data):
                self.data[m][i] = n
        self.myprint()

    def bdown(self):
        for i in range(4):
            list_data = []
            for j in range(4):
                temp = self.data[j][i]
                if temp != 0:
                    if not list_data:
                        list_data.append([temp])
                    elif list_data[-1][0] == temp and len(list_data[-1]) == 1:
                        list_data[-1].append(temp)
                        self.scores += 2 * temp
                    else:
                        list_data.append([temp])
            list_data = [sum(k) for k in list_data]
            for z in range(4):
                self.data[z][i] = 0
            for m, n in enumerate(list_data):
                self.data[4 - len(list_data) + m][i] = n
        self.myprint()

if __name__ == '__main__':
    GG = Gui2048()
    GG.myprint()
    GG.showit()
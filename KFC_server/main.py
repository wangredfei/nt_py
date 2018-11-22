import sys
from PyQt5.QtWidgets import *
# QApplication, QWidget, QPushButton
from PyQt5.QtGui import *

class MainWindow(QMainWindow):

    # def __init__(self):
    #     super().__init__()
    #     self.initUI()
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)       
        self.initUI()
    def initUI(self):
        
        self.L_button()
        # btn = QPushButton("Button",self)
        # # QPushButton(string text, QWidget parent = None)
        # btn.setToolTip("This is a QPushButton widget")
        # # 创建一个按钮并添加提示框
        # btn.resize(btn.sizeHint())
        # btn.move(150,50)
        # # 调整按钮大小,sizeHint提供一个默认的按钮大小
        self.setFixedSize(self.width(), self.height())   #禁止窗口拉伸
        self.setWindowFlags(Qt.FramelessWindowHint)  #取消窗口边框
        self.setGeometry(300,50,1300,800)
        # 四个值分别代表坐标x,y设置窗口大小的宽高
        self.setWindowTitle("KFC")
        self.setWindowIcon(QIcon("/home/tarena/nt_py/Small_Project/learn_pyqt5/web.png"))
        # 创建一个QIcon对象,然后接受一个路径作为参数显示图标

            

        self.show()
    def L_button(self):
        '''主界面的按钮'''
        
        btn = QPushButton("登录",self)
        btn.setToolTip("This is a QPushButton widget")
        btn.resize(150,40)
        btn.move(1100,600)

        btn = QPushButton("注册",self)
        btn.setToolTip("This is a QPushButton widget")
        btn.resize(150,40)
        btn.move(1100,400)

        btn = QPushButton("×",self)
        btn.setToolTip("This is a QPushButton widget")
        btn.resize(20,20)
        btn.move(1270,10)

        btn = QPushButton("=",self)
        btn.setToolTip("This is a QPushButton widget")
        btn.resize(20,20)
        btn.move(1250,10)

        btn = QPushButton("-",self)
        btn.setToolTip("This is a QPushButton widget")
        btn.resize(20,20)
        btn.move(1230,10)




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
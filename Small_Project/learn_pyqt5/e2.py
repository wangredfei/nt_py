import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        self.setGeometry(300,300,300,220)
        # 四个值分别代表坐标x,y设置窗口大小的宽高
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon("/home/tarena/nt_py/Small_Project/learn_pyqt5/web.png"))
        # 创建一个QIcon对象,然后接受一个路径作为参数显示图标
            

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

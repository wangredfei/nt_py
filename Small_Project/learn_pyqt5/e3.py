'''
此示例示意方一个按钮
'''
import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton,QApplication
from PyQt5.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        QToolTip.setFont(QFont("SansSerif", 30))
        # 设置提示框的字体
        self.setToolTip("This is a QWidge widget")
        # 创建提示框可以使用富文本格式的内容

        btn = QPushButton("Button",self)
        # QPushButton(string text, QWidget parent = None)
        btn.setToolTip("This is a QPushButton widget")
        # 创建一个按钮并添加提示框
        btn.resize(btn.sizeHint())
        btn.move(150,50)
        # 调整按钮大小,sizeHint提供一个默认的按钮大小


        self.setGeometry(300,300,300,200)
        self.setWindowTitle("Tooltips")
        self.show()
    
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

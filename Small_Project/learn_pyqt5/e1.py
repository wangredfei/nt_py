from PyQt5.QtWidgets import QApplication,QWidget
import sys

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    # 每个PyQt5 应用都必须创建一个应用对象
    w = QWidget()
    # QWidget 是一个用户界面的基本控件
    w.resize(250,150)
    # 设置窗口宽高
    w.move(300,300)
    # 控制控件位置的方法,放在坐标位置,原点为左上角
    w.setWindowTitle("Simple")
    # 设置标题
    w.show()
    
    sys.exit(app.exec_())
# -*- coding=utf-8 -*-
#标签的使用
import sys
from PyQt4 import QtCore, QtGui


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("hello")
        self.resize(300, 300)
        #添加标签
        label = QtGui.QLabel(u"这是标签")
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.setCentralWidget(label)

app = QtGui.QApplication(sys.argv)
demo = Window()
demo.show()
app.exec_()
# -*- coding=utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui


class MyWindow(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle("PyQt")
        self.resize(450, 600)


app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
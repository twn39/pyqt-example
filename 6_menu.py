# -*- coding=utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle(u"菜单")
        self.resize(500, 500)

        menubar = self.menuBar()
        self.file = menubar.addMenu('&File')
        open = self.file.addAction('Open')
        self.connect(open, QtCore.SIGNAL('triggered()'), self.OnOpen)

        save = self.file.addAction('Save')
        self.connect(save, QtCore.SIGNAL('triggered()'), self.OnSave)
        self.file.addSeparator()

        close = self.file.addAction("Close")
        self.connect(close, QtCore.SIGNAL('triggered()'), self.OnClose)

        self.label = QtGui.QLabel("this is a  google test")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.setCentralWidget(self.label)

    def OnOpen(self):
        self.label.setText("open")

    def OnSave(self):
        self.label.setText("save")

    def OnClose(self):
        self.close()
    # 点击右键显示菜单
    def contextMenuEvent(self, event):
       self.file.exec_(event.globalPos())

app = QtGui.QApplication(sys.argv)
win = Window()
win.show()
app.exec_()
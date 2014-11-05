#coding=utf-8
import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle(u"文本框")
        self.resize(500, 500)

        gridlayout = QtGui.QGridLayout()

        title = u"标题"
        label = QtGui.QLabel(title)
        label.setAlignment(QtCore.Qt.AlignCenter)
        gridlayout.addWidget(label)

        textFile = QtGui.QLineEdit()
        gridlayout.addWidget(textFile)

        passwordFile = QtGui.QLineEdit()
        passwordFile.setEchoMode(QtGui.QLineEdit.Password)
        gridlayout.addWidget(passwordFile)

        textArea = QtGui.QTextEdit()
        textArea.setText(u"这是多行文本")
        gridlayout.addWidget(textArea)

        self.setLayout(gridlayout)

app = QtGui.QApplication(sys.argv)
window = Window()
window.show()
app.exec_()
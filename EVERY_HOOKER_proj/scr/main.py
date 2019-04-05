import sys

from PyQt5.QtWidgets import QApplication, QLabel,QWidget, QPushButton, QAction, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QLineEdit,QLabel
from func import *

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'BAIKE_HOOKER'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 150
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 30)

        # create label
        self.labelFIR = QLabel("EVERY_HOOKER",self)
        self.labelFIR.move(120, 5)
        self.labelSEC = QLabel("轻松获取网站的内容到本地",self)
        self.labelSEC.move(80, 60)

        # Create a button in the window
        self.button = QPushButton('START', self)
        self.button.move(120, 100)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        url = self.textbox.text()
        html2mjo(url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exit(app.exec_())

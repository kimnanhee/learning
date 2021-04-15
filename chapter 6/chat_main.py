from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from chat import *
from chat_engine import make_reply

class Chat():
    def __init__(self):
        ui.pushButton.clicked.connect(lambda: self.send())

    def send(self):
        text = ui.lineEdit.text()
        if text == "":
            return
        print("input -", text)
        res = make_reply(text)
        print("output -", res)
        ui.lineEdit.setText("")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    chat = Chat()

    MainWindow.show()
    sys.exit(app.exec_())
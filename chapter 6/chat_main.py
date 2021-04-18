from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from chat import *
from chat_engine import make_reply

class Chat():
    text_list = []
    label_list = ["label_user_1", "label_bot_1", "label_user_2", "label_bot_2", "label_user_3", "label_bot_3"]
    def __init__(self):
        ui.pushButton.clicked.connect(lambda: self.send())

    def send(self):
        text = ui.lineEdit.text()
        if text == "":
            return

        self.text_list.append(text)
        self.text_list.append(make_reply(text))

        if len(self.text_list) > 6:
            for i, text in self.text_list[-6:]:
                print(i, text)
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
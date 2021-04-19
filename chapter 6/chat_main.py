from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from chat import *
from chat_engine import make_reply

class Chat():
    def __init__(self):
        self.text_list = []
        self.label_list = [ui.label_user_1, ui.label_bot_1, ui.label_user_2, ui.label_bot_2, ui.label_user_3, ui.label_bot_3]
        
        ui.pushButton.clicked.connect(lambda: self.send())

    def send(self):
        text = ui.lineEdit.text()
        if text == "":
            return

        self.text_list.append(text)
        self.text_list.append(make_reply(text))
 
        if len(self.text_list) > 6:
            for i, text in enumerate(self.text_list[-6:]):
                self.label_list[i].setText(text)
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
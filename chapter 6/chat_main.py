from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow
from chat import *
from chat_engine import make_reply

class Chat(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_list = [" " for i in range(4)]

        ui = Ui_MainWindow()
        ui.setupUi(self)

        self.label_list = [ui.label_user_1, ui.label_bot_1, ui.label_user_2, ui.label_bot_2, ui.label_user_3, ui.label_bot_3]
        
        ui.pushButton.clicked.connect(lambda: self.send())
        self.ui = ui
        # self.setMouseTracking(True)

    # def wheelEvent(self, e): # e ; QWheelEvent 
    #     print('wheel')
    #     print('(%d %d)' % (e.angleDelta().x(), e.angleDelta().y()))

    def send(self):
        text = self.ui.lineEdit.text()
        if text == "": return
        print(text)
        self.text_list.append(text)
        self.text_list.append(make_reply(text))

        for i, text in enumerate(self.text_list[-6:]):
            self.label_list[i].setText(text)
            print(i, text)

        self.ui.lineEdit.setText("")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = Chat()
    main.show()
    sys.exit(app.exec_())
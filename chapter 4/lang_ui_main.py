from PyQt5 import QtCore, QtGui, QtWidgets
from lang_ui import *
import joblib

# 학습 데이터 읽어오기
pklfile = "./lang/freq.pkl"
clf = joblib.load(pklfile)

# 판정하기
def detect_lang(text):
    # 알파벳 출현 빈도 구하기
    text = text.lower()
    code_a, code_z = ord("a"), ord("z")
    cnt = [0 for n in range(26)]
    for ch in text:
        n = ord(ch) - code_a
        if 0 <= n <= 26: cnt[n] += 1
    total = sum(cnt)
    if total == 0: return "No Input"
    freq = list(map(lambda n: n / total, cnt))

    # 언어 예측하기
    res = clf.predict([freq])

    # 언어 코드를 한글로 변환
    lang_dic = {"en" : "영어", "fr" : "프랑스어", "id" : "인도네시아", "tl" : "타갈로그어"}
    return lang_dic[res[0]]

def check(self):
    text = self.textEdit.toPlainText()
    if text != "":
        lang = detect_lang(text)
    self.label.setText(lang)

def signals(self):
    self.pushButton.clicked.connect(self.check)

Ui_MainWindow.signals = signals
Ui_MainWindow.check = check

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec_())
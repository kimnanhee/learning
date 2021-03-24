from sklearn import svm
from sklearn.externals import joblib
import json

# JSON 파일의 데이터 읽어오기
with open("./lang/freq.json", "r", encoding="utf-8") as fp:
    d = json.load(fp)
    print(d)
    data = d[0]
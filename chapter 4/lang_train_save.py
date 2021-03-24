from sklearn import svm
import joblib
import json

# JSON 파일의 데이터 읽어오기
with open("./lang/freq.json", "r", encoding="utf-8") as fp:
    d = json.load(fp)
    data = d[0]

# 데이터 학습하기
clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])

# 학습 데이터 저장하기
joblib.dump(clf, "./lang/freq.pkl")
print("ok")
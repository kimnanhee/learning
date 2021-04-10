from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from sklearn import model_selection, metrics
import json
import numpy

max_words = 56681 # 단어의 개수
nb_classes = 6 # 카테고리의 개수

batch_size = 64
epochs = 20

# MLP 모델 생성하기
def build_model():
    model = Sequential()
    model.add(Dense(512, input_shape=(max_words,)))
    model.add(Activation("relu"))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes))
    model.add(Activation("softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model

# 데이터 읽어 들이기
# data = json.load(open("./newstext/data_mini.json"))
data = json.load(open("./newstext/data.json"))
X = data["X"] # 텍스트를 나타내는 데이터
Y = data["Y"] # 카테고리 데이터

# numpy array형식으로 변환
X = numpy.array(X)
Y = numpy.array(Y)

# 학습하기
X_trian, X_test, Y_train, Y_text = train_test_split(X, Y)
Y_train = np_utils.to_categorical(Y_train, nb_classes)
print("len :", len(X_trian), len(Y_train))
model = KerasClassifier(
    build_fn=build_model,
    epochs=epochs,
    batch_size=batch_size
)
model.fit(X_trian, Y_train)

# 예측하기
predict = model.predict(X_test)
ac_score = metrics.accuracy_score(Y_text, predict)
cl_report = metrics.classification_report(Y_text, predict)
print("정답률 :",ac_score)
print("리포트", cl_report)
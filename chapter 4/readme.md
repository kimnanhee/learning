## Chapter 4

### 머신러닝(machine learning)

인공지능 연구 과제 중의 하나로, 인간의 뇌가 자연스럽게 수행하는 "학습"이라는 능력을 컴퓨터로 구현하는 방법입니다.



파이썬에서 쉽게 사용할 수 있는 머신러닝 프레임워크 : scikit-learn

```
pip install -U scikit-learn scipy matplotlib scikit-image
```



### 4-2

fit() - 학습 기계에 데이터를 학습

predict() - 데이터를 넣어 예측

​	xor_train : sklearn라이브러리의 함수를 사용하여 XOR 연산의 데이터를 학습시키고, 데이터로 결과를 예측하기

​	xor_train2 : 프레임워크를 사용하여 xor_train 코드를 간단하게 작성하기

​	iris_train : 붓꽃 분류 데이터를 사용하여 붓꽃의 품종 분류하기



### 4-3

​	mnist_download : MNIST 데이터 세트를 다운받아서 압출풀기

​	mnist_tocsv : 이미지 파일 열어서 이미지 데이터를 CSV파일에 저장하기. 10개의 테스트 이미지 파일 저장하기

​	mnist_train : CSV 파일의 데이터로 학습시키고,  데이터로 결과를 예측하기






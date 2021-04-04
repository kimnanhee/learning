## Chapter 5

### 딥러닝(deep learning)

여러 층을 가진 신경망을 사용해 머신러닝을 수행하는 것을 의미합니다.



구글에서 오픈소스로 제공하는 머신러닝 라이브러리 : tensor flow

아나콘다

```python
https://www.anaconda.com/download/
# 환경에 맞는 anaconda 설치

# anaconda prompt 실행
conda update -n base conda
conda update --all

conda create -n "가상환경 이름" python=3.6
activate "가상환경 이름"

python -m pip install --upgrade pip
pip install tensorflow
pip install numpy matplotlib pandas pillow graphviz
```

```python
conda info --envs # 가상환경 목록 조회
conda remove -n "가상환경 이름" --a
```



### 5-2

​	calc : TensorFlow를 사용해서 간단한 덧셈하기

​	calc2 : TensorFlow를 사용해서 간단한 사칙연산하기



### 5-4

​	var : 상수식을 연산하고 변수에 대입하기

​	placeholder : 세션을 실행할 때 값을 넣고 실행할 수 있는 플레이스 홀더를 정의해서 연산하기

​	placeholder2 : 플레이스 홀더의 크기를 None로 정의하고, 연산하기

​	bmi : bmi 정보가 저장된 csv 파일을 읽고, 소프트맥스 회귀 방법으로 그래프를 만들기. 교차 엔트로피를 사용하는 오차 함수를 활용해서 데이터를 학습하기



### 5-5

​	tb_mul : 간단한 곱셈 연산하고, 텐서보드로 시각화하기

```python
# Not a TBLoader or TBPlugin subclass: ValueError가 발생하면 아래의 명령어 입력
pip uninstall tensorboard
pip install tb-nightly
```


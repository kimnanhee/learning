## Chapter 5

### 딥러닝(deep learning)

여러 층을 가진 신경망을 사용해 머신러닝을 수행하는 것을 의미합니다.



구글에서 오픈소스로 제공하는 머신러닝 라이브러리 : tensor flow

anaconda

```python
https://www.anaconda.com/download/
# 환경에 맞는 anaconda 설치

# anaconda prompt 실행
conda update -n base conda
conda update --all

conda create -n "가상환경 이름" python=3.6
conda activate "가상환경 이름"
conda deactivate "가상환경 이름"

python -m pip install --upgrade pip
pip install tensorflow==1.14.0
pip install keras==2.2.2
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

​	tb_add : 덧셈 연산을 수행하는 그래프를 정의하고, 텐서보드로 시각화하기

```python
# Not a TBLoader or TBPlugin subclass: ValueError가 발생하면 아래의 명령어 입력
pip uninstall tensorboard
pip install tb-nightly
```

​	tb_bmi : 5-4의 bmi 코드에 이름을 붙여주고, 스코프로 묶어서 텐서보드로 시각화하기



### 5-6

합성곱 신경망(Convolutional Neural Network : CNN) : 입력층과 출력층 사이의 중간층에 합성곱층과 풀링층을 배치한 것.

​	mnist_deep : 합성곱층과 풀링층을 2개씩 넣고, 전결합층을 넣어서 구성. MNIST 손글씨 데이터를 내려받고, 소프트맥스 회귀 방법으로 그래프 만들기. 확률적 경사 강하법을 사용해서 교차 앤트로피의 값이 최소가 되도록 최적화하기



###  5-7

Keras : 머신러닝 라이브러리 Theano와 TensorFlow를 wapping한 라이브러리. 다양한 알고리즘으로 머신러닝 프로그램을 만들 수 있게 도와준다. Keras로 작성한 프로그램은 별도의 수정 없이 TensorFlow와 Theano를 바꿔 사용할 수 있다.

​	keras_mnist : MNIST 손글씨 데이터를 내려받고, add 메소드로 각 층 추가하기. compile 메소드로 모델 구축하기

​	keras_bmi : bmi csv 파일을 읽어와서, 정규화하기. batch_size와 np_epoch를 지정해서 compile 메소드로 모델 구축하기



### 5-8

​	pd_test_df : pandas에서 사용하는 기본 데이터 형식인 Data Frame 생성하고 출력하기

​	pd_test_s : Series 형식의 데이터 생성하고 출력하기

​	pd_test_key : Key로 원하는 열의 데이터를  출력하기

​	pd_test_filter : 원하는 조건의 값을 출력하기

​	pd_test_sort : 원하는 조건의 값으로 정렬하고 출력하기

​	pd_test_rot : 행과 열을 반전해서 출력하기
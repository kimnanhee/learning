## Chapter 5

### 딥러닝(deep learning)

여러 층을 가진 신경망을 사용해 머신러닝을 수행하는 것을 의미합니다.



구글에서 오픈소스로 제공하는 머신러닝 라이브러리 : tensor flow

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
